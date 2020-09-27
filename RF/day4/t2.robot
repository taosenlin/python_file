*** Settings ***
Resource    t1.robot


*** Test Cases ***
case1
    [Template]      loginandcheck
    [Teardown]      xxxx(收尾动作)
    abc     123      success
    abc     12       fail
    ab      123      fail




*** Keywords ***
getvar1
    ${var}    evaluate    [i for i in range(10)]
    #return返回值
    [Return]     ${var}


loginandcheck
    [Arguments]      ${username}     ${password}     ${expect}
    input username     abc
    input password     123
    checkpage        ${expect}






