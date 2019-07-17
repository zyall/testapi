#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging,os
from datetime import datetime


# ============================ Global parameter ==============================
baseurl = 'https://maam.pingan.com.cn'
headers ={"Content-Type":"application/json;charset=UTF-8"}
timeout = 1.0

proDir = os.path.split(os.path.realpath(__file__))[0]
# print(proDir)
xlsPath = os.path.join(proDir, 'testFile')
testCasePath = os.path.join(proDir, 'testCase')
caseListPath = os.path.join(proDir,'caseList.txt')
title = 'Test Report'
description = 'test'
# ============================ report config ==============================
resultPath = os.path.join(proDir,'result',str(datetime.now().strftime("%Y%m%d")))
if not os.path.exists(resultPath):
    os.mkdir(resultPath)
reportpath = os.path.join(resultPath,'report.html')

# ============================ Logger config ==============================

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(os.path.join(resultPath,'output.log'))
formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d]-%(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# ============================ email config ==============================
smtp_sever = "smtp.qq.com"
email_name = "1554754887@qq.com"
email_password = "123900600all"
email_To = "1554754887@qq.com"
# ============================ desired_caps ==============================
# desired_caps = {
#     "platformName": "ios",
#     "udid": "3d2b104a503ecb1f4d630c03937a4f153a214d4c",
#     "deviceName": "iPhone 6s",
#     "automationName": "XCUITest",
#     "bundleId": "com.farben.homs"
#
# }