# Time:2020-02-26 21:36
# Author:TSL

# 一、无线连接步骤：

# 1、先以USB有线连接方式连接到计算机
#
# 2、激活手机adb的无线服务
# 命令行输入： adb tcpip 5555

#中间步骤：断开USB连接

# 3、计算机以无线方式连接到手机
# 命令行输入： adb connect <deviceip>(手机上查看ip地址)

# 4、断开连接
# 命令行输入： adb disconnect <deviceip>



























