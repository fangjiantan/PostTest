import requests
import sys
import io
import json

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

body = {"account":"admin","password":"yingshitec2018@"}
headers = {"KEY":"Content-Type","VALUE":"application/json"}
url = 'http://api.chebaotec.com/washingmanage/n/login'
url2 = 'http://api.chebaotec.com/washingapp'


#r = requests.post(url=url,headers=headers,data=json.dumps(body))
#r1 = r.cookies.get_dict()
#print r1



#rr = requests.post(url=url2,headers=headers,data=json.dumps(body))
#r2 = rr.cookies.get_dict()
#print r2

cookies = {'JSESSIONID': '2c88f39f-b40b-4e33-a329-1e42bdba5d24'}

url3 = 'http://api.chebaotec.com/washingmanage/n/business/device/month?pageIndex=1&pageSize=3'
payload = {'pageIndex':'1','pageSize':'3'}
rs = requests.get(url=url3,params=payload,cookies=cookies)
print(rs.status_code)
print(rs.cookies.get_dict())
print(rs.text)





