# Time:2020-02-17 15:52
# Author:TSL

# css选择器是浏览器用来选择元素的，我们selenium也要选择元素，也可以使用scc的选择器语法
# 来选择web元素。这种方法效率很高。是用来定义如何显示HTML元素的，HTML元素可以看作是人，
# 而CSS可以看作是衣服，根据衣服很容易判断出来人

# 在selenium元素定位中，通常更多使用XPATH，css定位方式用的比较少
# 但有时候也存在优势：
# 1、一般情况下定位速度比XPATH快
# 2、语法比XPATH更简洁


from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.get("D:\PyCharm\sel\day3\\cssStu.html")
#访问网址

print(driver.find_element_by_css_selector("#a5072709d-1f45-4ad5-b4e3-19b6de4b0398").text)
print(driver.find_element_by_css_selector("h4").text)
print(driver.find_element_by_css_selector(".by_class").text)
print(driver.find_element_by_css_selector("ul.by_class_and_tag").text)
print(driver.find_element_by_css_selector("#e4c04b0b-7119-4c7e-a5c5-6aa2be9c7368 > div > table > tbody > tr:nth-child(1) > td:nth-child(2)").text)


time.sleep(5)

driver.quit()


































