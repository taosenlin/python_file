#Author : taosenlin
#Time : 2020/3/11 15:16

# 一、面向对象
# 面向对象的设计：一种设计思路
# 面向对象的语言：提供对面向对象设计的语言支持
# （非面向对象的语言也能实现面向对象的设计思路）

# 一切皆为对象
# 1、寻找出游戏里，涉及到的对象（类）
# 老虎、羊、房间   对象（Object）

# 2、类与实例
# 类：（1）一类具有相同特征的事物的统称
# （2）现实不存在---抽象的概念---人类--鸟类



# 3、python类的定义
'''
class ClassName:
    'class documentation string'
    class_suite
'''

# (1)关键字 class 类名(通常首字母大写)
# class Tiger:
#     classname = 'tiger'

# (2)属性(attribute):classname是一个属性

# 实例：（1）在这个类里面实际存在的个体  （2）实例是类的具体实例化体现



# 4、python类
# class Tiger:
#     classname = 'tiger'

# (1)实例化
# t1 = Tiger()
# 实例化后，就可以访问其属性
# t1.classname
'''
print(t1.classname)
tiger
'''


# (2)属性
# 概念： 本质：类里面一个变量        俗称：特征
# 调用： 实例.属性     类.属性

# 1、静态属性（类属性）
# 老虎的名称（该类的所有实例共享的属性）
# 属于整个类--每个个体都一样
'''
class Tiger:              #创建类
    className = '老虎'    #静态属性（老虎这个名称）

t1 = Tiger()              #创建实例
t1.className = 'hhh'      #实例.静态属性（类属性）（不影响其他输出）
print(t1.className)

Tiger.className = 'jjj'   #类.静态属性(后面的输出全部修改)
t2 = Tiger()              #创建实例
print(t2.className)
'''


# 2、实例属性
# (1)老虎的体重（每个实例独有的属性）
# (2)定义在初始化方法 __init__ 里
# (3)self的概念

# 注：如何去定义静态属性与实例属性？
# 看属性的特征，如果这个属性属于整个类，就定义成静态属性；
# 如果这个属性属于个体独有，则定义成实例属性
# (1)
'''
class Tiger:
    className = '老虎'
    #初始化方法---本质：函数
    def __init__(self):         #只要创建实例，就会自动被调用
        print('我执行了')

t1 =Tiger()
我执行了
'''
# (2)
'''
class Tiger:
    className = '老虎'
    def __init__(self,inWeight):      #self谁用就代表谁
        self.weight = inWeight

t1 = Tiger(200)         #t1(创建实例)，self就表示t1
print(t1.weight)
t2 = Tiger(100)         #t2,self就表示t2
print(t2.weight)
#注：类不能调用实例属性
# 200
# 100
'''
# (3)
'''
class Tiger:
    def __init__(self,inWeight=200):     #可缺省
        self.weight = inWeight

t1 = Tiger()
print(t1.weight)
# 200
t2 = Tiger(100)
print(t2.weight)
# 100
'''







































