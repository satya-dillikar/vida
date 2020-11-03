import re
import os
os.system('pip3 install paramiko')
import paramiko
import sys

host = sys.argv[1]
port = 10004
username = sys.argv[2]
password = sys.argv[3]

command1 = "helm delete wp; helm repo update"
command2 = "helm install wp hb/wordpress-mysql-stateless"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command1)
stdin.close()
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

stdout.close()
stdin.close()
ssh.close()

stdin, stdout, stderr = ssh.exec_command(command2)
stdin.close()
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

stdout.close()
stdin.close()
ssh.close()
