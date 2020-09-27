# Time:2020-02-21 12:18
# Author:TSL

#键盘事件
# Keys()类提供了键盘上几乎所有按键的方法，前面了解到，send_keys()方法可以用来
# 模拟键盘输入，除此之外，我们还可以用它来输入键盘上的按键，甚至是组合键，如
# Ctrl+A、Ctrl+C等
#
# 以下为常用的键盘操作：
# send_keys(Keys.BACK_SPACE) 删除键(BackSpace)
#
# send_keys(Keys.SPACE) 空格键(Space)
#
# send_keys(Keys.TAB) 制表键(Tab)
#
# send_keys(Keys.ESCAPE) 回退键(Esc)
#
# send_keys(Keys.ENTER) 回车键(Enter)
#
# send_keys(Keys.CONTROL,'a') 全选(Ctrl+A)
#
# send_keys(Keys.CONTROL,'c') 复制(Ctrl+C)
#
# send_keys(Keys.CONTROL,'x') 剪切(Ctrl+X)
#
# send_keys(Keys.CONTROL,'v') 粘贴(Ctrl+V)
#
# send_keys(Keys.F1) 键盘F1
#........
# send_keys(Keys.F12) 键盘F12




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#导入Keys类

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.implicitly_wait(5)
#隐式等待5秒
driver.get("https://www.baidu.com/")
#访问网址

#定位输入框
inpEle = driver.find_element_by_id("kw")
time.sleep(1)

#输入文本内容
inpEle.send_keys("selenium")
time.sleep(1)

#全选
inpEle.send_keys(Keys.CONTROL,"a")
time.sleep(1)

#剪切
inpEle.send_keys(Keys.CONTROL,"x")
time.sleep(1)

#再次输入文本内容
inpEle.send_keys("python")
time.sleep(1)

#粘贴
inpEle.send_keys(Keys.CONTROL,"v")





# time.sleep(5)

# driver.quit()
