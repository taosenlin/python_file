*** Settings ***
Library  mylib3

*** Test Cases ***
测试1
    #传递整数类型参数给关键字
    ${var}   convert to integer  2020
    printarg  ${var}
    #传递整数类型参数给关键字-方式2
    #RF会计算{}里的表达式
    printarg  ${10*10}

测试2
    ${list}   returnlist
    #scalar类型传参，传递是一个整体
    printarg  ${list}
    #list类型传参,传递列表中的所有元素，作为多个参数进行传递
    printarg  @{list}
    #取列表中的元素
    printarg  ${list[0]}     #方式1

    printarg  @{list}[0]     #方式2
    printarg  ${list}[0]     #方式3

测试3
    ${dict}   returndict
    #scalar类型传参，传递是一个整体
    printarg  ${dict}
    #dict类型传参，类似于List,将字典内的键值对作为多个参数进行传递
    printarg  &{dict}

    #取某个key对应的value
    printarg  ${dict['ele1']}    #方式1

    printarg  &{dict}[ele1]    #方式2
    printarg  ${dict}[ele1]     #方式3






