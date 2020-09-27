#*** Settings ***
#Library    SeleniumLibrary
#Library    Collections
#Library    delete_course1
#Resource    rc.robot

#套件文件
*** Settings ***
Resource     rc.robot
Suite Setup   websetup
Suite Teardown   webteardown


*** Test Cases ***
测试1
    [Setup]     DeleteAllCourse
    [Teardown]    DeleteAllCourse

    loginwebsite
    addCourse     robot    自动化框架课程     1
    checkCourse     robot
#    Close Browser


测试2
    [Setup]     DeleteAllCourse
    [Teardown]    DeleteAllCourse

    loginwebsite
    addCourse     webUI     UI自动化测试     1
    checkCourse     webUI
#    Close Browser



##用户关键字
#*** Keywords ***
#loginwebsite
#    Open Browser    http://localhost/mgr/login/login.html    chrome
#    Set Selenium Implicit Wait    10
#    Input Text    id=username    auto
#    Input Text    id=password    sdfsdfsdf
#    Click Element     tag=button
#
#
#addCourse
#    [Arguments]     ${name}      ${desc}      ${idx}
#    Click Element    css=button[ng-click="showAddOne=true"]
#    input text   css=input[ng-model='addData.name']     ${name}
#    input text   css=textarea[ng-model="addData.desc"]      ${desc}
#    input text   css=input[ng-model="addData.display_idx"]      ${idx}
#    Click Element    css=button[ng-click="addOne()"]
#    sleep   1
#
#
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






























































































































