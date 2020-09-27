*** Settings ***
Library  course_mgr
Library  SeleniumLibrary

*** Test Cases ***
用例1
    ${courses}  listcourse
    FOR   ${cour}  IN  @{courses}
        log to console  ${cour}
        log   ${cour}
    END
    #当参数是python表达式的时候，引用到RF中的变量 可以采用$var此形式
    #其他情况非python表达式，选择RF普通的传参形式${scalar}  @{list}  &{dict}
    should be true  $courses==['selenium','RF']

用例2
    Open Browser  https://www.vmall.com/   chrome
    ${eles}   get webelements  css=.home-recommend-goods.home-hot-goods .grid-list.clearfix .grid-title
    FOR  ${ele}  IN  @{eles}
        log to console  ${ele.text}
        log  ${ele.text}
    END
    close Browser