# Time:2020-02-26 22:06
# Author:TSL

# 一、Session机制
# (1)会话
# (2)用于隔离通信干扰
# a、Appinum测试程序和Appinum server之间的http请求都必须在一个session中进行
# b、session ID


# 二、webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#
# 1、客户端代码与appinumserver建立连接，并传递caps配置信息
# 2、Appinumserver检查配置信息是否符合要求
# 3、利用adb工具检查当前连接的移动设备
# 4、安装appinum-settings与uiautomator2到被测手机（首次运行脚本发生）
# 5、手机启动appinum-settings作为监听服务，用于和appinum-settings进行通信
# 6、uiautomator2启动被测app


























































