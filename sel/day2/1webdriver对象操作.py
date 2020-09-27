# Time:2020-02-10 21:40
# Author:TSL

#clear()  send_keys()  click()   submit()

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器

# driver.get("D:\PyCharm\sel\day2\\test.html") #访问网址

# #（1）寻找元素，找到用户名输入框，并输入文本
# driver.find_element_by_id("a3c3b6fd-2d79-457d-a41f-93695d76d24a").send_keys("这是用户名")
# time.sleep(3)
#
# #（2）clear() 清除输入框内容
# driver.find_element_by_id("a3c3b6fd-2d79-457d-a41f-93695d76d24a").clear()

driver.get("http://www.baidu.com")   #访问百度网址

ele = driver.find_element_by_id("kw")
ele.send_keys("松勤")
# (3)ele.submit() #提交表单的功能





time.sleep(5)

driver.quit()