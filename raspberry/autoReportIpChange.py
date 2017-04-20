#!/usr/bin/env python
# coding=utf-8
from threading import Timer,Thread,Event
# from requests import get
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header


from getpass import getpass
import json
import sys
from pprint import pprint
reload(sys)
sys.setdefaultencoding( "utf-8" )

def prompt(prompt):
    return input(prompt).strip()

def readSenderData():
    # print ((sys.path[0].decode('gbk')+'mailconfig.json11111').encode("utf-8"))
    with open((sys.path[0]+'/mailconfig.json')) as data_file:    
        data = json.load(data_file)
    # pprint(data)
    return data
readSenderData()
def getIp():
    try:
        ip = requests.get('https://api.ipify.org').text
        # r = requests.get(url, params={'s': thing})
        # pprint(ip)
        return ip
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print e
        return 'getIpFail'

def sendMailToQQ(msg):
    # 第三方 SMTP 服务
    mailinfo = readSenderData()
    mail_host=mailinfo["smtp"]  #设置服务器
    mail_user=mailinfo["sendaccount"]    #用户名
    mail_pass=mailinfo["pw"]   #口令 
    sender = mailinfo["sendaccount"]
    receivers = mailinfo["reciveaccount"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

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

oldIp = getIp()
print('My public IP address is: {}'.format(oldIp))

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(10):
            # print("my thread")
            self.job()
            # call a function
    def job(self):
        ip = getIp()
        # r = requests.get(url, params={'s': thing})
        if self.oldIp != ip :
            print ('ipchange',oldIp,ip)
            sendMailToQQ(ip)
            self.oldIp = ip

            


stopFlag = Event()
thread = MyThread(stopFlag)
thread.oldIp = oldIp
thread.start()


sendMailToQQ(oldIp)
# this will stop the timer
#stopFlag.set()
