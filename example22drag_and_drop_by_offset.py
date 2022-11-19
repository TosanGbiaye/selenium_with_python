# scenerio: handle drag and drop
#when you know the source of the object you want to drag but don't know
# the destination you want to drop ,you can use the drag_and_drop_by_offset command with ActionChains
# Perform method performs the operation on the browser.
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://jqueryui.com/draggable/")
driver.maximize_window()

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
time.sleep(3)
driver.switch_to.frame(fr)
obj = driver.find_element(By.ID, "draggable")

ActionChains(driver).drag_and_drop_by_offset(obj,50,50).perform()

time.sleep(3)
driver.quit()