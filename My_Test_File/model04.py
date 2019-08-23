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
        try:
            self.wait_xpath('//android.widget.TextView[@text="悦会会员"]').click()
            self.shanghai_city()
            self.wait_xpath('//android.widget.TextView[@text="话费加油"]').click()
            self.wait_xpath('//android.widget.TextView[@text="话费充值"]').click()
            self.wait_xpath('//*[@content-desc="立即充值"]').click()
            time.sleep(5)#需要多等待一会可能请求太快而失败
            # 查找今天的位置的下一位就是买明天的票
            print('话费加油订单下单成功')
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

