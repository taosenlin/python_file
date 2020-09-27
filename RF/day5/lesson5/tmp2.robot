*** Settings ***
#导入的格式模块名.类名
#Library  tlib2.SubLibrary

Library  tlib2.SubLibrary2   192.168.1.1   8080

#如果class和模块同名，导入的时候可以不用写模块名
Library  tlib2.tlib2    localhost   9090



*** Test Cases ***
case1
    ${var}  Printaddr
    log to console  ${var}

