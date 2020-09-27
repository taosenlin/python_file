*** Test Cases ***
测试
    #定义一个变量-scalar类型
    ${var}  set variable   hello
    #定义一个List类型的变量
    @{list}  create list  hello  world
    log to console  ${var}
#    log to console  @{list}
    log to console  ${list}

    #定义一个dict类型的变量
    ${dict}  create dictionary  key1=hello   key2=world
    log to console  ${dict}
