import re
import os
os.system('pip3 install paramiko')
import paramiko
print ("Testing Python")


import sys

host = sys.argv[1]
port = 10004
username = sys.argv[2]
password = sys.argv[3]

command = "kubectl --kubeconfig=kubeconfig.yaml  apply -f https://raw.githubusercontent.com/shefeekj/helm-repo/main/stateless/wordpress/mysql-deployment.yml -f https://raw.githubusercontent.com/shefeekj/helm-repo/main/stateless/wordpress/wordpress-deployment.yaml"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
stdin.close()
result = str(stdout.read().decode('ascii').strip("\n"))
lines = stdout.readlines()
print (result)

stdout.close()
stdin.close()
ssh.close()

