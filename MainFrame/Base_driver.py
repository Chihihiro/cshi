# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 15:01
# @Author  : Chihiro
import os
import time
import requests
import random
from appium import webdriver
from scrapy import Selector
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MainFrame.make_id_card import id_card

class Base_Driver(object):
    """手机app操作功能操作封装"""

    def __init__(self):
        self.desired_caps = {'platformName': 'Android',  # 平台名称
                             # 'deviceName': 'TNY_AL00',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                             # 'deviceName': 'MT7-TL10',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                             'deviceName': 'MuMu',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                             'noReset': True,  # 设置成False 的话会弹出需要你设置权限的弹窗默认使用True
                             'appPackage': 'com.yhouse.code',  # apk的包名
                             'appActivity': '.activity.SplashActivity',  # activity 名称
                             'unicodeKeyboard': True,
                             'resetKeyboard': True
                             }
        self.key = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16, 'A': 29,
                    'B': 30,
                    'C': 31,
                    'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38, 'K': 39, 'L': 40, 'M': 41, 'N': 42,
                    'O': 43,
                    'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48, 'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
                    'a': 29,
                    'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38, 'k': 39, 'l': 40,
                    'm': 41,
                    'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49, 'v': 50, 'w': 51, 'x': 52,
                    'y': 53,
                    'z': 54, '~': 61  # 61换行
                    }


    def setup(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)  # 设置延迟等待
        self.wait = WebDriverWait(self.driver, 10)
        self.id_card = id_card()

    def my_send(self, strs):
        """输入键盘操作"""
        for i in strs:
            time.sleep(0.1)
            self.driver.keyevent(self.key.get(i))

    def wait_xpath(self, xpath):
        """
        延迟等待10秒钟xpath的出现 时间可以在self.wait 做调整
        :param xpath: 传入xpath
        :return:  按钮
        """
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def take_screenshot(self):
        """手机截屏保存图片到文件夹↓"""
        path = os.getcwd() + '\\pngs'
        # path = os.getcwd()
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 通过时间进行命名
        screen_name = path + "\\" + rq + '.png'  # 双斜杠的意思是转译\，目的是：路径下的图像，例如：c:\文件路径\文件名.png
        try:
            self.driver.get_screenshot_as_file(screen_name)
            print("开始截图并保存")

        except Exception as e:
            print("出现异常", format(e))

    # 测试结束后执行的方法
    def tearDown(self):
        """关闭模拟器"""
        self.driver.quit()


class My_Tests(Base_Driver):
    # 测试开始前执行的方法
    """对yhouse， app的一些常用操作"""

    def __init__(self, phone=None, password=None):
        self.phone = phone
        self.password = password
        super(My_Tests, self).__init__()

    def login(self):
        """登入操作"""
        time.sleep(3)  # 设置延迟方便调试
        try:
            # 查看登入是否存在
            login = self.driver.find_element_by_xpath(
                '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[@text="登录享受更多服务"]')
        except BaseException:
            login = None
        print(login)
        if login:
            login.click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="账号登录"]').click()
            self.my_send(self.phone)
            self.my_send('~')
            self.my_send(self.password)
            self.driver.find_element_by_xpath(
                '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.TextView[3]').click()
            time.sleep(3)
            # print(self.driver.page_source)  # 把当前页给输出出来
            self.driver.find_element_by_xpath(
                '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()
        else:
            print('已经登入')
        self.alert_close()

    def my_touch(self, text="", down=0, right=0, xpath=None):
        """安住某个键滑动上下滑动
        xpath: 可传xath
        down:  down<0 往下滑动 , down>0 往上滑动
        right: right<0 往右面滑动 , right>0 往左滑动
        """
        if xpath:
            button = self.driver.find_element_by_xpath(xpath)
        else:
            button = self.driver.find_element_by_xpath(f'//android.widget.TextView[@text="{text}"]')
        Action = TouchActions(self.driver)
        Action.flick_element(button, right, down, 50).perform()

    def find_text_touch(self, text="", down=0, right=0, xpath=None, find=""):
        """安住某个键滑动上下滑动
        xpath: 可传xath
        down 和right 其中一个不写默认0
        down:  down<0 往下滑动 , down>0 往上滑动
        right: right<0 往右面滑动 , right>0 往左滑动
        down 和right 是滑动的速度
        """
        if xpath:
            button = self.driver.find_element_by_xpath(xpath)
        else:
            button = self.driver.find_element_by_xpath(f'//android.widget.TextView[@text="{text}"]')
        Action = TouchActions(self.driver)
        for i in range(100, 2500, 100):
            print('移动大小为：', i)
            if right > 0:
                Action.flick_element(button, -i, 0, abs(right)).perform()
            elif right < 0:
                Action.flick_element(button, i, 0, abs(right)).perform()
            else:
                pass
            if down > 0:
                Action.flick_element(button, -i, 0, abs(down)).perform()
            elif down < 0:
                Action.flick_element(button, i, 0, abs(down)).perform()
            else:
                pass
            html = self.driver.page_source
            info = Selector(text=html)
            buttons = info.xpath('//@text').extract()
            buttons = [i for i in buttons if i != '']
            if find in buttons:
                time.sleep(1)
                break

    def out_login(self):
        self.driver.find_element_by_xpath(
            '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]').click()
        self.driver.find_element_by_xpath(
            '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        size = self.driver.get_window_size()
        width = size["width"]
        print(width)
        height = size["height"]
        print(height)
        x1 = width * 0.5
        y1 = height * 0.9
        x2 = width * 0.5
        y2 = height * 0.3
        self.driver.swipe(x1, y1, x1, y2)
        # for i in range(2):  ###增加滑动次数，因为有时滑动不明显。这一步很有效果。2可以是更改的，如果滑动的少，可以增加滑动次数的。
        #     print(i)
        #     time.sleep(2)
        #     self.driver.swipe(x1, y1, x1, y2)
        self.driver.find_element_by_xpath(
            '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        self.driver.find_element_by_xpath(
            '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.Button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()

    def alert_close(self):
        try:
            self.driver.find_element_by_xpath('//*[@content-desc="悦会YHOUSE"]').click()
        except BaseException:
            pass

