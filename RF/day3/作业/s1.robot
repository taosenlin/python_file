*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    delete_course

*** Test Cases ***
测试1
    [Setup]     DeleteAllCourse
    [Teardown]    DeleteAllCourse
    Open Browser    http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait    10

    Input Text    id=username    auto
    Input Text    id=password    sdfsdfsdf
    Click Element     tag=button


    Click Element    css=button[ng-click="showAddOne=true"]
    input text   css=input[ng-model='addData.name']     计算机
    input text   css=textarea[ng-model="addData.desc"]      计算机1
    input text   css=input[ng-model="addData.display_idx"]      1
    Click Element    css=button[ng-click="addOne()"]

    sleep   1

    ${eles}       Get Webelements           css=tbody>tr>td:nth-child(2)>span
    ${lessons}     create list
    FOR     ${ele}    IN   @{eles}
#          log to console     ${ele.text}
        Append To List    ${lessons}    ${ele.text}
    ${expected}      create list       计算机
    Lists Should Be Equal       ${lessons}         ${expected}
    END

    Close Browser














































































