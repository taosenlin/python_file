# coding:utf8
# Time:2020-03-31 22:19
# Author:TSL

from selenium import webdriver
import time

def deleteAllCourse():

    driver = webdriver.Chrome(r'D:\ruanjiananzhuang\chromedriver.exe')

    driver.get('http://localhost/mgr/login/login.html')
    # driver.find_element_by_id('username').send_keys('auto')
    # driver.find_element_by_id('password').send_keys(r'sdfsdfsdf')
    driver.find_element_by_tag_name('button').click()
    driver.implicitly_wait(3)

    while True:
        delete_list = driver.find_elements_by_css_selector('tbody>tr>td:nth-child(4)>button:nth-child(2)')
        if delete_list:
            delete_list[0].click()
            driver.find_element_by_css_selector('button[class="btn btn-primary"]').click()
            time.sleep(1)
        else:
            break

    driver.implicitly_wait(10)
    driver.quit()


deleteAllCourse()