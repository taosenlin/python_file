# Time:2020-03-01 15:02
# Author:TSL

# 一、电脑上自动化手机模式的网页
# 1、利用浏览器的手机模式打开页面
#打开电脑上的浏览器以手机模式运行

chrome_options = webdriver.ChromeOptions()

#选择一种存在的模拟手机设备类型
chrome_options.add_experimental_option(
    "mobileEmulation",
    {"deviceName":"iPhone X"})



# 二、用手机浏览器自动化网页
#1、利用chrome浏览器
配置项添加，'browserName':'Chrome'
无需再指定app包名和入口信息

# 2、其他浏览器（前提有对应的驱动）
# 自行获取package以及activity
# 自行切换webview中



# 三、自动化嵌套在app内部的网页
# 1、了解webview

# 混合（Hybrid）应用
# 一部分是原生界面和代码，而另一部分是内嵌网页
# 比如支付宝、微信
# 内嵌了一个浏览器内核，由浏览器内核实现的
#
# 2、安卓应用中的内嵌的展示网页内容的模块，我们称之为webview

# 3、App内部webview
# 前提条件：
# 当以上方案不能用浏览器打开自动化webview对应的页面时
# 采用备选方案，直接对app内部webview自动化


准备工作1：修改源码-开启webviewdebug
# app修改编译
# 对webview对象加入setWebContentsDebuggingEnabled的调用
#
# protected void onCreate(Bundle savedInstanceState){
#     super.onCreate(savedInstanceState);
#     WebView myWebView = (WebView)findViewById(R.id.jcywebview);
#     myWebView.setWebContentsDebuggingEnabled(true);
# };
# Tips:从应用市场下载的app不具备此条件
# 只有修改此应用的源码才能进行webview自动化（需要开发人员修改后重新打包才能进行自动化测试）


准备工作2：查看webview元素
# WebView的内容依赖所在app
# 通过chrome的远程调试功能-需要科学上网
# 打开chrome浏览器，地址栏输入chrome://inspect
# 需要Android4.4(KitKat)或更高版本


准备工作3：选择合适的webdriver
# 查看webview实现(chrome_version)
# 选择匹配的chromedriver


WebView的自动化
# 1、WebView 的内容不依赖所在app
# 只是打开一个url
# 直接用chrome浏览器打开对应的网页
# 使用手机模式

# 2、Appium自动化webview
# appium中把所有的界面环境称之为 context
# native部分的context名字一般为NATIVE_APP  (原生)
# webview部分的context则为WEBVIEW_XXX (应用app package名)  (web)

# 我们怎么查看当前有哪些context呢？
# driver.contexts
# 而显示当前context的则是
# driver.current_context
# 切换 driver.switch_to.context(contextname)






































