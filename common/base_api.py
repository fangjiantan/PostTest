# coding:utf-8
import json
import requests
from common.readexcel import ExcelUtil
from common.writeexcel import copy_excel, Write_excel


def send_requests(s, testdata):
    method = testdata["method"]
    url = testdata['url']
    try:
        params = eval(testdata["params"])
    except:
        params = None
    try:
        headers = eval(testdata["headers"])
        print(u"请求头部：%s" % headers)
    except:
        headers = None
    type = testdata["type"]
    test_nub = testdata['id']
    print(u"******正在执行用例：-----%s-----******" % test_nub)
    print(u"请求方式：%s，请求url：%s" % (method, url))
    print(u"请求params：%s" % params)

    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post": print(u"post请求body类型为：%s,body内容为：%s" % (type, body))
    elif method == "get":print(u"get")
    verify = False
    #print(u'断点')
    res = {}
    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify,
                      )
        #print(u'断点1')
        print(u"页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res['statuscode'] = str(r.status_code)
        res['text'] = r.content.decode("utf-8")
        res['times'] = str(r.elapsed.total_seconds())
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果： %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        #print(u'断点2')
        res["msg"] = str(msg)
        return res


def wirte_result(result, filename="result.xlsx"):
    row_nub = result['rowNum']
    wt = Write_excel(filename)
    wt.write(row_nub, 8, result['statuscode'])
    wt.write(row_nub, 9, result['times'])
    wt.write(row_nub, 10, result['error'])
    wt.write(row_nub, 12, result['result'])
    wt.write(row_nub, 13, result['msg'])


if __name__ == "__main__":
    data = ExcelUtil("C:\\Users\Administrator\\PycharmProjects\\PostTest\\Testcase\\demo_api.xlsx",
                     sheetName="Sheet1").dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s,data[0])
    print(res)
    copy_excel("C:\\Users\Administrator\\PycharmProjects\\PostTest\\Testcase\\demo_api.xlsx",
               "C:\\Users\Administrator\\PycharmProjects\\PostTest\\report\\result.xlsx")
    wirte_result(res, filename="C:\\Users\Administrator\\PycharmProjects\\PostTest\\report\\result.xlsx")
