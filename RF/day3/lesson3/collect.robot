*** Settings ***
Library           Collections
#Collections库中包含生成列表以及字典的关键字

*** Test Cases ***
测试
    ${list}   create list
    append to list   ${list}   hello
    append to list   ${list}   world   ${2020}
    log to console   ${list}

测试2
    ${dict}   create dictionary
     set to dictionary  ${dict}   a=${1}  b=${2}  c=${3}
     log to console  ${dict}