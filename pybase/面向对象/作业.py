# Time:2020-02-16 22:27
# Author:TSL

class Tiger:                            #老虎
    aniName = '老虎'
    def __init__(self,inWeight):
        self.weight = inWeight

    def roar(self):            #叫
        print('我是老虎--wow!,体重减少5斤')
        self.weight -= 5       #体重减少5斤

    def feed(self,food):            #吃
        if food == '肉':
            print('恭喜，喂食正确，体重增加10斤')
            self.weight += 10
        else:
            print('抱歉，体重减少10斤')
            self.weight -= 10


class Sheep:                              #羊
    aniName = '羊'
    def __init__(self,inWeight):
        self.weight = inWeight

    def roar(self):
        print('我是羊--mie！,体重减少5斤')
        self.weight -= 5

    def feed(self,food):
        if food == '草':
            print('恭喜，喂食正确，体重增加10斤')
            self.weight += 10
        else:
            print('抱歉，体重减少10斤')
            self.weight -= 10



class Room:                               #房间
    def __init__(self,inNum,inAnimal):    #区分编号与动物
        self.num = inNum
        self.animal = inAnimal


import time
startTime = time.time()        #游戏开始时间
###########################################################
#游戏开始，创建10个房间，并且动物随机

from random import randint

roomList = []   #房间列表
for one in range(1,11):
    if  randint(0,1) == 1:
        ani = Tiger(200)
    else:
        ani = Sheep(100)
    room = Room(one,ani)    #房间对应的随机的动物
    roomList.append(room)

############################################################

############################################################
#游戏操作过程
while True:              #循环次数不定，根据时间结束游戏
    curTime = time.time()               #获取当前时间
    if curTime-startTime > 30:          #时间到，游戏结束
        for one in roomList:        #打印所有房间---操作列表里面每一个元素都需要遍历
            print(f'房间编号是:{one.num},动物是:{one.animal.aniName},体重是:{one.animal.weight}斤')  #one---列表里面的一个元素（房间实例）
        break


    roomNum = randint(1,10)

    roomObject = roomList[roomNum-1]
    #取出对应的房间实例（利用下表从元素列表取）

    answer = input(f'当前房间编号是:{roomNum},是否需要敲门(y/n)?')
    #提示用户在房间前是否选择敲门

    if answer == 'y':                          #判断用户的选择
        roomObject.animal.roar()               #这个房间.动物.叫

    #喂食
    food = input('请投喂食物:(肉/草)?')         #投入对应的食物
    roomObject.animal.feed(food)














































