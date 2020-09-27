*** Settings ***
Library    pylib.login.tlib1


*** Test Cases ***
case1
    ${user}    get user
    log to console  ${user}
