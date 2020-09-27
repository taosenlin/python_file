# Time:2020-02-18 13:39
# Author:TSL

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象

driver.implicitly_wait(5)   #隐式等待5秒

driver.get("http://www.51job.com")
#访问网址
driver.find_element_by_id("kwdselectid").send_keys("python") #找到输入框并输入python
time.sleep(3)

driver.find_element_by_id("work_position_input").click() #找到地址框

driverEle = driver.find_element_by_id("work_position_click_multiple_selected")  #找到已选择地区
# time.sleep(5)
driverSli = driverEle.find_elements_by_class_name("ttag")  #找到每一个已经存在选择地区的城市
for i in driverSli:
    i.click()            #遍历每一个已经选择的城市，然后点击清除

time.sleep(5)
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()  #选择杭州
# time.sleep(5)
driver.find_element_by_id("work_position_click_bottom_save").click()  #点击确定

driver.find_element_by_css_selector(".ush button").click()  #点击搜索按钮

jobsEle = driver.find_elements_by_css_selector("#resultList div[class=el]")  #找到所有需要的职位信息
for job in jobsEle:
    jobEleSli = job.find_elements_by_tag_name("span")
    jobs = [jobEle.text for jobEle in jobEleSli]
    print('|'.join(jobs))


























time.sleep(5)

driver.quit()