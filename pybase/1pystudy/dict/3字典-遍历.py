
# 通过for...in...的语法结构，我们可以遍历字符串、列表、元组、字典等数据结构

dict = {'name':'赵四','sex':'男','age':23}

# (1)遍历字典的key(键)
# print(dict)
# print('-'*40)
# for key in dict.keys():
#     print(key)

# {'name': '赵四', 'sex': '男', 'age': 23}
# ----------------------------------------
# name
# sex
# age



# (2)遍历字典的value(值)
# print(dict)
# print('-'*40)
# for value in dict.values():
#     print(value)

# {'name': '赵四', 'sex': '男', 'age': 23}
# ----------------------------------------
# 赵四
# 男
# 23



# (3)遍历字典的项(元素)
# print(dict)
# print('-'*40)
# for item in dict.items():
#     print(item)

# {'name': '赵四', 'sex': '男', 'age': 23}
# ----------------------------------------
# ('name', '赵四')
# ('sex', '男')
# ('age', 23)



# (4)遍历字典的key-value(键值对)
# print(dict)
# print('-'*40)
# for key,value in dict.items():
#     print("key=%s,value=%s"%(key,value))

# {'name': '赵四', 'sex': '男', 'age': 23}
# ----------------------------------------
# key=name,value=赵四
# key=sex,value=男
# key=age,value=23



# (5)实现带下标索引的遍历
# 方法一：
# chars = ['a','b','c','d']
# i = 0
# for char in chars:
#     print("%d %s"%(i,char))
#     i += 1

# 方法二：
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
# 组合为一个索引序列，同时列出数据和数据下标
# chars = ['a','b','c','d']
# for i,char in enumerate(chars):
#     print("%d %s"%(i,char))






















































