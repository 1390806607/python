from flask import Blueprint
from flask_restful import Api
user = Blueprint('/user',__name__)
user_api = Api(app=user)
from flask_execl.user import view