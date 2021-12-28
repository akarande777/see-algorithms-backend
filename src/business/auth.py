from ..database.models import User
from datetime import datetime
from ..utils import response
import hashlib


class Auth:
    def __init__(self, context):
        self.session = context['session']

    def login(self, email: str, password: str):
        try:
            hash = hashlib.md5(password.encode()).hexdigest()
            user = self.session.query(User).filter_by(
                email=email, password=hash).first()
            if not user:
                return response(None, False, "Invalid username or password")
            user.last_login = datetime.utcnow()
            user.login_count += 1
            self.session.commit()
            return response(user)
        except Exception as e:
            return response(None, False, "Internal server error")

    def register(self, email: str, password: str, display_name: str):
        try:
            if self.session.query(User).filter_by(email=email).scalar():
                return response(None, False, "User does exist with this email")
            user = User(
                email=email,
                password=hashlib.md5(password.encode()).hexdigest(),
                display_name=display_name,
                login_count=0,
            )
            self.session.add(user)
            self.session.commit()
            return response(None)
        except Exception as e:
            return response(None, False, "Internal server error")
