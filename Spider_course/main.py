#-*- coding: utf-8 -*- 
#!/usr/bin/env python
import e_mail
import spider_course
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

def excute():
    pass_ID = [("0121809361804","aonelovesay52she"),("0121809360716","12345ssdlh")]
    e_user = '1732615826@qq.com'
    e_pass = 'lgwdspcqbdlscaid'
    sender = '1732615826@qq.com'
    receiver = ['1732615826@qq.com','1165976033@qq.com']
    index = 0
    for each in pass_ID:
        spider_course.spider_session(each[0],each[1])
        e_mail.email(e_user,e_pass,sender,receiver[index])
        index += 1
 
#scheduler = BlockingScheduler()
#trigger = CronTrigger(day_of_week='mon-sun', hour='21', minute="31", second="0")
#scheduler.add_job(excute,trigger)
#scheduler.start()
    

excute()






