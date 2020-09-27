*** Settings ***
Library  Collections
Library  SeleniumLibrary

*** Variables ***
${url}    http://localhost/mgr/login/login.html
@{database}    127.0.0.1   3306
&{user1}     username=auto    pw=sdfsdfsdf

*** Keywords ***
loginwebsite
    go to        ${url}
    input text    id=username   &{user1}[username]
    input text    id=password   &{user1}[pw]
    click element   css=.btn-success

addCourse
    [Arguments]  ${name}    ${desc}   ${idx}
    #开始添加课程
    click element  css=[ng-click="showAddOne=true"]
    #课程名称
    input text     css=[ng-model="addData.name"]    ${name}
    #详情描述
    input text     css=[ng-model="addData.desc"]    ${desc}
    #展示次序
    input text     css=[ng-model="addData.display_idx"]   ${idx}
    #创建
    click element  css=[ng-click="addOne()"]


checkCourse
    [Arguments]  ${expect}
    ${eles}   get webelements    css=tbody td:nth-child(2)
    ${courses}   evaluate   [ele.text for ele in $eles]
    #判断课程列表中是否包含已添加课程
    should be true  $expect in $courses

deleteAllLesson
    loginwebsite
    #删除所有课程
    set selenium implicit wait  1

    FOR   ${i}   IN RANGE    9999

        ${del_btns}   get webelements   css=[ng-click="delOne(one)"]

        exit for loop if   $del_btns == []

        evaluate   $del_btns[0].click()

        #点击确认
        click element   css=.btn-primary
        #等待弹出框消失
        sleep    1
     END





















websetup
   open browser   http://localhost   chrome
   set selenium implicit wait  10


webteardown
   close browser

getvar1

    [Return]  123