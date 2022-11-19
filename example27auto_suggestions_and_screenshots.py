# How to handle auto suggestions and screenshot 5: 30-32

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com")
driver.maximize_window()

driver.find_element(By.ID, 'sb_form_q').send_keys("suren")
time.sleep(5)
p1 = driver.find_elements(By.XPATH, "//li[@class='sa_sg']")

# the below line will print the total no of values in the list
print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

#To capture screenshot we need to specify the file location we want the screenshot to be saved
driver.get_screenshot_as_file("C:/Users/hp/PycharmProjects/selenium_with_python/example27.png")


time.sleep(5)
driver.quit()