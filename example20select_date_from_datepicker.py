# 4: 40-46
# How to select date from a datepicker or calendar:
# 1. click on the text field 2. select a date 3 use the send key 4.copy n paste the date

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
driver.find_element(By.ID, 'datepicker').send_keys("11/03/2022")


time.sleep(3)
driver.quit()