import unittest
from selenium import webdriver
from pages import *
from locators import Locators
from testCases import test_cases
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from base import Page

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

    # def test_page_load(self):
    #     print "\n" + str(test_cases(0))
    #     page = LoginPage(self.driver)
    #     self.assertTrue(page.check_login_page_loaded())
    #
    # def test_login(self):
    #     print "\n" + str(test_cases(1))
    #     login_page = LoginPage(self.driver)
    #     login_page.enter_username()
    #     login_page.enter_password()
    #     home_page = login_page.click_sign_in_button()
    #     self.assertTrue(home_page.check_home_page_loaded())
    #
    # def test_open_global_site_view(self):
    #     print "\n" + str(test_cases(2))
    #     page = LoginPage(self.driver)
    #     home_page = page.login()
    #     devices_page = home_page.click_devices_menu_button()
    #     self.assertTrue(devices_page.click_global_site_view_site())
    #
    # def test_open_site_name_popup(self):
    #     print "\n" + str(test_cases(3))
    #     login_page = LoginPage(self.driver)
    #     home_page = login_page.login()
    #     devices_page = home_page.click_devices_menu_button()
    #     devices_page.click_global_site_view_site()
    #     self.assertTrue(devices_page.click_new_site_button())

    def test_create_and_delete_new_site(self):
        print "\n" + str(test_cases(4))
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        self.assertTrue(home_page.check_home_page_loaded())
        devices_page = home_page.click_devices_menu_button()
        self.assertTrue(devices_page.check_devices_page_loaded())
        devices_page.delete_site_if_exists()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name()
        self.assertTrue(devices_page.click_site_name_popup_OK_button())
        self.assertTrue(devices_page.check_site_is_created())
        devices_page.click_site_in_global_site_view()
        devices_page.click_delete_button()
        self.assertFalse(devices_page.click_Are_you_sure_Ok_button())


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)