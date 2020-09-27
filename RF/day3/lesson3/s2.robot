*** Settings ***
Library  mylib4

*** Test Cases ***
测试1
    ${res}   getWebInfo
    #判断Res是否包含对应的字符，如果有就打印
    run keyword if    '2021' in $res    #log to console    测试成功
    ...    log to console    测试成功
    ...    ELSE IF    'UTC' in $res      log to console   ${res}
    ...    ELSE     log to console      测试不成功








