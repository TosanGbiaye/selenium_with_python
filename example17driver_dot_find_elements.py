# salesforce account signup page>> capture the values of the dropdown roles

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://developer.salesforce.com/signup")
driver.maximize_window()

obj = driver.find_element(By.XPATH, "//main[@id='maincontent']/div/section[2]/div/dw-de-signup-form")
p1 = obj.find_elements(By.TAG_NAME, "option")

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)


time.sleep(5)
driver.quit()