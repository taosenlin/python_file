# Time:2020-02-20 23:23
# Author:TSL

#################################################################################
#鼠标事件
# 用selenium做自动化，有时候会遇到需要模拟鼠标操作才能进行的情况，比如单击、双击、
# 点击鼠标右键、拖拽等等。selenium给我们提供了一个类来处理这类时间——ActionChains

# ActionChains 类提供了鼠标操作的常用方法：
#
# perform() : 执行操作
# context_click() : 右击
# double_click() : 双击
# drag_and_drop() : 拖动     #操作比较特殊
# move_to_element() : 鼠标悬停(移动到某个需要悬停元素）



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#ActionChains类提供了鼠标操作的常用方法

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.implicitly_wait(5)
#隐式等待5秒
# driver.get("https://www.baidu.com/")
#访问网址
driver.get("D:\PyCharm\sel\day6\\test.html")
#鼠标拖动操作使用


#定位到想要操作的元素
# setting = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(setting).perform()  #鼠标悬停
# ActionChains(driver).double_click(setting).perform()   #鼠标双击
# ActionChains(driver).context_click(setting).perform()  #鼠标右击


#拖动操作：1、定位到起始元素
startEle = driver.find_element_by_id("blackSquare")
#拖动操作：2、定位的目标元素
toEle = driver.find_element_by_id("targetEle")

ActionChains(driver).drag_and_drop(startEle,toEle).perform()




# time.sleep(5)

# driver.quit()