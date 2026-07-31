import jwt
from datetime import datetime, timedelta

SECRET = "securechain"


def create_token(username):

    payload = {
        "user": username,
        "exp": datetime.utcnow() + timedelta(days=1)
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token):

    return jwt.decode(token, SECRET, algorithms=["HS256"])