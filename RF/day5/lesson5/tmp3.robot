*** Settings ***
Library    tlib2.SubLibrary
#用模块导入法最多只能引用到模块级别的函数，和模块同名类里面的方法
Library    pylib/login/tlib1.py
#Library    tlib2.SubLibrary2   localhost  3306
#Library    tlib2.py    localhost  3306

*** Test Cases ***
case1
    ${var}   returnint
    log to console  ${var}


#case2
#    Printaddr


case3
    printaddr