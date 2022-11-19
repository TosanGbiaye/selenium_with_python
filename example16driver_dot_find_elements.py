# driver.findElements: will get all the object info from a browser
#Scenerio: get all the option in the dropdown
# 1. bing.com>> inspect Auto>> these are the option values: Auto,10,15,30,50
# 2. all the options in the dropdown are starting with the tagname 'option'
#so we can use webdriver command to find all the options: driver.findElement by tagname "option"
# salesforce account creation page>>role dropdown values

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com/account/general")
driver.maximize_window()

p1 = driver.find_elements(By.TAG_NAME, 'option')

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)




time.sleep(5)
driver.quit()