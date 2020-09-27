# Time:2020-02-23 18:39
# Author:TSL

"""
维护登录页
"""

from sel.day7.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):
    def login(self):
        """
        登录测试用例
        :return:
        """
        self.open("管理员登录")
        ele = self.find_element((By.ID,"username"),5)
        self.send_keys(ele,"auto")
        ele = self.find_element((By.ID,"password"),5)
        self.send_keys(ele,"sdfsdfsdf")


if __name__ == '__main__':
    driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
    lp = LoginPage(driver, "http://localhost/mgr/login/login.html")
    lp.login()

























































