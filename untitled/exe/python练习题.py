#coding : utf8
#Author : taosenlin
#Time : 2020/3/24 15:13

#列表转字典
"""
i = ["a","b"]
l = [1,2]
print(dict([i,l]))
# {'a': 'b', 1: 2}
"""


########################################################
"""输入某年某月某日，判断这一天是这一年的第几天？"""
"""
year = int(input("输入年份："))
month = int(input("输入月份：")) - 1
day = int(input("输入日期："))
sum_day = day
lead = 0
if (year % 400 == 0) or (year % 4 ==0 and year % 400 != 0):
    lead = 1
    sum_day += lead
list_month = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(month):
    sum_day += list_month[i]
print("%s年%s月%s日,今年已经过了%s天" %(year,month,day,sum_day))
#################################################################
"""

"""
输出9*9 口诀表
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
"""
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" %(j,i,j*i),end=" ")
    print()
"""

"""
利用条件运算符的嵌套来完成此题：学习成绩>=90 分的同学用A表示， 60-89 分
之间的用B表示， 60 分以下的用C表示。
"""
"""
score = input("请输入学习成绩:")
if score >= "90":
    print("A")
elif "60" < score < "89":
    print("B")
elif score < "60":
    print("C")
"""
"""
score = input("请输入学习成绩：")
info = "A" if score >= "90" else "B" if score >= "60" else "C"
print(info)
"""

"""
一球从100 米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
第10 次落地时，共经过多少米？第10 次反弹多高？
"""
"""
height = 100
len = 100
for i in range(10):
    height /= 2
    len += height*2
print(height)
print(len)
"""

"""
从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入一个#为止
"""
"""
def writefile():
    f = open(r"D:\1.txt","a")
    while True:
        str = input("请输入字符：")
        if str == "#":
            break
        else:
            f.write(str+'\n')
            f.flush()
    f.close()

writefile()
"""
"""
从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入一个#为止
"""
"""
f = open(r'D:\tsl.txt','w')
while True:
    arg = input("请输入字符:")
    if arg == '#':
        break
    else:
        f.write(arg + '\n')
        f.flush()
f.close()
"""

"""
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘
文件“ test ”中保存。输入的字符串以！结束。
"""
"""
def writefile():
    f = open(r"D:\test.txt","w")
    str = input("请输入字符串:").upper()
    f.write(str + "!")
    f.flush()
    f.close()

writefile()
"""
"""
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
"""
"""
f = open(r"D:\test.txt",'w')
arg = input("请输入一个字符串:")
arg1 = arg.upper()
f.write(arg1)
f.flush()
f.close()
"""

"""
有两个磁盘文件A 和B,各存放一行字母, 要求把这两个文件中的信息合并（按字母
顺序排列），输出到一个新文件C中。
"""
"""
with open(r"D:\file1.txt","r") as f1,open(r"D:\file2.txt","r") as f2:
    f3 = f1.read() + "\n"
    f4 = f2.read()
    file = f3 + f4
    with open(r"D:\C.txt","w") as f:
        f.write(file)
"""
"""
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的
信息合并(按字母顺序排列), 输出到一个新文件C中。
"""
"""
with open(r'D:\file1.txt','r') as f1,open(r'D:\file2.txt','r') as f2:
    r1 = f1.read() + '\n'
    # print(r1)
    r2 = f2.read()
    r3 = r1 + r2
    with open(r'D:\file3.txt','w') as f3:
        f3.write(r3)
"""

"""
将一个列表的数据复制到另一个列表中
"""
"""
a = [1,2]
b = a[:]
print(b)
"""

""""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""
"""
l = []
for i in range(3):
    num = int(input("请输入整数："))
    l.append(num)
l.sort()
print(l)
"""
"""
输出 9*9 乘法口诀表
"""
"""
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
"""
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" %(j,i,j*i),end=" ")
    print()
"""

"""
暂停1秒输出
"""
"""
import time
myD = {'a':"tao",'b':"wu"}
for key,value in myD.items():
    print(key,value)
    time.sleep(1)
"""

""""
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方
分析：三位数 个位三次方+十位三次方+百位三次方 等于这个三位数
"""
"""
for i in range(100,1000):
    m = i // 100
    n = i // 10 % 10
    l = i % 10
    if i == m**3 + n**3 + l**3:
        print(i)
"""


"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

"""
alpha = 0
space = 0
digit = 0
other = 0

str = input("请输入一行字符：")
for i in str:
    if i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        other += 1
print("英文字母：%d,空格：%d,数字：%d，其他字符：%d" %(alpha,space,digit,other))
"""
"""
alpha = 0
space = 0
digit = 0
other = 0

str = input("请输入一行字符：")
i = 0
while i < len(str):
    if str[i].isalpha():
        alpha += 1
    elif str[i].isspace():
        space += 1
    elif str[i].isdigit():
        digit += 1
    else:
        other += 1
    i += 1
print("英文字母：%d，空格：%d，数字：%d，其他：%d" %(alpha,space,digit,other))
"""

"""一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
"""
100 50 25 12.5 
"""
"""
height = 100
len = 100
for i in range(10):
    height /= 2
    len += height * 2
print(height)
print(len)
"""

"""
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
"""
from functools import reduce

a = 2.0
b = 1.0
l = []
l.append(a/b)
for i in range(1,20):
    a,b = a+b,a
    l.append(a/b)
print(reduce(lambda x,y:x+y,l))
"""

"""
求1+2!+3!+...+20!的和。
程序分析：累加变成累乘  1+1x2+1x2x3...+1x2x3...x20
"""
"""
i = 0
n = 0
s = 1
for i in range(1,21):
    s *= i
    n += s
print("1+2!+3!+...+20!=",n)
"""

"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
程序分析
"""
"""
num = int(input("请输入一个不多于5位的正整数："))
a = num // 10000
b = num % 10000 // 1000
c = num % 1000 // 100
d = num % 100 // 10
e = num % 10

if a != 0:
    print(e,d,c,b,a)
elif b != 0:
    print(e,d,c,b)
elif c != 0:
    print(e,d,c)
elif d != 0:
    print(e,d)
else:
    print(e)
"""

"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
回文数即左右对称，可采取下标取值对称比较的方法
"""
"""
flag = True
num = input("输入一个五位数的数字：")
for i in range((len(num)-1)//2):
    if num[i] != num[len(num)-1-i]:
        flag = False
        break
if flag:
    print("%s是一个回文数" %num)
else:
    print("%s不是一个回文数" %num)
"""

"""
请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。
dataList = [Mon,Tue,Wed,Thu,Fri,Sat,Sun]
"""
"""
data = input("请输入任意星期的的第一个英文字母：")
if data == 'M':
    print('Monday')
elif data == 'W':
    print('Wednesday')
elif data == 'F':
    print('Friday')
elif data == 'S':
    # print("请输入星期的第二个英文字母：")
    data1 = input("请输入星期的第二个英文字母：")
    if data1 == 'a':
        print('Saturday')
    elif data1 == 'u':
        print('Sunday')
    else:
        print('data error')
elif data == 'T':
    # print("请输入第二个英文字母：")
    data2 = input("请输入第二个英文字母：")
    if data2 == 'u':
        print('Tuesday')
    elif data2 == 'h':
        print('Thursday')
    else:
        print('data error')
"""

"""
按相反的顺序输出列表的值。
"""
"""
a = ['123','456','789']
for i in a[::-1]:
    print(i)
"""

"""
按逗号分隔列表。
"""
"""
a = ['1','2','3','4']
str = ','.join(n for n in a)
print(str)
"""

"""
练习函数调用。
"""
"""
def hello_world():
    print("hello world")

def three_hellos():
    for i in range(3):
        hello_world()

if __name__ == '__main__':
    three_hellos()
"""

"""
求100之内的素数
程序分析：素数为大于1的 ，乘积为1和本身的数
"""
"""
lower = int(input("请输入最小的值："))
upper = int(input("请输入最大的值："))

for num in range(lower,upper+1):
    #素数大于1
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
"""

"""
对10个数进行排序。
"""
"""
l = []
N =10
for i in range(N):
    num = int(input("请输入10个数："))
    l.append(num)

# for i in range(len(l)-1):
#     for j in range(len(l)-i-1):
#         if l[j] > l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print(l)
"""

"""
求一个3*3矩阵主对角线元素之和。
"""
"""
a = []
sum = 0
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(int(input("请输入数字:")))
    print(a)

for i in range(3):
    sum += a[i][i]
print(sum)
"""

"""
将一个数组逆序输出。
思路：将第一个与最后一个交换
"""
"""
a = [1,4,5,6,9]
N = len(a)
for i in range(len(a)//2):
    a[i],a[N-1-i] = a[N-1-i],a[i]
print(a)
"""

"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
X = [[12,7,3],        
    [4 ,5,6],
    [7 ,8,9]]       
    
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]] 
思路分析：可以创建一个新的3X3矩阵，将X和Y对应位置的数据相加后，存放到新建的矩阵
"""
"""
X = [[12,7,3],
    [4,5,6],
    [7,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#遍历输出行
for i in range(len(X)):
    #遍历输出列
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
# print(result)
for r in result:
    print(r)
"""

"""
统计 1 到 100 之和。
"""
"""
num = 0
i = 1
while i <= 100:
    num = num + i
    i += 1
print(num)
"""
"""
temp = 0
for i in range(1,101):
    temp += i
print(temp)
"""

"""
求输入数字的平方，如果平方运算后小于 50 则退出。
"""
"""
while True:
    num = int(input("请输入数字："))
    nums = num * num
    print("运算结果为%d" %nums)
    if nums < 50:
        break
    else:
        continue
"""

"""
两个变量值互换。
"""
"""
def exchange(a,b):
    a,b = b,a
    return (a,b)

if __name__ == '__main__':
    x=10
    y=20
    x,y = exchange(x,y)
    print(x,y)
"""

"""
数字比较。
"""
"""
i = 10
j = 20
if i > j:
    print('%d 大于 %d' %(i,j))
elif i == j:
    print('%d 等于 %d' %(i,j))
elif i < j:
    print('%d 小于 %d' %(i,j))
else:
    print('未知')
"""

"""
输出一个随机数
"""
"""
import random
print(random.randint(0,1))
"""

"""
计算字符串长度
"""
"""
str = 'abcdefg'
print(len(str))
"""

"""
查找字符串
"""
"""
str = 'abcdefg'
str1 = 'cde'
print(str.find(str1))
"""

"""
输入3个数a,b,c，按大小顺序输出。
"""
"""
a = int(input("输入数字a:"))
b = int(input("输入数字b:"))
c = int(input("输入数字c:"))

for i in range(3):
    if a > b:
        a,b = b,a
    elif a > c:
        a,c = c,a
    elif b > c:
        b,c = c,b
print(a,b,c)
"""

"""
写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
"""
"""
def length():
    lens = len(input("请输入字符串:"))
    return lens

if __name__ == '__main__':
    print('输入的字符串长度为 %d' % length())
"""

"""
创建一个链表
"""
"""
nums = []
for i in range(6):
    num = int(input("请输入数字:"))
    nums.append(num)
print(nums)
"""

"""
反向输出一个链表
"""
"""
l = [int(input("请输入数字:")) for i in range(6)]
# print(l)
# l.reverse()
# print(l)
# [1, 2, 3, 4, 5, 6]
for i in range(len(l)//2):
    l[i],l[len(l)-1-i] = l[len(l)-1-i],l[i]
print(l)
"""

"""
列表排序及连接
"""
"""
a = [1,3,2]
b = [6,8,5]
# a.sort()
# print(a)
l = a + b      #临时-另存地址
# print(l)
# [1, 3, 2, 6, 8, 5]
a.extend(b)    #扩展-在已有地址里面对数据扩展
print(a)
"""

"""
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print(l)
"""
"""
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)
"""

"""
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""
"""
def even(n):
    num = 0
    for i in range(2,n+1,2):
        num += 1/i
    return num

def odd(n):
    num = 0
    for i in range(1,n+1,2):
        num += 1/i
    return num

if __name__ == '__main__':
    n = int(input("请输入一个数字:"))
    if n % 2 == 0 :
        num = even(n)
    else:
        num = odd(n)
    print(num)
"""

"""
循环输出列表
"""
"""
alist = [888,666,999,333]
"""
"""
for i in alist:
    print(i)
"""
"""
for i in range(len(alist)):
    print(alist[i])
"""

"""
找到年龄最大的人，并输出。请找出程序中有什么问题。
"""
"""
person = {"zhao":"28","qian":"30","sun":"32","li":"35","wang":"21"}
# print(person.keys())
m = 'wang'
for key in person.keys():
    if person[m] < person[key]:
        m = key
print("%s %s" %(m,person[m]))
"""

"""
字符串排序。
"""
"""
str1 = input("请输入字符串：")
str2 = input("请输入字符串：")
str3 = input("请输入字符串：")
for i in range(3):
    if str1 > str2:
        str1,str2 = str2,str1
    elif str1 > str3:
        str1,str3 = str3,str1
    elif str2 > str3:
        str2,str3 = str3,str2
print(str1,str2,str3)
"""

"""
连接字符串
"""
"""
a = ['abc','def','ghi']
print(','.join(a))
"""

"""
输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
程序分析：999999 / 13 = 76923
"""
"""
num = int(input("请输入一个奇数:"))
n = 1
sum = 9
m = 9
c = 1

while n != 0:
    if sum % num == 0:
        n = 0
    else:
        m *= 10
        sum += m
        c += 1
print("最少输入%d个9除以%d结果为整数，%d" %(c,num,sum))
"""

"""
两个字符串连接程序。
"""
"""
a = 'abcdefg'
b = 'hijklmn'
#连接字符串
c = a + b
print(c)
"""

"""
读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的*。
"""
"""
n = 1
while n <= 7:
    a = int(input("请输入一个整数:"))
    while a < 1 or a > 50:
        a = int(input("请输入一个整数:"))
    print(a * "*")
    n += 1
"""

"""
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
"""
"""
num = int(input("请输入四位整数:"))
a = []
a.append(num // 1000)
a.append(num % 1000 // 100)
a.append(num % 100 // 10)
a.append( num % 10)
for i in range(4):
    a[i] += 5
    a[i] %= 10
for i in range(2):
    a[i],a[4-1-i] = a[4-1-i],a[i]
for i in a:
    print(i,end='')
"""

"""
列表使用实例。
"""
# testList = [10086,'中国移动',[1,2,4,5]]
#列表长度
# print(len(testList))
# 3
# 到列表结尾
# print(testList[1:])
# ['中国移动', [1, 2, 4, 5]]
#添加元素
# testList.append('i\'m new here')
# print(testList)
# [10086, '中国移动', [1, 2, 4, 5], "i'm new here"]
#弹出列表的最后一个元素
# print(testList[-1])
# [1, 2, 4, 5]
# num = [[1,2,3],[4,5,6],[7,8,9]]
# print(num)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(num[1])
# [4, 5, 6]
# col = [row[1] for row in num]
# print(col)
# [2, 5, 8]
# col = [row[1] for row in num if row[1] % 2 == 0]
# print(col)

"""
时间函数举例1
"""
"""
import time
print(time.ctime())
"""

"""
时间函数举例2
"""
"""
import time
startTime = time.time()
for i in range(3000):
    print(i)
endTime = time.time()
print(endTime - startTime)
"""

"""
时间函数举例3
"""
"""
import time
startTime = time.clock()    #Python 3.8已将time.clock移除
for i in range(10000):
    print(i)
endTime = time.clock()
print("总耗时%6.3f" % (endTime - startTime))
"""

"""
时间函数举例4,一个猜数游戏，判断一个人反应快慢。
首先咨询用户是否需要玩，然后随机生成一个数字，从客户开始猜数字开始计时，(如果用户输入的数字
与随机生成的数字不相等，判断数字与随机生成数字的大小，并重新输入)
直到猜中数字结束，计算总时间 ，如果总时间小于10秒，聪明；10-15，良好；15-25，bad
"""
"""
import time
import random

st = input("do you want to play the game : 'Y' or 'N': \n")
while st == 'Y':
    num = int(random.randint(0,2**8))
    startTime = time.time()*10
    guess = int(input("please into number: \n"))
    while num != guess:
        if num > guess:
            print("please into a bigger number")
            guess = int(input("please into number: \n"))
        else:
            print("please into a smaller number")
            guess = int(input("please into number: \n"))
    endTime = time.time()*10
    var = (endTime - startTime) // 18.2
    print(var)
    if var < 10:
        print("your are clever")
    elif var < 15:
        print("you are good")
    elif var < 30:
        print("you are bad")
    print("The number you guess is %d" %guess)
    print("The time is %d" % var)
"""

"""
startTime = time.time()*10
for i in range(10000):
    print(i)
endTime = time.time()*10
print(startTime)
print(endTime)
print(endTime - startTime)
"""

"""
计算字符串中子串出现的次数
"""
"""
num1 = input("请输入一个字符串:")
num2 = input("请输入字符串的子串:")
ncount = num1.count(num2)
print(ncount)
"""

"""
列表转换为字典
"""
"""
i = ['a','b']
l = [1,2]
print(dict([i,l]))
# {'a': 'b', 1: 2}
"""

"""
获取 100 以内的质数。
程序分析：质数为大于1的自然数中，除了它本身和1之外没有别的因数的数称为质数
"""
"""
num = []
i = 2
for i in range(2,100):
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        num.append(i)
print(num)
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
money = int(input("请输入总资产:"))
while True:
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
    ]
    for i in range(len(goods)):
        print(i+1,goods[i]["name"],goods[i]["price"])
    good_dict = {}
    sum = 0
    while True:
        aOne = input("请输入所选择的商品序号(如果已经加入商品序号，请按Q退出):").upper()
        if aOne == "Q":
            break
        elif aOne not in ["1","2","3","4"]:
            continue
        else:
            aTwo = int(input("请输入所选择商品的份数:"))
        good_dict[int(aOne)] = aTwo
        total = goods[int(aOne) - 1]["price"] * aTwo
        sum += total
    if int(sum) > money:
        print("账户余额不足!")
    else:
        print("购物成功，当前账户余额为%d" %(money - int(sum)))
    s = input("是否还要继续购物?如果是，请选择Y:").upper()
    if s == "Y":
        continue
    else:
        break



























































































































