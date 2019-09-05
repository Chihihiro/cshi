# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro

import random
from MainFrame.Base_driver import *
import random
from datetime import datetime
import re

"""
酒店
"""

class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password

    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        '''
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    def main(self):
        # self.kill_advert()
        # try:
        self.wait_xpath('//android.widget.TextView[@text="悦会会员"]').click()
        self.shanghai_city()
        self.wait_xpath('//android.widget.TextView[@text="酒店特权"]').click()
        # self.wait_xpath('//android.widget.ImageView[@resource-id="com.yhouse.code:id/ivHotel"]')[1].click()
        self.wait_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()
        num = random.randint(300, 500)
        print('随机下滑', num)
        time.sleep(10)
        self.my_touch(xpath='//*[@content-desc="全部"]', down=-num)
        # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]',
        #               down=-random.randint(300, 2000))
        # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]', down=-random.randint(300, 1000))
        # self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]').click()
        nn = random.randint(1, 4)
        print(nn)
        self.driver.find_element_by_xpath(f'//android.widget.ListView/android.view.View[{nn}]/android.view.View[2]').click()
        # self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()



        self.random_click()
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
        # except BaseException as e:
        #     print(e)

    def random_click(self):
        time.sleep(3)  # 设置延迟方便调试
        # self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
        now = re.sub('-', '.', str(datetime.now())[:10])
        now2 = now[:5]+ str(int(now[6:7])) +'.'+ str(int(now[9:10]))

        try:
            self.driver.find_element_by_xpath('//*[@content-desc="选择日期："]')
        except BaseException:
            print('没有在正确页面点击返回')
            self.wait_xpath('//android.widget.ImageView[@resource-id="com.yhouse.code:id/header_left_back"]').click()


        try:
            cc = self.driver.find_element_by_xpath(f'//*[@content-desc="{now}"]')
            self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
            print(cc, '今天日期存在')
        except BaseException as e:
            print(e)
            cc = None

        try:
            zz = self.driver.find_element_by_xpath(f'//*[@content-desc="{now2}"]')
            self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
            print(zz, '今天日期存在')
        except BaseException as e:
            print(e)
            zz = None

        if cc or zz:
            try:
                time.sleep(1)
                x = [i for i in range(100,601,100)]
                x1 = random.choice(x)
                x2 = x1 + 100
                y = [i for i in range(300,1101,100)]
                y1 = random.choice(y)
                print('随机高度和左右', y1, x1, x2)
                self.touch_tap(x1, y1)
                self.touch_tap(x2, y1)
                print('随机点击点击完毕')
                time.sleep(1)
                self.wait_xpath('//android.widget.Button[@text="确认"]').click()
            except BaseException as e:
                print(e)
            self.random_click()
        else:
            print('不是今天了通过')



def run5():
    a = my_test(phone='13524422749', password='123456')
    a.setup()
    a.login()
    a.main()
    a.tearDown()


if __name__ == "__main__":
    run5()
