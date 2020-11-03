import re
import os
os.system('pip3 install paramiko')
import paramiko
import sys

host = sys.argv[1]
port = 10004
username = sys.argv[2]
password = sys.argv[3]

command = "helm delete wp; helm repo update;  helm install wp hb/wordpress-mysql-stateless"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
stdin.close()
lines = stdout.readlines()
for line in stdout:
    print('... ' + line.strip('\n'))

stdout.close()
stdin.close()
ssh.close()
