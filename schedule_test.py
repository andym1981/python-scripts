#! /usr/local/bin
import os 
import sys

#print "Python " + sys.version

import schedule
import time

def job():
    print("I'm working...")

def hourly_job():
    print("I'm working Hourly...")

def job():
    print("I'm working...")

schedule.every(1).minutes.do(job)
schedule.every().hour.do(hourly_job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
