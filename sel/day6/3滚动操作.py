# Time:2020-02-20 23:16
# Author:TSL

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.implicitly_wait(3)
#隐式等待3秒
driver.get("https://www.12306.cn/index/")
#访问网址

driver.execute_script("window.scrollBy(500,500)")
#window.scrollBy(x,y) 表示鼠标的滚动动作，在html页面Console下面输入即可调试




# time.sleep(5)

# driver.quit()