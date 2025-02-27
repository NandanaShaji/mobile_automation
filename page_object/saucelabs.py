from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
import pytest

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput



def scroll(driver):
    # global driver
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(571, 1982)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(571, 629)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(2)

def username():
    return "//android.widget.EditText[@content-desc='test-Username']"

def password():
    return "//android.widget.EditText[@content-desc='test-Password']"

def login():
    return '//android.widget.TextView[@text="LOGIN"]'

def pdt_count():
    return "//android.widget.TextView[@content-desc='test-Item title']"

def pdt_name(i):
    return "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]"

def pdt1():
    return "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]"

def pdt2():
    return  "//android.view.ViewGroup[@content-desc='test-ADD TO CART']"

def cart():
    return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"

def remove():
    return "//android.view.ViewGroup[@content-desc='test-REMOVE']"

def checkout():
    return "test-CHECKOUT"

def first_name():
    return "test-First Name"

def last_name():
    return "test-Last Name"

def pin():
    return "test-Zip/Postal Code"

def continue_button():
    return "test-CONTINUE"

def finish():
    return "test-FINISH"