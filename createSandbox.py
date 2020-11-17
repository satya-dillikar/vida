import os
import time
os.system('pip3 install requests')
import requests
import json
import time
# defining the api-endpoint for sandbox ceration
POST_API_ENDPOINT = "https://vida.esp-staging.vmware-aws.com/api/v1/vida/sandbox"

# data to be sent to api 

data= {
"username" : "hemantg@vmware.com",
"cloudVendorId": 1,
"planId": 1

}

jsonData = json.dumps(data)

headers = {"Content-Type": "application/json"} 

r = requests.post(url = POST_API_ENDPOINT, data = jsonData, headers=headers)

r_dictionary= r.json()

GET_API_ENDPOINT = "https://vida.esp-staging.vmware-aws.com/api/v1/vida/sandbox"+ "/"+ str (r_dictionary['id'])
r = requests.get(url = GET_API_ENDPOINT)

print ("===================Sandbox Created============\n")
print (r.text)




