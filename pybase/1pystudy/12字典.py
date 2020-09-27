#Author : taosenlin
#Time : 2020/3/9 17:18

# 一、字典的定义
# 1、内置类型--字典
# dict1 = {}
# dict2 = {'name':'jack','age':40}


# 2、 key value的概念
# dict2['name']
# dict2['age']
# 像字典前的索引，访问不存在的key会导致程序异常
# dict2.get('name',default=None)


# 3、字典定义：
# （1）键（哈希类型）:  #最常用：str
# 可以是： int、str、tuple、float （不可变类型）
# 不可以是：list、dict（可变类型）

# （2）值： 可以是任意类型

# （3）特性：键名唯一性


# 4、字典的特性
# （1）字典是mutable（可变）的

# （2）可以存储任意数量的元素

# （3）可以存储任何python数据类型
# a、value可以是任何类型
# b、key可以hash的类型（最常用的是数字和字符串）

# （4）以key:value，即"键:值"对的形式存储数据，每个键是唯一的

# （5）list、string、tuple特性称之为sequence
# dict特性称之为map

# 例：
# dict1 = {'name':'tom','age':'20'}
# print(dict1['name'])  #查询值---如果键名不存在，会报错
#tom

# student = {
#     'mike':{
#     'age':25
#     },
#     'tom':{
#     'age':30
#     }
# }
# print(student['tom']['age'])   #获取学生tom的年龄
#30



# 二、字典的常用操作
# dict1 = {'name':'tom','age':20}
# 1、查询---通过键去获取值(键不存在会报错)
# print(dict1['name'])
# tom


# 2、修改---通过键去修改值(键存在)
# dict1['name'] = 'jack'
# print(dict1)
#{'name': 'jack', 'age': 20}


# 3、增加---通过键去增加键值对(键不存在)
# dict1['weight'] = 150
# print(dict1)
#{'name': 'tom', 'age': 20, 'weight': 150}


# 4、in 通过键去判断（键存不存在）
# print('name' in dict1)
# True


# 5、删除---通过键去删除（没有dict1.remove()）
# del dict1['name']
# print(dict1)
# {'age': 20}
# dict1.pop('name')  #有返回值---打印
# print(dict1)
# {'age': 20}


# 6、键值的数量len(字典)
# print(len(dict1))
# 2


# 7、清空
# dict1.clear()
# print(dict1)
# {}


# 8、赋值
# dict1 = {}

# 区别
# def func1(arg):
#     arg.clear()
# a = {'age':'25','height':'180'}
# func1(a)
# print(a)
# {}


# 9、获取所有的key
# print(dict1.keys())       #返回是类列表
# dict_keys(['name', 'age'])


# 10、获取所有的value
# print(dict1.values())       #返回是类列表
# dict_values(['tom', 20])


# 11、获取所有的（键，值）
# print(dict1.items())          #返回是类列表
# dict_items([('name', 'tom'), ('age', 20)])

#类列表---不是列表，不支持下标获取，但支持for循环遍历
#可以通过list()---强制转化
# print(list(dict1.keys())[0])
# name

# 例：
# for one in dict1.keys():
#     print(one)
# name
# age

# for one,a in dict1.items():    #键值对
#     print(one,a)
# name tom
# age 20


# 12、字典的合并  dict1.update(字典)
# d = {1:'1',2:'2'}
# d.update({4:'4',5:'5'})
# print(d)
# {1: '1', 2: '2', 4: '4', 5: '5'}


# 13、字典的遍历
# student = {
#     'mike':{
#     'age':25
#     },
#     'tom':{
#     'age':30
#     }
# }
# (1)
# for name in student:
#     print(f'name:{name},age:{student[name]["age"]}')
# name:mike,age:25
# name:tom,age:30

# (2)
# for name,info in student.items():
#     print(f'name:{name},age:{info["age"]}')
# name:mike,age:25
# name:tom,age:30



# 三、字典的使用
# 一些简单的数据，无需字典，用列表即可
# 字典是无序的，如果需要按顺序，则不能用字典
















