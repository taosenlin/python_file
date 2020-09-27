#coding : utf8
#Author : taosenlin
#Time : 2020/5/20 14:58

# Python中 * 和 ** 的打包和解包
# python中的 * 和 ** 能够让函数支持任意数量的参数，它们在函数定义和调用中，有着不同目的。

# 一、*
# * 的作用：
# 1、在函数定义中，收集所有位置参数到一个新的元组，并将整个元组赋值给变量args。

"""
def f(*args):       # * 在函数定义中使用
    print(args)

f()             #()
f(1)            #(1,)
f(1,2,3,4)      #(1, 2, 3, 4)
"""

# 2、在函数调用中，*能够将元组或列表解包成不同的参数。

"""
def func(a,b,c,d):
    print(a,b,c,d)

args = (1,2,3,4)
func(*args)          # * 在函数调用中使用
# 1 2 3 4
args = [1,2,3,4]
func(*args)
# 1 2 3 4
"""


# 二、**
# ** 的作用：
# 1、在函数定义中，收集关键字参数到一个新的字典，并将整个字典赋值给变量kwargs。

"""
def f(**kwargs):
    print(kwargs)

f()           #{}
f(a=1,b=2)    #{'a': 1, 'b': 2}
"""

# 2、在函数调用中，** 会以键/值的形式解包一个字典，使其成为一个独立的关键字参数。

"""
def func(a,b,c,d):
    print(a,b,c,d)

kwargs = {"a":1,"b":2,"c":3,"d":4}
func(**kwargs)
# 1 2 3 4
"""


# 三、
# 在函数定义时，* 表示打包；在函数体内部，* 表示的却是解包
# 事实上，print(*args)是print()函数的调用

"""
def foo(*args,**kwargs):
    print(args)          #未解包参数
    print(*args)         #解包参数

v = (1,2,4)
d = {"a":1,"b":2}
foo(v,d)
# ((1, 2, 4), {'a': 1, 'b': 2})
# (1, 2, 4) {'a': 1, 'b': 2}
"""

# 注：* 和 ** 的打包和解包并不能脱离函数而存在。















































