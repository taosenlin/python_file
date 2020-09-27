#coding : utf8
#Author : taosenlin
#Time : 2020/5/18 15:35

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BasePage(object):
    def __init__(self,driver,base_url="https://webmeeting.moooo.com.cn/"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10

    def open(self):
        url = self.base_url
        self.driver.get(url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)


class LoginPage(BasePage):
    username_loc = (By.ID,'userAccount')
    password_loc = (By.ID,'password')
    login_loc = (By.ID,'LoginBtn')
    num_loc = (By.ID,'meetingNumber')
    join_btn = (By.CSS_SELECTOR,'div [class="ncontent"] #JoinBtn')

    # 输入用户名
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录
    def type_login(self):
        self.find_element(*self.login_loc).click()

    def type_num(self,num):
        self.find_element(*self.num_loc).send_keys(num)

    #点击创会
    def type_cli(self):
        self.find_element(*self.join_btn).click()


def test_user_login(driver,username,password,num):
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_login()
    login_page.type_num(num)
    login_page.type_cli()
    time.sleep(5)

def main():
    driver = webdriver.Chrome("E:\chromedriver.exe")
    driver.implicitly_wait(10)
    username = "taosenlin@kedacom.com"
    password = "061012tsl"
    num = "0000951"
    test_user_login(driver,username,password,num)
    time.sleep(3)

    # driver.quit()

if __name__ == '__main__':
    main()




















































































