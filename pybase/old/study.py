# Time:2019-12-22 18:38
# Author:TSL
# print(type(100))#查看对象类型
# print(type(3.14))
# print(type('hello'))
# import keyword
# print(keyword.kwlist)
# a=100
# a=200
# print(a)
# print('hello',3)
# info = 'name is tom'
# print(len(info))
# alist = [10,3.14,10,'hello',[100,200]]
# print(type(alist))
# print(id(alist))
# print(len(alist))
# print([100,200] in alist)
#1- 获取元素
# print(alist[-1][1])
#2- 获取几个元素
# print(alist[1:4])
# del alist[2]
# alist.pop(1)
# alist.remove(10)
# print(alist)
# tu1 = (10,3.14,'hello',[100,200],(20,30))
# alist = [10,20,30]
# print(10,20 in alist)
'''
score = 80
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('不及格')
print('run over!')
'''
'''
def get_sum(a,b):
    return a+b

res = get_sum(10,20)
print(res)
'''
'''
a = '80'
print(a,type(a))
b = int(a)
print(b,type(b))
'''

# a = 2
# b = 3
# if a > 1:
#     if b > 2:
#         print('a,b both > 1')
# if a > 1 and b > 2:
#     print('a,b both > 1')

# s = 90
# print('good')
#
# if s >= 90:
#     # print('good')
#     print('very good')

# def e1():
#     print('in e1')
#     return False

# False and e1()
# e1() and False
# True or e1()
# False or e1()
# e1()
# print('after call')

# print(max((11,22,33)))

# a = 'TSL'
# print(len(a))

# def t2(para):
#     para = 3
#
# b = [1]
# t2(b)

# def getName(srcStr):
#     print(srcStr.split(',')[1].split(' ')[3])
#
# getName('A pretty boy come in,the name is Patrick, level 194')

# for one in range(5,0,-1):
#     print(one)

# 请实现一个程序，实现如下需求点：
# 1.程序开始的时候提示用户输入学生年龄信息 格式如下：
# Jack Green ,   21  ;  Mike Mos, 9;
#
# 我们假设 用户输入 上面的信息，必定会遵守下面的规则：
#   学生信息之间用分号隔开（分号前后可能有不定数量的空格），
#   每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）
#
# 2. 程序随后将输入的学生信息分行显示，格式如下
# Jack Green :   21;
# Mike Mos   :   09;
# 学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零

# stu_Sta = input('Please input student age info:')  #输入学生年龄信息
# stu_Info = stu_Sta.split(';')                      #将输入的学生信息切割成列表形式
# for one in stu_Info:                               #循环判断学生信息中是否存在逗号
#     if ',' not in one:
#         continue
#
#     name,age = one.split(',')                      #将学生姓名和年龄切割成列表形式
#     name = name.strip()                            #去除左右空格
#     age = age.strip()                              #去除左右空格
#
#     if not age.isdigit():                          #判断输入的age是否为纯数字
#         continue
#
#     age = int(age)                                 #将age转换成整型
#
#     print('%-20s : %02d' %(name,age))               #按要求格式输出
#


# welcome = "您好，欢迎！"
# print("小陶"+ welcome)
# print("小吴"+ welcome)

# a = 10
# print(a)
# print(id(a))



# print('hello' + "123")
# print( 3 + 4)
# print('hello',3)


# info = 'name is tom'
# print(len(info))
# print(info[len(info)-1])
# print(info[-len(info)])

# print(id(info))
# print(info[5:5+2])
#
# print(id(info[:4]))
#
# print(info[-3:])

# info = 'name is tom'

# a = [123,'abc',4.56,['inner','list']]

# print(type(a[0]))
# print(type(a[1:4]))
# a[0] = 666
# a.append(888)
# a[-1].append(999)
# a.insert(1,777)
# del a[1],a[2]
# del a[1:1+2]
# a.pop(2)
# print(a.pop(2))
# print(a)

# a = (123,'abc',4.56,['inner','list'],(66,88))
# print(a.index(4.56))
# print(a[:4])

# alist = [10,20,30]
# print(tuple(alist))
# print(alist)

# print('abc' < 'b')

# alist = [123,'abc',789]
# print(123 not in alist)


# str1 = 'name is tom'
# print('n' in str1)
# print('name' in str1)
# print('e i' in str1)
# print( 3 > 1 or 2 == 0)

# score = 70
# if score >= 90:
#     print('优秀！')
# elif score >= 80:
#     print('中等！')
# else:
#     print('不及格！')


# score = 90
# if score >= 60:
#     if score >=  90:
#         print('A')
# else:
#     print('不及格！')
# print('run over!')


# age = 60
# gender = 'male'
# if age >= 60 and gender == 'male':
#     print('old gentleman')


# score = 80
# sex = 'M'
# if score >= 60 and sex == 'M'\
#     and sex == 'M' and sex == 'M'\
#     and sex == 'M' and sex == 'M':
#     print('及格男同学！')


# score = input('请输入分数：')
# # print(type(score))
# print(int(score) + 20)  #int（）-- 转成int


# if ' ':
#     print('条件满足了')


# from random import randint
# if randint(0,1):
#     print('条件满足了！')


# def func():
#     print('step1')
#     print('step2')
#     print('step3')
#
# func()
# print('运行结束！')


# def get_sum(a,b):
#     print(a,b)

# get_sum('hello',3)
# get_sum(b = 'hello',a = 2)
# get_sum('hello',b = 2)
# get_sum(a = 'hello',b = 2)


# def get_sum(a,b):
#     return a+b
#
# res = get_sum(10,20)
# print(res)
#
# print(print())


# def func(a,b):
#     if a > b:
#         return 1
#     elif a < b:
#         return -1
#     else:
#         return 0
#
# print(func('abcd','b'))


# a = (0,1,2,3,4,5)
# print(len(a))
# print(max(a))
# print(min(a))


# a = [10,20]
# print(type(a))
#
# b = str(a)
# print(len(b))


# a = '3'
# print(a,type(a))
# b = int(a)
# print(b,type(b))


# a = '100'
# print(a,type(a))
# b = float(a)
# print(b,type(b))

# str1 = 'aaabcdeeeefg'
# print(str1.count('a'))
#
# str = 'abcdaaa'
# # print(str.find('x'))   #如果查找的元素不在字符串里面，一定返回-1
# if str.find('a') != -1:
#     print('一定存在里面')

str = '  name is tom tom tom  '
# print(str.split('m'))   #按'm'切割字符串
# print(str.lower())      #将字符串中的大写字母全部转换为小写字母
# print(str.upper())        #将字符串中的小写字母全部转换为大写字母
# print(str.replace('tom','jack',2))
# print(str.strip())      #将字符串前后空格删除
# print(str.lstrip())     #将字符串前置空格删除
# print(str.rstrip())       #将字符串后置空格删除
# print(str.replace(' ',''))



# name = 'tom'
# height = 170
# print(type(height))
# print('我叫' + name + ',身高' + height  + '厘米')
# print('我叫%s,身高%scm' %(name,height))















































































































































