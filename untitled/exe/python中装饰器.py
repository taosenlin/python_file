#coding : utf8
#Author : taosenlin
#Time : 2020/6/11 19:47

# 一、装饰器的应用
# 装饰器的作用就是为已经存在的函数或对象添加额外的功能。


# 二、装饰器相关知识
# 装饰器 = 高阶函数 + 函数嵌套 + 闭包
# 高阶函数的定义：
# 1、函数接收的参数是一个函数名
# 2、函数的返回值是一个函数
# 3、满足上述条件任意一个，都可以称之为高阶函数


# 三、闭包
# 在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。
# python中形成闭包的三个条件:
# 1、必须有一个内嵌函数(函数里定义的函数）---这对应函数之间的嵌套
# 2、内嵌函数必须引用一个定义在闭合范围内(外部函数里)的变量---内部函数引用外部变量
# 3、外部函数必须返回内嵌函数---必须返回那个内部函数

# 一般情况下，如果一个函数运行结束了，内存中将不会存储任何关于该函数的东西，函数的局部变量都会消失，
# 但是闭包是一个特殊的情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，就把这个临时变量绑定给了内部函数，然后自己再结束。


"""
def outer():
    name = 'tsl'
    def inner():             # inner()是内函数
        # print(name)        #在内函数中，用到了外函数的临时变量
        print('里面一层',name)
    print('外面一层',name)
    return inner             #外函数的返回值是内函数的引用

a = outer()
a()
# 外面一层 tsl
# 里面一层 tsl
"""


# 四、装饰器

"""
# 1、最简单的装饰器
def test(func):
    def wrapper():
        print("装饰器")
        print("-"*20)
        func()
    return wrapper

# @test
def func1():
    print("from func1")

func1 = test(func1)
func1()
"""


"""
# 2、使用语法糖、对原函数有参数的函数进行装饰，为装饰器函数加上返回值
def test(func):
    def wrapper(*args,**kwargs):
        print("装饰器")
        print("-"*20)
        res = func(*args,**kwargs)
        return res
    return wrapper

@test
def func1():
    print('from func1')

@test
def func2(name,age):
    print('from func2')
    print(name)
    print(age)

@test
def func3(name,age,gender):
    print('from func3')
    print(name)
    print(age)
    print(gender)

@test
def func4(name,age,gender):
    print('from func4')
    print(name)
    print(age)
    print(gender)


func1()
print("*"*30)
func2('tsl',18)
print("*"*30)
func3(name='tsl',age=18,gender='男')
print("*"*30)
func4('tsl',18,gender='男')
"""


# 3、模拟购物商城登录权限验证的装饰器
# 实现功能，在每个功能函数执行前验证是否登录成功。
userinfo = [{"username":"tsl","pwd":"123"},
            {"username":"wl","pwd":"456"},
            {"username":"tt","pwd":"789"},
            {"username":"ll","pwd":"888"}
            ]
user_status = {"username":None,"status":False}

def auth_func(func):
    def wrapper(*args,**kwargs):
        if user_status["username"] and user_status["status"]:     #判断用户登录状态，如果已经登录则执行其他功能函数
            res = func(*args,**kwargs)
            return res

        username = input("请输入用户名:")
        pwd = input("请输入密码:")

        for i in userinfo:
            if i["username"] == username and i["pwd"] == pwd:
                print("登录成功:%s"%username)
                user_status["username"] = username
                user_status["status"] = True
                res = func(*args,**kwargs)
                return res
        else:
            print("登录失败，请重新输入密码!")
    return wrapper


@auth_func
def index():
    print("欢迎来到英雄联盟!")

@auth_func
def hero(name):
    print("%s:我的大刀已经饥渴难耐!"%name)

@auth_func
def skill(sk_name1,sk_name2,sk_name3):
    print("打团%s,%s,%s一通乱按!"%(sk_name1,sk_name2,sk_name3))

index()
hero("蛮王")
skill("Q","W","E")






















































































































