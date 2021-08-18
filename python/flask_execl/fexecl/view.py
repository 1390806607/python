

from flask_execl.fexecl import execl_api,execl
from flask_restful import Resource,request
from flask_execl import models,db
from datetime import  datetime, timedelta
# from email_ import send_mail
# from config import send
from decorator_ import login_reuqired
# from email.mime.text import MIMEText
# from email.header import Header
class ExeclView(Resource):
    @login_reuqired
    def get(self):
        e_list = []
        invaild_list = []       # 即将到期
        informations = models.Execl.query.all()
        for i in informations:
            a = i.to_json()
            # b = str(a.get('WarrantyEndDate'))   
            # a.get('WarrantyEndDate') = b
            if abs((a.get('WarrantyEndDate') - datetime.now()).days)<90:
                invaild_list.append(a.get('SerialNumber'))
            a['WarrantyEndDate'] =str(a.get('WarrantyEndDate')) 
            # print(a.get('WarrantyEndDate').day)
            e_list.append(a)
        # receivers = ['npeng@littelfuse.com', 'gzhuo@littelfuse.com']
        # Content = '即将到期的PC{}'.format(invaild_list)
        # message = MIMEText(Content,'plain', 'utf-8')
        # message['From'] = Header("Real Time Tracking System", 'utf-8')  # 发送者
        # message['To'] = Header("IT OPS", 'utf-8')
        # subject = 'Legacy PC reminder!'
        # message['Subject'] = Header(subject, 'utf-8')
        # send_mail(send['sender'],receivers,message,send['localhost'])

        return {'code':200, 'data':e_list }
    
    def post(self):
        SerialNumber = request.form.get('SerialNumber') if request.form.get('SerialNumber') else ''
        Model_ = request.form.get('Model')  if request.form.get('Model') else ''
        ImageName = int(request.form.get('ImageName')) if request.form.get('ImageName') else 0
        EndUserld = request.form.get('EndUserld') if request.form.get('EndUserld') else ''
        ComputerName = request.form.get('ComputerName') if request.form.get('ComputerName') else ''
        WarrantyEndDate = request.form.get('WarrantyEndDate')
        # "Z" biao shi  UTC  time     zhuan  huan beijing  time
        WarrantyEndDate = datetime.fromisoformat(WarrantyEndDate.split('.')[0])+timedelta(hours=8)
        try:
            if not all([SerialNumber,Model_,EndUserld,ComputerName,WarrantyEndDate]):
                return {'code':500, 'msg':'Warning:Please complete the information'}
            # if not re.match(r'\d{4}-\d{2}-\d{2}',WarrantyEndDate):
            #     return {'code':500,'msg':'Please input according to the formant:yyyy-mm-dd'}
            else:
                # list = WarrantyEndDate.split('-')
                # year = list[0]
                # month = list[1]
                # day = list[2][0]+list[2][1]
                # print(year)
                # print(month)
                # print(day)

                el = models.Execl.query.filter_by(SerialNumber=SerialNumber).first()
                if el:
                    #  Modify information
                    el.Model_ = Model_
                    el.ImageName = ImageName
                    el.EndUserld = EndUserld
                    el.ComputerName =ComputerName
                    el.WarrantyEndDate = WarrantyEndDate
                    # datatime.date  not modify 
                    # el.WarrantyEndDate.year = year   
                    # el.WarrantyEndDate.month = month
                    # el.WarrantyEndDate.day = day
                    db.session.commit()
                    return {'code':200, 'msg':'Modify success' }
                else:
                    # increase
                    execl = models.Execl(SerialNumber=SerialNumber,Model_=Model_,ImageName=ImageName,EndUserld=EndUserld,ComputerName=ComputerName,WarrantyEndDate=WarrantyEndDate)
                    db.session.add(execl)
                    db.session.commit()
                    return {'code':200,'msg':'Increase success'}     
        except Exception as e:
            print(e)

    def delete(self):
        SerialNumber = request.json.get('SerialNumber')
        execl = models.Execl.query.filter_by(SerialNumber=SerialNumber).first()
        db.session.delete(execl)
        db.session.commit()
        return {'code':200 , 'msg': 'Delete success'}

execl_api.add_resource(ExeclView,'/execl')

@execl.route('/ex', methods=['GET'])
def get_execl():
    e_list = []
    invaild_list = []
    informations = models.Execl.query.all()
    for i in informations:
        a = i.to_json()
            # b = str(a.get('WarrantyEndDate'))   
            # a.get('WarrantyEndDate') = b
        if abs((a.get('WarrantyEndDate') - datetime.now()).days)<90:
            invaild_list.append(a)
        a['WarrantyEndDate'] =str(a.get('WarrantyEndDate')) 
            # print(a.get('WarrantyEndDate').day)
        e_list.append(a)  
    return {'code':200, 'data':e_list }