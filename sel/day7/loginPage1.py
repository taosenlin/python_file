# Time:2020-02-23 22:01
# Author:TSL

from sel.day7.basePage import BasePage
from selenium.webdriver.common.by import  By
from selenium import  webdriver

class LoginPage(BasePage):
    def __init__(self,driver,url):
        super.(LoginPage,self).__init__(driver,url)  #调用父类的构造方法
        self.open("管理员登录")
        self.nameInp = (By.ID,"username")  #登录输入框
        self.pwdInp = (By.ID,"password")   #密码输入框
        self.loginBtu = (By.CLASS_NAME,"btn.btn-success")   #登录按钮
    def login(self):
        """
        登录测试用例
        :return:
        """
        #输入用户名
        ele = self.find_element(self.nameInp,5)
        self.send_keys(ele,"auto")
        #输入密码
        ele = self.find_element(self.pwdInp,5)
        self.send_keys(ele,"sdfsdfsdf")
        #点击登录按钮
        self.find_element(self.loginBtu,5).click()


if __name__ == '__main__':
    driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
    lp = LoginPage(driver,"http://localhost/mgr/login/login.html")
    lp.login()