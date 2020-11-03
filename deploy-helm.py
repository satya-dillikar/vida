import re
import os
os.system('pip3 install paramiko')
import paramiko
import sys

host = sys.argv[1]
port = 10004
username = sys.argv[2]
password = sys.argv[3]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
channel = ssh.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

stdin.write('''
helm delete wp
helm repo update
helm install wp hb/wordpress-mysql-stateless
''')
print (stdout.read())

stdout.close()
stdin.close()
ssh.close()
