
*** Settings ***


*** Test Cases ***
case1
#    ${datas}   readExcelData   xxxx.xls
    ${data}   create list  1    2   3   4
    FOR   ${d}  IN  @{data}
        log to console  ${d}
        should be true  int($d)%2 != 0
    END



*** Keywords ***

loginandcheck
    [Arguments]  ${a}
    log to console  ${a}