from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
import pytest
from page_object import saucelabs







@pytest.mark.usefixtures("launch_app")
class Test_Saucelabs:

    def test_launch_saucelabs(self,read_json):

        try:
            self.driver.find_element(AppiumBy.XPATH, saucelabs.username()).send_keys(read_json["username"])
            self.driver.find_element(AppiumBy.XPATH, saucelabs.password()).send_keys(read_json["password"])
            time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH, saucelabs.login()).click()
            time.sleep(2)

            el6 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.list_view())
            el6.click()
            time.sleep(2)
            el7 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.filter_option())
            el7.click()
            time.sleep(2)
            el8 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.low_to_high())
            el8.click()
            time.sleep(2)

            item1 = self.driver.find_element(AppiumBy.XPATH, saucelabs.low_to_high_1()).text
            # Extract digits using a loop and isdigit()
            price_item1 = ''.join(char for char in item1 if char.isdigit())

            item2 = self.driver.find_element(AppiumBy.XPATH, saucelabs.low_to_high_2()).text
            # Extract digits using a loop and isdigit()
            price_item2 = ''.join(char for char in item2 if char.isdigit())

            if int(price_item1) < int(price_item2):
                print("price of item 1 < price of item 2")

            el9 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.filter_option())
            el9.click()
            time.sleep(2)
            el10 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.high_to_low())
            el10.click()
            time.sleep(2)

            item3 = self.driver.find_element(AppiumBy.XPATH, saucelabs.high_to_low_1()).text
            # Extract digits using a loop and isdigit()
            price_item3 = ''.join(char for char in item3 if char.isdigit())

            item4 = self.driver.find_element(AppiumBy.XPATH, saucelabs.high_to_low_2()).text
            # Extract digits using a loop and isdigit()
            price_item4 = ''.join(char for char in item4 if char.isdigit())

            if int(price_item3) > int(price_item4):
                print("price of item 1 > price of item 2")

            pdt_count = len(self.driver.find_elements(AppiumBy.XPATH, saucelabs.pdt_count()))
            for i in range(1,pdt_count+1):
                name = self.driver.find_element(AppiumBy.XPATH, saucelabs.pdt_name(i)).text
                print(name)

            el11 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.list_pdt1())
            el11.click()
            time.sleep(2)
            el13 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.list_pdt2())
            el13.click()
            time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH, saucelabs.cart()).click()
            time.sleep(2)
            time.sleep(2)

            saucelabs.scroll(self.driver)

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