#coding:gbk
# Time:2020-03-17 21:54
# Author:TSL

"""
作用域是程序运行时变量可被访问的范围
      定义在函数内的变量是局部变量
      定义在模块最外层的变量是全局变量
"""


g = 99                 #全局变量，定义在模块当中，只在当前模块有效

def foo():
    l = 100            #局部变量，被定义在函数里面的

    print(g)
    print(l)

    def inner():
        e = 300
        print(e)       #嵌套作用域

foo()
print(g)
# print(l)

print(__name__)        #内置作用域，python内部定义
# __main__


# L (Local)      局部作用域
# E (Enclosing)  嵌套作用域
# G (Global)     全局作用域
# B (Built-in)   内置作用域
















































































































