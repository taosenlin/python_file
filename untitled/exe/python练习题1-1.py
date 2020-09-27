#coding : utf8
#Author : taosenlin
#Time : 2020/8/20 15:11

"""
执行Python脚本
"""
"""
# print("hello world!")
python test5.py
"""


"""
简述位和字节的关系
"""
"""
位：计算机的计算单位，代表0或者1
字节：8位表示一个字节
"""


"""
请写出"张三"分别用utf-8和gbk编码所占的位数
"""
"""
print(len("张三".encode("utf8")))
print(len("张三".encode("gbk")))
"""
"""
name = "张三"
print(len(bytes(name,encoding="utf8")))
print(len(bytes(name,encoding="gbk")))
"""


"""
利用内置函数chr()以及random模块写一个简单随机4位验证码
4位随机验证码包括大写字母、小写字母和数字
"""
"""
import random
li = []
for i in range(0,4):
    li.append(str(random.randint(0,9)))
print(''.join(li))
"""
"""
import random
li = ''
for i in range(0,4):
    n = random.randint(0,2)
    if n == 0:
        num = chr(random.randint(65,90))
        li += num
    elif n == 1:
        num = chr(random.randint(97,122))
        li += num
    else:
        num = str(random.randint(0,9))
        li += num
print(li)
"""


"""
如何查看变量在内存中的地址
"""
"""
name = "jack"
print(id(name))
"""


"""
执行Python程序时，自动生成的.pyc文件的作用是什么
"""
"""
python执行前生成的编译字节码文件
"""


"""
实现用户输入用户名和密码，当用户名为 seven
且密码为123时，显示登陆成功，否则登陆失败！
"""
"""
name = input("请输入用户名:")
psw = input("请输入密码:")
if name == "seven" and psw == "123":
    print("登陆成功!")
else:
    print("登陆失败!")
"""


"""
实现用户输入用户名和密码，当用户名为 seven且密码为123时，
显示登陆成功，否则登陆失败，失败时允许重复输入三次
"""
"""
n = 1
while n <= 3:
    name = input("请输入用户名:")
    psw = input("请输入密码:")
    if name == "seven" and psw == "123":
        print("登录成功!")
        break
    else:
        print("登录失败!")
    n += 1
"""


"""
实现用户输入用户名和密码，当用户名为 seven或alex且 密码为123时，
显示登陆成功，否则登陆失败，失败时允许重复输入三次
"""
"""
n = 1
while n <= 3:
    name = input("请输入用户名:")
    psw = input("请输入密码:")
    if (name == "seven" or name == "alex") and psw == "123":
        print("登录成功!")
        break
    else:
        print("登录失败!")
    n += 1
"""


"""
使用while循环实现输出2-3+4-5+6.....+100的和
"""
"""
sum = 0
for i in range(2,101):
    if i % 2 == 0:
        sum += i
    else:
        sum -= i
print(sum)
"""
"""
n = 2
sum = 0
while n <= 100:
    if n % 2 == 0:
        sum += n
    else:
        sum -= n
    n += 1
print(sum)
"""


"""
求1-2+3-4+5 ... 99的所有数的和
"""
"""
sum = 0
for i in range(1,100):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
"""
"""
n = 1
sum = 0
while n <= 99:
    if n % 2 == 0:
        sum -= n
    else:
        sum += n
    n += 1
print(sum)
"""


"""
使用while循环输入 1 2 3 4 5 6   8 9 10(跳过7)
"""
"""
n = 0
while n < 10:
    n += 1
    if n == 7:
        continue
    else:
        print(n)
"""


"""
输出 1-100 内的所有奇数
"""
"""
n = 0
while n < 100:
    n += 1
    if n % 2 == 0:
        continue
    else:
        print(n)
"""
"""
num = []
for i in range(1,100,2):
    num.append(i)
print(num)
"""


"""
输出 1-100 内的所有偶数
"""
"""
num = []
for i in range(0,100,2):
    if i == 0:
        continue
    num.append(i)
print(num)
"""
"""
n = 0
while n < 100:
    n += 1
    if n % 2 == 0:
        print(n)
    else:
        continue
"""


"""
分别书写数字5,10,32,7的二进制表示
"""
"""
a = [5,10,32,7]
for i in a:
    print(bin(i))
"""


"""
简述对象和类的关系
"""
"""
对象是类的实例化
"""


"""
现有如下两个变量，请简述n1和n2是什么关系
"""
"""
n1 = 123456
n2 = n1
print(id(n1))
print(id(n2))
两个变量引用同一个内存地址
"""


"""
如有一个变量n1 = 5，请使用int的提供的方法，
得出该变量至少可以用多少个二进制位表示
"""
"""
n1 = 5
print(bytes(n1))
print(len(bytes(n1)))
"""


"""
布尔值分别有什么
"""
"""
真 假
True False
0 1
"""


"""
阅读代码，请写出执行结果
"""
"""
a = "alex"
b = a.capitalize()
print(a)
print(b)
# alex
# Alex
"""


"""
写代码，有如下变量，请按照要求实现每个功能
"""
# name = " aleX "

# a.移除name变量对应的值两边的空格，并输入移除有的内容
# print(name.strip())
# aleX

# b.判断name变量对应的值是否以 "al"开头，并输出结果
# print(name.startswith("al"))
# False

# c.判断name变量对应的值是否以 "X"结尾，并输出结果
# print(name.endswith("X"))
# False

# d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果
# print(name.replace("l","p"))
# apeX

# e.将name变量对应的值根据 " l" 分割，并输出结果。
# print(name.split("l"))
# [' a', 'eX ']

# f.请问，上一题 e分割之后得到值是什么类型？
# 列表

# g.将name变量对应的值变大写，并输出结果
# print(name.upper())
# ALEX

# h.将name变量对应的值变小写，并输出结果
# print(name.lower())
# alex

# i.请输出name变量对应的值的第2个字符？
# print(name[1])
# a

# j.请输出name变量对应的值的前3个字符？
# print(name[:3])
# al

# k.请输出name变量对应的值的后2个字符？
# print(name[-2:])
# X

# l.请输出name变量对应的值中 "e" 所在索引位置？
# print(name.index("e"))
# 3

"""
字符串是否可迭代？如可以请使用for循环每一个元素？
"""
"""
name = " aleX "
for i in name:
    print(i)
"""

"""
请代码实现：利用下划线将列表的每一个元素
拼接成字符串，li = ['alex','eric','rain']
"""
# li = ['alex','eric','rain']
# print("_".join(li))

"""
写代码，有如下列表，按照要求实现每一个功能（所有练习题同样适用于元组）
"""
# li = ['alex','eric','rain']

# a.计算列表长度并输出
# print(len(li))

# b.列表中追加元素"seven"，并输出添加后的列表
# li.append("seven")
# print(li)

# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
# li.insert(0,"Tony")
# print(li)

# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
# li[1] = "Kelly"           #修改列表中的元素直接根据下标赋值即可
# print(li)

# e.请删除列表中的元素"eric"，并输出修改后的列表
# del li[1]
# print(li)
# li.pop(1)
# print(li)
# li.remove("eric")
# print(li)

# f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
# print(li[1])
# li.pop(1)
# print(li)

# g.请删除列表中的第3个元素，并输出删除元素后的列表
# del li[2]
# print(li)

# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:3]
# print(li)

# i.请将列表所有的元素反转，并输出反转后的列表
# print(li[::-1])

# j.请使用for、len、range 输出列表的索引
"""
li = ['alex','eric','rain']
for i in range(len(li)):
    print(i)
"""

# k.请使用enumrate输出列表元素和序号（序号从 100 开始）
"""
li = ['alex','eric','rain']
for index,item in enumerate(li,100):
    print(index,item)
"""

"""
写代码，有如下列表，请按照功能要求实现每一个功能
li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
a.请输出"Kelly"
b.请使用索引找到 'all'元素并将其修改为"ALL"
"""
# li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# print(li[2][1][1])
# print(li[2][2].upper())

"""
有如下变量，请实现要求的功能
tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
a. 讲述元组的特性
b. 请问 tu 变量中的第一个元素 "alex" 是否可被修改？
c. 请问 tu 变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
d. 请问 tu 变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
"""
# 元组内元素不可以发生改变，其他与列表一样
# 不能
# 列表  可以修改
"""
tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
tu1 = tu[1][2]["k2"].append("Seven")
print(tu)
"""
# 元组  不可以修改

"""
字典
"""
# dict={'k1':"v1","k2":"v2","k3":[11,22,33]}

# a. 请循环输出所有的 key
# for k in dict.keys():
#     print(k)

# b. 请循环输出所有的 value
# for v in dict.values():
#     print(v)

# c. 请循环输出所有的 key 和 value
# for k,v in dict.items():
#     print(k,v)

# d. 请在字典中添加一个键值对， "k4":"v4"，输出添加后的字典
# dict={'k1':"v1","k2":"v2","k3":[11,22,33]}
# dict["k4"] = "v4"
# print(dict)

# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dict={'k1':"v1","k2":"v2","k3":[11,22,33]}
# dict["k1"] = "alex"
# print(dict)

# f. 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
# dict={'k1':"v1","k2":"v2","k3":[11,22,33]}
# dict["k3"].append(44)
# print(dict)

# g. 请在 k3 对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dict={'k1':"v1","k2":"v2","k3":[11,22,33]}
# dict["k3"].insert(0,18)
# print(dict)

"""
转换
"""
# a. 将字符串 s="alex" 转换成列表
# s = "alex"
# print(list(s))

# b. 将字符串 s="alex" 转换成元祖
# s = "alex"
# print(tuple(s))

# b. 将列表 li=["alex","seven"] 转换成元组
# li=["alex","seven"]
# print(tuple(li))

# c. 将元祖 tu=('Alex',"seven") 转换成列表
# tu=('Alex',"seven")
# print(list(tu))

# d. 将列表 li=["alex","seven"] 转换成字典且字典的 key 按照 10 开始向后递增
"""
li=["alex","seven"]
li_dict = {}
for k,v in enumerate(li,10):
    li_dict[k] = v
print(li_dict)
"""

"""
转码
"""
# n="老男孩"
# a. 将字符串转换成 utf-8 编码的字节，并输出，然后将该字节再转换成 utf-8 编码字符串，再输出
# print(n.encode("utf8"))
# n1 = b'\xe8\x80\x81\xe7\x94\xb7\xe5\xad\xa9'
# print(n1.decode("utf8"))

# a. 将字符串转换成 gbk 编码的字节，并输出，然后将该字节再转换成 gbk 编码字符串，再输出
# print(n.encode("gbk"))
# n1 = b'\xc0\xcf\xc4\xd0\xba\xa2'
# print(n1.decode("gbk"))

"""
求 1-100 内的所有数的和
"""
"""
sum = 0
for i in range(1,101):
    sum += i
print(sum)
"""
"""
n = 1
sum = 0
while n <= 100:
    sum += n
    n += 1
print(sum)
"""

"""
元素分类
有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的
第一个 key 中，将小于 66 的值保存至第二个 key 的值中。
即： {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}
"""
"""
v1 = []
v2 = []
dict = {'k1':v1,'k2':v2}
li = [11,22,33,44,55,66,77,88,99,90]
for i in li:
    if i > 66:
        v1.append(i)
    else:
        v2.append(i)
print(dict)
"""

"""
查找元素，移除空格，并查找以 a或A开头 并且以 c 结尾的所有元素
"""
"""
li = ["alec", " aric", "Alex", "Tony", "rain"]
for i in li:
    if i.strip().startswith("a") or i.strip().startswith("A") and i.strip().endswith("c"):
        print(i.strip())
"""

"""
购物车
功能要求：
要求用户输入总资产，例如： 2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
goods=[
{"name":"电脑","price":1999},
{"name":"鼠标","price":10},
{"name":"游艇","price":20},
{"name":"美女","price":998},
]
"""
"""
money = int(input("请输入总资产:"))
while 1:
    print("########下面是商品展示########")
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
    ]
    for i in range(len(goods)):
        print(i,goods[i]["name"],goods[i]["price"])
    dict = {}
    sum_mon = 0
    while 1:
        num = input("请输入商品序号(请按Q退出!):")
        if num == "Q":
            break
        elif num not in ["0","1","2","3"]:
            continue
        else:
            num1 = int(input("请输入商品数量:"))
            total = goods[int(num)]["price"] * num1
            sum_mon += total
    print("您购买的商品总价为"+str(sum_mon))
    if int(sum_mon) > money:
        print("账户余额不足!")
    else:
        print("购物成功!")
    assure = input("请问是否需要继续购物(不需要请选N退出)?")
    if assure == "N":
        break
"""

"""
用户交互，显示省市县三级联动的选择。
1、用户交互，显示省市县三级联动的选择。

2、输入省份显示所有市。

3、输入市显示县。
"""

dic = {
    "河北":{
        "石家庄" :["鹿泉","藁城","元氏"],
        "邯郸" : ["永年","涉县","磁县"]
    },
    "河南":{
        "郑州":["巩义","登封","新密"],
        "开封":["金明","鼓楼","通许"]
    },
    "山西":{
        "太原":["古交","清徐","阳曲"],
        "大同":["天镇","阳高","广灵"]
    }
}






