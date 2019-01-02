"""User authentication"""
from flask import request, current_app
import datetime
import jwt
from functools import wraps


def login_required(f):
    @wraps(f)
    def authenticate(*args, **kwargs):
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            try:
                data = jwt.decode(token, current_app.config['SECRET_KEY'],
                                  algorithm='HS256')
            except jwt.ExpiredSignatureError:
                return 'expired token'
            except jwt.InvalidTokenError:
                return 'invalid token'
            return f(*args, **kwargs, current_user=data['username'])
        else:
            return 'missing token'
    return authenticate
