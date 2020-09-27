#coding : utf8
#Author : taosenlin
#Time : 2020/5/18 10:19

# from test_meet import testmeeting
from test_meet import TestMeetingPage

def main():
    username = "taosenlin@kedacom.com"
    password = "061012tsl"
    num = "0000951"
    # testmeeting(username,password,num)
    a = TestMeetingPage()
    a.testmeeting(username,password,num)

if __name__ == '__main__':
    main()



























































































