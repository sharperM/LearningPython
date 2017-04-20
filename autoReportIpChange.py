#!/usr/bin/env python
# coding=utf-8
from threading import Timer,Thread,Event
# from requests import get
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="659900896@qq.com"    #用户名
mail_pass="besideair23"   #口令 
from getpass import getpass

def prompt(prompt):
    return input(prompt).strip()

def sendMailToQQ(msg):
    sender = '659900896@qq.com'
    receivers = ['659900896@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("python脚本", 'utf-8')
    message['To'] =  Header("qq邮箱", 'utf-8')
     
    subject = '电信地址改变了'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host) 
        smtpObj.login( mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "send mail success"
    except smtplib.SMTPException:
        print "Error: cannot send mail"

oldIp = requests.get('https://api.ipify.org').text
print('My public IP address is: {}'.format(oldIp))

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(10):
            print("my thread")
            self.job()
            # call a function
    def job(self):
        try:
            ip = requests.get('https://api.ipify.org').text
            # r = requests.get(url, params={'s': thing})
            if self.oldIp != ip :
                sendMailToQQ(ip)
                self.oldIp = ip
            print(ip)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print e
            

stopFlag = Event()
thread = MyThread(stopFlag)
thread.oldIp = oldIp
thread.start()


sendMailToQQ(oldIp)
# this will stop the timer
#stopFlag.set()
