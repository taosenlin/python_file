*** Settings ***
Library    mylib3

*** Test Cases ***

测试
    ${var1}=     returndict
    printarg     ${var1}
    printarg     &{var1}
