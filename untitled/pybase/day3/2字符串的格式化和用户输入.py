#Author : taosenlin
#Time : 2020/3/2 16:50

# 一、字符串格式化一
# 1、字符串格式化---%
# 百分号格式化方法（往字符串里传递参数，也就是表达一个字符串）

# name = 'tom'
# height = 170
# print('我叫%s,身高%scm' %(name,height))

# %s  用str()函数进行字符串转换
# %d  转成有符号的十进制数
# %f  转成浮点数（小数部分自然截断）
# %x  转成无符号十六进制数（x/X代表转换后的十六进制字符的大小写）






# 2、常用方法
# （1）指定宽度
# print('%d' %56)      #56
# print('%10d' %56)    #        56  #元素长度为10个(%正数值d,右对齐,左补齐 补空格)
# print('%010d' %56)     #0000000056  #补零
#%负数值d,左对齐,右补齐 补空格


# (2)十六进制
# print("%x" %108)       #6c
# print("%X" %108)       #6C
# print("%#X" %108)      #0X6C  #号表示0X X表示十六进制
# print("%#x" %108)      #0x6c


# (3)小数
# print('%f' %1234.56789)     #1234.567890
# print('%.2f' %1234.56789)   #1234.57
# print('%9.2f' %1234.56789)  #  1234.57
# print('%09.2f' %1234.56789) #001234.57
#小数点前表示总长度，小数点后表示小数点后长度

# print('%f' %3.1415926)    #3.141593
#字符串格式化输出小数点后6位（四舍五入）






# 二、字符串格式化---format
# 1、顺序填值法--字符串.format()---位置不能空着
# print('my name is {},I am {} years old'.format('tom',16))
# my name is tom,I am 16 years old


# (1)、{}在字符串内部叫占位符
# 指定宽度  {: 方向 宽度}   >右对齐  <左对齐  ^中间对齐
# name = 'tom'
# age = 20
# info = 'my name is {:6},I am {:6} years old'.format(name,age)
# print(info)
# my name is tom   ,I am     20 years old
#format中对传入类型有区别，传入字符串左对齐，传入数值右对齐

# info = 'my name is {:>6},I am {:>6} years old'.format(name,age)
# print(info)
# my name is    tom,I am     20 years old

# info = 'my name is {:*>6},I am {:*>6} years old'.format(name,age)
# print(info)
# my name is ***tom,I am ****20 years old
#补元素在 :(冒号)与方向符号(> <)之间



# 2、下标填值法
# print('I am {1} years old,my name is {0}'.format('tom',16))
# I am 16 years old,my name is tom

# name = 'jack'
# age = 25
# info = 'my name is {1:>6},I am {1:>6} years old'.format(name,age)
# my name is     25,I am     25 years old
# info = 'my name is {0:>6},I am {1:>6} years old'.format(name,age)
# my name is   jack,I am     25 years old
# print(info)



# 3、变量填值
# print('my name is {name},I am {age} years old'.format(name='tom',age=16))
# my name is tom,I am 16 years old



# 特例：
# name = 'jack'
# info = 'my name is {0},I am {0},I have {{}}'.format(name)
# print(info)
# my name is jack,I am jack,I have {}
#{{}}表示打印出{}符号



# 扩展：
# name = 'jack'
# age = 20
# info = f'my name is {name},I am {age} years old'
# print(info)
#my name is jack,I am 20 years old

# info = f'my name is {name:<6},I am {age:<6} years old'
# print(info)
# my name is jack  ,I am 20     years old
# format中涉及到对齐，格式为：
# :(冒号) +(加) <(左对齐)/>(右对齐) +(加) 长度






# 三、字符终端输入
# input (内置函数)
# 1、不输入一直等待
# 2、敲回车结束输入
# 3、返回值是字符串

















































