# Time:2020-02-13 15:28
# Author:TSL

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器(创建浏览器驱动）

driver.get("D:\PyCharm\sel\day2\\test.html") #访问网址

# #（1）获取浏览器大小
# print(driver.get_window_size())
#
# #（2）浏览器最大化操作
# driver.maximize_window()
# time.sleep(5)


# #（3）最小化浏览器
# driver.minimize_window()
# time.sleep(5)
#
#
# #（4）获取浏览器大小
# print(driver.get_window_size())
#
#
# #（5）设定指定宽度和高度的浏览器
# driver.set_window_size(480,800) #宽度设定为480，高度设定为800
# time.sleep(5)


# driver.get("D:\PyCharm\sel\day2\\test.html")  #访问网址


#（6）控制浏览器前进
driver.forward()
time.sleep(5)

#（7）控制浏览器后退
driver.back()
time.sleep(5)

#（8）控制浏览器刷新
driver.refresh()
# time.sleep(5)



time.sleep(5)

driver.quit()