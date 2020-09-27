import time

from selenium import webdriver


def deleteAllLesson():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://localhost/mgr/login/login.html')
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_class_name('btn-success').click()
    #开始清除所有课程
    driver.implicitly_wait(1)
    while 1:
        del_btns = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        if del_btns == []:
            break
        del_btns[0].click()
        driver.find_element_by_class_name('btn-primary').click()
        time.sleep(2)

    driver.quit()


from ..cfg import *

if __name__ == '__main__':
    print()
