#coding : utf8
#Author : taosenlin
#Time : 2020/5/18 11:27

import unittest
from login_Page import LoginPage
from selenium import webdriver
import time


# 摩云会议登录创会测试
class TestMeetingPage(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome("E:\chromedriver.exe")
        pass

    def tearDown(self):
        # self.driver.quit()
        pass

    def testmeeting(self,username,password,num):
        # driver = self.driver
        driver = webdriver.Chrome("E:\chromedriver.exe")
        driver.implicitly_wait(10)
        url = "https://webmeeting.moooo.com.cn/"
        # username = "taosenlin@kedacom.com"
        # password = "061012tsl"
        # num = "0000951"
        testmt_Page = LoginPage(driver,url)
        #打开登录页面
        testmt_Page.open(url)
        time.sleep(3)
        #登录摩云会议
        testmt_Page.username(username)
        testmt_Page.password(password)
        testmt_Page.login_button()
        time.sleep(3)
        #输入会议号，创会
        testmt_Page.inp_num(num)
        testmt_Page.join_cli()
        time.sleep(5)



































































































