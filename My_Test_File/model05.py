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

    def phoneNORandomGenerator(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153",
                   "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    def main(self):
        # self.kill_advert()
        # try:
        self.wait_xpath('//android.widget.TextView[@text="悦会会员"]').click()
        # self.shanghai_city()
        self.wait_xpath('//android.widget.TextView[@text="酒店特权"]').click()
        # self.wait_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[5]').click()
        time.sleep(3)
        self.wait_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/tv_findHotel"]').click()


        self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]',
                      down=-random.randint(500, 1000))
        time.sleep(3)
        bb = random.choice([0,1,2,3])
        for i in range(bb):
            self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]',
                          down=-random.randint(300, 1000))
        time.sleep(3)
        self.touch_tap(500, 600)
        # x = [2, 3, 4, 5, 6]
        # y = random.choice(x)
        # self.wait_xpath(f'//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[{y}]/android.widget.LinearLayout[1]').click()
        # self.wait_xpath('//android.widget.TextView[@text="立即预订"]')[1].click()
        # self.wait_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()

        # num = random.randint(300, 500)
        # print('随机下滑', num)

        # time.sleep(10)
        # self.my_touch(xpath='//*[@content-desc="全部"]', down=-num)
        # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]',
        #               down=-random.randint(300, 2000))
        # self.my_touch(xpath='//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]', down=-random.randint(300, 1000))
        # self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/title_tv"]').click()
        # nn = random.randint(1, 4)
        # print(nn)
        # self.driver.find_element_by_xpath(f'//android.widget.ListView/android.view.View[{nn}]/android.view.View[2]').click()


        # self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()



        self.random_click()
        self.wait_xpath('//android.widget.TextView[@text="立即预订"]').click()
        self.wait_xpath('//*[@content-desc="立即预订"]').click()
        name = self.wait_xpath('//android.widget.EditText[@text="请输入姓名"]')
        name.click()
        time.sleep(3)
        txt = self.random_name()
        phone1 = self.phoneNORandomGenerator()
        field = f'{txt}~{phone1}'
        self.my_send(field)#模拟键盘输入
        self.wait_xpath('//android.widget.Button[@text="立即预约"]').click()
        time.sleep(3)
        print('酒店订单下单成功')

        try:
            # 查看登入是否存在
            # 'com.yhouse.code:id/header_txt_title'
            # zf = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/header_txt_title"]')
            zf = self.driver.find_element_by_xpath('//android.widget.TextView[@text="支付"]')
        except BaseException:
            zf = None

        if zf:
            return 1
        else:
            return 0



    def random_click(self):
        time.sleep(3)  # 设置延迟方便调试
        # self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
        now = re.sub('-', '.', str(datetime.now())[:10])
        now2 = now[:5]+ str(int(now[5:7])) +'.'+ str(int(now[8:10]))
        now3 = now[:5]+ str(now[5:7]) +'.'+ str(now[8:10])

        print('now2:', now2)

        try:
            self.driver.find_element_by_xpath('//*[@content-desc="选择日期："]')
        except BaseException:
            print('没有在正确页面点击返回')
            self.wait_xpath('//android.widget.ImageView[@resource-id="com.yhouse.code:id/header_left_back"]').click()


        try:
            cc = self.driver.find_element_by_xpath(f'//*[@content-desc="{now3}"]')
            # self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
            print(cc, '今天日期存在')
        except BaseException as e:
            print(e)
            cc = None

        try:
            zz = self.driver.find_element_by_xpath(f'//*[@content-desc="{now2}"]')
            # self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
            print(zz, '今天日期存在')
        except BaseException as e:
            print(e)
            zz = None

        if zz or cc:
            try:
                self.wait_xpath('//*[@content-desc="选择日期："]/following-sibling::android.view.View').click()
                time.sleep(1)
                x = [i for i in range(100, 601, 100)]
                x1 = random.choice(x)
                x2 = x1 + 100
                """
                y最大1300
                
                24：y = [i for i in range(800,1301,100)]
                """
                y = [i for i in range(1190, 1301, 100)]
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
    # a.setup()
    # a.login()
    count = 0
    while count == 0:
        a.setup()
        zf = a.main()
        print('zf返回为：', zf)
        count = count + zf
    a.tearDown()


if __name__ == "__main__":
    run5()
