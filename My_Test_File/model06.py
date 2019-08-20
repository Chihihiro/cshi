# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro


from MainFrame.Base_driver import *

"""
会员解锁
"""

class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password

    def main(self):
        try:
            self.wait_xpath('//android.widget.TextView[@text="悦会会员"]').click()
            self.wait_xpath('//android.widget.TextView[@text="解锁/激活更多权益"]').click()
            self.wait_xpath('//*[@content-desc="b_btn"]').click()
            time.sleep(3)
            self.wait_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.Button[1]').click()
            time.sleep(3)
            print('订单下单成功')
        except BaseException as e:
            print(e)



if __name__ == "__main__":
    a = my_test(phone='13524422749', password='123456')
    a.setup()
    a.login()
    a.main()
    a.tearDown()
