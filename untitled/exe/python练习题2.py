#coding : utf8
#Author : taosenlin
#Time : 2020/5/11 14:02

"""
求 1-100 内的所有数的和
"""
"""
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
"""
"""
sum = 0
for i in range(1,101):
    sum += i
print(sum)
"""


"""
1.创建并输出菜单, 菜单是不可变的. 所以使用元组
menus = ("1, 录入", "2, 查询", "3, 删除", "4, 修改", "5, 退出")

存储用户的信息    idm: {'name':'名字', 'weight':体重, 'height':身高}
例如：目前有两个用户信息：1. 汪峰， 2. 章子怡
存储结构：
{
  1:{'name':'汪峰', 'weight':80, 'height':1.8, 'BMI':24.7},
  2:{'name':'章子怡', 'weight':50, 'height':1.65, 'BMI':18.4}
}
bodies = {}

body_id = 1  # 编号从1开始

体质指数（BMI）= 体重（kg）÷ (身高(m) x 身高(m))
体重的单位: KG
身高的单位: m
需求：首先。打印菜单，然后用户输入选择的菜单项
输入1：进入录入环节。用户需要录入：名字,身高,体重.
      由程序计算出BMI指数. 保存到bodies字典中. 第一个用户的id是1, 第二个是2, 以此类推
      录入完毕后. 提示用户是否继续录入. 如果选择是, 则继续进行录入, 直到用户输入否. 则返回到主菜单
输入2: 进入查询环节, 提示用户输入要查询的人的id. 如果不存在,给与提示, 如果存在. 则显示出该用户的全部信息(名字,身高,体重,BMI)
      然后提示用户是否继续查询. 如果选择是, 继续进行查询, 直到用户输入否, 返回主菜单
输入3: 进入删除环节, 提示用户输入要删除的人的id, 如果id不存在, 给与提示, 如果存在, 则执行删除操作. 并提示删除成功.
       然后提示用户是否继续删除, 如果是, 继续让用户选择要删除的id, 直到用户输入否, 返回主菜单
输入4: 进入修改环节, 首先让用户输入要修改的人的id, 根据id查找用户信息, 如果不存在, 给与提示, 如果存在, 将用户原信息进行打印,
      然后提示用户输入新的名字, 身高, 体重. 由程序重新计算BMI指数. 并将新的信息保存在bodies中. 同时给用户展示新的用户信息
      然后提示用户是否继续修改, 如果是, 则继续要求用户输入id信息. 直到用户输入否, 返回主菜单.
输入5: 程序退出.
输入其他任何内容. 都予以提示不合法. 让用户重新进行输入
"""

menus = ("1, 录入", "2, 查询", "3, 删除", "4, 修改", "5, 退出")
bodies = {}
body_id = 1

def main():
    while True:
        for menu in menus:
            print(menu)
        option = int(input("请输入编号:"))
        choose_option(option)


def choose_option(option):
    if option < 1 or option > 5:
        print("请重新输入！")
        # return

    if option == 1:
        create_user()
    elif option == 2:
        read_user()
    elif option == 3:
        del_user()
    elif option == 4:
        update_user()
    elif option == 5:
        exit()



def com_BMI(weight,height):
    return weight/(height * height)

def create_user():
    global body_id
    while True:
        name = input("请输入姓名:")
        weight = float(input("请输入体重(kg):"))
        height = float(input("请输入身高(m):"))
        BMI = com_BMI(weight,height)
        bodies[body_id] = {'name':name,'weight':weight,'height':height,'BMI':BMI}
        body_id += 1
        print(bodies[body_id - 1])
        print("是否继续录入(Y/N)?")
        s = input("请输入:").upper()
        if s == "Y":
            continue
        else:
            break

def read_user():
    while True:
        # print("请输入要查询的人的id")
        n = int(input("请输入要查询的人的id:"))
        if n not in bodies.keys():
            print("输入的id不存在!")
        else:
            print(bodies[n])
        print("是否继续查询(Y/N)?")
        s = input("请输入：").upper()
        if s == "Y":
            continue
        else:
            break

def del_user():
    while True:
        # print("请输入要删除的人的id")
        n = int(input("请输入要删除的人的id:"))
        if n not in bodies.keys():
            print("输入的id不存在!")
        else:
            print(bodies.pop(n))
        print("是否继续删除(Y/N)?")
        s = input("请输入:").upper()
        if s == "Y":
            continue
        else:
            break

def update_user():
    while True:
        # print("请输入要修改的人的id:")
        n = int(input("请输入要修改的人的id:"))
        if n not in bodies.keys():
            print("输入的id不存在!")
        else:
            print(bodies[n])
        print("请输入新的用户信息!")
        name = input("请输入姓名:")
        weight = float(input("请输入体重(kg):"))
        height = float(input("请输入身高(m):"))
        BMI = com_BMI(weight,height)
        bodies[n] = {'name':name,'weight':weight,'height':height,'BMI':BMI}
        print(bodies[n])
        print("是否继续修改(Y/N)?")
        s = input("请输入:").upper()
        if s == "Y":
            continue
        else:
            break

if __name__ == '__main__':
    main()



















































































