from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time


class DockerApp:

    cap = {
        "deviceName" : "Samsung",
        "platformName" : "Android",
        "automationName" : "UiAutomator2",
        "udid" : "emulator-5554", #mandatory when multiple devices are connected
        "browserName" : "chrome", # not mandatory for mobile automation
        "app" : ""
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

    def Validate_Launch_Screen(self):

        try:
            #validate launch screen image
            if driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.naukri.recruiterapp:id/iv_logo']").is_displayed():
                print("Launch Screen Image is present")

                #click on skip button
                driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.naukri.recruiterapp:id/tv_skip']").click()
                time.sleep(5)
                print("User clicked on SKIP button")

                #Enter email and password
                driver.find_element(AppiumBy.XPATH, "com.naukri.recruiterapp:id/edt_email_id").send_keys("test@email.com")
                driver.find_element(AppiumBy.XPATH, "com.naukri.recruiterapp:id/edt_password").send_keys("password1")
                print("User has entered id/pw")

                time.sleep(20)

    
        except:
            print("kubernetes logo is not present")

    def close_driver(self):
        driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)


obj = DockerApp()
obj.initiate_Driver()
obj.Validate_Launch_Screen()
obj.close_driver()