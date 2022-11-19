# 6:19 - 6:37
# get the row names in the Tag name column
#steps: 1. identify the xpath of the first 3 objects and see if there is any similarity btw all of them

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/default.asp")
time.sleep(2)
driver.close()