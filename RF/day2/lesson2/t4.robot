*** Test Cases ***
验证
    ${num}=  convert to integer   32
    log to console   ${num}

    ${num2}=  convert to Number   32.1
    log to console   ${num2}
