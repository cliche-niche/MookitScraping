from selenium import webdriver
import time

'''
This file first logs-in to helloiitk, thengoes to the page of the course provided, loads
all of the rendered content on the page and saves it in the "page.html" file.

Further this file in itself can be used to make the csv file too by making a soup
at the end and following the exact same procedure as in "scrape.py".
'''


#Operating in headless mode.
settings = webdriver.chrome.options.Options()
settings.add_argument("--headless")
driver = webdriver.Chrome(options=settings)

#I used my own credentials to download the page.
driver.get("https://hello.iitk.ac.in/index.php/user/login")
time.sleep(2)

username = driver.find_element_by_name("name")
username.clear()
username.send_keys("<USERNAME>") #Replace this with your username.

password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("<PASSWORD>") #Replace this with your password.

driver.find_element_by_name("op").click()
time.sleep(2)


#Accessing the course page.
course = None #You may replace this with a different course name.
url = "https://hello.iitk.ac.in/esc201a21/#/home"
if course is not None: 
    url="https://hello.iitk.ac.in/"+course+"/#/home"

driver.get(url)
time.sleep(2)
htmlSource = driver.page_source
driver.quit()

with open("page.html", 'w', encoding='utf-8') as f:
    print(htmlSource, file=f) #Saving content of the page.