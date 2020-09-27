#coding : utf8
#Author : taosenlin
#Time : 2020/5/18 10:46

from selenium.webdriver.common.by import By
from base_Page import BasePage
#登录模块继承基础模块

class LoginPage(BasePage):
    username_loc = (By.ID,'userAccount')
    password_loc = (By.ID,'password')
    login_loc = (By.ID,'LoginBtn')
    num_loc = (By.ID, 'meetingNumber')
    join_btn = (By.CSS_SELECTOR, 'div [class="ncontent"] #JoinBtn')

    # 定义打开登录页面方法
    # def _open(self):
    #     url = self.base_url
    #     self.driver.get(url)
        # self.driver.switch_to.frame('摩云会议')

    # 定义open方法，调用_open()进行打开
    def open(self,url):
        # self._open()
        self.driver.get(url)

    def username(self,username):
        self.clear(self.username_loc)
        self.input_text(self.username_loc,username)

    def password(self,password):
        self.input_text(self.password_loc,password)

    def login_button(self):
        self.click(self.login_loc)

    def inp_num(self,num):
        self.input_text(self.num_loc,num)

    def join_cli(self):
        self.click(self.join_btn)




























































































