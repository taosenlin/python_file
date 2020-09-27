*** Settings ***
Library  mylib3

*** Test Cases ***
关键字测试
    ${num}  convert to integer  2020         #（传递）转换成整型（数值）
    ${list}   returnlist
    ${dict}   returndict
#    printarg   @{list}[0]
#    printarg  ${list[0]}

#    printarg  &{dict}[ele1]
    printarg  ${dict['ele1']}

    #for循环

#    FOR   ${i}   IN   @{list}
#        log to console  ${i}
#    END
#    LOG TO CONSOLE  循环外面-出循环体

    #for-range
    FOR  ${i}  IN RANGE  10
        log to console  ${i}
    END


