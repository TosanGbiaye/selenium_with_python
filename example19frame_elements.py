# 4:30
# https://jqueryui.com/
# selenium.common.exceptions.NoSuchElementException: Message: no such element:
# Unable to locate element: {"method":"css selector","selector":"[id="datepicker"]"}
# Getting this error message when you input the correct element means that the desired object might be sitting on a frame
# To confirm whether the desired object is sitting on a frame, trace its parent up to the html tag.
# if it has frame or iframe then it is sitting on a frame. if it is sitting on a frame then we need to
#use switch-to.frame() concept in webdriver.

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

driver.switch_to.default_content()
# To switch back to the original html content of the webpage

time.sleep(5)
driver.quit()