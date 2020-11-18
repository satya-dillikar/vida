import os
import sys
import json
import os
from urllib.parse import urlparse
get_version_cmd ="cat ./resource-helmChart/version"
chart_version = os.system(get_version_cmd)
print ("Chart-version: ",get_version_cmd )
get_metadata_cmd = "cat ./resource-helmChart/metadata.json"
with open('./resource-helmChart/metadata.json') as f:
  meta_data_json = json.load(f)
for item in meta_data_json:
        if item["name"] == "repository":
                helm_server= item["value"]
        if item["name"] == "chart":
                chartname= item["value"]
print ("helm_server: ",helm_server )   
print ("chartname: ",chartname )
parsed_url = urlparse(helm_server).hostname
print(parsed_url)
api_end_point = parsed_url + "/api/v2.0"
helm_server = helm_server.replace(parsed_url,api_end_point)
print(helm_server)
url = helm_server + "/charts/" + chartname + "/" + str(chart_version) + "/labels"
command = "curl -k -v  -u admin:VMware@vida12345  -X POST \""  + url + "\" -H 'accept: application/json' -H 'Content-Type: application/json' -d '{\"id\": 1}'"
os.system(command)
print(command)
