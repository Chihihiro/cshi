# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:18
# @Author  : Chihiro


from MainFrame.Base_driver import *
from iosjk import *
from engines import choise_engine


class my_test(My_Tests):

    def __init__(self, phone, password):
        super(my_test, self).__init__()
        self.phone = phone
        self.password = password

    def main(self):
        # try:
        # self.kill_advert()
        names = [
            ['0元专区', '¥'], ['星爸爸', '¥'], ['话费充值', '元'],['交通出行','￥', '精选'],
            ['全国加油', '元'],
            ['影音追剧', '¥'],
            ['口碑', '¥'],
            ['外卖', '¥'],
            ['奶茶/冰淇淋', '¥'],
            ['肯德基', '￥', '精选'],
            ['休闲零食', '元'],
            ['超市便利', '¥'],
            ['上海迪士尼', '￥', '精选'],
            ['考拉海淘', '¥'],


        ]
        right_inerest_type = []

        for name in names:
            print(name[0])
            self.wait_xpath(f'//android.widget.TextView[@text="{name[0]}"]').click()
            # self.shanghai_city()
            time.sleep(10)
            html = self.driver.page_source
            print(html)
            if name[1] in html:
                print(name[1])
                right_inerest_type.append([name[0], 'pass'])
            else:
                right_inerest_type.append([name[0], 'warning'])
            try:
                if name[0] == '考拉海淘':
                    self.wait_xpath('//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]').click()
                else:
                    back = self.wait_xpath(
                        '//android.widget.ImageView[@resource-id="com.yhouse.code:id/web_back_btn"]')
                    back.click()
            except BaseException as e:
                print(e)
            if len(name) == 3:
                self.wait_xpath(f'//android.widget.TextView[@text="{name[2]}"]').click()
        print(right_inerest_type)
        df = pd.DataFrame(right_inerest_type)
        df.columns = ['right_interest', 'pass_type']
        to_sql('right_and_interest', choise_engine, df, type='update')







def run2():
    for iii in range(1000000):
        a = my_test(phone='13524422749', password='123456')
        # a.login()
        a.setup()
        a.main()
        a.tearDown()


if __name__ == "__main__":
    run2()
