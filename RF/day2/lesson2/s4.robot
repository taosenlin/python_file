*** Settings ***
Library  mylib3

*** Test Cases ***
测试
    ${res}=   create list  a   b   c
    ${list2}=  Returnlist
    ${dict2}=   Returndict
#    printarg   ${list2[0]}   #@对应的传参类型1  2  3  4   $[1, 2, 3, 4]
#    printarg   @{list2}[0]
    printarg   ${dict2['ele1']}

#    ${expct}=   set variable   松勤软件测试
#    should be true   $expct=='松勤软件测试'
#    printarg  ${expct}










