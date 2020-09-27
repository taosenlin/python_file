#*** Settings ***
#Variables  cfg/cfg.py


*** Test Cases ***
case1
#    log to console  ${username}
#    log to console  ${password}
#    log to console  @{database}[1]
    log to console  ${user1['name']}
    log to console  &{user1}[pwd]