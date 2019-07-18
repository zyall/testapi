from selenium.webdriver.common.by import By
from Base.PageBase import PageBase


class PageTestJD(PageBase):
    def __init__(self,driver,desired_caps):
        PageBase.__init__(self,driver,desired_caps)

    element_linjindou = (By.XPATH,'//XCUIElementTypeOther[@name="领京豆"]')
    element_qiandao = (By.XPATH,'//XCUIElementTypeOther[@name="签到领京豆"]')

    element_shuangqian = (By.XPATH,'//XCUIElementTypeOther[@name="双签领豆"]')

    def test_input(self):
        print(self.element_linjindou)
        self.wait_element(*self.element_linjindou).click()
        # self.wait_element(*self.element_qiandao).click()
        self.wait_element(*self.element_shuangqian).click()





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