# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 10:06
# @Author  : Chihiro


import requests
import json

url1 = 'http://m.yhouse.com/api/m/equities/equitiesCheck?equitiesCode=6&equityId=63&appUserId=EKZkZQtkAJ9bJD'
url11 = 'http://m.yhouse.com/api/m/brand/order/confirmOrder?cardId=660378&cityId=2&equityId=63&equityNum=1&siteCode=m&appUserId=EKZkZQtkAJ9bJD'

url2 = 'http://m.yhouse.com/api/m/ticket/equitiesCheck?equitiesCode=15&equityId=47&appUserId=EKZkZQtkAJ9bJD'
url21 = 'http://m.yhouse.com/api/m/ticket/createOrder?cityId=2&fillMobile=13524422749&rechargeId=3&siteCode=m&appUserId=EKZkZQtkAJ9bJD'

url3 = 'https://m.yhouse.com/api/m/ticket/equitiesCheck?equitiesCode=10&equityId=2&appUserId=EKZkZQtkAJ9bJD'
url31 = 'https://m.yhouse.com/api/m/ticket/createOrder?bookDate=2019-11-10&cityId=2&fillAddress=&fillIdCard=310225199212246612&fillIdCardType=1&fillMobile=18939832542&fillName=test&fillNameCard=&payAmount=53600&quantity=1&siteCode=m&ticketEquityId=2&appUserId=EKZkZQtkAJ9bJD'

url4 = 'http://m.yhouse.com/api/m/ticket/equitiesCheck?equitiesCode=11&equityId=52&appUserId=EKZkZQtkAJ9bJD'
url41 = 'http://m.yhouse.com/api/m/brand/order/confirmOrder?cityId=2&equityId=52&equityNum=1&siteCode=m&appUserId=EKZkZQtkAJ9bJD'

url5 = 'https://m.yhouse.com/api/m/promocode/vip/list?amount=39900&vipLevelId=597&appUserId=EKZkZQtkAJ9bJD'
#
# url6 = 'https://api.yhouse.com/m/promocode/exchangedlist?subscribeId=26381&subscribeType=12&appUserId=EKZkZQtkAJ9bJD'
# url61 = 'https://api.yhouse.com/m/hotel/room/order'

a = [url1,url11,url2,url21,url3,url31,url4,url41]
import time
def run():
    while True:
        for url in a:
            print(url)
            html = requests.get(url)
            print(html.text)
            time.sleep(2)

        time.sleep(480)

run()