# coding:utf8
# Time:2020-03-27 7:37
# Author:TSL

from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\ruanjiananzhuang\chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.vmall.com/index.html')
time.sleep(5)

comEle = driver.find_elements_by_xpath('//div[@class="span-968 fl"] //li //div')
time.sleep(10)
# print(comEle)
for com in comEle:
    time.sleep(5)
    print(com.text)

time.sleep(5)
driver.quit()