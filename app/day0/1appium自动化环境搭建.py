# coding:utf8
# Time:2020-04-13 22:15
# Author:TSL

# 一、Appium1-简介
# 1、安装1-客户端

# 安装Appium Python Client包
# pip install Appium-Python-Client
# 要确保安装匹配版本的selenium和appium
# pip install selenium -U


# 2、安装2-服务端
# 安装Appium Desktop(windows版本)
# 下载桌面版程序(可见云盘 工具-appium)


# 3、安装3-电脑端环境
# 安装JDK1.8
# 配置JAVA_HOME环境变量


# 4、安装4-电脑端环境
# 安装AndroidSDK(可见云盘 appium)

# 配置ANDROID_HOME环境变量
# 设置为sdk根目录的路径
# sdk\platform-tools\ 加入到环境变量Path中（方便使用adb命令）


# 5、安装5-手机端设置
# 电脑端的手机驱动，确保电脑能识别出手机（win10默认不需要）
# 可以通过手机助手（驱动安装完成请卸载，否则会造成adb冲突）或者对应品牌的官网去下载

# 手机端开启USB设置
# 用usb线连接到电脑，一头连手机，一头连电脑
# 进入手机设置-关于手机
# 不断点击版本号（7次以上），激活开发者模式
# 退出到上级菜单，在开发者模式中，启动usb调试
# 手机端设置USB连接为MTP媒体传输模式
# 确认授权电脑端调试

# 启动adb连接
# 打开cmd命令行，输入 adb devices -l
# 若不能识别，请确保安装对应的手机USB驱动


# 环境搭建小结
# 1、确保电脑上没有其他的adb程序软件，如杀毒软件-安全管家-手机助手
# 2、确保手机端开发者选项中对应的adb权限全部打开
# 3、（可选）确保手机端appium相关的app对应权限打开
# （设置-应用管理-权限设置-找到对应的app，查看权限）


















































































