import unittest
from selenium import webdriver
from pages import *
from locators import Locators
from testTitles import test_title
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging


class TestsSiteCreation(unittest.TestCase):

    print ("\n" + "Test suite: Site creation (Suite ID: 9111)")

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(Settings.baseUrl)
        WebDriverWait(cls.driver, 120).until(EC.presence_of_element_located((By.XPATH, Locators.BUTTON_SIGN_IN)))
        login_page = LoginPage(cls.driver)
        login_page.login()
        home_page = HomePage(cls.driver)
        home_page.close_popups()
        devices_page = home_page.open_devices_menu()
        devices_page.check_devices_page_loaded()

    # def setUp(self):
    #     home_page = HomePage(self.driver)
    #     home_page.close_popups()
    #     devices_page = home_page.open_devices_menu()
    #     devices_page.check_devices_page_loaded()

    def test_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name")
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(Variables.site_name)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.site_name)
        devices_page.click_site_name_popup_ok_button()
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.site_name))
        '''Post-conditions'''
        devices_page.delete_site_from_gsv(Variables.site_name)
        print ("Test is passed")

    def test_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.click_site_name_popup_cancel_button()
        self.assertTrue(devices_page.is_element_not_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.default_site_name)
        devices_page.click_site_name_popup_ok_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
        '''Post-conditions'''
        devices_page.click_error_popup_ok_button()
        devices_page.click_site_name_popup_system_button_close()
        print ("Test is passed")

    def test_create_site_with_fifty_one_symbols(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(Variables.fifty_symbols_name)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.fifty_one_symbols_name)
        devices_page.click_site_name_popup_ok_button()
        self.assertFalse(devices_page.check_if_site_is_in_gsv(Variables.fifty_one_symbols_name))
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.fifty_symbols_name))
        '''Post-conditions'''
        devices_page.delete_site_from_gsv(Variables.fifty_symbols_name)
        print ("Test is passed")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(Variables.parent_site_name)
        devices_page.create_parent_site(Variables.parent_site_name)
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.parent_site_name))
        devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_1_name)
        self.assertTrue(devices_page.check_if_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_1_name))
        devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_2_name)
        self.assertTrue(devices_page.check_if_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_2_name))
        '''Post-conditions'''
        devices_page.delete_site_from_gsv(Variables.parent_site_name)
        print ("Test is passed")

    # def tearDown(self):
    #     page = HomePage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())