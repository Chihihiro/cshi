# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro

import random
from MainFrame.Base_driver import *

"""
酒店
"""

class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password

    def main(self):
        # self.kill_advert()
        try:
            self.wait_xpath('//android.widget.TextView[@text="悦会会员"]').click()
            self.wait_xpath('//android.widget.TextView[@text="酒店特权"]').click()
            # self.wait_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/tv_findHotel"]').click()
            self.wait_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()
            num = random.randint(400, 800)
            print('随机下滑', num)
            time.sleep(10)
            self.my_touch(xpath='//*[@content-desc="全部"]', down=-num)
            # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]',
            #               down=-random.randint(300, 2000))
            # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]', down=-random.randint(300, 1000))
            # self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]').click()
            nn = random.randint(1,5)
            print(nn)
            # self.driver.find_element_by_xpath(
            #     f'//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[{nn}]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
            self.driver.find_element_by_xpath(f'//android.widget.ListView/android.view.View[{nn}]/android.view.View[2]').click()
            self.wait_xpath('//android.widget.TextView[@text="立即预订"]').click()
            self.wait_xpath('//*[@content-desc="立即预订"]').click()
            name = self.wait_xpath('//android.widget.EditText[@text="请输入姓名"]')
            name.click()
            time.sleep(3)
            txt = self.random_name()
            field = f'{txt}~13524422749'
            self.my_send(field)#模拟键盘输入
            self.wait_xpath('//android.widget.Button[@text="立即预约"]').click()
            time.sleep(3)
            print('酒店订单下单成功')
        except BaseException as e:
            print(e)



def run():
    a = my_test(phone='13524422749', password='123456')
    a.setup()
    a.login()
    a.main()
    a.tearDown()


if __name__ == "__main__":
    run()
