import unittest
from selenium import webdriver
from pages import *
from locators import Locators
from testTitles import test_title
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class TestCases(unittest.TestCase):

    def setUp(self):
        # pass
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(Settings.baseUrl)
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, Locators.BUTTON_SIGN_IN)))
        self.driver.implicitly_wait(1)

    def test_page_load(self):
        print ("\n" + str(test_title(0)))
        page = LoginPage(self.driver)
        self.assertTrue(page.check_login_page_loaded())
        print ("Test is passed")

    def test_login(self):
        print ("\n" + str(test_title(1)))
        login_page = LoginPage(self.driver)
        login_page.enter_username()
        login_page.enter_password()
        home_page = login_page.click_sign_in_button()
        self.assertTrue(home_page.check_home_page_loaded())
        print ("Test is passed")

    def test_open_site_name_popup(self):
        print ("\n" + str(test_title(2)))
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + str(test_title(3)))
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.delete_site_if_exists()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name()
        devices_page.click_site_name_popup_OK_button()
        self.assertTrue(devices_page.check_if_site_is_in_gsv())
        '''post-conditions'''
        devices_page.delete_site_from_gsv()
        print ("Test is passed")

    def test_cancel_creating_site(self):
        print ("\n" + str(test_title(4)))
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.click_site_name_popup_cancel_button()
        self.assertTrue(devices_page.is_element_not_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + str(test_title(5)))
        site_name = "Default Site"
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(site_name)
        devices_page.click_site_name_popup_OK_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
        '''post-conditions'''
        devices_page.click_error_popup_Ok_button()
        devices_page.click_site_name_popup_system_button_close()
        print ("Test is passed")

    def test_create_site_with_fifty_one_symbol(self):
        print ("\n" + str(test_title(6)))
        site_name_max = "51symbols51symbols51symbols51symbols51symbols<o&k>"
        site_name_fifty_one_symbols = site_name_max + "1"
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.delete_site_if_exists(site_name_max)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(site_name_fifty_one_symbols)
        devices_page.click_site_name_popup_OK_button()
        self.assertFalse(devices_page.check_if_site_is_in_gsv(site_name_fifty_one_symbols))
        self.assertTrue(devices_page.check_if_site_is_in_gsv(site_name_max))
        '''post-conditions'''
        devices_page.delete_site_from_gsv(site_name_max)
        print ("Test is passed")

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite)