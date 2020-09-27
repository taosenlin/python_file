# coding:utf8
# Time:2020-04-06 10:26
# Author:TSL

# 一、用户关键字
# 1、什么是用户关键字？

# 语法：由RF层面的关键字组成
# 作用：类似于RF层面的函数，用于封装一些步骤



# 2、 定义、使用用户关键字
# （1）首先我们要创建关键字表
# （2）用户关键字的定义和定义一个用例的写法非常类似

# *** Keywords ***      #用户关键字表
# loginwebsite
#     Open Browser    http://localhost/mgr/login/login.html     chrome
#     Set Selenium Implicit Wait   10


# (3)参数的支持
# *** Keywords ***
# loginwebsite
#     [Arguments]    ${username}    ${password}
#     Open Browser    http://localhost/mgr/login/login.html     chrome
#     Set Selenium Implicit Wait    10
#     Input Text    id=username    ${username}
#     Input Text    id=password    ${password}


# (4)返回值
# GetLessonList
#     ${eles}=    Get Webelements    css=tr>td:nth-child(2)
#     ${lessons}    create list
#     :FOR    ${ele}    IN    @{eles}
#     \    log to console    ${ele.text}
#     \    Append To List    ${lessons}    ${ele.text}

#     [Return]    ${lessons}



# 二、资源文件
# 1、在测试套件文件中定义关键字的问题
# (1)只能在本测试套件中有效，无法共享给其他测试套件使用

# 2、使用资源文件
# 3、资源文件其实就是RF层面的库文件（不能包含测试用例）
# (1)里面可以包含用来共享的 变量和关键字
# (2)资源文件的格式基本也和 测试套件文件 类似

# *** Settings ***
# Library    Selenium2Library
# Resource    rc.robot

# (3)搜索规则
# 当前用例文件所在目录
# 如果找不到，就在Python的模块搜索路径中搜索



# 三、数据驱动（参数化）
# 1、什么是数据驱动？
# 用例逻辑相同，每次输入的数据不同，并且数据量很大的时候

# 2、RF如何实现数据驱动？
# (1)使用 [template] 用户关键字
# (2)自发实现









































