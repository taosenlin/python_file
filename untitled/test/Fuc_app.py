# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import configparser
import os
import sys
import threading
import login
import xlsxwriter
import xlrd
import pandas as pd
from Ui_appiumtool import Ui_MainWindow


def MyThread(t):
    t1 = threading.Thread(target=t)
    t1.start()


def screencap():
    os.popen('mkdir screencap')
    os.popen('adb shell /system/bin/screencap -p /data/local/tmp/1.png')
    os.popen('adb pull /data/local/tmp/1.png ./screencap')


class AppUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AppUI, self).__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(lambda:MyThread(self.CreatTerminalinfo))
        self.pushButton.clicked.connect(
            lambda: MyThread(self.CreatTerminalinfo))
        self.pushButton_2.clicked.connect(lambda: MyThread(self.CreatTestData))
        self.pushButton_3.clicked.connect(lambda: MyThread(self.openxlsx))
        self.pushButton_4.clicked.connect(lambda: MyThread(self.adbconnect))
        self.pushButton_5.clicked.connect(lambda: MyThread(self.logintest))
        self.pushButton_6.clicked.connect(lambda: MyThread(self.adbdisconnect))
        self.lineEdit.setPlaceholderText("请输入终端ip")
        self.lineEdit_2.setText(self.getipfromcfg())
        self.lineEdit_3.setText(str(min(self.textnumber())))
        self.lineEdit_4.setText(str(max(self.textnumber())))

    # 获取输入的ip地址，生成terminalinfo.ini配置文件

    def CreatTerminalinfo(self):
        try:
            terminalIP = self.lineEdit.text()
            platformName = 'Android'
            automationName = 'UiAutomator2'
            # self.textBrowser.setText(terminalIP)
            r0 = os.popen('adb connect '+terminalIP)
            r0 = r0.buffer.read().decode(encoding='utf8')
            self.textBrowser.append(r0)

            # 获取deviceName
            r1 = os.popen('adb devices')
            r1 = r1.buffer.read().decode(encoding='utf8')
            self.textBrowser.append(r1)
            s1 = 'List of devices attached'
            pos = r1.find('device', len(s1))
            deviceName = r1[len(s1):pos].strip()

            # 系统版本号platformVersion
            r2 = os.popen('adb shell getprop ro.build.version.release')
            platformVersion = r2.buffer.read().decode(encoding='utf8')
            platformVersion = str(platformVersion).strip()

            # 分析apk名称，获取appPackage，appActivity的信息
            filename = os.listdir()
            dd = [i for i, x in enumerate(filename) if x.find('.apk') != -1]
            for i in dd:
                r3 = os.popen('aapt dump badging '+filename[i])
                r3 = r3.buffer.read().decode(encoding='utf8')

                # 获取包名appPackage
                package = 'package: name='
                packagePos = r3.find(package)
                nPos = r3.find('\'', packagePos)
                nPos1 = r3.find('\'', nPos+1)
                appPackage = r3[nPos+1:nPos1]

                # 获取启动名称appActivity
                activity = 'launchable-activity: name='
                activityPos = r3.find(activity)
                nPos = r3.find('\'', activityPos)
                nPos1 = r3.find('\'', nPos+1)
                appActivity = r3[nPos+1:nPos1]

        except Exception as e:
            self.textBrowser.append(repr(e))
            print(e)

        # 生成配置文件
        config = configparser.ConfigParser()
        config.add_section('Terminalinfo')
        config.set('Terminalinfo', 'terminalIP', terminalIP)
        config.set('Terminalinfo', 'platformName', platformName)
        config.set('Terminalinfo', 'platformVersion', platformVersion)
        config.set('Terminalinfo', 'deviceName', deviceName)
        config.set('Terminalinfo', 'appPackage', appPackage)
        config.set('Terminalinfo', 'appActivity', appActivity)
        config.set('Terminalinfo', 'automationName', automationName)

        # 写入文件
        with open('Terminalinfo.ini', 'w+') as fw:
            config.write(fw)

    def CreatTestData(self):
        datas = (
            ['赵一', '8888880000006', '888888', '172.16.176.120', '已成功注册H323会议服务器！'],
            ['孙子Son', '1234560000093', '999999',
                '172.16.177.213', '连接平台172.16.177.213，用户名或密码错误'],
            ['qianer', '1234560000093', '888888',
                '172.16.177.213', '已成功注册H323会议服务器！'],

        )

        # 创建表格

        workbook = xlsxwriter.Workbook('testdata.xlsx')
        worksheet = workbook.add_worksheet('login')

        # 添加全局格式
        bold = workbook.add_format({'bold': True})

        # 添加表格头，附带格式
        worksheet.write('A1', 'devname', bold)
        worksheet.write('B1', 'user', bold)
        worksheet.write('C1', 'pwd', bold)
        worksheet.write('D1', 'ip', bold)
        worksheet.write('E1', 'exp', bold)
        # 数据表格偏移
        row, col = 1, 0

        # 添加数据
        for devname, user, pwd, ip, exp in datas:
            # 按照行列单元格添加数据
            worksheet.write(row, col, devname)
            worksheet.write(row, col+1, user)
            worksheet.write(row, col+2, pwd)
            worksheet.write(row, col+3, ip)
            worksheet.write(row, col+4, exp)

            row += 1

        # 存储退出
        workbook.close()

    def openxlsx(self):
        os.system('start testdata.xlsx')
    # 获取配置ip地址

    def getipfromcfg(self):
        try:
            config = configparser.ConfigParser()
            config.read('Terminalinfo.ini')
            ip = config.get("Terminalinfo", "terminalIP")
            return ip
        except configparser.NoSectionError as e:
            self.textBrowser.append('找不到配置文件：'+repr(e))

        except Exception as e:
            self.textBrowser.append(repr(e))

    def adbconnect(self):
        terminalIP = self.lineEdit_2.text()
        r0 = os.popen('adb connect '+terminalIP)
        r0 = r0.buffer.read().decode(encoding='utf8')
        self.textBrowser.append(r0)
        # 获取deviceName
        r1 = os.popen('adb devices')
        r1 = r1.buffer.read().decode(encoding='utf8')
        self.textBrowser.append(r1)

    def adbdisconnect(self):
        terminalIP = self.lineEdit_2.text()
        r0 = os.popen('adb disconnect '+terminalIP)
        r0 = r0.buffer.read().decode(encoding='utf8')
        self.textBrowser.append(r0)

    # 测试用例总数
    def textnumber(self):
        try:
            df = pd.read_excel('testdata.xlsx', 'login')
            df = df.to_dict(orient='records')
            testmin = 0
            testmax = len(df)
        except FileNotFoundError as e:
            self.textBrowser.append('找不到testdata.xlsx文件')
            testmin = 0
            testmax = 0
            return(testmin, testmax)
        return(testmin+1, testmax)

    def logintest(self):
        self.textBrowser.append('启动Appium会话，请稍后')
        login.setdriver()
        self.textBrowser.append('启动Appium成功')
        df = pd.read_excel('testdata.xlsx', 'login')
        df = df.to_dict(orient='records')

        # 测试用例总数
        testmin = int(self.lineEdit_3.text())
        testmax = int(self.lineEdit_4.text())
        for i in range(testmin-1, testmax):
            info = df[i]
            self.textBrowser.append('第'+str(i+1)+'条测试用例数据：\n'+repr(info))
            user = login.User()
            exp = user.login(info['devname'], info['user'],
                             info['pwd'], info['ip'])
            if exp == info['exp']:
                self.textBrowser.append('第'+str(i+1)+'条用例结果:Pass'+'\n')
            else:
                self.textBrowser.append('第'+str(i+1)+'条用例结果:Failed'+exp+'\n')

        self.textBrowser.append('测试结束\n')


if __name__ == '__main__':

    # 设置任务栏图标显示
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

    app = QApplication(sys.argv)
    #mainWindow = QMainWindow()
    ui = AppUI()
    ui.show()
    sys.exit(app.exec_())
