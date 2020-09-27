# coding:utf8
# Time:2020-07-02 22:02
# Author:TSL

# 1、请写代码， 用if语句判断字符串变量var的长度是否大于10，并且其中是否包含'ok'，如果两个条件都满足，就打印ok

"""
var = input("请输入相关字符串:")
if len(var)>10 and 'ok' in var:
    print('ok')
"""


# 2、下面的列表里面包含了一些字符串元素

"""
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
# 请用for循环 写一段代码打印其中所有包含ok的字符串元素

for i in info:
    if 'ok' in i:
        print("此字符串元素中包含ok:",i)
"""


# 3、下面的列表里面包含了一些字符串元素

"""
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
# 请用while 循环 写一段代码打印其中所有包含ok的字符串元素

i = 0
while i < len(info):
    if 'ok' in info[i]:
        print("此字符串元素中有ok:",info[i])
    i += 1
"""


# 4、下面的函数目的是把参数字符串倒序返回，请补全代码，完成功能
# 下面的程序用来将字符串倒序，
# 请补全代码

"""
def reverseStr(source):
    # 将字符串中的每个字符放入列表中
    tmp = [c for c in source]
    # 列表倒序
    tmp.reverse()
    return ''.join(tmp)
print (reverseStr('hello'))
"""


# 5、这样的字符串

"""
info = '姓名=小王&年龄=16&身高=175'
# 用一行代码，得到其中的年龄数字，不要数索引
str = info.split('&')
str1 = str[1].split('=')
print(str1[1])
"""


# 6、如下变量对应了 学生的姓名、年龄和身高

"""
name   = '小明'
age    = 16
height = 170
# 用一行代码，打印出如下格式的字符串
# 姓名=xx&年龄=xx&身高=xx

print("姓名=%s&年龄=%d&身高=%d" %(name,age,height))
"""


# 7、浏览器进入网页云音乐  https://music.163.com/
# 在首页的发现音乐菜单，点击进入排行榜>云音乐新歌版
# 查看排名前三的歌曲下的评论，在精彩评论部分找到点赞数量最高的评论，获取评论作者，内容，时间和当前点赞数量

"""
from selenium import webdriver
import time
import re

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
driver.get("https://music.163.com/")
driver.implicitly_wait(5)

#点击排行榜
driver.find_element_by_css_selector(".nav li:nth-child(2)").click()
time.sleep(1)
#切换到iframe
iframe = driver.find_element_by_id("g_iframe")
driver.switch_to.frame(iframe)
#点击云音乐新歌榜
driver.find_element_by_css_selector('div[class^="n-minelst"] ul:nth-child(2) li:nth-child(2)').click()


#获取点赞数列表
com_list = driver.find_elements_by_xpath('//div[@class="rp"]/a[1]')
#在评论列表中循环获取评论的点赞数
thu_list = []
for ele in com_list:
    thu_list.append(ele.text)
# print(thu_list)
#去除点赞数括号,并获取最大点赞数
num_list = []
for ele1 in thu_list:
    if ele1 != '':
        # print(ele1)
        ele2 = re.findall(r'[(](.*?)[)]',ele1)
        # print(ele2[0])
        num_list.append(int(ele2[0]))
# print(num_list.index((max(num_list))))
#当前最大点赞数
num_max = max(num_list)
# print(num_max)
#获取评论列表
com_list = driver.find_elements_by_xpath('//div[@class="cmmts j-flag"]/div')
# print(com_list)
#根据最大点赞数的下标，找到点赞最多的评论
num1 = com_list[num_list.index((max(num_list)))]
# print(num1)
#点赞最多评论的具体内容
com = num1.find_element_by_xpath('//div[@class="cnt f-brk"]')
res = com.text
# print(res.split("："))
#评论作者
author = res.split("：")[0]
# print(author)
#评论内容
content = res.split("：")[1]
# print(content)
#点赞时间
ti = num1.find_element_by_xpath('//div[@class="rp"]/div').text
# print(ti)

print("当前点赞数量最高的评论的作者是:%s\n内容:%s\n时间:%s\n当前点赞数量:%d" %(author,content,ti,num_max))

driver.switch_to.default_content()

time.sleep(3)
driver.quit()

# 当前点赞数量最高的评论的作者是:张二二涵
# 内容:许嵩是值得尊重的音乐人 不喜欢听可以不听，但不要诋毁。
# 时间:2017年12月2日
# 当前点赞数量:1188
"""



































































