#2 in webdriver we have a select class that we can use to select value from the dropdown

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())
driver.get("https://www.bing.com/account/general")
driver.maximize_window()

dd= driver.find_element(By.ID, 'rpp')
# dd means it is a dropdown information itself

s = Select(dd)
#s.select_by_index(2)
# if we want to select the first value from the dropdown then we need to input index as 0
#s.select_by_value("50")
# for select by value put the value in a string
s.select_by_visible_text("Auto")

p1 = s.options
print(p1)
#options captures all the values in the dropdown
for element in p1:
    p2 = element.get_attribute("value")
    print(p2)
# get attribute is a command that captures attributes of an object

time.sleep(5)
driver.quit()