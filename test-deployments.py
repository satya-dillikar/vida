import re
import os
os.system('pip3 install paramiko')
import paramiko
import sys
 
host = sys.argv[1]
port = 10004
username = sys.argv[2]
password = sys.argv[3]

command = "kubectl --kubeconfig=kubeconfig.yaml  get all"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
stdin.close()
result = str(stdout.read().decode('ascii').strip("\n"))
print (result)
pod_status = re.findall(r"pod\/\S+\s+\d\/\d\s+(\w+)", result)
print ("PODS", pod_status)
stdout.close()
stdin.close()
ssh.close()

