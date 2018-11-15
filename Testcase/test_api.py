# coding:utf-8
import unittest
import ddt
import os
import requests
from common import base_api
from common import readexcel
from common import writeexcel
from common.readexcel import ExcelUtil

curpath = os.path.dirname(os.path.realpath(__file__))
textxlsx = os.path.join(curpath,"demo_api.xlsx")

report_path = os.path.join(os.path.dirname(curpath),"report")
reportxlsx = os.path.join(report_path,"result.xlsx")

testdata = readexcel.ExcelUtil(textxlsx,sheetName="Sheet1").dict_data()

@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        writeexcel.copy_excel(textxlsx,reportxlsx)
    @ddt.data(*testdata)
    def test_api(self,data):
        res = base_api.send_requests(self.s,data)
        base_api.wirte_result(res,filename=reportxlsx)
        check = data["checkpoint"]
        print(u"检查点->:%s"%check)
        res_text = res['text']
        print(u"返回实际结果->:%s"%res_text)
        self.assertTrue(check in res_text)

if __name__ == "__main__":
    unittest.main()