*** Settings ***
#套件级别的初始化与清除用于处理套件中所有用例通用的数据环境
Suite Setup       log to console   \n --- Suite st2 Setup ---
Suite Teardown    log to console   \n --- Suite st2 Teardown ---


*** Test Cases ***
测试1
    [Setup]    log to console  \n *** case st setup ****
    log to console   测试用例主体部分11
    [Teardown]    log to console   \n *** case st teardown ****


测试2
    log to console   测试用例主体部分22


测试3
    log to console   测试用例主体部分33

