from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 

file_html = open("C:\\Users\\2022413\\Downloads\\links.html","w")

tableHeader = '''
<!DOCTYPE html>
        <head>
            <title>Page Title</title>
        </head>
        <body>

        <style>
        table, th, td {
        border:1px solid black;
        }
        </style>

        <table>
        <tr>
            <th>Sl.No.</th>
            <th>Link Name</th>
            <th>Link href</th>
        </tr>
    
'''
 


driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.zomato.com/")

totalLinks = len(driver.find_elements(By.XPATH, "//a"))

htmlBody = ""

for i in range(1, totalLinks + 1):
    LinkName = driver.find_element(By.XPATH, "(//a)[" + str(i) + "]").text
    hrefvalue = driver.find_element(By.XPATH, "(//a)[" + str(i) + "]").get_attribute("href")
      
    print(LinkName)
    print(hrefvalue)

    data = "<tr><th>"+str(i)+"</th><th>"+str(LinkName)+"</th><th>"+str(hrefvalue)+"</th></tr>"
    htmlBody = htmlBody+data


driver.implicitly_wait(10)
driver.quit()

table_footer = '''

</table>
</body>
</html>

'''

#write the html
file_html.write(tableHeader+htmlBody+table_footer)

#saving the data into the html file
file_html.close()