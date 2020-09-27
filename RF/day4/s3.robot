#套件文件
*** Settings ***
Resource    rc.robot


*** Test Cases ***

测试2
    [Setup]     DeleteAllCourse
    [Teardown]    DeleteAllCourse
    #数据驱动
    [Template]     addCourseandcheck
    robot     自动化框架课程       1
    selenium     webUI            1
    jmeter       性能测试         1



*** Keywords ***
addCourseandcheck
    [Arguments]      ${name}      ${desc}      ${idx}
    loginwebsite
    addCourse      ${name}    ${desc}     ${idx}
    checkCourse     ${name}
    Close Browser















































































