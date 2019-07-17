from selenium.webdriver.common.by import By
from Common.newPageBaselos import newPageBaselos


class PageTestApp(newPageBaselos):
    def __init__(self, driver, desired_caps):
        newPageBaselos.__init__(self, driver, desired_caps)

    element = (By.XPATH,'//XCUIElementTypeTextField[@name="IntegerA"]')

    def test_input(self,content):
        self.wait_element(*self.element).click()
        self.wait_element(*self.element).send_keys(content)


if __name__ == '__main__':
    driver = None
    desired_caps = {
        "app": "/Users/zq1/Downloads/git_test/test-appnium/sample-code/sample-code/apps/TestApp/build/Release-iphonesimulator/TestApp-iphonesimulator.app",
        "platformName": "ios",
        "platformVersion": "12.1",
        "deviceName": "iPhone 6s",
        "automationName": "XCUITest"
    }
    TestApp = PageTestApp(driver, desired_caps)
    TestApp.test_input("123")