#coding : utf8
#Author : taosenlin
#Time : 2020/5/20 13:24

"""
class Person():          #定义一个类
    role = "person"      #类属性
    def walk(self):      #实例方法
        print("person is walking....")
print(Person.role)
print(Person.walk)     #函数的内存地址
"""

"""
class Person():               #定义一个类
    role = "person"           #类属性
    def __init__(self,name):  #初始化函数(构造函数),一般存放实例属性（谁调用就是谁的）
        self.name = name

    def walk(self):           #实例方法
        print("person is walking...")

# print(Person.role)
# print(Person.walk)

t = Person('tsl')        #实例化(的过程就是类-->对象的过程)
print(t.name)            #查看属性  对象名.属性名
print(t.walk())          #调用方法  对象名.方法名()
"""

"""
#############################人狗大战#########################
class Person:                            #创建一个类
    role = 'person'                      #类属性
    def __init__(self,name,aggressivity,life_value,money):
        self.name = name                  #每个角色都有自己的名字
        self.aggressivity = aggressivity  #每个角色都有自己的攻击力
        self.life_value = life_value      #每个角色都有自己的生命值
        self.money = money                #每个角色有多少金币

    def attack(self,dog):
        #人可以攻击狗，这里的狗也是一个对象
        #人攻击狗，那么狗的生命值就会随着人的攻击力而下降
        dog.life_value -= self.aggressivity

# r = Person('tt',100,1000)
# print(r.name)
# print(r.aggressivity)
# print(r.life_value)
# print(r.attack)

class Dog:
    role = 'dog'
    def __init__(self,name,breed,aggressivity,life_value):
        self.name = name
        self.breed = breed
        self.aggressivity = aggressivity
        self.life_value = life_value

    def bite(self,people):
        #狗可以咬人，这里人也是一个对象
        #狗咬人，那么人的生命值就会随着狗的攻击力而下降
        people.life_value -= self.aggressivity

# p = Person('tt',100,1000)
# d = Dog('2ha','哈士奇',50,600)
# print(d.life_value)
# p.attack(d)
# print(d.life_value)

class Weapon:                                #定义一个武器类
    def __init__(self,name,price,aggress,life_v):
        self.name = name                     #武器的名字
        self.price = price                   #武器的价格
        self.aggress = aggress               #加攻击力
        self.life_v = life_v                 #加生命值

    def update(self,obj):                    #obj为要带这个装备的角色
        obj.money -= self.price              #要买这个装备，这个角色的钱会根据装备价格相应减少
        obj.aggressivity += self.aggress     #增加这个角色的攻击力
        obj.life_value += self.life_v        #增加这个角色的生命值

    def prick(self,obj):                     #该装备的主动技能，扎向对方
        obj.life_value -= 500                #攻击力500

a = Person('tt',100,1000,600)
b = Dog('2ha','哈士奇',60,800)
c = Weapon('长枪',300,300,200)

if a.money > c.price:      #如果角色自身金币大于武器价格，就可以购买一件武器
    c.update(a)            #角色使用金币买了一件武器，自身属性得到提升
    a.weapon = c           #角色装备上武器

# print(a.money,a.aggressivity,a.life_value)

print(b.life_value)
a.attack(b)               #人攻击了狗一下
print(b.life_value)
a.weapon.prick(b)         #人使用武器扎了一下狗
print(b.life_value)
"""

"""
from math import pi

class Circle:
    '''
    定义一个圆形类；
    提供计算圆形面积(area)和周长(perimeter)的方法
    '''
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return  pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius

t = Circle(10)
print(t.area())
print(t.perimeter())
"""

#####################面向对象的组合方法#####################
"""
class Weapon:
    def prick(self,obj):             #该装备的主动技能，扎对手
        obj.life_value -= 500        #每扎一下，对手生命值减少500

class Person:
    role = 'person'             #类属性（人的角色属性都是人）
    def __init__(self,name):
        self.name = name        #每个角色都有自己的昵称
        self.weapon = Weapon()  #给角色绑定一个武器

t = Person('tt')
t.weapon.prick()
"""

"""
###############################环形类#####################
from math import pi

class Circle:                      #先定义一个圆形类
    def __init__(self,r):
        self.r = r

    def area(self):
        return pi * self.r * self.r

    def per(self):
        return 2 * pi * self.r

# t = Circle(10)
# print(t.area())
# print(t.per())

class Ring:            #再定义一个环形类
    '''
    定义一个圆环类
    提供圆环的面积和周长的计算方法
    '''

    def __init__(self,r_out,r_in):
        self.out_circle = Circle(r_out)             #组合圆形的实例作为自己的属性来用
        self.in_circle = Circle(r_in)

    def area(self):
        return self.out_circle.area() - self.in_circle.area()

    def per(self):
        return self.out_circle.per() + self.in_circle.per()

t = Ring(10,5)
print(t.area())
"""

"""
class Animal:
    def eat(self):
        print("eat food!")

    def drink(self):
        print("drink cola")

class Cat(Animal):
    def __init__(self,name):
        self.name = name
        self.breed = '猫'

    def climb(self):
        print("爬树ing...")

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        self.breed = '狗'

    def look_house(self):
        print("汪汪汪...")

# a = Cat("蓝猫")
# print(a.name)
# print(a.drink())
# b = Dog("京东狗")
# print(b.eat())
# print(b.look_house())
"""

"""
class A:
    __role = 'CHINA'
    @classmethod
    def show_role(cls):
        print(cls.__role)

    @staticmethod
    def get_role():
        return A.__role

    @property
    def role(self):
        return self.__role

a = A()
print(a.role)
print(a.get_role())
a.show_role()
# __role在类中有哪些身份？
# 以上代码分别输出哪些内容？
# 这三个装饰器分别起了什么作用？有哪些区别？
# CHINA
# CHINA
# CHINA
"""

"""
class Animal:
    '''
    人和狗都是动物
    '''
    def __init__(self,name,aggressivity,life_value):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def eat(self):
        print("%s is eating" %self.name)

class Person(Animal):
    pass

class Dog(Animal):
    pass

a = Person('tt',100,1000)
b = Dog('2ha',60,800)
print(a.eat())
print(b.eat())
"""


"""
class Animal:
    '''
    人和狗都属于动物
    '''
    def __init__(self,name,aggressivity,life_value):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def eat(self):
        print('%s is eating' %self.name)

class Person(Animal):
    '''
    人类继承Animal
    '''
    def attack(self,dog):
        '''
        派生新的技能，人可以攻击狗
        :param dog:
        '''
        dog.life_value -= self.aggressivity

class Dog(Animal):
    '''
    狗类继承Animal
    '''
    def bite(self,people):
        '''
        派生新的技能，狗可以咬人
        :param people:
        '''
        people.life_value -= self.aggressivity

a = Person('tt',100,1000)
b = Dog('2ha',60,800)
print(b.life_value)
a.attack(b)
print(b.life_value)
#注意：像b.life_value之类的属性引用，先从实例中找life_value，然后去类中找，最后去父类中找...直至最顶级父类
"""

"""
class A:
    def hahaha(self):
        print('A')

class B(A):
    def hahaha(self):
        super().hahaha()
        #super(B,self).hahaha()
        #A.hahaha(self)
        print('B')

a = A()
b = B()
print(b.hahaha())
print(super(B,b).hahaha())
"""

"""
class Animal:
    def __init__(self,name,aggressivity,life_value):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def eat(self):
        print("%s is eating" %self.name)

class Person(Animal):
    def __init__(self,name,aggressivity,life_value,money):
        super().__init__(name,aggressivity,life_value)       #执行父类的init方法
        self.money = money       #派生出了新的属性

    def attack(self,dog):
        '''
        派生出了新的技能：人有攻击能力
        :param dog:
        '''
        dog.life_value -= self.aggressivity

    def eat(self):
        # Animal.eat(self)
        super().eat()          #继承父类的eat()方法
        print("from Person")

class Dog(Animal):
    def __init__(self,name,breed,aggressivity,life_value):
        super().__init__(name,aggressivity,life_value)       #执行父类的init方法
        self.breed = breed        #派生出了新的属性

    def bite(self,people):
        '''
        派生出了新的技能：狗会咬人
        :param people:
        '''
        people.life_value -= self.aggressivity

    def eat(self):
        super().eat()         #继承父类的eat()方法
        #Animal.eat(self)
        print("from Dog")

a = Person('tt',100,1000,600)
b = Dog('2ha','哈士奇',60,800)
print(a.name)
print(b.name)
a.eat()
"""

"""
class Teacher:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def teach(self):
        print('%s is teaching' %self.name)

class Professor(Teacher):
    pass

a = Professor('tt','male')
a.teach()
print(a.gender)
"""

"""
#私有变量
class A:
    __N = 0      #类的数据属性设为私有的__N,会变形为_A__N
    def __init__(self):
        self.__X = 10    #变形为self._A__X
    def __foo(self):
        print('from A')
    def bar(self):
        self.__foo()    #只有在类内部才能通过__foo的形式访问到

#依然可以通过a._A__N访问到,只是做语法上的变形，并不是一种严格意义上的限制外部访问
a = A()
a._A__foo()
a.bar()
"""

"""
#私有方法
#在继承中如果父类不想子类覆盖自己的方法，可以将方法定义为私有方法

#将fa定义为私有的即__fa
class A:
    def __fa(self):         #在定义时就变形成_A__fa
        print('from A')
    def test(self):
        self.__fa()         #只会以自己所在的类为准，即调用_A__fa

class B(A):
    def __fa(self):
        print('from B')

b = B()
b.test()
"""

"""
#类的封装与扩展性
class Room:
    def __init__(self,name,owner,width,height,length):
        self.name = name
        self.owner = owner
        self.__width = width
        self.__height = height
        self.__length = length

    def tell_area(self):          #对外提供的接口，隐藏内部实现，外部在想求面积或者体积时，只要修改下面一行代码
        return self.__width * self.__length * self.__height

#对于使用tell_area接口的人来说，无需改动自己的代码，就可以使用上述新的功能
a = Room('伟星玖璋台','tt',10,3,16)
print(a.tell_area())
"""










































