# !/usr/bin/python3

"""
FileName    : common.py
Author      : ken
Date        : 2018-04-21
Describe    : common method for test
"""

import os

import xlrd
import xlwt

from commonFile import getDir
from commonFile.Log import MyLog

proDir = getDir.proDir


class PyExcel:
    """Use the given excel_name and sheet_name, sheet_value, write excel and read excel.
        1. write_excel
        2. read_excel
    """
    TestFile = os.path.join(proDir, "testFile")
    suffix = ".xls"

    def __init__(self, excel_name, sheet_name=None, sheet_value=None):
        """
        initialization parameter
        :param excel_name: The file suffix must be "xls"
        :param sheet_name: set the workbook's sheetName
        :param sheet_value: The type of object must be "list" or "tuple"
        """
        self.excel_name = excel_name
        self.sheet_name = sheet_name
        self.sheet_value = sheet_value

        self.logger = MyLog.get_log().get_logger()

        if not str(self.excel_name).endswith(self.suffix):
            raise Exception('%s suffix is not "%s"' %
                            (self.excel_name, self.suffix))
        self.EXCEL_PATH = os.path.join(self.TestFile, self.excel_name)

        if self.sheet_value is not None:
            try:
                if isinstance(self.sheet_value, list) or isinstance(self.sheet_value, tuple):
                    for i in range(len(self.sheet_value)):
                        assert isinstance(self.sheet_value[i], list)
            except TypeError as e:
                self.logger.error(e, exc_info=True)
                print(e)

    def write_excel(self):
        if self.sheet_name is not None:
            wb = xlwt.Workbook()
            sheet = wb.add_sheet(self.sheet_name)

            for i in range(len(self.sheet_value)):
                for j in range(len(self.sheet_value[i])):
                    sheet.write(i, j, self.sheet_value[i][j])

            wb.save(self.EXCEL_PATH)
            print("write date success!")
        else:
            return False

    def read_excel(self):
        workbook = xlrd.open_workbook(self.EXCEL_PATH)
        if self.sheet_name:
            work_sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            work_sheet = workbook.sheet_by_index(0)

        for i in range(work_sheet.nrows):
            for j in range(work_sheet.ncols):
                print(work_sheet.cell_value(i, j), "\t", end="")
            print()


def get_excel_value(excel_name, sheet_name):
    """
    get excel value by given excel_name and sheet_name
    :param excel_name:
    :param sheet_name:
    :return: cls
    """
    cls = []
    excel_path = os.path.join(proDir, "testFile", excel_name)
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows

    for i in range(nrows):
        if sheet.row_values(i)[0] != "case_num":
            cls.append(sheet.row_values(i))
    return cls


if __name__ == "__main__":
    # value = (
    #     ["case_num", "case_name", "username", "password", "excepted"],
    #     ["login_test_01", "用户名正确，密码错误", "qiutiandeyanjin@163.com", "efg", "用户名或密码不正确"],
    #     ["login_test_02", "有用户名没有密码", "qiutiandeyanjin@163.com", "", "请输入密码"],
    #     ["login_test_03", "没有用户名有密码", "", "efg", "请输入帐号"]
    # )
    # excel = PyExcel(excel_name="loginCase.xls", sheet_name="login_test", sheet_value=value)
    # excel.write_excel()
    # excel.read_excel()
    test = get_excel_value(excel_name="loginCase.xls", sheet_name="login_test")
    print(test)
