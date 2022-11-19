# Scenerio: How to handle dropdowns:
# 1. Use send_keys command and see if we can change the value of the dropdown or not.
# a. Open the App browser and Identify the dropdown property
# use a sendkeys command as an input to send a value which is existing in the dropdown
#2 in webdriver we have a select class that we can use to select value from the dropdown

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com/account/general")
driver.maximize_window()

driver.find_element(By.ID, 'rpp').send_keys("10")

time.sleep(5)
driver.quit()