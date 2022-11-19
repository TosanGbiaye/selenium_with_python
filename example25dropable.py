# perform drag and drop when you know the source and the destination(droppable)
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
time.sleep(3)
driver.switch_to.frame(fr)

src = driver.find_element(By.ID, "draggable")
dest = driver.find_element(By.ID, "droppable")

ActionChains(driver).drag_and_drop(src,dest).perform()

time.sleep(3)
driver.quit()