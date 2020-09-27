*** Settings ***
Library    SeleniumLibrary
Library    course_mgr
Library    Collections

*** Test Cases ***
用例1
    ${courseList}   listCourse     1   20
    :FOR    ${ele}    IN    @{courseList}
    \      log to console    ${ele}

    ${expected}    Create List    初中化学15841443347941      初中化学15841462425068
    Lists Should Be Equal    ${courseList}    ${expected}