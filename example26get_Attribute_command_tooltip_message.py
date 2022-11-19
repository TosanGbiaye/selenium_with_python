#tooltip message: 5:19-21
# Whenever we are working on any ecommerce application , usually the price information will
# be stored in the value or title property.inorder to capture the stored info we use get_Atrribute command
# whenever we mouse over a browser some message is displayed which is called tooltip message
# get_Attribute is used to get specific property of an object

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://jqueryui.com/tooltip/")
driver.maximize_window()

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
time.sleep(3)
driver.switch_to.frame(fr)
obj = driver.find_element(By.ID, "age")
p1 = obj.get_attribute("title")
print("tooltip message is: ", p1)





time.sleep(3)
driver.quit()