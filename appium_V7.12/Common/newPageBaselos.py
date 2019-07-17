from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from conf import logger


class newPageBaselos(object):
    def __init__(self, driver,desired_caps):
        if driver is None:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self.driver = driver

    def get_element(self, *locator):
        logger.info("查找元素 %s" % str(locator))
        return self.driver.find_element(*locator)

    #获取元素，智能等待
    def wait_element(self, *locator):
        ele = None
        count = 0
        while ele is None:
            count = count + 1
            try:
                ele = self.driver.find_element(*locator)
            except:
                pass
            flag = ele is not None
            logger.info("查找元素第%d次 %s %s " % (count, flag, str(locator)))
            time.sleep(0.1)
            if count > 30:
                logger.info("没有找到元素 %s" % str(locator))
                break
        return ele


    def wait_elements(self, *locator):
        eles = None
        count = 0
        while eles is None:
            count = count + 1
            try:
                eles = self.driver.find_element(*locator)
            except:
                pass
            flag = eles is not None
            logger.info("查找元素第%d次 %s %s " % (count, flag, str(locator)))
            time.sleep(0.1)
            if count > 30:
                logger.info("没有找到元素 %s" % str(locator))
                break
        return eles


    def long_touch(self,element):
        ta = TouchAction(self.driver)
        ta.long_press(element,duration=1000).perform()



if __name__ == '__main__':
    driver = None
    desired_caps = {
        "platformName": "ios",
        "udid": "3d2b104a503ecb1f4d630c03937a4f153a214d4c",
        "deviceName": "iPhone 6s",
        "automationName": "XCUITest",
        "bundleId": "com.360buy.jdmobile"

    }
    Page = newPageBaselos(driver,desired_caps)