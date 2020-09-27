*** Settings ***
Library  mylib3

*** Test Cases ***

遍历list变量
    ${list}=     returnlist
    :FOR    ${index}    IN   @{list}
    \    Log To Console    ${index}

遍历list变量2
    ${list}=     returnlist
    FOR    ${index}    IN RANGE  9
        Log To Console    ${index}
    END