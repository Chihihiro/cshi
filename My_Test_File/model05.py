# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro

import random
from MainFrame.Base_driver import *
import random

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
        # self.wait_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/tv_findHotel"]').click()
        self.wait_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()
        num = random.randint(300, 500)
        print('随机下滑', num)
        time.sleep(10)
        self.my_touch(xpath='//*[@content-desc="全部"]', down=-num)
        # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]',
        #               down=-random.randint(300, 2000))
        # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]', down=-random.randint(300, 1000))
        # self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]').click()
        nn = random.randint(2,3)
        print(nn)
        # self.driver.find_element_by_xpath(
        #     f'//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[{nn}]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        self.driver.find_element_by_xpath(f'//android.widget.ListView/android.view.View[{nn}]/android.view.View[2]').click()
        self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
        # screen_width
        # Out[9]: 810
        # screen_height = self.driver.get_window_size()['height']
        # screen_height
        # Out[11]: 1440
        time.sleep(3)
        x = [i for i in range(100,601,100)]
        x1 = random.choice(x)
        x2 = x1 + 100

        y = [i for i in range(900,1101,100)]
        y1 = random.choice(y)


        self.touch_tap(x1, y1)
        self.touch_tap(x2, y1)
        # self.driver.execute_script("alert('hello,selenium');")
        self.wait_xpath('//android.widget.Button[@text="确认"]').click()
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



def run5():
    a = my_test(phone='13524422749', password='123456')
    a.setup()
    a.login()
    a.main()
    a.tearDown()


if __name__ == "__main__":
    run5()
