*** Settings ***
Library  mylib4

*** Test Cases ***
测试1
    #获取接口返回
    ${text}   getwebinfo
    #打印变量
    log to console  ${text}   #$text这种写法只能用于python表达式类型的参数中
    #如果2020再返回的字符串中，就打印测试通过
    run keyword if  '2020' in $text and 'UTF' in $text
    #换行...之后至少空两格
    ...          log to console  测试通过
    ...          ELSE IF   'Wed123' in $text   log to console   今天是周三

    #ELSE不可以小写
    ...           ELSE    log to console  测试不通过


