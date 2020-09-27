*** Test Cases ***
#RF中只有FOR循环没有while循环



#老语法
    ${list}    create list   a  b   c  d

    :FOR  ${one}  IN   @{list}
    \   log to console  ${one}
    \   log to console  -----
    log to console   循环外面




#新语法
    ${list}    create list   a  b   c  d
    #注意列表要以list形式传递
    FOR  ${one}  IN  @{list}
    log to console  ${one}
    log to console  ----
    END

    log to console  循环结束


RANG控制循环
    #注意 IN RANGE 之间只有一个空格！！！
    FOR  ${one}  IN RANGE   10
        log to console  ${one}
    END

    log to console  循环结束




#新语法a
#    ${list}  create list   猫    狗   猪  aaa   bbb   ccc
#    FOR    ${animal}  IN RANGE  10
#        Log To Console    ${animal}
#        Log To Console    testloop
#    END  #循环体结束标志
#    Log To Console   循环外面
