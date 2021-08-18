# import zmail

# def send_mail(from_email,password,to_email,subject,txt):
#     mail = zmail.server(from_email,password)
#     mail.send_mail(to_email,{'subject':subject,'content_text':txt})
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = 'IT@CHINAIT.COM'
receivers = ['1390806607@qq.com']
Content = '测试'
message = MIMEText(Content,'plain', 'utf-8')
message['From'] = Header("Real Time Tracking System", 'utf-8')  # 发送者
message['To'] = Header("IT OPS", 'utf-8')
subject = 'Legacy PC reminder!'
message['Subject'] = Header(subject, 'utf-8')
def send_mail(sender,receivers,message,localhost):
    try:
        smtpObj = smtplib.SMTP(localhost)
        smtpObj.sendmail(sender, receivers, message.as_string())

        print('mail was sent successful')
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

from config import send

send_mail(sender,receivers,message,send.get('localhost'))