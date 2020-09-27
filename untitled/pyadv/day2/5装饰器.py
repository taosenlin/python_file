# coding:utf8
# Time:2020-03-17 23:19
# Author:TSL

import time


# 1-
'''
def foo():
    beginTime = time.time()
    print("执行测试用例，调用很多接口！")
    time.sleep(1)
    endTime = time.time()

    print(endTime - beginTime)

foo()
'''



# 2-
def show_time(func):     #装饰函数
    def inner(case_name):
        beginTime = time.time()
        func(case_name)
        endTime = time.time()
        print("总耗时:",endTime - beginTime)
    return inner


@show_time               #相当于 foo = show_time(foo)     # 相当于foo == inner
def foo(case_name):               #被装饰函数
    print("执行测试用例，调用很多接口！",case_name)
    time.sleep(1)



# show_time(foo)

# foo = show_time(foo)     # 相当于foo == inner
foo()                     #相当于 show_time(foo)()




























































































