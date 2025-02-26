import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest



@pytest.fixture(scope="function")
def launch_app(request):
    try:
        cap = {
        "deviceName" : "Samsung",
        "platformName" : "Android",
        "automationName" : "UiAutomator2",
        "app" : ""
    }
        print("initiating app instance driver")
        driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
        request.instance.driver = driver

        yield driver

        driver.quit()
    except:
        print("unable to launch the app")