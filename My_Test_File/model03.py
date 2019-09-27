# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro


from MainFrame.Base_driver import *

"""
爱奇艺VIP会员年卡
"""

class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password

    def main(self):
        # try:
        self.wait_xpath('//android.widget.TextView[@text="悦会会员"]').click()
        self.shanghai_city()
        self.wait_xpath('//android.widget.TextView[@text="娱乐追剧特权"]').click()
        time.sleep(1)
        self.wait_xpath('//android.widget.TextView[@text="爱奇艺VIP会员年卡"]').click()
        time.sleep(3)
        self.wait_xpath('//*[@content-desc="特惠购买"]').click()
        time.sleep(5)
        print('爱奇艺VIP会员年卡订单下单成功')
        try:
            # zf = self.driver.find_element_by_xpath(
            #     '//android.widget.TextView[@resource-id="com.yhouse.code:id/header_txt_title"]')
            zf = self.driver.find_element_by_xpath('//android.widget.TextView[@text="支付"]')
        except BaseException:
            zf = None

        if zf:
            return 1
        else:
            return 0.5

    def ref(self):
        # 'com.yhouse.code:id/header_left_back'
        fan = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.yhouse.code:id/header_left_back"]')
        fan.click()



def run3():
    a = my_test(phone='13524422749', password='123456')
    # a.login()
    count = 0
    while count == 0:
        a.setup()
        zf = a.main()
        print('zf返回为：', zf)
        count = count + zf
    a.tearDown()


if __name__ == "__main__":
    run3()
