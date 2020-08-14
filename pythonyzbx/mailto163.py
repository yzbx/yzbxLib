# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sendmail(sender="youdaoyzbx@163.com",
             receivers=['wangjiaxin15@mails.ucas.ac.cn'],
             files=[],
             ):
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = "{}<{}>".format(sender,Header(sender, 'utf-8'))
    message['To'] =  "{}<{}>".format(receivers[0],Header(receivers[0], 'utf-8'))
    subject = 'send image and tensorboard log'
    message['Subject'] = Header(subject, 'utf-8')
     
    #邮件正文内容
    text='send files: \n' + '\n'.join(files)
    message.attach(MIMEText(text, 'plain', 'utf-8'))
     
    for f in files:
        att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(f))
        message.attach(att)
     
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("send mail okay")
    except smtplib.SMTPException:
        print("Error: cannot send mail")

if __name__ == '__main__':      
    sendmail()