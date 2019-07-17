from Page.JD import PageTestFabentong
import unittest
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class TestCase01(unittest.TestCase):

    def test_case01(self):
        driver = None
        desired_caps = {
            "platformName": "ios",
            "udid": "3d2b104a503ecb1f4d630c03937a4f153a214d4c",
            "deviceName": "iPhone 6s",
            "automationName": "XCUITest",
            "bundleId": "com.360buy.jdmobile"

        }
        TestApp = PageTestFabentong(driver, desired_caps)
        TestApp.test_input()
        print("success")
if __name__=='__main__':
    unittest.main()