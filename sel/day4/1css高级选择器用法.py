# Time:2020-02-18 15:54
# Author:TSL

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.get("D:\PyCharm\sel\day4\\test.html")
#访问网址

























time.sleep(5)

driver.quit()