#usr/bin/python
# encoding:utf-8
from ddt import ddt, data
from conf import xlsPath
import unittest
from utils.readcsv import get_data_csv
from conf import desired_caps
from selenium.webdriver.common.by import By
from Base.PageBase import PageBase

filename = xlsPath + '/test.csv'
testdata = get_data_csv(filename)


@ddt
class TestCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = None
        cls.TestApp = PageBase(driver, desired_caps)
        element_linjindou = (By.XPATH,'//XCUIElementTypeOther[@name="领京豆"]')
        cls.TestApp.wait_elements(*element_linjindou).click()
        print("****Start Test*******")

    @classmethod
    def tearDownClass(self):
        self.TestApp.kill_idevicesyslog()
        print("****End Test*******")
    #
    # def test_case_linjindou(self):
    #     element_qiandao = (By.XPATH,'//XCUIElementTypeOther[@name="签到领京豆"]')
    #     self.TestApp.wait_elements(*element_qiandao).click()
    def test_case_shuangqian(self):
        element_shuangqian = (By.XPATH, '//XCUIElementTypeOther[@name="双签领豆"]')
        # element_quqiandao = (By.ID,"去签到")
        # element_quxiao = (By.ID,"取消")
        self.TestApp.wait_elements(*element_shuangqian).click()
        # self.TestApp.wait_elements(*element_quqiandao).click()
        # self.TestApp.wait_elements(*element_quxiao).click()

    # def test_case_store(self):
    #     element_linjindou = (By.XPATH,'//XCUIElementTypeOther[@name="领京豆"]')
    #     self.TestApp.wait_elements(*element_linjindou).click()
    #     element_jindian = (By.ID,'进店领豆')
    #     self.TestApp.wait_elements(*element_jindian).click()
    #     element_jindian1 = (By.XPATH,'(//XCUIElementTypeOther[@name="即将开始"])[2]')
    #     self.TestApp.wait_elements(*element_jindian1).click()
    #     # element_jindian2 = (By.XPATH,'xpath	(//XCUIElementTypeOther[@name="即将开始"])[4]')
    #     # self.TestApp.wait_elements(*element_jindian2).click()






if __name__=='__main__':
    unittest.main()

