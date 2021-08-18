
from flask_execl import models
from flask_execl.user import user_api,user
from flask_restful import request,Resource
from flask_execl import db
import jwt
from datetime import datetime
from config import SECRET_KEY
class User(Resource):
    def post(self):
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        email = request.form.get('email')
        phone = request.form.get('phone')
        try:
            if not all([name,pwd]):
                return {'msg':'Please input name and password'}
            user = models.User.query.filter_by(name=name).first()
            if user:
                return {'msg':'name already exists'}
            else:
                user = models.User(name = name,password=pwd,email=email,phone=phone)
                db.session.add(user)
                db.session.commit()
                return {'code':200,'msg':'register success'}
        except Exception as e:
            print(e)


user_api.add_resource(User,'/user')


@user.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    try:
        if not all([name,pwd]):
            return {'msg':'Please input name and password'}
        else:
            user = models.User.query.filter_by(name=name).first()
            if user:
                if user.check_password(pwd):
                    payload ={
                        'name':name,
                        'exp': datetime.utcnow(),
                    }
                    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                    return {'code':200,'msg':'login success','token':token}
            else:
                return {'msg':'登录失败,此用户不存在'}
    except Exception as e:
        print(e)
        return {'code':500, 'msg':'name and password  is not true'}


