*** Settings ***
Library  st
Library  Collections
Library  SeleniumLibrary


*** Keywords ***
loginwebsite
    open browser  http://localhost/mgr/login/login.html   chrome
    set selenium implicit wait  10
    input text    id=username   auto
    input text    id=password   sdfsdfsdf
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