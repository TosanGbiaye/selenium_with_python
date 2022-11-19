# Locators : it is the heart of any automation testing
# xpath syntax is    //html tagname[@property type='property value']
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://www.bing.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='sb_form_q']").send_keys("Tosan gbiaye")
driver.find_element(By.XPATH, "//label[@id='search_icon']").click()
time.sleep(3)
driver.quit()   # quit command terminates the browser and release the memory
# to confirm your xpath on the console : $x("xpath") example: $x("//label[@id='search_icon']")
# click() is used to perform operstions on any button or link or image  or check box, radio
# if we are not writing a command to close the browser our system will experience memory issue over time which will reduce the speed of our system
