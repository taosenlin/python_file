#思路1：SeleniumLibrary
#思路2：python+selenium

*** Settings ***
Resource  rc.robot

*** Test Cases ***
case2
    [Setup]   deleteAllLesson
    [Teardown]  deleteAllLesson
    [Template]  addCourseandcheck
    robot    自动化框架课程    1
    selenium   webUI        2
    jmeter     性能测试       3


*** Keywords ***
addCourseandcheck
    [Arguments]  ${name}    ${desc}   ${idx}
    loginwebsite
    addCourse   ${name}      ${desc}    ${idx}
    #检查课程是否被添加
    checkCourse   ${name}
    close browser