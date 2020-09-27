*** Settings ***
#Library  mylib4

*** Test Cases ***
测试1
#    ${res}   getWebInfo
    ${var}   evaluate  print('hello')
    #evaluate作用为执行(后面)传递的python表达式
    log to console   ${var}


测试2
    ${var}    evaluate     [i for i in range(10) if i%2==0]  #python条件表达式(只能一行)
    #evaluate后面表达式有返回值,下面log to console才会接收并打印
    #如果没有返回值(None),则直接输出None
    log to console    ${var}























































































