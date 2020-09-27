*** Settings ***
Library    mylib3

*** Test Cases ***
测试
    ${var1}=     returnlist
    printarg   ${var1}
