# Time:2020-02-18 23:21
# Author:TSL

#xpath语法
# xpath通过"路径表达式"来选择节点。在形式上，"路径表达式"与传统的文件系统非常类似。

# 相对路径：即相对于上下文节点的路径
# //ul/li
# 绝对路径：即从根目录开始的完整的路径
# /html/body/div/ul/li


# .表示当前节点
# ..表示当前节点的父节点
# ./html/body/div/..

# @表示选择属性
# //p[@title='f']


# /表示选择根节点，也可以选择直接子元素，相当于css中的>
# //表示选择任意位置的某个节点，也可以选择后代元素，相当于css中div p中的空格

# *表示通配符




from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.get("D:\PyCharm\sel\day5\\xpathStu.html")
#访问网址





time.sleep(5)

driver.quit()