from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time



class TestPlaywright_NS:


    def launch_playwright_NS(self):

        #launch playwright
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://playwright.dev/")
        time.sleep(5)


    def validate_logo_headerMenuOptions_NS(self):

        #validating if the logo is present in the header
        logo = driver.find_element(By.XPATH, "//a[@class='navbar__brand']")
        if logo.is_displayed():
            print("logo is present in the header")


        #validating 4 header menu options
        count = len(driver.find_elements(By.XPATH, "//a[@class='navbar__item navbar__link']"))

        for i in range(1, count+1):
            xpath = "(//a[@class='navbar__item navbar__link'])["+str(i)+"]"
            item = driver.find_element(By.XPATH, xpath).text
            print("\'",item,"\' is present in the header")

        global nodejs
        nodejs = driver.find_element(By.XPATH, "(//a[text()='Node.js'])[1]")
        if nodejs.is_displayed():
            print("\'", nodejs.text, "\' dropdown is present in the header")


    def validate_nodeJS_NS(self):

        # hover to node.js
        hover = ActionChains(driver).move_to_element(nodejs)
        hover.perform()
        time.sleep(3)

        #selecting 'python' from the dropdown
        python_dropdown = driver.find_element(By.XPATH, "(//a[text()='Python'])[1]")
        python_dropdown.click()
        time.sleep(3)


    def validate_python_NS(self):

        #validating if the dropdown text has changed to 'python'
        python_header = driver.find_element(By.XPATH, "(//a[text()='Python'])[1]")
        if python_header.is_displayed():
            print("dropdown text changed to \'", python_header.text, "\'")


    def validate_getStarted_NS(self):

        #clicking on 'get started' button
        get_started = driver.find_element(By.XPATH, "//a[text()='Get started']")
        get_started.click()
        time.sleep(5)

        #clicking on back button
        driver.back()
        time.sleep(5)


    def validate_companyLogos_NS(self):

        #Scroll down to Chosen by companies and open source projects section
        companies = driver.find_element(By.XPATH, "//h2[text()='Chosen by companies and open source projects']")
        actions = ActionChains(driver) # creating an object of action class
        actions.move_to_element(companies).perform()
        time.sleep(5)

        #printing the list of 9 companies
        company = driver.find_elements(By.XPATH,"//ul[@class='logosList_zAAF']/li/a/img")
        count = len(company)
        print("total no. of companies =", count)

        for i in company:
            name = i.get_attribute("alt")
            print(name)


    def validate_gitHub_NS(self):

        #scrolling to github
        github = driver.find_element(By.XPATH, "//a[@aria-label='GitHub repository']")
        actions = ActionChains(driver) # creating an object of action class
        actions.move_to_element(github).perform()
        time.sleep(5)

        # Store the ID of the original window
        original_window = driver.current_window_handle # mandatory
        # Check we don't have other windows open already
        assert len(driver.window_handles) == 1 # not mandatory
        github.click()
        time.sleep(5)

        # this time, the total window count will be 2; one for 'playwright', and another for 'github'
        total_windows = driver.window_handles # list of objects
        assert len(total_windows) == 2
        # Loop through until we find a new window handle
        for current_window in total_windows:
            if current_window != original_window:
                driver.switch_to.window(current_window)
                get_github_url = driver.current_url
                get_github_title = driver.title
                print(get_github_url)
                print(get_github_title)

                #checking if 'playwright' is present in the github url
                if 'playwright' in get_github_url:
                    print("\'playwright\' is present in twitter url")
                driver.close()
                time.sleep(5)

        driver.switch_to.window(original_window)
        get_playwright_url = driver.current_url
        get_playwright_title = driver.title
        print(get_playwright_url)
        print(get_playwright_title)


    def printLinks_NS(self):

        #printing all links
        link_count = len(driver.find_elements(By.XPATH, "//a"))

        for i in range(1, link_count + 1):
            link_name = driver.find_element(By.XPATH, "(//a)[" + str(i) + "]").text
            print(link_name)


 


obj = TestPlaywright_NS()
obj.launch_playwright_NS()
obj.validate_logo_headerMenuOptions_NS()
obj.validate_nodeJS_NS()
obj.validate_python_NS()
obj.validate_getStarted_NS()
obj.validate_companyLogos_NS()
obj.validate_gitHub_NS()
obj.printLinks_NS()