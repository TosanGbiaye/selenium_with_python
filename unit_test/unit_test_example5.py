import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # will write logic to launch the browser and open the application and also maximize the browser
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("https://login.salesforce.com/")
        cls.driver.maximize_window()



    def test_login(self):
        # In this test i want to create a logic that will login to the app.
        # i.e , enter username, password and click on the login button
        self.driver.find_element(By.ID, "username").send_keys("tosangbiaye@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Salesforce@10")
        self.driver.find_element(By.ID, "Login").click()
        time.sleep(35)

    def test_createAccount(self):
        # click on create , click on user then username
        self.driver.find_element(By.XPATH, "//a[@title='Create Menu']").click()
        self.driver.find_element(By.XPATH, "(//span[@class='slds-align-middle'])[1]").click()
        frame1 = self.driver.find_element(By.XPATH, "//iframe[@title='New User ~ Salesforce - Developer Edition']")
        self.driver.switch_to.frame(frame1)
        self.driver.find_element(By.ID, "name_firstName").send_keys("tosan")

    @classmethod
    def tearDownClass(cls):
        # will write logic to wait for sometime and terminate the browser
        time.sleep(5)
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
