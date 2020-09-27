#coding : utf8
#Author : taosenlin
#Time : 2020/6/9 18:59

# 一、time模块
# 三种时间表示
# 在Python中，通常有这几种方式来表示时间：

# 1、时间戳(timestamp) ： 通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
# （从1970年到现在这一刻一共有多少秒）我们运行“type(time.time())”，返回的是float类型。如 time.time()=1525688497.608947

# 2、格式化的时间字符串（字符串时间） 如“2018-05-06”

# 3、元组(struct_time) （结构化时间） ： struct_time元组共有九个元素:
# (年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)


"""
# 1- time.time
# 返回当前时间的时间戳
import time
ti = time.time()
print(ti)
# 1591701420.130372
"""


"""
# 2- time.localtime([secs])
# 将一个时间戳转换为当前时区的struct_time，即时间数组格式的时间 。secs参数未提供，则以当前时间为准。
import time
ti = time.localtime()
print(ti)
print(ti.tm_year)
print(ti.tm_mon)
print(ti.tm_mday)
ti1 = time.localtime(1500000000)
print(ti1)
# time.struct_time(tm_year=2020, tm_mon=6, tm_mday=9, tm_hour=19, tm_min=17, tm_sec=33, tm_wday=1, tm_yday=161, tm_isdst=0)
# 2020
# 6
# 9
# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=10, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)
"""


"""
# 3- strftime(format[,t])
# 把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。
# 如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23） #注意是大写
# %M 分钟数（00=59） #注意是大写
# %S 秒（00-59） #注意是大写
import time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
2020-06-09 19:22:40
"""



# 二、random模块
# 产生随机数值的模块

"""
# 1- random.random()
# 随机产生大于0且小于1之间的小数
import random
v1 = random.random()
print(v1)
# 0.9848839393182642
"""


"""
# 2- random.uniform(a,b)
# 返回一个介于a和b之间的浮点数。一般是a<b，即返回a和b之间的浮点数，如果 a大于b，则是b到a之间的浮点数。
# 这里的a和b都有可能出现在结果中。
import random
v1 = random.uniform(1.1,2.8)
print(v1)
# 2.647384018758186
"""


"""
# 3- random.randint(a,b)
# 返回range[a,b]之间的一个整数，即整数
import random
v1 = random.randint(1,3)
print(v1)
# 3
"""


"""
# 4- random.randrange(start,stop[,step])
# random.randrange(start, stop[, step]) # 返回range[start,stop)之间的一个整数，start\stop必须是整数，可加step，跟range(0,10,2)类似。
# start缺省值为1,stop值不能取到。
import random
v1 = random.randrange(0,10,2)
print(v1)
# 8
"""


"""
# 5- random.choice(seq)
# 从非空序列seq（字符串也是序列）中随机选取一个元素。如果seq为空则弹出 IndexError异常。
import random
v1 = random.choice([1,5,2,"ni",["hi",8],{"k1":"v1"}])
print(v1)
print(random.choice("nicholas"))
"""


"""
# 6- random.sample( population, k)
# 从population样本或集合中随机选取k个不重复的元素组成新的序列
import random
v1 = random.sample([1,5,2,"ni",["hi",8],{"k1":"v1"}],3)
print(v1)
# [['hi', 8], 1, {'k1': 'v1'}]
"""


"""
# 7- random.shuffle()
# 将列表的顺序打乱
import random
li = [2,5,6,8]
random.shuffle(li)
print(li)
# [5, 8, 2, 6]
"""



# 三、string模块（了解）
# 下面是一些字符串常量

"""
# 1- string.ascii_lowercase
# 返回字符串小写字母’abcdefghijklmnopqrstuvwxyz’
import string
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
"""


"""
# 2- string.ascii_uppercase
# 返回字符串大写的字母’ABCDEFGHIJKLMNOPQRSTUVWXYZ’
import string
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""


"""
# 3- string.ascii_letters
# 返回小写的a~z加上大写的A~Z组成的字符串,即string.ascii_lowercase连接string.ascii_uppercase组成的字符串
import string
print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
"""


"""
# 4- string.digits
# 数字0到9的字符串:’0123456789’
import string
print(string.digits)
# 0123456789
"""


"""
# 5- string.hexdigits
# 返回字符串’0123456789abcdefABCDEF’，即十六进制的所有字符（英文字母加上大小写）组成的字符串
import string
print(string.hexdigits)
# 0123456789abcdefABCDEF
"""


"""
# 6- string.octdigits
# 返回八进制的所有字符组成的字符串
import string
print(string.octdigits)
# 01234567
"""


"""
# 7- string.punctuation
# 返回所有标点字符
import string
print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
"""


"""
# 8- string.printable
# 返回所有的可打印的字符的字符串。包含数字、字母、标点符号和空格
import string
print(string.printable)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 分析：即string.digits加上string.ascii_letters加上string.punctuation组成的字符串
"""



# 四、验证码练习
# 生成四位数字验证码

"""
# 1、
import random
li = [str(i) for i in random.sample(range(0,10),4)]
print(li)
print("".join(li))
"""

"""
# 2、
import random
li = []
for i in range(0,4):
    li.append(str(random.randint(0,9)))
print("".join(li))
"""



# 生成数字加字母的四位验证码
import random
import string
# flag = False
while True:
    res_str = ("%s%s")%(string.ascii_letters,string.digits)
    code = "".join(random.sample(res_str,4))
    if code.isalpha():
        continue
    else:
        # flag = True
        print(code)
        break
    # if flag:
    #     break


































































