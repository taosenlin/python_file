# Time:2020-02-18 13:13
# Author:TSL

from selenium import webdriver
from selenium.webdriver.support.select import Select      #下拉框中查找值时使用

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.get("D:\PyCharm\sel\day3\\selectStu.html")
#访问网址

ele = driver.find_element_by_id("bc288089-c52d-497b-aa4d-71f81b24faa3")
# Select(ele).select_by_value("3")        #根据value值寻找
Select(ele).select_by_visible_text("3333333")  #根据下拉框的内容寻找

time.sleep(5)

driver.quit()











