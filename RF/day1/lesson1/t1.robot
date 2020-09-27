*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
百度搜索松勤
    #接下来打开百度页面
    Open Browser                https://www.baidu.com/   chrome
    input text                  id=kw                    松勤\n
    set selenium implicit wait  1
    ${res}                      get text                 id=1
    should contain              ${res}                   松勤网 - 松勤软件测试
    close browser




