#Author : taosenlin
#Time : 2020/3/10 16:46

# 一、变量的作用域
# x = 2    #全局变量：在一个.py模块里面，从定义那行开始，后面代码都可以使用
# def func():
#     x = 9     #局部变量：定义在函数里面（只在本函数范围内有效）
#     print("this x is in the func:-->1",x)
#
# func()
# print("-------")
# print("this x is out of func:-->2",x)
#
# this x is in the func:-->1 9
# -------
# this x is out of func:-->2 2

#将局部变量（函数内部）改为全局变量，需在函数内部申明
      # global x
      # x = 9



# 二、缺省参数（可填可不填）
# 变量 = 值       缺省参数
# 变量            必填参数
# 必填参数需在缺省参数前面
# 可查看print
# print('hello')
# print('tom')
# hello
# tom

# print('hello',end='***')
# print('tom')
# hello***tom

# print(1,2,3,4,5)
# 1 2 3 4 5
# print(1,2,3,4,5,sep='$')
# 1$2$3$4$5

# 总结：
# 1、不指定，就使用缺省参数
#   statmf(students)    #不会报错
# 2、没有缺省值的参数我们可以叫做必填参数
# 3、缺省参数可以定义多个
#   def statmf(a,b=1,c=2,d=3):
# 4、定义函数的时候一定要必填参数在前，缺省参数在后
# 5、缺省参数在内置的库和第三方库里面均有大量的使用



# 三、可变数量参数
# print(1,2,3,4,5,6) #实参参数数量不定，没有要求

#可变数量参数（0-n）
# def func(a,*b,c=10):  #函数定义的时候， * 封装一个元组
#     print(a,b,c)

# func(1)
# 1 () 10
# func(1,2,3)
# 1 (2, 3) 10
# func(1,2,3,c=20)
# 1 (2, 3) 20

#三者顺序：必填、可变数量参数、可缺省参数
# def get_sum(*number):
#     total = 0
#     print(number)
#     for n in number:
#         total = total + n
#     return total
#
# alist = [1,2,3]
# print(get_sum(*alist))      #函数调用的时候，* 可以展开元组或者列表
# (1, 2, 3)
# 6



# 四、关键字可变数量参数
# 1、允许在调用函数时，传入任意个含参数名的参数
# def register_student(name,age,**kargs):
#     print('name:',name,'age:',age,'other:',kargs)
# 除了必选参数name和age外，还接受关键字参数kargs

# 2、只传必填参数
# register_student('michael',30)
# name: michael age: 30 other: {}

# 3、加上任意个数的关键字参数
# register_student('Bob',35,city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}


# def func(a,c=2,*b,**kwargs):   #函数定义的时候， ** 封装一个字典
#     print(a,c,b,kwargs)
# (1)
# func(1,2,4,5,6,7,name='tom',age=20)
# 1 2 (4, 5, 6, 7) {'name': 'tom', 'age': 20}
# (2)
# dict1 = {'name':'tom'}
# func(1,2,4,5,6,7,**dict1)      #展开字典
# 1 2 (4, 5, 6, 7) {'name': 'tom'}
# (3)
# dict1 = {'name':'tom',1:100}
# func(1,2,4,5,6,7,**dict1)
#报错,键最好定义为str / 'age'=100即可
# dict1 = {'name':'tom','age':100}
# func(1,2,4,5,6,7,**dict1)
# 1 2 (4, 5, 6, 7) {'name': 'tom', 'age': 100}



# 五、综合使用
# def func(a,b,c=0,*args,**kwargs):
#     print(a,b,c,args,kwargs)

# func(1,2)
# 1 2 0 () {}

# func(1,2,c=3)
# 1 2 3 () {}

# func(1,2,c=3,5) #错误（写法）
# func(1,2,c=3,r=5)
# 1 2 3 () {'r': 5}

# func(1,2,3,'a','b')
# 1 2 3 ('a', 'b') {}

# func(1,2,3,'a','b',x=99)
# 1 2 3 ('a', 'b') {'x': 99}

































