import unittest
from selenium import webdriver
from pages import *
from locators import Locators
from testCases import test_cases
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>


class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver = webdriver.Firefox()
        self.driver.get(Settings.baseUrl)
        # self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, Locators.BUTTON_SIGN_IN)))
        self.driver.implicitly_wait(5)

    def test_page_load(self):
        print "\n" + str(test_cases(0))
        page = LoginPage(self.driver)
        self.assertTrue(page.check_login_page_loaded())

    def test_login(self):
        print "\n" + str(test_cases(1))
        login_page = LoginPage(self.driver)
        login_page.enter_username()
        login_page.enter_password()
        home_page = login_page.click_sign_in_button()
        self.assertTrue(home_page.check_home_page_loaded())

    def test_open_global_site_view(self):
        print "\n" + str(test_cases(2))
        page = LoginPage(self.driver)
        home_page = page.login()
        devices_page = home_page.click_devices_menu_button()
        self.assertTrue(devices_page.click_global_site_view_site())

    def test_open_site_name_popup(self):
        print "\n" + str(test_cases(3))
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        devices_page = home_page.click_devices_menu_button()
        devices_page.click_global_site_view_site()
        self.assertTrue(devices_page.click_new_site_button())

    def test_create_new_site(self):
        print "\n" + str(test_cases(4))
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        devices_page = home_page.click_devices_menu_button()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name()
        result = devices_page.click_site_name_OK_button()
        self.assertTrue(self.driver.find_element_by_xpath(Locators.TREE_GLOBAL_SITE_VIEW + "/*" +
                                                          Locators.SITE_SITE_NAME), result)
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
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run()