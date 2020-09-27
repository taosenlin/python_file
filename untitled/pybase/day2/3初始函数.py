#Author : taosenlin
#Time : 2020/2/28 14:59

# 一、函数的定义：
# 函数本质上来说是一段代码的名称(变量是对象的名称)

# def 函数名():   #函数的定义--不会执行里面任何代码
                  #用意：告诉python解释器有一个函数名称

# 例：
# def func():
#     print('up1')
#     print('up2')
#
# func()                  #函数的调用--会执行里面代码
# print('运行结束！')

# up1
# up2
# 运行结束！






# 二、函数的定义与作用
# a、定义：就是一段代码的组合，一般实现一个具体的功能
# b、函数名就是：代表一段代码的变量
# c、可以实现一个个的函数，最好组合起来






# 三、函数的调用
# 1、调用函数，其实就是去执行函数定义里面的代码块
# 2、函数的定义要在函数的调用前面






# 四、函数的参数
# 1、必填形参
# def get_sum(a,b):     #形参：在函数定义的地方--形式主义；如果形参只有变量名，为必填形参
#     print(a,b)
#
# # get_sum(6,8)          #函数调用时个数与定义时个数一定要一致（否则出错）
#
# get_sum('hello',3)      #实参：函数调用时实际传入的值
# get_sum(b='hello',a=2)
# get_sum('hello',b=2)
# get_sum(a='hello',b=2)  #函数调用时，一旦出现变量=值（a='hello'）的写法,后面参数要保持队形


# 2、关键字参数调用
# (1)次序可以颠倒
# (2)一旦第n个参数使用了关键字参数（诸如上述a=2,b=2）,后面所有的参数都必须使用关键字






# 五、函数的返回值
#1、函数运行完成后，会有一个对象（值）返回

# def get_sum(a,b):
#     # print(a+b)
#     return a+b          #谁调用给谁（同一个缩进下面不能有代码--无意义）
#
# res = get_sum(10,20)
# print(res)

#当return后面只有一个返回值，返回值什么类型就什么类型
#当return后面有俩个或以上的返回值，则返回元组类型



# 2、结束函数
# def func():
#     if xxx:
#         return         #结束函数

# def func(a,b):      #知识点：return是一个函数的结束
#     if a > b:
#         return 1
#     elif a < b:
#         return -1
#     else:
#         return 0
#
# res = func('abcd','b')
# print(res)






# 六、内置函数
# 1、 print、len、max、min



# 2、 str、int、float---类型转换

# (1)str() --- 转成字符串类型
# a = 10
# print(type(a))
# b = str(a)
# print(type(b))

# a = [10,20]
# print(type(a))
# b = str(a)
# print(type(b))



# (2)int() --- 字符串转换成int类型 要求：1、数值（整型数值）2、浮点型转成int--只取整数部分
#round(小数，位数)

# a = 'tom'
# print(a,type(a))
# b = int(a)
# print(b,type(b))      #报错

# a = '3.14'
# print(a,type(a))
# b = int(a)
# print(b,type(b))        #报错

# a = 3.14
# print(a,type(a))
# b = int(a)
# print(b,type(b))
# 3.14 <class 'float'>
# 3 <class 'int'>



# (3)float()
# a = '3.14'
# print(a,type(a))
# b = float(a)
# print(b,type(b))
# 3.14 <class 'str'>
# 3.14 <class 'float'>

# a = 100
# print(a,type(a))
# b = float(a)
# print(b,type(b))
# 100 <class 'int'>
# 100.0 <class 'float'>














