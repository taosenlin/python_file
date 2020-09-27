*** Settings ***
Resource     rc.robot


*** Test Cases ***

用例1
    [Setup]       deleteAllCourse
    [Teardown]     deleteAllCourse
    [Template]      addCourseandcheck
    robot    自动化框架课程     2


用例2
    [Setup]       deleteAllCourse
    [Teardown]     deleteAllCourse
    [Template]      addCourseandcheck
    selenium     webUI     1


*** Keywords ***
addCourseandcheck
    [Arguments]    ${name}    ${desc}    ${idx}
    loginwebsite
    addCourse     ${name}    ${desc}    ${idx}
    checkCourse    ${name}
    close browser
