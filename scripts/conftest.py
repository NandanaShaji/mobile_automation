import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions





@pytest.fixture(scope="class")
def launch_app(request):
    try:
        cap = {
        "appium:deviceName": "Samsung",
        "appium:platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "C:\\Users\\2022413\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
        "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity",
        "chromedriverExecutable" : "C:\\Users\\2022413\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    }
        print("initiating app instance driver")
        driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
        request.cls.driver = driver

        yield driver

        driver.quit()
    except:
        print("unable to launch the app")



@pytest.fixture
def read_json():
    with open("C:\\Users\\2022413\\html_programs\\testdata\input.json") as config_file:
        data = json.load(config_file)
    return data