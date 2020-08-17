# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import argparse
import time

# localhost + 25
# smtp.163.com + 465
def sendmail(sender="yzbx_yzbx@163.com",
             receivers=['wangjiaxin15@mails.ucas.ac.cn'],
             files=[],
             host='smtp.163.com',
             port=465,
             note='test'
             ):
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = "{}<{}>".format(sender,Header(sender, 'utf-8'))
    message['To'] =  "{}<{}>".format(receivers[0],Header(receivers[0], 'utf-8'))
    subject =note + ' send image and tensorboard log'
    message['Subject'] = Header(subject, 'utf-8')
     
    #邮件正文内容
    time_str = time.strftime("%Y-%m-%d___%H-%M-%S", time.localtime())
    text=note+ ' send files: \n' + '\n'.join(files) + '\n'+ time_str
    message.attach(MIMEText(text, 'plain', 'utf-8'))
     
    for f in files:
        att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(f))
        message.attach(att)
     
    try:
        if host=='localhost':
            smtpObj = smtplib.SMTP('localhost',port)
        else:
            # port=465/994
            smtpObj = smtplib.SMTP_SSL(host,port)
            smtpObj.login('yzbx_yzbx@163.com','ABEUWDHJMAWUSQBU')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("send mail okay")
    except smtplib.SMTPException as e:
        print("Error: cannot send mail, {}".format(e))

if __name__ == '__main__':     
    parser=argparse.ArgumentParser()
    parser.add_argument('--port',type=int,default=25,help='port for stmp server')
    parser.add_argument('--host',choices=['localhost','smtp.163.com'],help='host for stmp server')
    args=parser.parse_args()
    sendmail(host=args.host,port=args.port)