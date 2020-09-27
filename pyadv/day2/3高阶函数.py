# coding:utf8
# Time:2020-03-17 22:49
# Author:TSL

# 1-
'''
def foo():
    print("888")
    print("666")

#函数名可以被赋值给其他对象
a = foo
a()
# 888
# 666
'''



# 2-
'''
#函数名可以作为返回值
def foo():
    print("执行了")
    def inner():
        print("999")
    return inner

a = foo()        #相当于 a = inner
a()              #inner()
# 执行了
# 999
'''



# 3-
'''
#函数名可以作为参数传递
def foo(func):
    func()

def bar():
    print(100)

foo(bar)
# 100
'''

















































































