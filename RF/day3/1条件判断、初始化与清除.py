# coding:utf8
# Time:2020-03-28 20:19
# Author:TSL

# 一、条件判断

# 1、RF中用Run Keyword If 关键字做条件判断(python条件表达式)

# 条件表达式参数给python的eval函数
# run keyword if    '2019' in $html    log to console    内容

# 2、参数放在下一行
# run keyword if    '2019' in $html and 'UTC' in $html
#  ...              log to console    \n2019年的,UTC时间



# 二、ELSE 分支

# 1、ELSE
# run keyword if      '2019' in $html and 'UTC' in $html
# ...                log to console     \n2019年的,UTC时间
#    ...    ELSE         log to console      \n不是2019年的时间


# 2、ELSE IF 参数
# run keyword if      '2019' in $html and 'UTC' in $html
# ...                log to console     \n2019年的,UTC时间
#      ...   ELSE IF     '2019' in $html    log to console     \n2019年的
#     ...   ELSE IF     'UTC' in $html     log to console     \nUTC时间
#      ...  ELSE                            log to console    \n以上都不是



# 三、循环里面的判断

# 1、 Exit For Loop 与 Continue For Loop

# FOR    ${one}   in range    99999
#         ${weight}=    get value from user       请输入你的体重    60
#         当用户输入cont,终止本次循环,重新开始测试
#         run keyword if     $weight=='cont'      Continue For Loop
#         当用户输入over,就退出循环
#         run keyword if     $weight=='over'      Exit For Loop
#         run keyword if     int($weight)>60      Log to console      太重了
# END


# 2、Exit For Loop If 与 Continue For Loop If

# :for    ${one}     in range    99999
#     \    ${weight}=      get value from user     请输入你的体重    60
#     \    Continue For Loop If     $weight=='cont'
#     \    Exit For Loop If         $weight=='over'
#     \    run keyword if      int($weight)>60    log to console    太重了




















































