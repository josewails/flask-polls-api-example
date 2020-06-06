import datetime

from app.core.utils import generate_uuid
from app.exts import db
import config

import jwt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(64), primary_key=True, default=generate_uuid(), nullable=False, unique=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def encode_auth_token(cls, user_id):
        payload = dict(
            exp=datetime.datetime.utcnow() + datetime.timedelta(seconds=5),
            iat=datetime.datetime.utcnow(),
            sub=user_id
        )

        return jwt.encode(
            payload,
            config.SECRET_KEY,
            algorithm='HS256'
        )

    @classmethod
    def decode_auth_token(cls, auth_token):
        try:
            payload = jwt.decode(auth_token, config.SECRET_KEY, algorithms=['HS256'])
            return payload['sub']

        except jwt.ExpiredSignature:
            return "Signature expired. Please log in again"

        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again"
