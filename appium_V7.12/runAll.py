#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner
from conf import *

class RunCaseList():
    def Case_List(self):
        '''
        读取CaseList.txt文件内容，返回一个list
        :return:
        '''
        self.CaseList = []
        fb = open(caseListPath)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.CaseList.append(data.replace("\n",""))
        fb.close()
        return self.CaseList

    def Case_Suite(self):
        '''

        :return:
        '''
        self.Case_List()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.CaseList:
            case_name = case.split("/")[-1]
            print(case_name)
            discover = unittest.defaultTestLoader.discover(testCasePath, pattern=case_name, top_level_dir=None)
            suite_model.append(discover)

        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def Run(self):
        try:
            suit = self.Case_Suite()
            if suit is not None:
                logger.info("******** TEST START *********")
                fp = open(reportpath,'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=title,description=description)
                runner.run(suit)
            else:
                logger.info("Have no case to test")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("******** TEST END *********")

if __name__ == '__main__':
    A = RunCaseList()
    A.Run()