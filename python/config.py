# import os
# SECRET_KEY=os.urandom(16)
class Config:
    DIALECT='mysql'
    DRIVER='pymysql'
    USERNAME='root'
    PASSWORD='litao123'
    HOST='localhost'
    PORT='3306'
    DABABASE='flask_execl'
    
    
    SQLALCHEMY_DATABASE_URI='{}+{}://{}:{}@{}:{}/{}'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DABABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS=True
SECRET_KEY = b'\xdc\x9c\xb3\x9d\x86\x14\xd4\xae\xd5\x99\xe6/\x88\x11$4'
class Development(Config):
    DEBUG =True
class Production(Config):
    pass

map = {
    'develop' : Development,
    'product' : Production
}

# send = {
#     'from_email' : '1390806607@qq.com',
#     'password' : 'mducqvonpheoibfd'
# }

jwt_exp= 7*24*3600
# 发送邮件所需的地址
send = {
   'localhost' :'mailrelay.america.littelfuse.com',
    'sender' : 'IT@CHINAIT.COM' 
}
