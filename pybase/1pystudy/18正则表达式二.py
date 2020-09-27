#coding : utf8
#Author : taosenlin
#Time : 2020/3/17 18:04

# 一、re 模块
# 使用正则表达式需要制定一些规则来描述那些你希望匹配的字符串集合

# 正则表达式并不是python的一部分,它被嵌入到python中,并通过re模块提供使用

# 正则表达式(Regular expressions也称为REs) 本质上是一个微小的且高度专业化的编程语言



# 二、re模块-常用方法

# 1、 re.match(pattern,string,flags=0)
# 从字符串的起始位置匹配的一个模式，如果起始位置没有的话，match()就返回none


# 2、 re.search(pattern,string,flags=0)
# 扫描整个字符串并返回第一个成功的匹配


# 3、 re.sub(pattern,repl,string,count=0)
# 用于替换字符串中的匹配项, repl:替换的字符串,也可为一个函数


# 4、 re.compile(pattern[,flags])
# 用于编译正则表达式，生成一个正则表达式(pattern)对象，供match()和search()这两个函数使用


# 5、 findall(string[,pos[,endpos]])
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表


# 6、 split(pattern,string[,maxsplit=0,flags=0])
# 能够匹配的子串将字符串分割后返回列表


# 三、re模块-实际使用

# import re

# 1、compile --- 生成正则表达式对象
# (1)
# 定义一个封装对象
# rr = re.compile('\W+')
# res = rr.findall('*#abcd123_ABC###')
# print(res)
# ['*#', '###']
# (2)
# res = re.findall('\W+','*#abcd123_ABC###')
# print(res)
# ['*#', '###']


# 2、match --- 从字符串起始位置匹配,如果开头没有则无
# (1)找到就停止查找   (2)具体查看内容:  .group()
# rr = re.compile('\w+')
# res = rr.match('*#abcd123_ABC###')
# print(res)
# None
####################################
# rr = re.compile('\w+')
# res = rr.match('abcd123_ABC###').group()
# print(res)
# abcd123_ABC


# 3、search --- 扫描整个字符串并返回第一个成功的匹配(并不是从头开始)
# rr = re.compile('\w+')
# res = rr.search('*##abcd123_ABC###123').group()
# print(res)
# abcd123_ABC


# 4、sub --- 用于替换字符串中的匹配项
# res = re.sub('\w+','-','*##abc123_ABC##123')
# print(res)
# *##-##-


# 5、split --- 用于分割匹配的子串并将分割后的字符串以列表形式返回
# res = re.split('\W','123#abc#')
# print(res)
# ['123', 'abc', '']



# 四、re模块-常用修饰符

# 修饰符     描述
# re.I       使匹配对大小写不敏感
# re.S       使 . 匹配包换换行在内的所有字符
# re.M       多行匹配，影响 ^ 和 $

# 取值可以使用按位或运算符 '|' 表示同时生效，比如
# re.I|re.M



# 五、re模块-正则表达式实战

# 1、获取 abc123-23dc-3345-ddfc4
# 网址: https://cn.api.com/?src=888/user/abc123-23dc-3345-ddfc4

# import re

# url = 'https://cn.api.com/?src=888/user/abc123-23dc-3345-ddfc4'
# res = re.findall('\w+-\w+-\w+-\w+',url)
# print(res)
# ['abc123-23dc-3345-ddfc4']


# 2、获取正确的手机号码
# 手机号码规则：
# 1、130-139
# 2、145 147
# 3、150 151 152 153 155-159
# 4、166
# 5、170 171 173 175-178
# 6、180-189
# 7、198 199

# rr = re.compile('^13[0-9]|14[5|7]|15[0-3|5-9]|166|17[0|1|3]|17[5-8]|18[0-9]\d{8}')
#
# res = rr.findall('abc17521369688#adc18119955930badcc2854321')
# print(res)
























