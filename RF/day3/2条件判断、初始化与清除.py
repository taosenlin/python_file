# coding:utf8
# Time:2020-03-29 10:12
# Author:TSL

# 一、collection标准库
# 1、collection标准库

# 针对List 和 Diction处理
# 创建并添加元素
# 数字变量   ${1}    ${2}



# 二、Evaluate(python条件表达式)

# 1、直接用python代码表达式来生成一个结果

# ${var}=     set variable       ${890}
# 可以写成
# ${var}=     evaluate      890

# 复杂的表达式
# ${var}=     evaluate     ['hello']*10



# 三、初始化和清除

# setup 是测试一个用例(或者套件)前要做的事情
# teardown 是测试后要做的事情
# 在RF中,每个测试套件目录、测试套件文件、测试用例都可以有自己的setup 和 teardown
# 所有的setup 和 teardown 操作都只能由一个关键字语句构成

# 1、测试用例的setup、teardown
# 写在测试用例表的配置项中

# *** Test Cases ***

# 测试1
#    用例执行之前的操作
#    [Setup]    log to console    \n *** case st setup ***
#    log to console     测试用例主体部分
#    用例执行之后的操作
#    [Teardown]    log to console    \n *** case st teardown ***



# 2、测试套件文件的setup、teardown
# 写在测试套件文件的settings表中

# 两种类型

# Suite setup/teardown
# 进入和退出这个suite执行用例前后必须执行且只分别执行一次

# Test setup/teardown
# 如果suite内的用例本身没有 setup/teardown 才执行


# *** Settings ***
# Suite Setup        log to console     \n --- Suite Setup ---
# Suite Teardown     log to console     \n --- Suite Teardown ---
# Test Setup        log to console     \n --- Test Default Setup ---
# Test Teardown     log to console     \n --- Test Default Teardown ---



# 3、测试套件目录的setup、teardown
# 在其目录下的初始化文件 __init__.txt 或者 __init__.robot 里的settings表中

# 两种类型

# Suite setup/teardown
# 进入和退出这个suite执行用例前后必须执行且分别执行一次

# Test setup/teardown
# 如果suite内的 用例、或者子套件 本身没有setup/teardown 才执行

# *** Settings ***
# Suite Setup      log to console    \n --- Suite Setup ---
# Suite Teardown   log to console    \n --- Suite Teardown ---
# Test Setup      log to console    \n --- Test Default Setup ---
# Test Teardown   log to console    \n --- Test Default Teardown ---















































