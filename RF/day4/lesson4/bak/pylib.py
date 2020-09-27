import time

from selenium import webdriver

#清除所有课程

def deleteAllLesson():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)

    #先登录
    driver.get('http://localhost/mgr/login/login.html')
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn-success').click()

    driver.implicitly_wait(1)
    #开始删除课程
    while True:
        delbtns = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        #如果课程删除完毕，delbutns就为空[]
        if delbtns==[]:
            #退出循环
            break
        delbtns[0].click()
        #点击确认按钮
        driver.find_element_by_css_selector('.btn-primary').click()
        time.sleep(1)
    driver.implicitly_wait(10)
    driver.quit()

if __name__ == '__main__':

    deleteAllLesson()
