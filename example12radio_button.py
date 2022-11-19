# Handling radio button: Open the app > identify the desired object property > use click command to change the status
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com/account/general")
driver.maximize_window()

driver.find_element(By.ID, "adlt_set_strict").click()
p1 = driver.find_element(By.ID, "adlt_set_strict").is_selected()
print(p1)
#we use is_selected command to know the status of the checkbox or radio button

time.sleep(5)
driver.quit()