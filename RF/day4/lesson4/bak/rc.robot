

#资源文件的定义和套件文件一样，唯一的区别是资源文件里面不含用例表
*** Keywords ***
loginwebsite
     #chromedriver的路径配置到了环境变量中
    open browser  http://localhost/mgr/login/login.html   chrome
    set selenium implicit wait  10
    #输入用户名和密码
    input text  id:username   auto
    input text  id:password   sdfsdfsdf
    #点击登录按钮
    click element  css:.btn-success

addCourse
    [Arguments]  ${name}   ${desc}   ${idx}
    #开始添加课程，点击添加课程按钮
    click element  css:[ng-click="showAddOne=true"]
    #输入课程名称
    input text  css:[ng-model="addData.name"]   ${name}
    #输入详情描述
    input text  css:[ng-model="addData.desc"]   ${desc}
    #输入展示次序
    input text  css:[ng-model="addData.display_idx"]   ${idx}
    #点击创建
    click element  css:[ng-click="addOne()"]

checkCourse
    [Arguments]   ${expect}
    #校验课程
    ${courses}   get webelements  css:tbody td:nth-child(2)
    #用列表生成式
    ${lessons}   evaluate   [ele.text for ele in $courses]
    should be true   $expect in $lessons


