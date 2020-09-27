#coding : utf8
#Author : taosenlin
#Time : 2020/5/18 9:33

"""
# from selenium import webdriver
# import time
"""

"""
# driver = webdriver.Chrome("E:\chromedriver.exe")
# 
# driver.get("http://www.baidu.com")
# 
# time.sleep(3)
# driver.quit()
"""


class BasePage:
    """
    BasePage基类:所有的page都应该继承该类
    """
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.timeout = 10

    #定位方法的封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    #输入参数的封装
    def input_text(self,loc,text):
        self.find_element(*loc).send_keys(text)

    def clear(self,loc):
        self.find_element(*loc).clear()

    #获取标题的封装
    def get_title(self):
        return self.driver.title

    def click(self,loc):
        self.find_element(*loc).click()
























































































