# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro


from MainFrame.Base_driver import *

"""
话费加油
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
        self.wait_xpath('//android.widget.TextView[@text="话费加油"]').click()
        time.sleep(1)
        self.wait_xpath('//android.widget.TextView[@text="话费充值"]').click()
        time.sleep(1)
        self.wait_xpath('//*[@content-desc="立即充值"]').click()
        time.sleep(3)
        try:
            zf = self.driver.find_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.yhouse.code:id/header_txt_title"]')
            # zf = self.driver.find_element_by_xpath('//android.widget.TextView[@text="爱奇艺VIP会员年卡"]')
        except BaseException:
            zf = None

        if zf:
            return 1
        else:
            return 0.5



def run4():
    a = my_test(phone='13524422749', password='123456')
    # a.setup()
    # a.login()
    # a.main()
    count = 0
    while count == 0:
        a.setup()
        zf = a.main()
        print('zf返回为：', zf)
        count = count + zf
    a.tearDown()


if __name__ == "__main__":
    run4()

