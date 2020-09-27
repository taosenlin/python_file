*** Settings ***
#模块导入法-和python规则相同
#Library  tlib1_1
#路径导入法-导入的文件绝对或者相对路径
#Library  tlib1_1.py

Library  ../pylib/tlib.py

*** Test Cases ***
case1
    ${var1}   return_list
    log to console  ${var1}