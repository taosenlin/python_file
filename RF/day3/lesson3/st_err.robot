*** Settings ***
Library    mylib4                 #使用opencalc需要先声明导入mylib4,否则报错

Suite Setup       opencalc
#Suite Setup       log to console   \n --- Suite st Setup ---
Suite Teardown    log to console   \n --- Suite st Teardown ---
Test Setup       log to console   \n --- Test st Default Setup ---
Test Teardown    log to console   \n --- Test st Default Teardown ---


*** Test Cases ***
测试1
    [Setup]    log to console  \n *** case st setup ****
    log to console   测试用例主体部分11
    [Teardown]    log to console   \n *** case st teardown ****


测试2
    log to console   测试用例主体部分22

测试3
    log to console   测试用例主体部分33