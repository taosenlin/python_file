*** Settings ***
Library   pylib.WebOpAdmin


*** Test Cases ***
创建培训班期1
    [Setup]    run keywords    deleteAll    trainGrade
    ...    AND     deleteAll     train
    ...    AND     deleteAll     teacher
    ...    AND     deleteAll     course
    ...    AND    addCourse    初中语文    初中语文    2
    ...    AND    addCourse    初中数学    初中数学    1
    ...    AND    addTrain     技能培训    初中班   1    初中语文     初中数学

    [Teardown]      run keywords     deleteAll    trainGrade
    ...    AND    deleteAll    train
    ...    AND    deleteAll    teacher
    ...    AND    deleteAll    course


    trainGrade    初中班1期    初中   1    初中班
    ${trainGrade}    getTrainGradeList
    should be true    '初中班1期' in $trainGrade












































































