#coding : utf8
#Author : taosenlin
#Time : 2020/3/27 10:20

"""
from selenium import webdriver
import time

driver = webdriver.Chrome(r'E:\chromedriver.exe')

driver.get("http://www.baidu.com")




time.sleep(5)
driver.quit()
"""


"""
flag = False

for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("层",j)
        if j == 6:
            flag = True
            break
    if flag:
        break
"""





import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ssh.connect("172.16.72.152",22,"taosenlin","061012")

stdin,stdout,stderr = ssh.exec_command("cd tmp;echo print(888) > test.py")

print(stdout.read().decode("utf8"))


ssh.close()















