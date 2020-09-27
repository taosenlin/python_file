# Time:2020-02-22 20:43
# Author:TSL

#查看设备   adb devices
#查看具体调试的设备   adb devices -l


#发现appPackage和appActivity(使用下面命令）

# （1）app已经在手机上安装
# adb shell dumpsys activity recents | findstr "intent={"

# intent={act=android.intent.action.MAIN cat=
# [android.intent.category.LAUNCHER] flg=0x10200000
# cmp=com.hpbr.bosszhipin/.module.launcher.WelcomeActivity}

# appPackage :  com.hpbr.bosszhipin                   #包名
# appActivity :  .module.launcher.WelcomeActivity     #程序入口



# （2）app还以apk的形式在电脑上时
# 可通过 androidsdk\build-tools 找到该目录下的aapt.exe文件
# 然后直接在上方路径下输入cmd命令，进去cmd目录下的该路径
# 使用命令：
#    aapt.exe dump badging D:\apk\toutiao.apk 可查看
#或者aapt.exe dump badging D:\apk\toutiao.apk > D:\info.txt && D:\info.txt
#找到并在info.txt文件中打开



# (3)"http://127.0.0.1:4723/wd/hub"的解释
# 127.0.0.1和localhost的是“等价的”，代表本机

# 端口号：4723
# 在cmd查看目前占用的端口号，输入命令
# netstat -ano查看所有端口占用；
# netstat -ano | findstr “4723” 查看4723端口号被哪个程序占用
# 也可以打开appium服务，发现appium服务端口号为4723

# /wd/hub
# wd可以理解为WebDriver的缩写
# hub是指主（中心）节点，在selenium 分布式里中心节点




























