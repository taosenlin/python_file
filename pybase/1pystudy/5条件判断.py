#Author : taosenlin
#Time : 2020/2/28 14:33

# 一、if条件判断

# (1)if-elif-else语句
# score = 80
# if score >= 80:
#     print('A')
# elif score >= 70:
#     print('B')
# else:
#     print('不及格')



# (2)if嵌套   #分层条件
# score = 80
# if score >= 60:
#     if score >=90:
#         print('A')
# else:
#     print('不及格')
# print('run over!')



# (3)复合条件判断
# age = 60
# gender = 'male'
# if age >= 60 and gender == 'male':
#     print('old gentleman')

# score = 80
# sex = 'M'
# if score >= 60 and sex == 'M'\
#     and sex == 'M' and sex == 'M'\
#     and sex == 'M' and sex == 'M':
#     print('及格男同学')





# 扩展---1、获取用户输入
# input()   1-返回你输入的内容（字符串）
#           2-只有按回车键才结束输入

# score = input('请输入分数：')      #30
# print(type(score))                #<class 'str'>
# print(int(score) + 20)            #50



# 2、if的条件为真: 非零数值、非空字符串、非空元组、非空列表

# if 0:
#     print('条件满足了')      #无返回值

# if 1:
#     print('条件满足了')      #条件满足了

# if ' ':
#     print('条件满足了')        #条件满足了



# 3、取随机数
# from random import randint
# if randint(0,1):
#     print('条件满足了')           #无返回值/条件满足了













































