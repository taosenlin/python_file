*** Settings ***
Library    lesson2.pylib.mylib3

*** Test Cases ***
测试
    ${res}=   create list   a  b  c
    ${list2}=   Returnlist
    ${dict2}=   Returndict
    #printarg    ${list2[0]}         # $对应传参类型  $[1,2,3,4]
    #printarg    @{list2}[0]         # @对应的传参类型 1 2 3 4

    printarg    ${dict2['ele1']}            # $对应的传参类型 {'ele1' : 'male','ele2' : 'female'}
    #printarg    &{dict2}[ele1]             # &对应的传参类型 'ele1' : 'male'   'ele2' : 'female'











































































