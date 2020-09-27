# Time:2020-02-13 12:58
# Author:TSL


#size  text  get_attribute()  is_displayed()

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器

driver.get("D:\PyCharm\sel\day2\\test.html") #访问网址

ele = driver.find_element_by_id("a3c3b6fd-2d79-457d-a41f-93695d76d24a")
#ele 就是一个webElement
# ele.size  #获取元素的尺寸
print("元素的尺寸 =",ele.size)   #获取元素的尺寸
print("元素的文本 =",ele.text)   #获取元素的文本
print("元素的name属性 =",ele.get_attribute("name")) #获取元素的name属性
print("元素是否可见 = ",ele.is_displayed()) #检查元素是否可见




time.sleep(5)

driver.quit()