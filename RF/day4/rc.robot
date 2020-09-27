#资源文件(不能包含测试用例表)

*** Settings ***
Library    SeleniumLibrary
Library    Collections
#Library    delete_course1

*** Variables ***
${url}    http://localhost/mgr/login/login.html
&{user1}     username=auto     pw=sdfsdfsdf


#用户关键字
*** Keywords ***
loginwebsite
    go to      ${url}
#    Open Browser    http://localhost/mgr/login/login.html    chrome
#    Set Selenium Implicit Wait    10
    Input Text    id=username     &{user1}[username]
    Input Text    id=password     &{user1}[pw]
    Click Element     tag=button


addCourse
    [Arguments]     ${name}      ${desc}      ${idx}
    Click Element    css=button[ng-click="showAddOne=true"]
    input text   css=input[ng-model='addData.name']     ${name}
    input text   css=textarea[ng-model="addData.desc"]      ${desc}
    input text   css=input[ng-model="addData.display_idx"]      ${idx}

    Click Element    css=button[ng-click="addOne()"]
    sleep   1



checkCourse
    [Arguments]   ${expect}
    ${eles}   get webelements    css=tbody td:nth-child(2)
    ${courses}   evaluate   [ele.text for ele in $eles]
    #判断课程列表中是否包含已添加课程
    should be true  $expect in $courses



#checkCourse
#    [Arguments]     ${expect}
#    ${eles}       Get Webelements           css=tbody>tr>td:nth-child(2)>span
#    ${lessons}     create list
#    FOR     ${ele}    IN   @{eles}
##          log to console     ${ele.text}
#        Append To List    ${lessons}    ${ele.text}
#    ${expected}      create list      ${expect}
#    Lists Should Be Equal       ${lessons}         ${expected}
#    END

deleteAllCourse
    loginwebsite
    #删除所有课程
    set selenium implicit wait  1

    FOR   ${i}  IN RANGE   9999

        ${del_btns}   get webelements   css=[ng-click="delOne(one)"]

        exit for loop if   $del_btns == []

        evaluate   $del_btns[0].click()

        #点击确认
        click element   css=.btn-primary
        #等待弹出框消失
        sleep    1
     END

#    close browser

websetup
    open browser     http://localhost    chrome
    set selenium implicit wait    10

webteardown
    close browser
