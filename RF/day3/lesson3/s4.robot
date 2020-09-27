*** Settings ***
Library  mylib4
Library  Dialogs
#Dialogs库中的关键字 get value from user

*** Test Cases ***
测试1

    FOR  ${i}   IN RANGE   99
        #获取用户输入
        ${score}   get value from user  请输入成绩
        continue for loop if  $score == 'cont'
        Exit For Loop if  $score == 'over'
        run keyword if  int($score) >= 60   log to console  及格了
        ...    ELSE   log to console  不及格

    END








