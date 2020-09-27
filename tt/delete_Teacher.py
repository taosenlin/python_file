# coding:utf8
# Time:2020-07-04 20:41
# Author:TSL

from selenium import webdriver
import time

def delAllTeacher():

    driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
    driver.get("http://localhost/mgr/login/login.html")
    driver.implicitly_wait(5)
    #用户名
    # driver.find_element_by_id("username").send_keys("auto")
    #密码
    # driver.find_element_by_id("password").send_keys("sdfsdfsdf")
    #点击登录
    driver.find_element_by_css_selector(".btn.btn-success").click()
    #点击切换老师界面
    driver.find_element_by_css_selector(".nav.navbar-nav li:nth-child(2)").click()

    #删除按钮列表
    del_list = driver.find_elements_by_css_selector("tbody>.ng-scope td:nth-child(6) button:nth-child(2)")
    for i in range(len(del_list)):
        del_list1 = driver.find_elements_by_css_selector("tbody>.ng-scope td:nth-child(6) button:nth-child(2)")
        del_list1[0].click()
        driver.find_element_by_css_selector(".btn.btn-primary").click()
        time.sleep(1)
    driver.quit()


delAllTeacher()













































