#Author : taosenlin
#Time : 2020/3/12 17:30

# 一、异常的概念
# 代码运行产生错误，无法继续执行



# 二、异常的产生
# 例：输入0会导致当前程序的异常退出
'''
while True:
    num = input("input a number:")
    print("100/%s = %s" %(num,100/int(num)))
'''
# 希望的行为：
# 1、程序不要退出
# 2、提示用户输入错误
# 3、继续让用户重新输入数字，继续执行



# 三、异常的捕获与处理
# 1、捕获一种异常

# （1）关键字
# try...except...

'''
try:
    b = 4/0
except ZeroDivisionError:
    print("handle ZeroDivisionError")
'''

# （2）try  代码块  指明作用域

# （3）ZeroDivisionError(类)  指明专门捕获ZeroDivisionError异常

# （4）except 代码块 是异常处理的代码

# （5）执行结果
# 1、除以0的异常被 try...except捕获了
# 2、并执行了except里面的代码
# 3、其他的异常不会被捕获


# 2、例：

# 注：if...过滤...过滤已知     前置
#     try...except...         后置
'''
while True:
    num = input("input a number:")
    try:
        print("100/%s = %s" %(num,100/int(num)))
    # except ZeroDivisionError:
    #     print("除数不能为0！")
    # except ValueError:
    #     print("请输入数值！")
    except ZeroDivisionError as e:
        print("handle ZeroDivisionError:",e)
    # handle ZeroDivisionError: division by zero
'''


# 3、获取异常信息
# （1）捕获后得到详细的异常信息
'''
try:
    ohmy
except NameError as e:
    print("handle NameError:",e)
# handle NameError: name 'ohmy' is not defined
'''
# （2）e 就是异常对象
# （3）我们可以打印出里面存储的具体错误信息



# 四、捕获所有异常
'''
try:
    ohmy
    b = 4/0
except ZeroDivisionError:
    print("handle ZeroDivisionError")
except NameError:
    print("handle NameError")
# handle NameError
'''
# 1、ZeroDivisionError 指明专门捕获ZeroDivisionError异常
# 2、NameError 指明专门捕获NameError异常
# 3、对应的处理代码区块
# 4、执行结果是 NameError 而不是 ZeroDivisionError

# 5、有时我们不知道会抛出什么异常，故捕获所有异常
'''
try:
    ohmy
    b = 4/0
# except Exception as e:            #Exception 指明所有异常（父类）
#     print("handle unkown exception:",e)
# except :                 #Exception可不写（所有异常）
#     print("异常了！")
'''


# 6、如果要知道异常信息
'''
import traceback
try:
    ohmy
except:
    #打印出错误信息
    print("handle unkown exception \n" + traceback.format_exc())
    #将错误信息存到日志中，可用于定位问题
    traceback.print_exc(file=open('./error.txt','w',encoding='utf8'))
'''


# 7、finally语句
# 不管是否有异常,我们都要执行一段代码
'''
try:
    b = 4/0
    ohmy
except ZeroDivisionError:
    print("xxx")
except:
    print("yyy")
finally:
    print("in finally")
#finally一定要放在最后

xxx
in finally
'''


# 8、else语句
# 没有异常的情况下,要执行一段代码
'''
try:
    print("do something")
except ZeroDivisionError:
    print("xxx")
except:
    print("yyy")
else:
    print("zzz")
finally:
    print("jjj")
#else 必须跟在所有except代码块后面,在finally前面

do something
zzz
jjj
'''


# 五、函数调用栈
'''
def f3():
    print("in f3 - begin")
    b = 4/0
    print("in f3 - end")

def f2():
    print("in f2 - begin")
    f3()
    print("in f2 - end")

def f1():
    print("in f1 - begin")
    f2()
    print("in f1 - end")

f1()
'''
#函数调用栈关系(一层层上报)
#总结:出现报错信息可以从下面开始查看最开始引发错误的地方

# 例:
# try:
#     fo = open("文件不存在!")
# except:
#     print("路径找不到!")
# 路径找不到!



# 六、自定义异常
#异常是个类,类就可以定义

# 1、继承自 Exception
'''
class NameTooLongError(Exception):
    pass
class NameTooShortError(Exception):
    pass
'''


# 2、使用 raise 抛出
'''
raise NameTooLongError
'''


# 3、抛出异常用在:
# (1)当函数里面出现错误,代码无法继续执行的时候
# (2)告诉上层调用代码,什么样执行错误产生了
# (3)由上层调用代码决定如何处理

'''
#异常类
class NameTooLongError(Exception):
    print("NameTooLongError")
    def methFun(self):
        pass

#自定义异常---name 过短异常---继承
class NameTooShortError(Exception):             #异常类
    print("NameTooShortError")

    def inputName(self):
        name = input("请输入用户名:")
        if len(name) > 10:
            #自定义的异常要自行抛出
            raise NameTooLongError
        elif len(name) < 5:
            #自定义的异常要自行抛出
            raise NameTooShortError

        try:
            inputName()
        except NameTooShortError:
            print("您输入的用户名太短!")
        except NameTooLongError as e:
            print("您输入的用户名太长!",e)
            e.methFun()
'''


# 注:
'''
for one in range(1,5):
    if one == 3:
        raise ValueError("异常了,抛出")
    print(one)
#当你想抛出异常时,可人为制造异常
'''


# 七、断言
# assert ---检查点---如果后续代码比较重要,而且很依靠前面的数据或者状态

'''
tel = input("请输入手机号码:")
assert len(tel) == 11,"手机位数有误!"
print("我在处理手机运营商操作")
'''






























