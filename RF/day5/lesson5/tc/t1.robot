#*** Settings ***
#Resource   rc.robot

#引用变量表 Variables
#Variables  cfg/cfg.py


*** Test Cases ***
case1
    log to console  ${MgrLoginUrl}
    log to console  ${StudentLoginUrl}
    log to console  ${database}
    log to console  ${database[0]}
    log to console  @{database}[0]
    log to console  ${user1}
    log to console  &{user1}[name]
    log to console  ${user1['name']}

