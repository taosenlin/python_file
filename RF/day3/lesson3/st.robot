#自动化测试用例的原则
#1.用例不可以有耦合现象，用例之间不可以相互依赖，执行任意一条用例都要确保可以正常运行
#2.不要尝试控制测试用例流程


*** Test Cases ***
测试1
    #用例执行之前做的操作
    [Setup]    log to console  \n *** 测试用例1 setup ****
    #用例执行之后做的操作
    [Teardown]    log to console   \n *** 测试用例 1 teardown ****
    log to console   测试用例1主体部分
    should be true   10<9
    log to console  xxxx


测试2
    log to console   测试用例2主体部分


测试3
    log to console   测试用例3主体部分
