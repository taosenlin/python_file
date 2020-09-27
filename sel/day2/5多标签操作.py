# Time:2020-02-13 16:36
# Author:TSL

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器（创建浏览器驱动）

driver.get("http://www.baidu.com")
#访问网址

ele = driver.find_element_by_id("kw").send_keys("松勤")
#输入搜索元素-松勤

search_ele = driver.find_element_by_id("su").click()
#点击搜索按钮
time.sleep(3)

#搜索松勤官网
driver.find_element_by_css_selector("#\\34  > h3 > a > em").click()

time.sleep(3)

# print(driver.title)

# #(1)获取当前标签页的句柄
# current_handle = driver.current_window_handle
# print("当前标签页句柄",current_handle)
# print("当前标签页title",driver.title)
# # 当前标签页句柄 CDwindow-D6AEF7EBB8972DF84D56703407E82495
# # 当前标签页title 松勤_百度搜索



#(2)获取所有标签页句柄
handle_list = driver.window_handles

for i in handle_list:
    driver.switch_to.window(i) #根据句柄切换到对应的标签页
    current_handle = driver.current_window_handle
    print("当前标签页句柄",current_handle)
    print("当前标签页title",driver.title)


# (3)driver.close()  #关闭当前标签页


time.sleep(5)

driver.quit()   #退出整个浏览器