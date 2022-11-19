# Clicking on Checkbox
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com/account/general")
driver.maximize_window()
p1 = driver.find_element(By.ID, 'enAS').is_selected()
print(p1)

if p1:
    print("already checked")

else:
    driver.find_element(By.ID, 'enAS').click()
    print("successfully checked")
time.sleep(5)
driver.quit()