# Time:2020-02-13 21:49
# Author:TSL

from selenium import webdriver

import time

def get_weathermsg():
    driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
    #创建浏览器实例
    driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")
    #搜索天气网址

    #取出所有城市的天气信息
    city_list = driver.find_element_by_id("forecastID")
    print(city_list.text)

    city_list1 = city_list.text + "\n"  #加回车符方便下面切割

    weather_msg = city_list1.split("℃\n") #切割出每个城市对应的温度
    # print(weather_msg)
    driver.quit()
    return weather_msg

def get_lowsetemp(weather_msg):
    lowset_temp = None       #定义一个变量
    cities = []              #定义一个空列表，存放城市名
    for msg in weather_msg[:-1]:
        city_name = msg.split("\n")[0]
        # print(city_name)
        temp = msg.split("\n")[1]
        # print(temp)
        low_temp = min([int(one) for one in temp.split("℃/")])
        # print(low_temp)

        #第一次还没有获取最低温度或者循环获取的当前温度比已经获取的最低温度还要低
        if lowset_temp == None or low_temp < lowset_temp:
            lowset_temp = low_temp
            cities = [city_name]
        elif low_temp == lowset_temp:
            cities.append(city_name)

    print("最低温度是{}℃，城市有{}".format(lowset_temp,cities))


if __name__ == '__main__':
    weather_msg = get_weathermsg()
    get_lowsetemp(weather_msg)
