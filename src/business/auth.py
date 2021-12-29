from ..database.models import User
from datetime import datetime
from flask import render_template
from ..utils import *
from ..config import BASE_URL
import hashlib


class Auth:
    def __init__(self, context):
        self.session = context['session']
        self.mail = context['mail']

    def login(self, email: str, password: str):
        try:
            hash = hashlib.md5(password.encode()).hexdigest()
            user = self.session.query(User).filter_by(
                email=email, password=hash, confirmed=True).first()
            if not user:
                return reject("Failed to login. Please check your email or password.")
            user.last_login = datetime.utcnow()
            user.login_count += 1
            self.session.commit()
            return resolve(user)
        except Exception:
            return reject("Internal server reject")

    def register(self, email: str, password: str, display_name: str):
        try:
            if self.session.query(User).filter_by(email=email).scalar():
                return reject("User does exist with this email.")
            user = User(
                email=email,
                password=hashlib.md5(password.encode()).hexdigest(),
                display_name=display_name,
                login_count=0,
            )
            self.session.add(user)
            self.session.commit()
            token = generate_token(email)
            confirm_url = f"{BASE_URL}?token={token}"
            html = render_template('confirm_email.html',
                                   confirm_url=confirm_url)
            subject = "Please confirm your email"
            mail = write_mail(user.email, subject, html)
            self.mail.send(mail)
            return resolve()
        except Exception:
            return reject("Internal server reject")

    def confirm_email(self, token: str):
        try:
            email = confirm_token(token)
        except:
            return reject("Confirmation link is invalid or has expired.")
        user = self.session.query(User).filter_by(email=email).first()
        if user.confirmed:
            return reject("Account already confirmed. Please login.")
        else:
            user.confirmed = True
            self.session.commit()
        return resolve()
