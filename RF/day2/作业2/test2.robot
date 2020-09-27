*** Settings ***
Library   SeleniumLibrary

*** Test Cases ***
用例1
     Open Browser   https://www.vmall.com/index.html     chrome
     Set Selenium Implicit Wait    5
     ${eles}   Get Webelements   xpath=//div[@class="span-968 fl"] //li //div
     :FOR   ${ele}  IN   @{eles}
     \     log to console     ${ele.text}
     \     ${eles}   evaluate   $ele.get_attribute('innerText')
     \     log to console    ${eles}


