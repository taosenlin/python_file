# Time:2020-02-20 22:17
# Author:TSL

#对于通过input标签实现的上传功能，可以将其看作是一个输入框，即通过send_keys指定
#本地文件路径的方式实现文件上传

#####################################################################

# 对于通过操作系统控件的方式上传文件，比如 https://tinypng.com/可采用
# 直接发送键盘消息给当前应用程序
# 前提是浏览器必须是当前应用
# pip install pypiwin32
#
# import win32com.client
# shell=win32com.client.Dispatch("WScript.Shell")
# shell.Sendkeys(r'd:\baidu.png'+'\n')

#####################################################################


from selenium import webdriver
import win32com.client                  #上传文件所需模块

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.implicitly_wait(3)
#隐式等待3秒
driver.get("https://tinypng.com/")
#访问网址

#触发上传文件的操作
driver.find_element_by_css_selector("#top .icon").click()
sh = win32com.client.Dispatch("WScript.shell")
time.sleep(3)
sh.Sendkeys("D:\PyCharm\sel\day6\qqjt.png\n")   #无目标的，单纯的敲击键盘
time.sleep(3)












# time.sleep(3)

# driver.quit()
















