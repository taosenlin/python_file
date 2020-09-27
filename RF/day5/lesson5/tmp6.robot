*** Settings ***

Library  pylib.login.other.Child


*** Test Cases ***
case01
    ${var}   money

    log to console  ${var}
