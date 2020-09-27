# coding:utf8
# Time:2020-03-22 14:38
# Author:TSL


import threading

def foo(something):
    return something


class MyThreading(threading.Thread):
    def __init__(self,func,args=[]):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args


    def run(self):
        self.result = self.func(*self.args)


    def get_result(self):
        threading.Thread.join(self)
        return self.result



t = MyThreading(foo,["888"])
t.start()
print(t.get_result())


























































