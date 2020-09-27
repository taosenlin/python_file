# coding:utf8
# Time:2020-03-17 23:07
# Author:TSL

# 闭包：
# 在一个内部函数里边，对在外部作用域（但不是全局作用域）的变量进行引用，那么这个内部函数就被认为是闭包

'''
def outer():
    x = 10
    #闭包
    def inner():
        print(x)
    return inner

#当需要调用inner函数时
a = outer()     #相当于 a = inner
a()             #相当于 inner()
# 10
outer()()       #相当于 inner()
# 10
'''





























































































