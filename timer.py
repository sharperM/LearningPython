#!/usr/bin/env python
# coding=utf-8
from threading import Timer,Thread,Event
from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))

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
        ip = get('https://api.ipify.org').text
        print(ip)
stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
# this will stop the timer
#stopFlag.set()
