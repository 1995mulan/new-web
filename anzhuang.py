# encoding=utf8
import paramiko
import time

#ssh登录一键安装工控系统

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.10.231', 22, 'root', '1')
stdin, stdout, stderr = ssh.exec_command('cd /opt/dev;tar -zxvf dbsec_gk1.0.5-FR.972_971_all.tar.gz;',get_pty=True)
time.sleep(60)
stdin, stdout, stderr = ssh.exec_command('cd /opt/dev/deploy;chmod 777 install.sh;./install.sh -p=c226',get_pty=True)
time.sleep(120)
stdin, stdout, stderr = ssh.exec_command('systemctl start dbsecd')
print (stdout.read())
ssh.close();
time.sleep(120)
