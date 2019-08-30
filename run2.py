# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 14:10
# @Author  : Chihiro

import os
import threading
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import schedule
from My_Test_File.model01 import run1 as run1
from My_Test_File.model02 import run2 as run2
from My_Test_File.model03 import run3 as run3
from My_Test_File.model04 import run4 as run4
from My_Test_File.model05 import run5 as run5
from My_Test_File.model06 import run6 as run6


# path = os.getcwd() + '\My_Test_File'
# ll = os.listdir(path)
# os.chdir(path)

# def job():
#     contab = [run1, run2, run3, run4, run5, run6]
#     for i in contab:
#         print(i)
#         try:
#             i()
#         except BaseException as e:
#             print('再试一次',e)
#             time.sleep(10)
#             i()
#             print('再试一次成功')
#         else:
#             time.sleep(5)

def job2():
    contab = [run2, run3, run4, run5, run6, run1]
    cc = []
    while len(contab) > 0:
        job = contab[-1]
        if cc.count(job.__name__) >= 3:
            """失败超过三次剔除掉"""
            contab.pop()
        else:
            pass
        try:
            job()
            print(len(contab))
            contab.pop()
        except BaseException as e:
            print(e)
            cc.append(job.__name__)
        print(len(contab))
        print('cc:', cc)



if __name__ == '__main__':
    count = 0
    while True:
        count += 1
        print('计数：', count)
        job2()
        time.sleep(1)
