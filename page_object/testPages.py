import unittest
from selenium import webdriver
from pages import *
from testCases import test_cases
from settings import Settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #self.driver = webdriver.Firefox()
        self.driver.get(Settings.baseUrl)
        self.driver.implicitly_wait(30)

    def test_page_load(self):
        print "\n" + str(test_cases(0))
        page = LoginPage(self.driver)
        time.sleep(10)
        self.assertTrue(page.check_page_loaded())

    def test_login(self):
        print "\n" + str(test_cases(1))
        page = LoginPage(self.driver)
        time.sleep(15)
        result = page.login()
        time.sleep(15)
        # result = page.click_sign_in_button()
        # page.open()
        #result = page.login_with_valid_user("valid_user")
        #result = page.login_with_valid_user()
        self.assertTrue(Locators.BUTTON_EXIT, result)

    # def test_search_item(self):
        # print "\n" + str(test_cases(1))
        # page = LoginPage(self.driver)
        # search_result = page.search_item("Nexus 5")
        # self.assertIn("Nexus 5", search_result)

    # def test_sign_up_button(self):
        #print "\n" + str(test_cases(2))
        #page = LoginPage(self.driver)
        #signUpPage = page.click_sign_up_button()
        #self.assertIn("ap/register", signUpPage.get_url())

    #def test_sign_in_button(self):
        #print "\n" + str(test_cases(3))
        #page = LoginPage(self.driver)
        #page.click_sign_in_button()
        #self.assertIn("testteamdev", page.get_url())

    #def test_sign_in_with_valid_user(self):
        #print "\n" + str(test_cases(4))
        #page = LoginPage(self.driver)
        #result = page.login_with_valid_user("valid_user")
        #self.assertIn("testteamdev", result.get_url())

    #def test_sign_in_with_in_valid_user(self):
        #print "\n" + str(test_cases(5))
        #page = LoginPage(self.driver)
        #result = page.login_with_in_valid_user("invalid_user")
        #self.assertIn("testteamdev", result.get_url())

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)

