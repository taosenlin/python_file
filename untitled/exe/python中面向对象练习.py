#coding : utf8
#Author : taosenlin
#Time : 2020/7/17 14:39

# 1、面向对象三大特性，各有什么用处。
"""
封装：明确区分内外，控制外部对隐藏属性的操作行为，隔离复杂度
继承：解决代码重用的问题
多态：多态性，可以在不考虑对象类型的情况下而直接使用对象
"""


# 2、类的属性和对象的属性有什么区别。
"""
类的属性：数据属性和函数属性，数据属性是所有对象共有的，函数属性是绑定对象使用的
对象的属性：对象是类的实例化
"""


# 3、面向过程编程与面向对象编程的区别与应用场景。
"""
面向过程编程：更倾向于将编程中复杂的问题流程化、简单化
应用场景：不需要再扩展了、自动部署测试环境、监测脚本、软件解压安装

面向对象编程：具有特征和技能的结合体，一切皆为对象
应用场景：用户需求经常变化，多用于互联网应用、游戏、企业内部应用等开发
"""


# 4、类和对象在内存中是如何保存的。
"""
类和对象的属性：在内存中以字典的形式保存
"""


# 5、什么是绑定到对象的方法、绑定到类的方法、解除绑定的函数、如何定义、如何调用、给谁用？有什么特性。
"""
绑定到对象的方法：由对象调用，def tell_info():...obj.tell_info()
绑定到类的方法：由类来调用，@classmethod def from_conf():...class.from_conf()
非绑定方法：不与类和对象绑定，谁都可以调用，@staticmethod def create_id():...obj.create_id()\class.create_id()
"""


# 6、使用实例进行获取、设置、删除数据，分别会触发类的什么私有方法。

"""
class A(object):
    pass
    
a = A()

a["key"] = "val"
a = a["key"]
del a["key"]
"""

"""
class A(object):
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__.get(item)

    def __delitem__(self, key):
        del self.__dict__[key]

a = A()
a["key"] = "val"
print(a.__dict__)
a = a["key"]
print(a)
del a["key"]
print(a.__dict__)
"""


# 7、python中经典类和新式类的区别
"""
经典类：python2中没有继承object的类，以及继承其的子类都是经典类---深度优先
新式类：python3中继承object的类，以及继承其的子类都是新式类---广度优先
"""


# 8、用面向对象形式优化以下代码。
"""
在没有学习类这个概念时，数据与功能是分离的
   def exc1(host,port,db,charset):
   　　conn=connect(host,port,db,charset)
   　　conn.execute(sql)
   　　return xxx
   def exc2(host,port,db,charset,proc_name)
   　　conn=connect(host,port,db,charset)
   　　conn.call_proc(sql)
   　　return xxx
   # 每次调用都需要重复传入一堆参数
   exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
   exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')
"""

"""
class Exc:
    def __init__(self,host='127.0.0.1',port=3306,db='db1',charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset

    def exc1(self,sql):
        conn = connect(self.host,self.port,self.db,self.charset)
        res = conn.execute(sql)
        return res

    def exc2(self,sql):
        conn = connect(self.host,self.port,self.db,self.charset)
        res = conn.call_proc(sql)
        return res
####################################优化#####################################
"""
"""
class Exc:
    def __init__(self,host,port,db,charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset
        self.conn = connect(self.host,self.port,self.db,self.charset)

    def exc1(self,sql):
        res = self.conn.execute(sql)
        return res

    def exc2(self,sql):
        res = self.conn.call_proc(sql)
        return res
"""


# class People(object):
#     __name = "luffy"
#     __age = 18
#
# p1 = People()
# print(p1._People__name,p1._People__age)    #luffy 18
# print(p1.__dict__)
# print(People.__dict__)


# class People:
#     def __init__(self):
#         print("__init__")
#
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         return object.__new__(cls, *args, **kwargs)
#
# People()


# 11、简单解释Python中 staticmethod（静态方法）和 classmethod（类方法）, 并分别补充代码执行下列方法
"""
静态方法：非绑定方法，类和对象都可以调用
类方法：绑定给类的方法，给类调用
"""
"""
class A:
    def __init__(self,name):
        self.name = name

    def foo(self,name):
        print("executing foo(%s,%s)" %(self,name))

    @classmethod
    def class_foo(cls,name):
        print("executing class_foo(%s,%s)" %(cls,name))

    @staticmethod
    def static_foo(name):
        print("executing static_foo(%s)" %(name))


a = A("tao")
a.foo("tao")
A.class_foo("tao")
a.static_foo("tao")
A.static_foo("tao")
"""


# 执行以下代码，解释错误原因，并修正错误
"""
class Dog:
    def __init__(self,name):
        self.name = name

    @property
    def eat(self):
        print("%s is eating" %(self.name))

a = Dog("keji")
# a.eat()      #property将函数属性变成数据属性(加property将普通方法变成静态方法，调用时不用加())
# a.eat        #keji is eating
"""


# 13、下面这段代码的输出结果将是什么？请解释
"""
class Parent:
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

# print(Parent.x,Child1.x,Child2.x)
# print(id(Parent.x),id(Child1.x),id(Child2.x))
Child1.x = 2
print(Parent.x,Child1.x,Child2.x)
print(id(Parent.x),id(Child1.x),id(Child2.x))
Parent.x = 3
print(Parent.x,Child1.x,Child2.x)
print(id(Parent.x),id(Child1.x),id(Child2.x))
"""












































