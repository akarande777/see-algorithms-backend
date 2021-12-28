from datetime import datetime, timedelta
from .config import JWT_SECRET_KEY
import jwt


def map_resolver(obj, resolver):
    for key, value in resolver.items():
        obj.field(key)(value)


def response(data, status=True, message=None):
    return {'data': data, 'status': status, 'message': message}


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
