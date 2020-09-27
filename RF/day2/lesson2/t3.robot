*** Test Cases ***
测试1
    ${var1}  set variable  he
    ${var2}  convert to integer  2020

    #关键字执行失败就不会运行后续的步骤
    should contain  hello  h
#    should be true  'h' in 'hello'

    #若Python表达式需要使用RF中的变量去掉{}即可,$变量名
    should be true  $var1 in 'hello'
    should be true  'hello'.startswith('he')
    # $var  这样表示参数的用法仅限于RF参数是python表达式
#    log to console  $var1

    #比较两个对象是否相等
#    should be equal  ${var1}   ${var2}


