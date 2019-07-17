from selenium.webdriver.common.by import By
from Common.newPageBaselos import newPageBaselos


class PageTestFabentong(newPageBaselos):
    def __init__(self,driver,desired_caps):
        newPageBaselos.__init__(self,driver,desired_caps)

    element = (By.XPATH,'//XCUIElementTypeOther[@name="领京豆"]')
    element2 = (By.XPATH,'//XCUIElementTypeOther[@name="签到领京豆"]')


    def test_input(self):
        self.wait_element(*self.element).click()
        self.wait_element(*self.element2).click()




if __name__ == '__main__':
    driver = None
    desired_caps = {
        "platformName": "ios",
        "udid": "3d2b104a503ecb1f4d630c03937a4f153a214d4c",
        "deviceName": "iPhone 6s",
        "automationName": "XCUITest",
        "bundleId": "com.360buy.jdmobile"

    }
    TestApp = PageTestFabentong(driver,desired_caps)
    TestApp.test_input()