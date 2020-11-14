  
import re
import os
import time
os.system('pip3 install paramiko')
import paramiko
import sys

#Opening config file....

with open('./resource-sandboxInfo/inputs/sandbox1_info.json') as f:
  data = json.load(f)


host = data["ip"]
port = data["port"]
username = data["username"]
password = data["password"]



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
