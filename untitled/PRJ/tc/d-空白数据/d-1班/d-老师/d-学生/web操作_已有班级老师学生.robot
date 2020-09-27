*** Settings ***
Library     pylib.WebOpLib
Variables   cfg.py

Suite Setup         setupBrowser
Suite Teardown      tearDownBrowser


*** Test Cases ***

老师发布作业1 - tc005101

    teacherLoginPage    xiaotao    888888
    teacher assign work     exam_math66

    studentLoginPage    xiaoyu     888888
    student finish work

    teacherLoginPage     xiaotao     888888
    ${teacher_check}=         teacher check work
    should be true      $teacher_check==['A', 'A', 'A']














