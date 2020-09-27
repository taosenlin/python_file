*** Settings ***
Library   SeleniumLibrary   implicit_wait=10

*** Test Cases ***
百度搜索

    Open Browser    http://www.baidu.com    chrome
#    set selenium implicit wait  10
    Input Text    id=kw    松勤\n
    ${firstRet}=    Get Text    id=1
    Should Contain    ${firstRet}    松勤网
    should be true   '松勤网' in $firstRet
