*** Settings ***
Library  Collections

*** Test Cases ***
测试1
    ${list}   create list   1  2  3
    append to list  ${list}   d  e  f
    log to console  ${list}

    ${d}    create dictionary   a=1   b=2   c=3
     set to dictionary   ${d}    e=4   f=5
#     log to console  ${d}

     ${l2}   evaluate    [i for i in range(100)]

     log to console  ${l2}