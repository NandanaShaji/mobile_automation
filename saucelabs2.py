from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
from page_object import saucelabs







# @pytest.mark.usefixtures("launch_app")
class Saucelabs:

    cap = {
        "appium:deviceName": "Samsung",
        "appium:platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "C:\\Users\\2022413\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
        "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity",
        "chromedriverExecutable" : "C:\\Users\\2022413\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    }

    def initiate_Driver(self):

        #self.appium_service = AppiumService()
        #global appium_service
        try:
            global driver
            # driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error: Appium Server not working...")
            self.appium_service.stop()

    def launch_saucelabs(self):

        try:
            driver.find_element(AppiumBy.XPATH, saucelabs.username()).send_keys("standard_user")
            driver.find_element(AppiumBy.XPATH, saucelabs.password()).send_keys("secret_sauce")
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, saucelabs.login()).click()
            time.sleep(2)

            el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.list_view())
            el6.click()
            time.sleep(2)
            el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.filter_option())
            el7.click()
            time.sleep(2)
            el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.low_to_high())
            el8.click()
            time.sleep(2)

            item1 = driver.find_element(AppiumBy.XPATH, saucelabs.low_to_high_1()).text
            # Extract digits using a loop and isdigit()
            price_item1 = ''.join(char for char in item1 if char.isdigit())

            item2 = driver.find_element(AppiumBy.XPATH, saucelabs.low_to_high_2()).text
            # Extract digits using a loop and isdigit()
            price_item2 = ''.join(char for char in item2 if char.isdigit())

            if int(price_item1) < int(price_item2):
                print("price of item 1 < price of item 2")

            el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.filter_option())
            el9.click()
            time.sleep(2)
            el10 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.high_to_low())
            el10.click()
            time.sleep(2)

            item3 = driver.find_element(AppiumBy.XPATH, saucelabs.high_to_low_1()).text
            # Extract digits using a loop and isdigit()
            price_item3 = ''.join(char for char in item3 if char.isdigit())

            item4 = driver.find_element(AppiumBy.XPATH, saucelabs.high_to_low_2()).text
            # Extract digits using a loop and isdigit()
            price_item4 = ''.join(char for char in item4 if char.isdigit())

            if int(price_item3) > int(price_item4):
                print("price of item 1 > price of item 2")

            pdt_count = len(driver.find_elements(AppiumBy.XPATH, saucelabs.pdt_count()))
            for i in range(1,pdt_count+1):
                name = driver.find_element(AppiumBy.XPATH, saucelabs.pdt_name(i)).text
                print(name)

            el11 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.list_pdt1())
            el11.click()
            time.sleep(2)
            el13 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucelabs.list_pdt2())
            el13.click()
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, saucelabs.cart()).click()
            time.sleep(2)
            time.sleep(2)

            saucelabs.scroll(driver)

            el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.checkout())
            el9.click()
            time.sleep(2)

            el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.first_name())
            el10.send_keys("abc")
            time.sleep(2)

            el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.last_name())
            el11.send_keys("def")
            time.sleep(2)

            el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.pin())
            el12.send_keys("123456")
            time.sleep(2)

            el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.continue_button())
            el13.click()
            time.sleep(2)
            
            saucelabs.scroll(driver)

            el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucelabs.finish())
            el14.click()
            time.sleep(2)

        except:
            print("cant add item to cart")

    def close_driver(self):
        driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)


obj = Saucelabs()
obj.initiate_Driver()
obj.launch_saucelabs()
obj.close_driver()