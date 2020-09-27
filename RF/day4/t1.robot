*** Test Cases ***
case1
    log to console    1
    should be true    1==1
    ${list}    getvar1
    log to console     ${list}



#用户关键字
*** Keywords ***
getvar1
    ${var}    evaluate    [i for i in range(10)]
    #return返回值
    [Return]     ${var}