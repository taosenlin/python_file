# Time:2020-02-19 19:21
# Author:TSL

#############################################################################
# 警告框分三种：
#
# 一、点击显示对话框
# 对话框只有一个确定按钮（无法点击） 此类属于浏览器的一个控件，不是html标签元素
#
# 二、点击显示确认框
# 确认框有俩个按钮：确定、取消
#
# 三、点击显示提示框
# 提示框有一个输入部分以及 俩个按钮：确定、取消

#############################################################################
#警告框处理
# 在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，具体做法
# 是使用switch_to.alert方法定位到alert/confirm/prompt，然后使用text/accept/dismiss
# /send_keys等方法进行操作

# text:返回alert/confirm/prompt中的文字信息
# accept():接受现有警告框
# dismiss():解散现有警告框
# send_keys(keysToSend):发送文本至警告框

#############################################################################










from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.implicitly_wait(5)
#隐式等待5秒
driver.get("D:\PyCharm\sel\day6\\警告框.html")
#访问网址


# #触发对话框
# driver.find_element_by_id("bu1").click()
# al = driver.switch_to.alert
# time.sleep(3)
# al.accept()     #确认对话框


# #触发确认框
# driver.find_element_by_id("bu2").click()
# al = driver.switch_to.alert
# al.accept()   #确认对话框
# driver.find_element_by_id("bu2").click()
# al.dismiss()  #取消对话框


# #触发提示框
# driver.find_element_by_id("bu3").click()
# al = driver.switch_to.alert
# # time.sleep(5)
# al.send_keys("生活越来越美好")
# # time.sleep(5)
# al.accept()    #确认对话框



time.sleep(5)

driver.quit()