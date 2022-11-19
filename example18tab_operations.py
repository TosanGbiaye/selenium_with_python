# Perform tab operations on all the links on bing.com
# will revisit this topic using another video

import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com")
driver.maximize_window()

p1 = driver.find_elements(By.TAG_NAME, 'a')


print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
        #p1[element].send_keys(keys.TAB)




time.sleep(5)
driver.quit()