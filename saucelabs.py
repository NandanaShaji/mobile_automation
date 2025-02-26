from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput



class DockerApp:

    cap = {
        "appium:deviceName": "Samsung",
        "appium:platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "C:\\Users\\2022413\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
        "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity",
        "chromedriverExecutable" : "C:\\Users\\2022413\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    }

    def scroll(self):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(571, 1982)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(571, 629)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(2)


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

    def hamburger_validation(self):

        try:
            driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='test-Username']").send_keys("standard_user")
            driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='test-Password']").send_keys("secret_sauce")
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="LOGIN"]').click()
            time.sleep(2)

            pdt_count = len(driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='test-Item title']"))
            for i in range(1,pdt_count+1):
                name = driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]").text
                print(name)

            driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]").click()
            time.sleep(5)
            driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-ADD TO CART']").click()
            time.sleep(5)

            driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView").click()
            time.sleep(2)
            count = len(driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-REMOVE']"))
            print("items in cart: ",count)

            self.scroll()

            el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"2\")")
            el8.click()
            el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CHECKOUT")
            el9.click()
            time.sleep(2)

            el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-First Name")
            el10.send_keys("abc")
            time.sleep(2)

            el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Last Name")
            el11.send_keys("def")
            time.sleep(2)

            el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
            el12.send_keys("123456")
            time.sleep(2)

            el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CONTINUE")
            el13.click()
            time.sleep(2)
            
            self.scroll()

            el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-FINISH")
            el14.click()
            time.sleep(2)

         
        except:
            print("cant add item to cart")

    def close_driver(self):
        driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)


obj = DockerApp()
obj.initiate_Driver()
obj.hamburger_validation()
obj.close_driver()