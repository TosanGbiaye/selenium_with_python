import time

from selenium import webdriver
import chromedriver_autoinstaller


def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jumia.com")
    time.sleep(3)
    driver.quit()


main()