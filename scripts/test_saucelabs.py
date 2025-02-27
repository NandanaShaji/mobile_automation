from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
import pytest
from page_object import saucelabs







@pytest.mark.usefixtures("launch_app")
class Test_DockerApp:

    def test_hamburger_validation(self,read_json):

        try:
            self.driver.find_element(AppiumBy.XPATH, saucelabs.username()).send_keys(read_json["username"])
            self.driver.find_element(AppiumBy.XPATH, saucelabs.password()).send_keys(read_json["password"])
            time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH, saucelabs.login()).click()
            time.sleep(2)

            pdt_count = len(self.driver.find_elements(AppiumBy.XPATH, saucelabs.pdt_count()))
            for i in range(1,pdt_count+1):
                name = self.driver.find_element(AppiumBy.XPATH, saucelabs.pdt_name(i)).text
                print(name)

            self.driver.find_element(AppiumBy.XPATH, saucelabs.pdt1()).click()
            time.sleep(5)
            self.driver.find_element(AppiumBy.XPATH, saucelabs.pdt2()).click()
            time.sleep(5)

            self.driver.find_element(AppiumBy.XPATH, saucelabs.cart()).click()
            time.sleep(2)
            count = len(self.driver.find_elements(AppiumBy.XPATH, saucelabs.remove()))
            print("items in cart: ",count)

            saucelabs.scroll(self.driver)

            # el8 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"2\")")
            # el8.click()
            el9 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.checkout())
            el9.click()
            time.sleep(2)

            el10 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.first_name())
            el10.send_keys(read_json["first_name"])
            time.sleep(2)

            el11 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.last_name())
            el11.send_keys(read_json["last_name"])
            time.sleep(2)

            el12 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.pin())
            el12.send_keys(read_json["pin"])
            time.sleep(2)

            el13 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.continue_button())
            el13.click()
            time.sleep(2)
            
            saucelabs.scroll(self.driver)

            el14 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.finish())
            el14.click()
            time.sleep(2)

         
        except:
            print("cant add item to cart")

    def test_close_driver(self):
        self.driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)