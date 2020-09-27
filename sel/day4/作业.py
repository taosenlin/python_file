# Time:2020-02-18 22:15
# Author:TSL

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象

driver.implicitly_wait(5)   #隐式等待5秒

driver.get("http://www.51job.com")
#访问网址

driver.find_element_by_css_selector(".more").click()
#点击高级搜索
driver.find_element_by_id("kwdselectid").send_keys("python")
#输入python
driver.find_element_by_id("work_position_input").click()
#点击进入选择地址

citySel = driver.find_element_by_id("work_position_click_multiple_selected")
#找到已选城市栏（列表）
# time.sleep(5)
cityEle = driver.find_elements_by_class_name("ttag")
for i in cityEle:
    i.click()        #逐个点击，清空已选列表
time.sleep(3)
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
#点击选择杭州
driver.find_element_by_id("work_position_click_bottom_save").click()
#点击确定

driver.find_element_by_css_selector(".rtit.r1").click()
#点击历史记录刷新一下页面以免输入python会有下拉框遮挡

driver.find_element_by_id("funtype_click").click()
#点击职能类别选择
driver.find_element_by_id("funtype_click_center_right_list_category_0100_0100").click()
#点击选择计算机软件
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_0106").click()
#点击选择高级计算机软件
driver.find_element_by_id("funtype_click_bottom_save").click()
#点击确定

driver.find_element_by_id("cottype_list").click()
#点击选择公司性质
driver.find_element_by_css_selector("#cottype_list span.li[data-value=\"04\"]").click()
#点击选择公司
driver.find_element_by_id("workyear_list").click()
#点击选择工作年限
driver.find_element_by_css_selector("#workyear_list span.li[data-value=\"02\"]").click()
#选择1-3年

driver.find_element_by_css_selector(".btnbox span").click()
#点击搜索按钮

jobsList = driver.find_elements_by_css_selector("#resultList div[class=el]")
#搜索出所有职位列表
for jobs in jobsList:              #将所获取的元素全部遍历一遍
    jobEle = jobs.find_elements_by_tag_name("span")   #遍历后根据span找到需要的信息
    job =  [jobSli.text for jobSli in jobEle]         #再次遍历获取所需要的信息
    print('|'.join(job))    #按格式打印


time.sleep(5)

driver.quit()