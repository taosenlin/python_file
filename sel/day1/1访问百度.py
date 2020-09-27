# Time:2020-02-09 16:20
# Author:TSL

from selenium import webdriver
#文件名，模块名不要和现有的库名称相同
import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("松勤")#找到输入框，输入想搜索的值

driver.find_element_by_id("su").click()#点击百度一下

time.sleep(5)

driver.quit()
