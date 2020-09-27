*** Test Cases ***
test1
    Should Be Equal As Integers  10  010  #转换成数字对象比较，结果是true   #默认将俩个参数转换成数字对象去比较
    Should Be Equal   10    010           #字符串对象比较，结果是False     #默认将俩个参数作为字符串去比较
