#Author : taosenlin
#Time : 2020/3/12 10:46

# 一、对象方法（本质是一个函数）
# 概念：通过定义在类里面的函数
# 实例方法：每个具体实例相关的方法
# 静态方法：共有的方法，与每个具体实例无关



# 1、实例方法
# （1）每个具体实例相关的方法
# （2）如果代码中的实例方法不访问任何实例属性，一般建议实现为静态方法
# （3）初始化方法就是一个实例方法
# （4）一般实例方法都要访问self
'''
class Tiger:
    className = '老虎'
    def __init__(self,inWeight=200):
        self.weight = inWeight

    #1-实例方法--函数--跟实例有关
    def roar(self):       #self--不需要你操作--谁调用就是谁
        print('wow,叫一声体重减5斤')
        self.weight -= 5

    #2-实例方法
    def feed(self,food):
        if food == '肉':
            print('喂食正确，体重加10斤')
            self.weight += 10
        else:
            print('喂食错误，体重减少10斤')
            self.weight -= 10
'''

'''
t1 = Tiger(200)
print(t1.weight)
t1.roar()
t1.feed('草')
print(t1.weight)
200
wow,叫一声体重减5斤
喂食错误，体重减少10斤
185
'''


# 2、静态方法
# (1)与每个具体实例无关
# (2)  @staticmethod 修饰（装饰器）
'''
@staticmethod
def static_roar():
    print('只是简单的叫一声--wow!,静态方法')
'''

# 注：如何判断什么时候使用实例方法，什么时候使用静态方法？
# 看方法中有没有涉及到实例属性（实例属性的即使用实例方法）



# 二、对象组合
# 1-房间10个，随机放动物（Tiger、Sheep）
'''
class Room:
    def __init__(self,inNum,inAni):
        self.number = inNum
        self.animal = inAni

class Sheep:
    def __init__(self,inWeight=100):
        self.weight = inWeight

    def roar(self):
        print('mie--叫一声体重减10斤')
        self.weight -= 10

    def feed(self,food):
        if food == '草':
            print('喂食正确体重涨20斤')
            self.weight += 20
        else:
            print('喂食错误体重减20斤')
            self.weight -= 20

# t1 = Sheep()     #实例化一只羊
# r1 = Room(1,t1)  #实例化一个房间，并放入一个可以调用的羊


# 2-游戏初始化--创建10个房间实例（包含房间编号与随机的动物）
from random import randint
roomList = []                 #创建一个空列表存放房间实例
for one in range(1,11):
    if randint(0,1) == 1:      #randint函数特性双闭区间
        ani = Tiger
    else:
        ani = Sheep
    room = Room(one,ani)
    roomList.append(room)


# 3-游戏限时2分钟,时间到立即结束游戏
import time
# print(time.time())             #单位是s---从1970年到现在
#游戏开始定义一个开始时间
startTime = time.time()
while True:
    curTime = time.time()
    if curTime - startTime > 120:
        break
'''


# 三、对象的继承
# 1、python里面对象的继承
'''
class SubClassName(ParentClass1[,ParentClass2,...]):
    'Optional class documentation string'
    class_suite
'''
# 注：1、括号里面的是被继承的类，叫做父类（或者基类）
# SubClassName是继承类，叫做子类（或者继承类）
# 2、父类可以有多个（多重继承）

# 例：
# 1、
'''
class SouTiger(Tiger):    #扩展需求--功能：减少代码量
    pass

s1.static_roar()       
s1 = SouTiger()           #实例化
print(s1.className)       #调用父类的类属性
'''


# 2、
'''
class Tiger:
    __name = '私有属性'      #双下划线开头（私有属性）
    def __func(self):       #私有方法
        pass
'''


# 2、类的继承
# 注意：子类里没有初始化方法时，会自动调用父类的初始化方法（跟子类自动调用父类的方法一样）
# 如果子类里有自己的初始化方法，想调用父类的初始化方法需要自己写进去
'''
class Tiger:
    className = '老虎'
    def __init__(self,inWeight=200):
        self.weight = inWeight
        
class NewTiger(Tiger):
    def __init__(self, inNewWeight):
    # 方式一：
    #     Tiger.__init__(self,inWeight=200)      #调用父类的初始化方法
    # 方式二：
    #     super().__init__(inWeight=200)    #调用父类初始化方法另一形式
'''


# 3、方法重写
'''
class Animal:
    def __init__(self,inWeight):
        self.weight = inWeight

    def roar(self):
        print('大叫三声，你敢答应吗？wow wow wow')

    def run(self):
        print('日行千里XRV')

class Dog(Animal):
    #构造函数，调用父类的构造函数初始化属性值
    def __init__(self,inNewWeight):
        #继承父类的初始化方法
        super().__init__(inWeight)     

    def roar(self):
        print('大叫一声 汪')      #方法重写

    def run(self):
        print('日行百里卡罗拉')   #方法重写
'''
#同一种方法（例如roar、run）在父类和子类不同的用法，子类觉得父类不好用故重写时























































