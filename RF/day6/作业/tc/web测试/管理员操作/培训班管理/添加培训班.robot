*** Settings ***
Library   pylib.WebOpAdmin

*** Test Cases ***
添加培训班1
    [Setup]    run keywords    deleteAll    train
    ...    AND    deleteAll    course
    ...    AND    addCourse    初中语文    初中语文    2
    ...    AND    addCourse    初中数学    初中数学    1

    [Teardown]     Run Keywords     deleteAll    train
    ...    AND    deleteAll    teacher
    ...    AND    deleteAll    course


    addTrain     技能培训    初中班    1    初中语文     初中数学
    ${trains}     getTrainList
    should be true     '技能培训' in $trains

