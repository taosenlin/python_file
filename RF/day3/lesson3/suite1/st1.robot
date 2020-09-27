*** Settings ***
Library   mylib4
Suite Setup       log to console   \n --- Suite st1 Setup ---
Suite Teardown    log to console   \n --- Suite st1 Teardown ---


*** Test Cases ***
测试1
    [Setup]    log to console  \n *** case st setup ****
    [Tags]  smokingtest
    log to console   测试用例主体部分11
    [Teardown]    log to console   \n *** case st teardown ****


测试2
    log to console   测试用例主体部分22

测试3
    log to console   测试用例主体部分33

