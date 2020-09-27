*** Settings ***
Library     lesson2.pylib.mylib3

*** Test Cases ***
测试用例1
        ${var}    set variable    ${12+12}
        ${list}   create list    1   ${2}    ${3}
        printarg    ${list}
