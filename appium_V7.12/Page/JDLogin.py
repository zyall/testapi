from selenium.webdriver.common.by import By
from Base.PageBase import PageBase


class PageTestJD(PageBase):
    def __init__(self,driver,desired_caps):
        PageBase.__init__(self,driver,desired_caps)

    element_iknow = (By.ID,'com.jingdong.app.mall:id/br9')
    element_start = (By.ID,'com.jingdong.app.mall:id/c7g')
    element_continue = (By.ID,'com.jingdong.app.mall:id/ari')
    element_always_allow = (By.ID,'com.android.packageinstaller:id/permission_allow_button')
    element_login = (By.ID,'com.jingdong.app.mall:id/ark')


    def test_input(self):
        self.wait_element(*self.element_iknow).click()
        self.wait_element(*self.element_start).click()
        self.wait_element(*self.element_continue).click()
        self.wait_element(*self.element_always_allow).click()
        self.wait_element(*self.element_always_allow).click()
        self.wait_element(*self.element_login).click()
    def window_size(self):
        size = driver.get_window_size()
        print(size)

if __name__ == '__main__':
    driver = None
    caps_android = {
        "autoAcceptAlerts": "true",
        "platformName": "android",
        "platformVersion": "7.0",
        "deviceName": "03157df369b19a2b",
        "appPackage": "com.jingdong.app.mall",
        "appActivity":"com.jingdong.app.mall.main.MainActivity"
    }
    TestApp = PageTestJD(driver,caps_android)
    TestApp.test_input()
    TestApp.kill_idevicesyslog()
    size = driver.get_window_size()
