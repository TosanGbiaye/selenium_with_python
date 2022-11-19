# scenerio: capture coordinates for draggable objects
# getAttributes is used to get specific property of an object

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
# the below command will capture the height and width of the object
s = obj.size
#below command will capture the x and y coordinates of the object
l = obj.location
print(obj.get_attribute("style"))

print(s)
print(l)


time.sleep(3)
driver.quit()