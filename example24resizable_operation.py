# scenerio: perform resizable operation 5;12-14
#
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://jqueryui.com/resizable/")
driver.maximize_window()

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
time.sleep(3)
driver.switch_to.frame(fr)
obj = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-e']")

ActionChains(driver).drag_and_drop_by_offset(obj,100,80).perform()

time.sleep(3)
driver.quit()