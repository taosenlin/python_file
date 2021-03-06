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
#函数运行完成后，会有一个对象（值）返回



















































