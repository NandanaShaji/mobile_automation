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

        driver.get("https://kubernetes.io/")
        time.sleep(15)

    def docker_logo_validation(self):

        try:
            if driver.find_element(AppiumBy.XPATH, "//a[@class='navbar-brand img-fluid']").is_displayed():
                print("kubernetes logo is present")
            driver.find_element(AppiumBy.XPATH, "//button[@id='hamburger']").click()
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, "(//a[text()='Training'])[2]").click()
            time.sleep(2)
        except:
            print("kubernetes logo is not present")

    def close_driver(self):
        driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)


obj = DockerApp()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.docker_logo_validation()
obj.close_driver()