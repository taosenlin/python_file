# coding:utf8
# Time:2020-04-02 21:10
# Author:TSL

# 一、变量表中声明变量

# 首先我们要创建 Variables表
# 公共变量表
# *** Variables ***

# 1、Scalar (普通)变量
# ${MgrLoginUrl}     http://localhost/mgr/login/login.html
# ${StudentLoginUrl}   http://localhost/student/login/login.html


# 2、List 变量
#  @{database}     127.0.0.1     3306


# 3、Dict 变量
# &{user1}       name=auto      pw=sdfsdfsdf


# 注：也可以通过命令行中指定配置文件相对路径执行
# robot --variablefile(-V) cfg/cfg.py t1.robot

# robot -help 可以查询相关简写命令



# 二、使用变量文件
# 1、也可以使用Python模块文件提供公共变量给RF使用。只需要直接定义变量就可以，
#    语法完全就是python

# MgrLoginUrl='http://localhost/mgr/login/login.html'
# StudentLoginUrl='http://localhost/student/login/login.html'

# 2、RF声明使用变量文件
# *** Settings ***
# Variables   cfg.py

# 3、变量文件声明的时候，可以使用绝对路径，也可以使用相对路径
# 4、使用相对路径的时候，RF搜索规则和资源文件搜素规则一样
# (1)先在相对当前文件的目录，匹配搜索
# (2)在python的模块搜索路径中搜索，可以用 -pythonpath(-P)参数

# 5、命令行参数指定变量文件
# robot --variablefile cfg\cfg.py tc\t1.robot



# 三、Python扩展关键字
# 1、Python模块作为测试库
# (1)模块文件名作为测试库名字
# (2)比如Python模块叫MyLibrary，对应的Python文件是MyLibrary.py。
#    那么测试库名字就是MyLibrary
# (3)定义在Python模块文件中的函数，名称前有_前缀的不会作为关键字

"""
def returnlist():
    return [1,2]

def _returnlist2():
    return [1,2]
"""
# (4)要保证其在Python模块的搜索路径中，这样RF才能找到它
# 直接设置环境变量
# 用 --pythonpath 参数

# (5)RF使用关键字的时候
# 中间可以加上任意的空格
# 大小写也可以任意
# returnlist
# return list
# Returnl ist


# 2、Python类作为测试库
# (1)比如Python文件是 tlib2.py
'''
class SubLibrary:
    def returnint(self):
        return 3
    
    def _returnint2(self):
        return 4
'''

# (2)声明
# *** Settings ***
# Library   tlib2.SubLibrary

# (3)该类中的成员方法，名称前有 _ 前缀的不会作为关键字

# (4)导入时的参数，对应类的初始化方法

# (5)如果类和模块文件同名，声明的时候就可以省略后面的类名



# 四、Python扩展库的搜索规则
# 1、完全是按照python的模块的搜索规则来的

# (1)如果在包内  pylib/login/rightpass.py
# *** Settings ***
# Library   pylib.login.rightpass
# -------------------------------------
# Library    pylib/login/rightpass.py

# (2)在 settings 中声明 资源文件和变量文件：
# 路径，目录之间的分割符，不用 点 .  而是用 斜杠 /

# (3)在 settings 中声明 测试库：
# 路径，目录之间的分割符，可以用 点 .  也可以用 斜杠 /
# 路径分割符 用点后面不加 py, 用斜杠后面加 .py


# 2、Python库引入了其他模块
# 确保导入的模块路径和RF导入的模块起始路径统一

# 3、Python库中的class存在继承：
# 确保导入的模块路径和RF导入的模块起始路径统一
# 使用的时候RF文件只需导入子类即可












