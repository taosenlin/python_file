# Time:2020-03-01 9:45
# Author:TSL

# UIautomatorAPI定位元素

# 前面的方法，底层都是通过 UIAutomator API
# id
# class name
# accessibility id
# xpath

# UI Automator 测试框架提供了一组 API 来构建 UI 测试
# 利用 UI Automator API, 控制测试设备
# UI Automator 测试框架非常适合编写黑盒自动化测试
# API 就是库的编程接口 application programming interface
# UiSelector类就是用来选择web元素的



# 一、UIautomatorAPI定位元素
# 表达形式（java代码）

# (1)通过ID选择
# new UiSelector().resourceId("io.manong.developerdaily:id/targetid")

# (2)通过CLASS选择
# new UiSelector().className("android.widget.TextView")

# (3)通过text选择
# new UiSelector().text("软件测试工程师")

# (4)组合使用
# new UiSelector().text("我的").className("android.widget.TextView")
#不用另起一个new，可以直接在后面加. 组合起来寻找我们想要的元素

# (5)选择子元素
# new UiSelector().resourceId("io.manong.developerdaily:id/tab_bar").
# childSelector(new
# UiSelector().className("android.widget.TextView").instance(3))

# textContains、textStartsWith、textMatches（正则表达式）方法
# new UiSelector().textContains("工程师")    #包含工程师字段
# new UiSelector().textMatches("\d\d-\d\dK")  #10-15K


# 注意：隐式等待的作用用于找元素




































































