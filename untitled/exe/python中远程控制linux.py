#coding : utf8
#Author : taosenlin
#Time : 2020/3/23 18:05

import paramiko

def sshclient(hostname,port,username,password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,port=port,username=username,password=password)
    stdin,stdout,stderr = ssh.exec_command("ls")

    print(stdout.read().decode("utf8"))

    ssh.close()

def main():

    hostname = '172.16.72.152'
    port = 22
    username = 'taosenlin'
    password = '061012'

    sshclient(hostname,port,username,password)


if __name__ == '__main__':
    main()



































































