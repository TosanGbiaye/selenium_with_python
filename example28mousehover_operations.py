# How to handle mousehover and click operations 5:34 - 6:19
# open the browser> inspect manage menu (Accept cookies prevented the code from running)

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.maximize_window()
driver.get("https://www.emirates.com/in/english/")
#the below code is to accept cookies
driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()

#driver.implicitly_wait(30)

driver.find_element(By.XPATH, "//a[@data-link='MANAGE']").click()

obj = driver.find_element(By.XPATH, "(//a[@class='thirdlevel-title'])[2]")
ActionChains(driver).move_to_element(obj).perform()
#move_to_element is a command that will move the cusor to a specific object

driver.find_element(By.XPATH, "(//i[@class='thirdlevel__menu-link'])[11]").click()

time.sleep(5)
driver.quit()

