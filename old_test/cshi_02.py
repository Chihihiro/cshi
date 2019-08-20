# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 17:36
# @Author  : Chihiro


from MainFrame.Base_driver import *
"""
晒图评测
"""

class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password

    def test_calculator(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="咖啡甜品特权"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="意式咖啡买一赠一"]').click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@content-desc="立即领取"]').click()
            self.driver.find_element_by_xpath(
                '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        except BaseException:
            print('已经领过了去使用')
            pass
        self.driver.find_element_by_xpath('//*[@content-desc="立即使用"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@content-desc="确认品鉴"]').click()
        self.driver.find_element_by_xpath('//*[@content-desc="晒图评测"]').click()
        # 点击一张图片
        self.driver.find_element_by_xpath(
            '//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="下一步(1张)"]').click()
        self.my_send('perfect')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="发布"]').click()
        print('发送成功')

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    phones = ['18351923285', '18351923260']
    phone = random.choice(phones)
    a = my_test('18351923260', '123456')
    a.setup()
    a.login()
    a.test_calculator()
    a.tearDown()
