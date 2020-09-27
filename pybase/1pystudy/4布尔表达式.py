#Author : taosenlin
#Time : 2020/2/28 10:20

# 一、布尔类型
# (1)只要俩种取值
# True  (真,对)   #不可以小写
# False (假,错)   #不可以小写



# 二、布尔表达式
# isSelect = True
# print(3+1)           #算术表达式
# print(3>1)             #>=、==、!=、<=  关系运算符（均为布尔类型）

"""
比较：验证地方在python解释器里面
1-  ==  表示左右俩边的对象值（内容）相等 ---[-5,256]
2-  is  表示俩个对象完全相等（值、地址）
"""



# 三、字符串的比较
# print('abc'>'b')    # a-97  A-65  字符串比较--不比数量，比对应位置的ASCII值



# 四、in 和 not in
#(1)列表
# alist = [10,20,30]
# print(10 in alist)          #True   #前者可以是后者的一个元素
# print(40 in alist)          #False
# print(40 not in alist)      #True
# print([10,20] in alist)     #False  #无此情况


#(2)字符串
# a = '12345678'
# print('123' in a)          #True
# print('0123' in a)         #False

# str1 = 'name is tom'
# print('n' in str1)           #True
# print('name' in str1)        #True
# print('e i' in str1)         #True
#字符串：1、前者可以是后者的一个元素  2、前者可以是后者的连续一段



# 五、条件组合
# （1）逻辑条件

# a、且(and)       b、或(or)       c、不(not)

# 逻辑优先级： 有括号，先算括号； 无括号 not>and>or


































