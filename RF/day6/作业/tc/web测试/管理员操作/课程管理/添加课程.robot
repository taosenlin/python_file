*** Settings ***
Library   pylib.WebOpAdmin

*** Test Cases ***

添加课程1
    [Setup]    deleteAll     course
    [Teardown]     deleteAll    course

    addCourse     初中语文    初中语文    2
    ${lessons}     getCourseList
    should be true    '初中语文' in $lessons


    addCourse     初中数学    初中数学    1
    ${lessons}     getCourseList
    should be true    '初中数学' in $lessons

