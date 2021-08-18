from flask import Blueprint
from flask_restful import Api
execl = Blueprint('execl',__name__)
execl_api = Api(execl)
from flask_execl.fexecl import view