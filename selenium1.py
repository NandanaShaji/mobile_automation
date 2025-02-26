from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time





#launch playwright
global driver
#driver = webdriver.Edge()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-dev-shm-usage")
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()
driver.get("https://www.docker.com/")
time.sleep(5)

# Find all link elements
links = driver.find_elements(By.TAG_NAME, 'a')

# Iterate over link elements
for link in links:
    print(link.get_attribute('href'))

