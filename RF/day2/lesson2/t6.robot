*** Test Cases ***
整数比较
    ${num}=  convert to integer  20
    should be true    ${num}>19


字符串比较
    ${str1}=  set variable  hello
    should be true   ${str1}=='hello'            # hello='hello'
    should be true   $str1=='hello'              # 'hello'='hello'
#    should be true   '${str1}'=='hello'

# ${str1} 计算变量的值
# $str1   传递变量本身
