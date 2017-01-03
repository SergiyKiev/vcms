import unittest
from selenium import webdriver
from pages import *
from locators import Locators
from testTitles import test_title
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(Settings.baseUrl)
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, Locators.BUTTON_SIGN_IN)))
        # self.driver.implicitly_wait(1)

    def test_01_instance_is_loaded(self):
        print ("\n" + "TC#0001. Open the instance")
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.check_login_page_loaded())
        print ("Test is passed")

    def test_02_login(self):
        print ("\n" + "TC#9056. Login to the console")
        login_page = LoginPage(self.driver)
        login_page.enter_username()
        login_page.enter_password()
        home_page = login_page.click_sign_in_button()
        self.assertTrue(home_page.check_home_page_loaded())
        print ("Test is passed")

    def test_03_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup")
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed")

    def test_04_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name")
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.close_popups()
        devices_page = home_page.open_devices_menu()
        devices_page.delete_site_if_exists(Variables.site_name)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.site_name)
        devices_page.click_site_name_popup_OK_button()
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.site_name))
        '''Post-conditions'''
        devices_page.delete_site_from_gsv(Variables.site_name)
        print ("Test is passed")

    def test_05_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field")
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.close_popups()
        devices_page = home_page.open_devices_menu()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.click_site_name_popup_cancel_button()
        self.assertTrue(devices_page.is_element_not_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed")

    def test_06_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name")
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.close_popups()
        devices_page = home_page.open_devices_menu()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.default_site_name)
        devices_page.click_site_name_popup_OK_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
        '''Post-conditions'''
        devices_page.click_error_popup_Ok_button()
        devices_page.click_site_name_popup_system_button_close()
        print ("Test is passed")

    def test_07_create_site_with_fifty_one_symbol(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.close_popups()
        devices_page = home_page.open_devices_menu()
        devices_page.delete_site_if_exists(Variables.fifty_symbols_name)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.fifty_one_symbols_name)
        devices_page.click_site_name_popup_OK_button()
        self.assertFalse(devices_page.check_if_site_is_in_gsv(Variables.fifty_one_symbols_name))
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.fifty_symbols_name))
        '''Post-conditions'''
        devices_page.delete_site_from_gsv(Variables.fifty_symbols_name)
        print ("Test is passed")

    def test_08_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.close_popups()
        devices_page = home_page.open_devices_menu()
        devices_page.delete_site_if_exists(Variables.parent_site_name)
        '''Test body'''
        devices_page.create_parent_site(Variables.parent_site_name)
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.parent_site_name))
        devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_1_name)
        self.assertTrue(devices_page.check_if_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_1_name))
        devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_2_name)
        self.assertTrue(devices_page.check_if_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_2_name))
        '''Post-conditions'''
        devices_page.delete_site_from_gsv(Variables.parent_site_name)
        print ("Test is passed")

    def tearDown(self):
        # time.sleep(1)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())