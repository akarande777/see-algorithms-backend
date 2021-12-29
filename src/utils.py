from datetime import datetime, timedelta
from .config import *
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
import jwt


def map_resolver(obj, resolver):
    for key, value in resolver.items():
        obj.field(key)(value)


def resolve(data=None):
    return {'data': data, 'status': True}


def reject(message=None):
    return {'status': False, 'message': message}


def auth_token(user_id: int):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id,
        }
        return jwt.encode(
            payload,
            JWT_SECRET_KEY,
            algorithm='HS256',
        )
    except Exception:
        return ''


def generate_token(email: str):
    serializer = URLSafeTimedSerializer(SERIALIZER_SECRET_KEY)
    return serializer.dumps(email, salt=SERIALIZER_PASSWORD_SALT)


def confirm_token(token: str, exp: int = 3600):
    serializer = URLSafeTimedSerializer(SERIALIZER_SECRET_KEY)
    return serializer.loads(
        token,
        salt=SERIALIZER_PASSWORD_SALT,
        max_age=exp
    )


def write_mail(to, subject, html):
    return Message(
        subject,
        recipients=[to],
        html=html,
        sender=MAIL_USERNAME
    )
