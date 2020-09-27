# coding:utf8
# Time:2020-03-17 22:46
# Author:TSL

# a = 99
#
# def foo():
#     global a          #加global 将 a 改变为全局变量
#     a = 100
#     print(a)
#
#
# foo()
#
# print(a)
# # 100
# # 100



# 函数之间的调用
def foo():

    def foo1():

        def foo2():
            print(888)
        foo2()
    foo1()


foo()























































