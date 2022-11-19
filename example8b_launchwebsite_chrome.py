import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.bing.com/account/general")
driver.maximize_window()
time.sleep(4)
driver.quit()