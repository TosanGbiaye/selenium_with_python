import time
from selenium.webdriver.common.by import  By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com/account/general")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='enAS']").click()
time.sleep(5)
driver.quit()