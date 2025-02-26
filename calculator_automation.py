from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time


class DockerApp:

    cap = {
        "appium:deviceName" : "Samsung",
        "platformName" : "Android",
        "appium:automationName" : "UiAutomator2",
        "appium:appPackage": "com.google.android.calculator",
        "appium:appActivity": "com.android.calculator2.Calculator"
    }

    def initiate_Driver(self):

        try:
            global driver
            # driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error: Appium Server not working...")

    def calculator_addition(self):

        try:
            #validate launch screen image
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_3").click()
            time.sleep(2)
            #click on skip button
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_5").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()
            time.sleep(2)
            result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text

            if int(result) == 8:
                print("the result is as expected: ",result)

            time.sleep(5)

    
        except:
            print("kubernetes logo is not present")


    def close_driver(self):
        driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)


obj = DockerApp()
obj.initiate_Driver()
obj.calculator_addition()
obj.close_driver()