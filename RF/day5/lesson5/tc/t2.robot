*** Settings ***
Resource  rc.robot
#Variables  cfg.py

#1 通过指定变量文件的相对路径
#2 通过设定pythonpath  文件所在目录
#3 在命令行里面设置环境变量pythonpath

*** Test Cases ***
case1
    log to console  ${MgrLoginUrl}
#    log to console  ${var1}
    log to console  ${StudentLoginUrl}
