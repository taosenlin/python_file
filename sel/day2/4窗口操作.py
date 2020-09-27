# Time:2020-02-13 16:17
# Author:TSL

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器（创建浏览器驱动）

driver.get("D:\PyCharm\sel\day2\\test.html")
#访问网址

#(1)获取当前窗口的title
print(driver.title)

#(2)获取当前窗口的url
print(driver.current_url)

#(3)截屏，截取整个页面
driver.get_screenshot_as_file("./all.png")

#(4)截屏，截取单个元素
ele = driver.find_element_by_css_selector("body > div:nth-child(2)")
ele.screenshot("./ele.png")



time.sleep(5)

driver.quit()


