# usr/bin/python
# encoding:utf-8
from ddt import ddt, data
from conf import xlsPath
import unittest
from utils.readexcel import ExcelUtil
from Page.fabentong import PageTestFabentong

filepath = xlsPath + '/test.xlsx'
testdata = ExcelUtil(filepath, sheetIndex=0).dict_data()


@ddt
class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = None
        desired_caps = {
            "platformName": "ios",
            "udid": "3d2b104a503ecb1f4d630c03937a4f153a214d4c",
            "deviceName": "iPhone 6s",
            "automationName": "XCUITest",
            "bundleId": "com.farben.homs"

        }
        cls.TestApp = PageTestFabentong(driver, desired_caps)
        print("****Start Test*******")

    @classmethod
    def tearDownClass(self):
        self.TestApp.kill_idevicesyslog()
        print("****End Test*******")

    @data(*testdata)
    def test_case_01(self, data):
        self.TestApp.test_input(data['employeeId'], data['password'])
