# coding:utf8
# Time:2020-03-29 23:38
# Author:TSL

from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\ruanjiananzhuang\chromedriver.exe')

driver.get('http://localhost/mgr/login/login.html')
# driver.find_element_by_id('username').send_keys('auto')
# driver.find_element_by_id('password').send_keys(r'sdfsdfsdf')
driver.find_element_by_tag_name('button').click()
time.sleep(3)

driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
time.sleep(1)

s1 = driver.find_element_by_css_selector("input[ng-model='addData.name']")
s1.send_keys('计算机科学')
time.sleep(1)

s2 = driver.find_element_by_css_selector('textarea[ng-model="addData.desc"]')
s2.send_keys('计算机科学1')
time.sleep(1)

s3 = driver.find_element_by_css_selector('input[ng-model="addData.display_idx"]')
s3.send_keys('1')
time.sleep(1)

driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()
time.sleep(3)


coursrList = []
courseName = driver.find_elements_by_css_selector('tbody>tr>td:nth-child(2)>span')
for i in courseName:
    print(i.text)
    coursrList.append(i.text)


driver.implicitly_wait(10)
driver.quit()



































































