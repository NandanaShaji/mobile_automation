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
        "version" : "9.0", #not mandatory
        "udid" : "emulator-5554", #mandatory when multiple devices are connected
        "browserName" : "chrome", #mandatory for web automation
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

    def launch_Appium_Driver(self):

        driver.get("https://www.quest-global.com/")
        time.sleep(5)

    def hamburger_validation(self):

        try:
            if driver.find_element(AppiumBy.XPATH, "//span[@class='navbar-toggler-icon']").is_displayed():
                print("hamburger button is present")

            driver.find_element(AppiumBy.XPATH, "//span[@class='navbar-toggler-icon']").click()
            count = len(driver.find_elements(AppiumBy.XPATH, "//ul[@class='navbar-nav ms-auto']/li"))
            for i in range(1,count+1):
                item = driver.find_element(AppiumBy.XPATH, "(//ul[@class='navbar-nav ms-auto']/li/a)["+str(i)+"]").text
                print(item)

            
                
        except:
            print("hamburger button is not present")

    def close_driver(self):
        driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)


obj = DockerApp()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.hamburger_validation()
obj.close_driver()