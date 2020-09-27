# Time:2020-02-13 20:36
# Author:TSL

from selenium import webdriver

# import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象

driver.get("http://music.baidu.com/top/new")
#访问网址

#需求：抓取歌曲排行版信息

#可以依层寻找
songList = driver.find_element_by_id("songListWrapper")  #确定歌曲排行版范围
songList = songList.find_element_by_tag_name("ul")       #缩小范围
songList = songList.find_elements_by_tag_name("li")      #获取每首歌曲的列表

#此时，在元素列表中每一个元素就是一行歌曲信息
for li in songList:
    #获取一行歌曲里面的上升（up)的歌曲
    upSong = li.find_elements_by_class_name("up")
    if upSong:
        #获取歌曲名和演唱者名
        spanTag = li.find_element_by_class_name("song-title")
        songName = spanTag.find_element_by_tag_name("a").text

        #获取演唱者
        songAuthor = li.find_element_by_class_name("author_list").text

        print("{}:{}".format(songName,songAuthor))

driver.quit()












































