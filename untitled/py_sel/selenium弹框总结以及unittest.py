#coding : utf8
#Author : taosenlin
#Time : 2020/5/26 10:59

# 一、Selenium元素定位中弹框的几种方式

# 1、弹出框是alert(警告框)类型
# selenium提供switch_to_alert()方法：捕获弹出对话框(可以定位alert、confirm、prompt对话框)

# 2、弹出框不是alert类型
# (1)弹出框是div层，跟平常一样定位，不用管弹出框
# 点击退出按钮
# FindElement(self.brower,"classname","btn-exit").click()
# time.sleep(3)
# 点击确认按钮(直接定位元素不用管页面的弹出样式，driver.window_handles打印出来的窗口在同一个页面)
# FindElement(self.brower, "classname", "pro-btn.btn-2.btn-confirm").click()

# (2)弹出框是iframe
# driver.switch_to.frame("frame1")之后进行定位元素

# (3)弹出的内容是嵌入的窗口解决思路：
# 打印所有的handle
# all_handles = driver.window_handles
# print(all_handles)
# 切换到新的handle上
# driver.switch_to.window(all_handles[1])



# 二、unittest单元测试框架使用步骤

# unittest框架的TestSuite()类是用来创建测试套件的
# 1、suite = unittest.TestSuite()

# addTest()方法是将测试用例添加到测试套件中，如下方，是将test_baidu模块下的Testbaidu类下的test_baidu测试用例添加到测试套件。
# 2、suite.addTest(test_baidu.Testbaidu('test_baidu'))

# unittest.TextTestRunner():unittest框架的TextTestRunner()类，通过该类下面的run()方法来运行suite所组装的测试用例，入参为suite测试套件。
# 3、runner = unittest.TextTestRunner()

# run()方法是运行测试套件的测试用例，入参为suite测试套件。
# 4、runner.run(suite)









































































