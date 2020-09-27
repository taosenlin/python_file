# Time:2020-01-04 13:38
# Author:TSL
#1、用户输入一个手机号码，判断出运营商（移动、联通、电信）
#2、输入位数不对，提示用户位数有误
#3、输入非数字，提示有非法字符
cm = '150' #中国移动
cu = '175' #中国联通
ct = '181' #中国电信
PhoneNumber = input('请输入手机号码：') #输入手机号码
if len(PhoneNumber) == 11:             #判断号码位数
    if PhoneNumber.isdigit():          #判断非法字符
        number = PhoneNumber[:3]
        if number == cm:
            print('移动用户.')
        elif number == cu:
            print('联通用户.')
        elif number == ct:
            print('电信用户.')
        else:
            print('其他用户.')
    else:
        print('您输入的号码有非法字符！')
else:
    print('您输入的号码位数有误！')

