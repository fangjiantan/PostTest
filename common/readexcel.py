#coding:utf-8
import json
from time import sleep

import xlrd
from xlrd import open_workbook

class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                s['rowNum'] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

if __name__ == "__main__":
    filepath = "C:\\Users\\Administrator\\PycharmProjects\\PostTest\\Testcase\\demo_api.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath,sheetName)

    print(data.dict_data())

