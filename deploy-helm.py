import re
import os
import time
os.system('pip3 install paramiko')
import paramiko
import sys

host = sys.argv[1]
port = 10004
username = sys.argv[2]
password = sys.argv[3]


command = "export KUBECONFIG=/root/kubeconfig.yaml; helm delete wp; helm repo update;helm install wp hb/wordpress-mysql-stateless"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
print (stdout.read())
time.sleep(10)

stdout.close()
stdin.close()
ssh.close()
