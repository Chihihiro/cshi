# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro


from MainFrame.Base_driver import *

"""
迪士尼门票购买
"""

class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password

    def main(self):
        try:
            self.wait_xpath('//android.widget.TextView[@text="悦会会员"]').click()
            self.find_text_touch(text='我的会员', right=70, find="迪士尼及景区")
            self.wait_xpath('//android.widget.TextView[@text="迪士尼及景区"]').click()
            self.wait_xpath('//android.widget.TextView[@text="迪士尼门票"]').click()
            self.wait_xpath('//android.widget.TextView[@text="迪士尼乐园一日成人票"]').click()
            self.wait_xpath('//*[@content-desc="特惠购买"]').click()
            time.sleep(5)#需要多等待一会可能请求太快而失败
            # 查找今天的位置的下一位就是买明天的票
            html = self.driver.page_source
            info = Selector(text=html)
            ll = info.xpath('//@content-desc').extract()
            index_num = ll.index('今天')
            text = ll[index_num + 1]
            self.wait_xpath(f'//*[@content-desc="{text}"]').click()
            time.sleep(5)
            #填写信息
            name = self.wait_xpath('//android.widget.EditText[@text="请输入姓名"]')
            name.click()
            time.sleep(3)
            field = f'test~{self.id_card}~13524422749'
            self.my_send(field)#模拟键盘输入
            self.wait_xpath('//*[@content-desc="立即支付"]').click()
            time.sleep(2)
            print('订单下单成功')
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
