# coding=utf-8
import os
import time
import log
from time import sleep


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import xlrd
import pandas as pd
import configparser

# ---------------日志格式化输出---------------------------------------


def printlog(self):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+':' + self)
    log.log(self)

# --------------------------------------------------------------------

# 元素是否存在


def is_element_exist(element):
    source = driver.page_source

    if element in source:
        return True
    else:
        return False


def check(*element):

    count = 0
    is_exist = False
    while(not is_exist):
        for i in element:
            is_exist = is_element_exist(i)
            if is_exist == True:
                return i
                break
        if count > 30:
            printlog('检测'+repr(element)+'超时')
            break
        else:
            count += 1
            sleep(0.5)
# ---------------类---------------------------------------


def setdriver():
    config = configparser.ConfigParser()
    config.read('Terminalinfo.ini')
    platformName = config.get("Terminalinfo", "platformName")
    platformVersion = config.get("Terminalinfo", "platformVersion")
    deviceName = config.get("Terminalinfo", "deviceName")
    appPackage = config.get("Terminalinfo", "appPackage")
    appActivity = config.get("Terminalinfo", "appActivity")
    automationName = config.get("Terminalinfo", "automationName")

    desired_caps = {}
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity
    desired_caps['automationName'] = automationName
    print(desired_caps)
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print(123)


class User(object):
    def __init__(self):
        check('com.kedacom.kdv.mt.sky_desktop:id/ivMore')
        printlog('进入主界面')
        # 点击更多
        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/ivMore').click()
        printlog('点击更多')
        # 点击设置
        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/ivSetting').click()
        printlog('点击设置')
        sleep(1)
        # 点击管理员设置
        driver.find_element_by_android_uiautomator(
            'new UiSelector().text("高级设置")').click()

        printlog('点击高级设置')


    def login(self, devicesname, accout, password, ip):
        self.devicesname = devicesname
        self.account = accout
        self.password = password
        self.ip = ip

        driver.find_element_by_android_uiautomator(
            'new UiSelector().text("登录")').click()
        printlog('登录')

        sleep(1)
        # 清空设备名称
        edDeviceName = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edDeviceName')
        edDeviceName.clear()
        edDeviceName.send_keys(devicesname)
        # 检查云服务登录是否开启
        isopen = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/titleLogincLoudServices').get_attribute('text')
        print(isopen)
        if isopen == '登录云服务':

            # 登录云服务关闭按钮
            TouchAction(driver).tap(x=1502, y=311).perform()
            printlog('开启登录云服务成功')
            driver.implicitly_wait(1)
        # 输入账号
        edE164 = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edE164')
        edE164.clear()
        edE164.send_keys(accout)
        printlog('输入账号成功')
        # 输入密码
        edPassword = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edPassword')
        edPassword.clear()
        edPassword.send_keys(password)
        printlog('输入密码成功')

        # 输入登录ip
        edIpDomain = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edIpDomain')
        edIpDomain.clear()
        edIpDomain.send_keys(ip)
        printlog('输入ip成功')
        # 保存
        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/goBack').click()

        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/goBack').click()
        sleep(1)

        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/ivSndOrderBack').click()
        printlog('复位成功')

        value = check('com.kedacom.kdv.mt.sky_desktop:id/tvInfo',
                      'com.kedacom.kdv.mt.sky_desktop:id/tvAlert')
        print(value)

        exp = driver.find_element_by_id(value).get_attribute('text')
        printlog(exp)
        return exp

    def creatconf(self):
        pass

    def setip(self, ip, mask, gateway, dns, dnsbak):
        self.ip = ip
        self.mask = mask
        self.gateway = gateway
        self.dns = dns
        self.dnsbak = dnsbak

        driver.find_element_by_android_uiautomator(
            'new UiSelector().text("网络")').click()
        printlog('网络')
        driver.find_element_by_android_uiautomator(
            'new UiSelector().text("以太网")').click()
        printlog('以太网')
        edIpaddress = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edIpaddress')
        edIpaddress.clear()
        edIpaddress.send_keys(ip)

        edSubNetMask = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edSubNetMask')
        edSubNetMask.clear()
        edSubNetMask.send_keys(mask)

        edGateWay = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edGateWay')
        edGateWay.clear()
        edGateWay.send_keys(gateway)

        edDnsServer = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edDnsServer')
        edDnsServer.clear()
        edDnsServer.send_keys(dns)

        edReserveDnsServer = driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/edReserveDnsServer')
        edReserveDnsServer.clear()
        edReserveDnsServer.send_keys(dnsbak)
        # 保存
        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/goBack').click()
        sleep(1)
        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/goBack').click()
        sleep(1)
        printlog('复位成功')
        driver.find_element_by_id(
            'com.kedacom.kdv.mt.sky_desktop:id/ivSndOrderBack').click()
