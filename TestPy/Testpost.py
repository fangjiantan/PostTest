#conding: utf-8
import json
import requests
import unittest
import traceback

url = "http://api.chebaotec.com/washingmanage/n/login"
body = {"account":"admin","password":"yingshitec2018@"}
headers = {"KEY":"Content-Type","VALUE":"application/json"}

#r = requests.request("POST",url,headers = headers,data = json.dumps(body))
#rs = json.loads(r.text)
#print (r.text)
#print "Http Code:",r.status_code
#print "Rcode:",rs['rcode'],'\n',"Rinfo:",rs['rinfo']
try:
    r = requests.request("POST", url, headers=headers, data=json.dumps(body))
    if r.status_code == 200:
        rs = json.loads(r.text)
        if rs['rcode'] == 0:
            print "Success!"
        else:
            print "Fail!"
            print "Rcode:",rs['rcode']
    else:
        raise Exception("Http error info:%s" %r.status_code)

except:
    traceback.print_exc()


