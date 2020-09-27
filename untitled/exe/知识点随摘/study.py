#coding : utf8
#Author : taosenlin
#Time : 2020/4/13 14:35

"""
random() 函数
"""
"""
import random

#产生1到10的整数型随机数
print(random.randint(1,10))        

#产生随机浮点数
print(random.random())      #0到1之间
print(random.uniform(1,10))

#产生随机字符
print(random.choice('tomorrow'))

#随机选取0到100之间的偶数：
print(random.randrange(0,101,2))

randint和randrange的区别
区别：randint左右闭区间，randrange左闭右开
共性：输出都是整数
"""
"""
a = [1,3,5,7,9]
#将列表a中的元素顺序打乱
random.shuffle(a)
print(a)
"""


"""
ASCII码中
0-31及127（共33个）是控制字符或通信专用字符（其余为可显示字符）

32-126（共95个）是字符（32是空格）
48-57为0到9十个阿拉伯数字
65-90为26个大写英文字母
97-122为26个小写英文字母
其余为一些标点符号、运算符号等
"""


"""
Python中chr与ord函数的使用
"""
'''
chr()函数是将已知字母的顺序值转换成其对应的字母(这个函数传入的参数值为整数)
ord()函数是将已知字母转换成其顺序值
'''
"""
print(ord('a'))    #97
print(ord('A'))    #65
print(chr(97))     #a
print(chr(65))     #A
"""


"""
bin()  #二进制
oct()  #八进制
hex()  #十六进制
"""
"""
a = [2,4,6,8]
for i in a:
    print(bin(i))
"""


"""
python中capitalize()函数的用法
capitalize()函数
描述：将字符串的第一个字母变成大写，其余字母变为小写
语法：str.capitalize() -- str 返回字符串
"""
"""
str1 = 'i Love python'
str2 = 'I Love python'
print(str1.capitalize())
print(str2.capitalize())
"""


"""
enumerate()是python的内置函数
enumerate在字典上是枚举、列举的意思
函数原型：enumerate(sequence, [start=0])
功能：将可循环序列sequence以start开始分别列出序列数据和数据下标
即对一个可遍历的数据对象(如列表、元组或字符串)，
enumerate会将该数据对象组合为一个索引序列，同时列出数据和数据下标。
"""
# 如果对一个列表，既要遍历索引又要遍历元素时，可以这样写
"""
list = ['1','3','5','7']
for i in range(len(list)):
    print(i,list[i])
0 1
1 3
2 5
3 7
"""
# 上述方法有些累赘，利用enumerate()会更加直接和优美
"""
list = ['1','3','5','7']
for index,item in enumerate(list):
    print(index,item)
0 1
1 3
2 5
3 7
"""
# enumerate还可以接收第二个参数，用于指定索引起始值
"""
list = ['1','3','5','7']
for index,item in enumerate(list,1):
    print(index,item)
1 1
2 3
3 5
4 7
"""




# 查看python版本和支持的文件格式
"""
# 1、查看python版本
# python
"""

# 2、查看文件支持格式
"""
# import pip._internal
# print(pip._internal.pep425tags.get_supported())
"""










































