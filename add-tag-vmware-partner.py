import os
import sys
import json
import os
from urllib.parse import urlparse
get_version_cmd ="cat ./resource-helmChart/version"
chart_version =  open("./resource-helmChart/version").read()
get_metadata_cmd = "cat ./resource-helmChart/metadata.json"
with open('./resource-helmChart/metadata.json') as f:
  meta_data_json = json.load(f)
for item in meta_data_json:
        if item["name"] == "repository":
                helm_server= item["value"]
        if item["name"] == "chart":
                chartname= item["value"]
parsed_url = urlparse(helm_server).hostname
print(parsed_url)
api_end_point = parsed_url + "/api/v2.0"
helm_server = helm_server.replace(parsed_url,api_end_point)
print(helm_server)
url = helm_server + "/charts/" + chartname + "/" + str(chart_version).strip() + "/labels"

print ("url: ",url)
command_vmw = "curl -k -v  -u admin:VMware@vida12345  -X POST \""  + url + "\" -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"id\": 1}'"
os.system(command_vmw)
command_pvw = "curl -k -v  -u admin:VMware@vida12345  -X POST \""  + url + "\" -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"id\": 2}'"
os.system(command_pvw)
#print(command_vmw)
#print(command_pvw)
