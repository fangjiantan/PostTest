#conding: utf-8
import json
import requests
url = "http://api.chebaotec.com/washingmanage/n/login"

body = {"account":"admin","password":"yingshitec2018@"}

headers = {"KEY":"Content-Type","VALUE":"application/json"}



r = requests.request("POST",url,headers = headers,data = json.dumps(body))

print (r.text)
print r.status_code
