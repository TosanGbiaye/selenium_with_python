#

from PageObjectModelOne.Pages.LoginPage import LoginPageProp
from PageObjectModelOne.Pages.HomePage import HomePageProp
from PageObjectModelOne.Pages.CreateUserPage import CreateUserPageProp
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
        login_prop = LoginPageProp()
        # In this test i want to create a logic that will login to the app.
        # i.e , enter username, password and click on the login button
        self.driver.find_element(By.ID, login_prop.username_textfield_id).send_keys("tosangbiaye@gmail.com")
        self.driver.find_element(By.ID, login_prop.password_textfield_id).send_keys("Salesforce@10")
        self.driver.find_element(By.ID, login_prop.login_button_id).click()
        time.sleep(35)

    def test_createAccount(self):
        homepage = HomePageProp()
        # click on create , click on user then username
        self.driver.find_element(By.XPATH, homepage.create_button_xpath).click()
        self.driver.find_element(By.XPATH, homepage.create_user_xpath).click()
        time.sleep(8)

        create_user = CreateUserPageProp
        frame1 = self.driver.find_element(By.XPATH, create_user.create_user_new_frame_xpath)
        self.driver.switch_to.frame(frame1)
        self.driver.find_element(By.ID, create_user.firstname_id).send_keys("tosan")

    @classmethod
    def tearDownClass(cls):
        # will write logic to wait for sometime and terminate the browser
        time.sleep(5)
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()