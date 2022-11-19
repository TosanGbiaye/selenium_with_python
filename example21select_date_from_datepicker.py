# How to select date from a datepicker or calendar: 4:46-48
# 1. use the click command 2. click on a date and inspect, you will notice that the dates starts with tagname as <a
# for any element starting with tagname "a" we can perform click operation
# locating the element by LINK-TEXT
# to select next month date inspect the next month forward arrow, create a relative xpath

import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(fr)
driver.find_element(By.ID, 'datepicker').click()

#driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  #next month date

driver.find_element(By.LINK_TEXT, "7").click()


time.sleep(3)
driver.quit()