*** Test Cases ***
关键字测试1
        should be equal    hello    hello    #msg=值不一样
        #如果检查点不通过，下面语句不会执行
        log to console    测试通过
        #将想要输出的信息打印到控制台
        log         测试通过
        #将想要输出的信息输出到日志中


关键字测试2
        #${num}    convert to integer     2020
        #将字符串类型的2020 转换成整型
        ${num}    convert to number     2020.1
        #将字符串类型的2020.1 转换成浮点数
        ${var1}     set variable      he
        #设置普通变量(变量的值为字符串类型)
        #should be equal      hello       ${num}
        #将前后俩个参数作比较（相等则pass）
        #should be equal as integers     ${var1}     ${num}
        #将前后俩个参数作为整型相比较
        should not be equal as strings      ${var1}     ${num}
        #将前后俩个参数作为字符串相比较
        #should not be equal           ${var1}      ${num}
        #将前后俩个参数作比较（不相等则pass）
        #should contain     helloworld    world
        #前面语句包含后面内容


        should be true      $var1 in 'hello'
        #should be true后面可以直接写python表达式
        #${var1} in 'hello' 表示 he in 'hello'  执行结果为'he in 'hello'',此时he为变量
        #$var1 in 'hello   表示 'he' in 'hello' 执行结果为true
        #$var1 这种用法只能用于python表达式中


        #如果检查点不通过，下面语句不会执行
        log to console    ${var1}    #测试通过

        log         测试通过
