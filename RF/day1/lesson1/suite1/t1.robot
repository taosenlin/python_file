*** Settings ***
Library  SeleniumLibrary
Force Tags  somketest


*** Test Cases ***
case001
    [Documentation]  冒烟测试xxxx干嘛的
    [Tags]  tes1

    [Timeout]  60
    log to console                  李建航
    testsq

case002
    log to console  RF

*** Variables ***
${url}   xxxxx


*** Keywords ***
testsq
    Open Browser    http://www.baidu.com    chrome
#    set selenium implicit wait  10
    Input Text    id=kw    松勤\n
    ${firstRet}=    Get Text    id=1
    Should Contain    ${firstRet}    松勤网
    should be true   '松勤网' in $firstRet