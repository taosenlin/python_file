*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
用例1
    #用例主体部分另起一行,并且至少缩进两个空格
    #关键字和参数至少空两格,如果传多个参数,参数与参数之间也是至少两个空格
    log to console      hello robot

用例2
    [Documentation]      百度搜索松勤
    Open Browser    https://www.baidu.com/    chrome
    #打开网址使用（chrome）浏览器
    set selenium implicit wait           10
    #设置selenium隐式等待时间
    input text        id=kw            松勤\n
    ${res}         get text           id = 1
    should contain          ${res}       松勤网 - 松勤软件测试
    #应该包含（前者包含后者则为真）
    close Browser





























































