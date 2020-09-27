*** Settings ***
Library  mylib3

*** Test Cases ***
测试ABC
    ${var}   set variable  ${12+12}
    ${list}    create list  1   ${2}   ${3}
    printarg   ${list}




















