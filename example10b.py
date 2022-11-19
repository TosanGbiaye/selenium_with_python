import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

def main():
    driver = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://login.salesforce.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("sandra")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
    driver.find_element(By.XPATH, "//input[@id='Login']").click()
    time.sleep(4)
    driver.quit()

main()




