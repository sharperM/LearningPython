#!/usr/bin/env python
# coding=utf-8
import time
import datetime

class Clock:

    def __init__(self):

        # set the initial time
        self.hour = 0
        self.minute = 0
        self.second = 0
        # the update interval in seconds
        self.update_interval = 1
        self.keep_running = True
        # the instance of the alarm
        self.alarm = AlarmClock()

    def run(self):
        while self.keep_running:
            # update the clock time
            now = datetime.datetime.now()
            self.hour = now.hour
            self.minute = now.minute
            self.second = now.second

            # now check if the alarm should not be started
            if self.alarm.is_active():
                if self.alarm.time_till_next_alarm() < 1:
                    # has to be done in separate thread
                    self.alarm.on_wake_up()
            time.sleep(self.update_interval)

    def get_alarm(self):
        return self.alarm


class AlarmClock:
    def __init__(self, hour=8, minute=0):
        # We start with predefined alarm at 8:00 which is not active
        self.hour = hour
        self.minute = minute
        self.active = False
        # the alarm should be stopped after some time (1h 00min)
        self.duration = datetime.timedelta(hours=1, minutes=0)

    def time_till_next_alarm(self):
        now = datetime.datetime.now()  # get current date & time

        # separate date and time from each other:
        currdate = datetime.date(now.year, now.month, now.day)
        currtime = datetime.time(now.hour, now.minute)
        alarmtime = self.get_wake_up_time()
        # add today's date onto the alarm time entered
        alarmdatetime = datetime.datetime.combine(currdate, alarmtime)
        if alarmtime <= currtime:  # if the alarm time is less than the current time set clock for tomorrow
            alarmdatetime += datetime.timedelta(hours=24)
        return (alarmdatetime - now).total_seconds()

    def set_time(self, hour, minute):
         self.hour = hour
         self.minute = minute

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def on_wake_up(self):
        # start the wake up
        print 'Wake up!'
    def get_wake_up_time(self):
        return datetime.time(self.hour,self.minute)


#Execution starts here
if __name__ == '__main__':

    clock = Clock()
    clock.get_alarm().activate()
    clock.get_alarm().set_time(15,23)
    clock.run()
