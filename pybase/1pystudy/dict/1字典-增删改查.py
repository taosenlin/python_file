
# info = {'name':'科达','id':100,'sex':'f','address':'中国上海'}

# print(info['name'])
# print(info['address'])
# print(info['age'])       #查看不存在的键，会报错


# (1)get方法
# print(info.get('age'))
# #在我们不确定字典中是否存在某个键而又想获取其值时，可以使用get方法(不存在会返回None)


# (2)修改元素
# print('修改之前的id为:%d'%info['id'])
# print('-'*20)
# newId = input('请输入新的学号：')
#
# info['id'] = int(newId)
#
# print('修改后的id为：%d'%info['id'])



info = {'name':'科达','sex':'f','address':'中国上海'}

# (3)添加元素
# print('修改之前的id为：%d'%info['id'])  //访问不存在的键会报错
# print(info)
# print('-'*70)
# newId = input('请输入新的id：')
#
# info['id'] = int(newId)
# print('-'*20)
# print('添加之后的id为:%d'%info['id'])
# print(info)
# print('-'*70)


# (4)删除元素

# a、del删除指定的元素
# print(info)
# print('-'*70)
#
# del info['name']
#
# print(info)
# print('-'*70)


# b、del删除整个字典
# print(info)
# print('-'*70)
#
# del info
#
# print(info)
# print('-'*70)


# c、clear清空整个字典
# print(info)
# print('-'*70)
#
# info.clear()
#
# print(info)
# print('-'*70)
















































