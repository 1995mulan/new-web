#!/usr/bin/python 
import paramiko

                                    


t = paramiko.Transport(('192.168.10.28',22))
t.connect(username = 'root', password = 'root')
sftp = paramiko.SFTPClient.from_transport(t)  #使用t的设置方式连接远程主机

remotepath='/home/secsmart/license/E3060500FFFBEBBF/authorization.license'
localpath='C:/dd/authorization.license'

sftp.get(remotepath, localpath)  #下载文件
t.close()







'''
import paramiko
import time
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.10.28', username='root', password='root')



stdin, stdout, stderr = ssh.exec_command('sz /home/secsmart/license/E3060500FFFBEBBF/authorization.license')
print(stdout.readlines())
print(stdout.read().decode())
ssh.close()
''' 


