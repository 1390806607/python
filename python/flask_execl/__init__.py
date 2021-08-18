from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import map

db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    obj = map.get(config_name)
    app.config.from_object(obj)
    db.init_app(app)

    from flask_execl.fexecl import execl
    app.register_blueprint(execl)
    from flask_execl.user import user
    app.register_blueprint(user)
    return app