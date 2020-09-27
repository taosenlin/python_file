# Time:2020-02-12 13:37
# Author:TSL
from selenium import webdriver
#文件名，模块名不要和现有的库名称相同
import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器

driver.get("D:\PyCharm\sel\day1\\test.html") #访问网址
time.sleep(5)


# #（1）寻找元素   根据css_selector 根据css选择器定位
# textElemnet = driver.find_element_by_css_selector("body > p:nth-child(1)")
# #打印文本信息
# print(textElemnet.text)


# #（2）寻找元素   根据xpath定位
# textElemnet = driver.find_element_by_xpath("/html/body/p[2]")
# #打印文本信息
# print(textElemnet.text)


# #（3）寻找元素  根据id定位
# inputElement = driver.find_element_by_id("a3c3b6fd-2d79-457d-a41f-93695d76d24a")
# inputElement.send_keys("陶森林")


# （4）寻找元素 根据name定位
# inputElement = driver.find_element_by_name("passwd")
# inputElement.send_keys("123")


# #（5）寻找元素 根据class_name定位
# linkElement = driver.find_element_by_class_name("dot")
# linkElement.click()


#（6）寻找元素 根据tag_name定位
# tagElement = driver.find_element_by_tag_name("p")
# #打印标签的文本内容
# print(tagElement.text)


# #（7）获取元素列表
# tagElementlist = driver.find_elements_by_tag_name("p")
# for i in tagElementlist:
#     print(i.text)


# #（8）寻找元素  根据link_text(链接文本）定位
# linkElement = driver.find_element_by_link_text("抗击肺炎")
# linkElement.click()


# #（9）寻找元素  根据链接文本（link_text)模糊搜索
# linkElement = driver.find_element_by_partial_link_text("抗击")
# linkElement.click()


# #（10）寻找元素 获取元素属性信息 get_attribute
# inputElement = driver.find_element_by_id("9d0418fe-f24d-4e3a-b58c-4e841575ab97")
# #获取元素属性，get_attribute
# elementAttribute = inputElement.get_attribute("name")
# print(elementAttribute)


# #（11）查找出整个列表
# inputElement = driver.find_elements_by_css_selector("body > div:nth-child(2) > input")
# for i in inputElement:
#     print(i.get_attribute("name"))


time.sleep(5)

driver.quit()


