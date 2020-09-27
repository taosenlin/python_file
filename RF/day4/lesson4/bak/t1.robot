*** Settings ***
Resource   rc.robot
Library  SeleniumLibrary
Library  pylib

*** Test Cases ***
case1
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    loginwebsite
    addCourse  robotframework   RF课程  1
    checkCourse  robotframework
    close browser


case2
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    loginwebsite
    addCourse  pytest   pytest课程    2
    checkCourse   pytest
    close browser


