import re
import os
os.system('pip3 install paramiko')
import paramiko
print ("Testing Python")


import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

host = sys.argv[2]
port = sys.argv[1]
username = sys.argv[3]
password = sys.argv[4]

command = "kubectl --kubeconfig=kubeconfig.yaml  apply -f https://raw.githubusercontent.com/shefeekj/helm-repo/main/stateless/wordpress/mysql-deployment.yml -f https://raw.githubusercontent.com/shefeekj/helm-repo/main/stateless/wordpress/wordpress-deployment.yaml"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
stdin.close()
result = str(stdout.read().decode('ascii').strip("\n"))
lines = stdout.readlines()
print (result)
tso_flag = re.findall(r":\s(\w+)", result)
channel = ssh.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

stdin.write('''
cd tmp
ls
exit
''')
print (str(stdout.read().decode('ascii').strip("\n")))

stdout.close()
stdin.close()
ssh.close()

