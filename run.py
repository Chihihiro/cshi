# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 14:10
# @Author  : Chihiro

import os
import threading
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import schedule
from My_Test_File.model01 import run as run1
from My_Test_File.model02 import run as run2
from My_Test_File.model03 import run as run3
from My_Test_File.model04 import run as run4
from My_Test_File.model05 import run as run5
from My_Test_File.model06 import run as run6


# path = os.getcwd() + '\My_Test_File'
# ll = os.listdir(path)
# os.chdir(path)

def job():
    contab = [run1, run2, run3, run4, run5, run6]
    for i in contab:
        print(i)
        try:
            i()
        except BaseException as e:
            print(e)
        else:
            time.sleep(10)


if __name__ == '__main__':
    job()
    schedule.every(10).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(10)
