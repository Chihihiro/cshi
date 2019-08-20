# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 15:29
# @Author  : Chihiro


from MainFrame.Base_driver import *
"""
分享朋友圈快照
"""

class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password
        self.wait = WebDriverWait(self.driver, 10)

    def test_course(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="会员社区"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="关注"]').click()
        time.sleep(20)
        self.my_touch('推荐好友', down=-200)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="分享"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="朋友圈快照"]').click()
        time.sleep(3)
        # 点击图片截屏
        self.driver.find_element_by_xpath('//*[@content-desc="图片"]').click()
        time.sleep(3)
        self.take_screenshot()
        self.driver.find_element_by_xpath('//*[@content-desc="返回"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text="发表"]').click()


if __name__ == "__main__":
    phones = ['18351923285', '18351923260']
    phone = random.choice(phones)
    a = my_test(phone='18351923260', password='123456')
    a.setup()
    a.login()
    a.test_course()
    a.tearDown()
