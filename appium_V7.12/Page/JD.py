from selenium.webdriver.common.by import By
from Base.PageBase import PageBase


class PageTestJD(PageBase):
    def __init__(self,driver,desired_caps):
        PageBase.__init__(self,driver,desired_caps)

    element_login = (By.ID,'com.jingdong.app.mall:id/ark')


    def test_input(self):
        self.wait_element(*self.element_login).click()






if __name__ == '__main__':
    driver = None
    desired_caps = {
        "platformName": "ios",
        "udid": "3d2b104a503ecb1f4d630c03937a4f153a214d4c",
        "deviceName": "iPhone 6s",
        "automationName": "XCUITest",
        "bundleId": "com.360buy.jdmobile"

    }
    TestApp = PageTestJD(driver,desired_caps)
    TestApp.test_input()