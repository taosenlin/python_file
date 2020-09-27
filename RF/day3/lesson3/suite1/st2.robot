*** Settings ***

Suite Setup       log to console   \n --- Suite st2 Setup ---
Suite Teardown    log to console   \n --- Suite st2 Teardown ---
#套件的默认初始化与清除遵循就近原则(里面定义了Test就使用自身的,未定义就使用__init__中的)
Test Setup       log to console   \n --- Test st2 Default Setup ---
Test Teardown    log to console   \n --- Test st2 Default Teardown ---


*** Test Cases ***
测试1
    [Setup]    log to console  \n *** case st setup ****
    log to console   测试用例主体部分11
    [Teardown]    log to console   \n *** case st teardown ****


测试2
    log to console   测试用例主体部分22

测试3
    log to console   测试用例主体部分33

