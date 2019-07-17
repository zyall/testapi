from selenium.webdriver.common.by import By
from Common.newPageBaselos import newPageBaselos


class PageTestFabentong(newPageBaselos):
    def __init__(self,driver,desired_caps):
        newPageBaselos.__init__(self,driver,desired_caps)

    element_no = (By.XPATH,'//XCUIElementTypeOther[@name="farben-homs"]/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTextField')
    element_password = (By.XPATH,'//XCUIElementTypeOther[@name="farben-homs"]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeSecureTextField')
    element_login = (By.XPATH,'//XCUIElementTypeButton[@name="登录"]')
    def test_input(self,number,password):
        self.wait_element(*self.element_no).click()
        self.wait_element(*self.element_no).clear()
        self.wait_element(*self.element_no).send_keys(number)
        self.wait_element(*self.element_password).click()
        self.wait_element(*self.element_password).clear()
        self.wait_element(*self.element_password).send_keys(password)
        self.wait_element(*self.element_login).click()


if __name__ == '__main__':
    driver = None
    desired_caps = {
        "platformName": "ios",
        "udid": "3d2b104a503ecb1f4d630c03937a4f153a214d4c",
        "deviceName": "iPhone 6s",
        "automationName": "XCUITest",
        "bundleId": "com.farben.homs"

    }
    TestApp = PageTestFabentong(driver,desired_caps)
    TestApp.test_input("06359",'120347')