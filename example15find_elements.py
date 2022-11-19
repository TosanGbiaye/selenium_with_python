#find element identify an object in the browser with the specified property
#find elements identify multiple objects in a browser with the specified property
# if there are no object with that property it won't capture anything
#Scenerio 1: Identify all the objects in bing.com homepage which start with tagname as 'a'
# OR Identify all the links in a browser or webpage because every link in a webpage start with a tagname "a"
#steps: Open the browser> then on your pycharm enter the command driver.findelement by tagname a

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com")
driver.maximize_window()

p1 = driver.find_elements(By.TAG_NAME, 'a')
#whenever we are using findelements the output will be a collection of multiple objects
#so we can use a for loop to print out all the values
#len(list) is the total no of value in the list
#is_displayed checks whether the object is displayed in the browser or not

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)




time.sleep(5)
driver.quit()