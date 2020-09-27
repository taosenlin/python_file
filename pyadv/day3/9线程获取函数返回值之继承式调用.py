# coding:utf8
# Time:2020-03-21 9:03
# Author:TSL

import threading

def foo():
    return "hello"

def threading_get_return():
    sli = []
    for i in range(10):
        res = foo()
        sli.append(res)


class MyThread(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = self.func(*self.args)














































































































