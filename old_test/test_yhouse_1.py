#coding=utf-8
import time
from appium import webdriver
import requests
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
from scrapy import Selector
"""
购买迪斯尼门票
这个脚本写的早没使用框架
"""

#模拟按键对应的值调用my_send()
kk = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16, 'A': 29, 'B': 30, 'C': 31,
      'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38, 'K': 39, 'L': 40, 'M': 41, 'N': 42, 'O': 43,
      'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48, 'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54, 'a': 29,
      'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38, 'k': 39, 'l': 40, 'm': 41,
      'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53,
      'z': 54, 'tab': 61, '~': 61
      }

class MyTests():
    # 测试开始前执行的方法
    def __init__(self, phone):
        self.phone = phone


    def my_send(self, strs):
        for i in strs:
            time.sleep(0.1)
            self.driver.keyevent(kk.get(i))

    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        # 'platformVersion': '4.4.2',  # 系统版本号
                        # 'deviceName': 'TNY_AL00',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        # 'deviceName': 'MT7-TL10',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'deviceName': 'MuMu',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'noReset': True, #设置成False 的话会弹出需要你设置权限的弹窗默认使用True
                        'appPackage': 'com.yhouse.code',  # apk的包名
                        'appActivity': '.activity.SplashActivity',  # activity 名称
                        'unicodeKeyboard': True,
                        'resetKeyboard': True
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8) #设置延迟等待

    def get_yzm(self):
        try:
            url = 'http://api-test.yhouse.com/m/internal/smscode/' + self.phone
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'Host': 'api-test.yhouse.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
            pw = requests.get(url, headers=header).text
        except BaseException:
            print('请求失败再来一次')
            time.sleep(1)
            self.get_yzm()

        return pw

    def login(self):
        time.sleep(3)#设置延迟方便调试
        try:
            #查看登入是否存在
            login = self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[@text="登录享受更多服务"]')
        except BaseException:
            login = None
        print(login)
        if login:
            login.click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="账号登录"]').click()
            self.my_send(self.phone)
            self.my_send('~123456')

            self.driver.find_element_by_xpath(
                '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.TextView[3]').click()
            time.sleep(3)
            print(self.driver.page_source)  # 把当前页给输出出来
            self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()
        else:
            print('已经登入')

    def my_touch(self):

        button = self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的会员"]')
        Action = TouchActions(self.driver)

        """从button元素像下滑动200元素，以50的速度向下滑动"""
        for i in range(100, 1500, 100):
            print('移动大小为：', i)
            Action.flick_element(button, -i, 0, 50).perform()
            html = self.driver.page_source
            info = Selector(text=html)
            buttons = info.xpath('//@text').extract()
            buttons = [i for i in buttons if i != '']
            if '票务出行特权' in buttons:
                time.sleep(2)
                break


    def test_calculator(self):
        self.my_touch()
        time.sleep(3)

        print('huadong ~~~~~')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="票务出行特权"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="迪士尼"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="上海迪士尼门票"]').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[13]/android.view.View[2]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@content-desc='今天 ¥0.01']").click()

        print('开始填写身份证')
        time.sleep(3)
        # self.driver.find_element_by_xpath("//*[@content-desc='+']").click()
        name = self.driver.find_element_by_xpath('//android.widget.EditText[@text="请输入姓名"]')
        name.click()
        time.sleep(3)
        field = 'chihiro~310225199212246617~18939862542'
        self.my_send(field)#模拟键盘输入

        self.driver.find_element_by_xpath('//*[@content-desc="立即支付"]').click()
        time.sleep(2)


        self.driver.find_element_by_xpath('//android.view.ViewGroup[1]/android.widget.TextView[@text="0.01 元"]').click()
        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()

        self.yy()#强行刷出yhouse 收款
        self.zhifu()#强行刷出支付
        print('购买成功')

    def yy(self):

        try:
            yhouse = self.driver.find_element_by_xpath('//*[@text="上海悦会信息科技有限公司"]')
        except BaseException:
            yhouse = None
        if yhouse is None:
            self.driver.find_element_by_xpath('//*[@content-desc="返回"]').click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@text="支付宝支付"]').click()
            self.driver.find_element_by_xpath('//*[@text="微信支付"]').click()
            self.driver.find_element_by_xpath(
                '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]').click()
            self.yy()

    def zhifu(self):
        self.driver.find_element_by_xpath('//*[@text="立即支付"]').click()
        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]').click()
        self.my_send('408')
        time.sleep(3)
        self.my_send('828')
        try:
            zf = self.driver.find_element_by_xpath('//*[@text="返回商家"]')
            zf.click()
        except BaseException:
            zf = None
        if zf is None:
            time.sleep(3)
            self.zhifu()



    def out_login(self):
        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]').click()
        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
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

        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.Button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]').click()

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    a = MyTests('18351923260')
    a.setUp()
    a.login()
    a.test_calculator()
    a.tearDown()
