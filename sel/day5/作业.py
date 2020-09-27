# Time:2020-02-19 14:20
# Author:TSL

from selenium import webdriver
from  selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
#访问网址

driver.implicitly_wait(5)
#隐式等待5秒

startCity = driver.find_element_by_id("fromStationText")
#出发城市
startCity.click()
#聚焦输入框
startCity.clear()
#清除默认值
startCity.send_keys("南京南\n")
#输入出发城市名称


toCity = driver.find_element_by_id("toStationText")
#到达城市
toCity.click()
#聚焦输入框
toCity.clear()
#清除默认值
toCity.send_keys("杭州东\n")
#输入到达城市


startTime = driver.find_element_by_id("cc_start_time")
#找到出发时间选择框
Select(startTime).select_by_visible_text("06:00--12:00")
#根据下拉框选择出发时间

trueTime = driver.find_element_by_css_selector("#date_range li:nth-of-type(2)")
trueTime.click()
#选择当前时间的下一天


tranEle = driver.find_elements_by_xpath("//tbody[@id=\"queryLeftTable\"]//td[4][@class]/../td[1]//a")
#找到有票的车次对应的车次号
for i in tranEle:
    print(i.text)


time.sleep(5)

driver.quit()