import re
from werkzeug.security import generate_password_hash,check_password_hash
from flask_execl import db
from datetime import datetime

    

class Execl(db.Model):
    __tablename__ = 't_execl'
    WarrantyEndDate = db.Column(db.DateTime)
    CreateTime = db.Column(db.DateTime,default= datetime.today,onupdate=datetime.now)
    id = db.Column(db.Integer,primary_key=True)
    SerialNumber = db.Column(db.String(128),unique=True)
    Model_ = db.Column(db.String(64))
    ImageName = db.Column(db.String(128))
    EndUserld = db.Column(db.String(64))
    ComputerName= db.Column(db.String(36))

    def to_json(self):
        return {
            'WarrantyEndDate' : self.WarrantyEndDate,
            'SerialNumber' : self.SerialNumber,
            'Model' : self.Model_,
            'ImageName' : self.ImageName,
            'EndUserld' : self.EndUserld,
            'ComputerName' : self.ComputerName
        }

class User(db.Model):
    CreateTime = db.Column(db.DateTime,default= datetime.today)
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False)
    pwd = db.Column(db.String(128))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(32))

    # 定义一个装饰器
    @property
    def password(self):
        return self.pwd

    @password.setter
    def password(self,t_pwd):
        self.pwd = generate_password_hash(t_pwd)
        return self.pwd

    def check_password(self,t_pwd):
        return check_password_hash(self.pwd,t_pwd)

    

