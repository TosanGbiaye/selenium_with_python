# multiple window handling : 5: 55-58
# Login to salesforce application>>click on create>>select user which is 1st option on the list>>
# in the user creation window select maqnifying icon >which opens a new window
# >>enter a value into the search field>>click on the search button

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.maximize_window()
driver.get("https://login.salesforce.com/")
driver.find_element(By.ID, "username").send_keys("hello@gmail.com")
driver.find_element(By.XPATH, "//input[@class='input r4 wide mb16 mt8 password']").send_keys("password")
driver.find_element(By.XPATH, "//input[@class='button r4 wide primary']").click()

time.sleep(5)
driver.quit()

