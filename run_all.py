# coding=utf-8
import unittest
import time
from common import HTMLTestRunner
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath,"report")
if not os.path.exists(report_path):os.mkdir(report_path)
case_path = os.path.join(curpath,"Testcase")

def add_case(casepath=case_path,rule="test*.py"):
    discover = unittest.defaultTestLoader.discover(casepath,pattern=rule)
    return  discover

def run_case(all_case,reportpath=report_path):
    htmlreport = reportpath+r"\result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="测试报告",description="用例执行情况")
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)