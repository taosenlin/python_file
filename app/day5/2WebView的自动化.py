# Time:2020-03-01 22:18
# Author:TSL

# 一、WebView的自动化
1、WebView的内容 不依赖所在app
# 只是打开一个url
# 直接用chrome浏览器打开对应的网页
# 使用手机模式



2、Appium自动化webview
#(1) appium中把所有的界面环境称之为context
#(2)native部分的context名字一般为NATIVE_APP
#(3)webview部分的context则为WEBVIEW_XXXX(应用app package名)

#(4)我们怎么查看当前有哪些context呢？
# driver.contexts

#(5)而显示当前context的则是
# driver.current_context
# 切换driver.switch_to.context(contextname)



# 总结：1、在电脑上自动化手机页面不需要Appium
# 2、用手机浏览器自动化需要匹配手机浏览器版本的驱动
# 3、只有开启debug模式的app才能被自动化webview的内容
# 4、自动化webview界面内容需要匹配webview版本的驱动














































































