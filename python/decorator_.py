import jwt
from flask import request
import functools
from config import SECRET_KEY,jwt_exp
from flask_execl import models
def login_reuqired(func):
    functools.wraps(func)
    def verify_token(*args,**kwargs):
        try:
            token = request.headers.get('token')
            if token:
                payload = jwt.decode(token,SECRET_KEY,algorithms=["HS256"],leeway=jwt_exp,options={"verify_exp": True})
        except Exception as e:
            return {'msg':'请先登录'}
        return func(*args,**kwargs)
    return verify_token
