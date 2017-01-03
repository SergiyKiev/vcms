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
        page = LoginPage(self.driver)
        self.assertTrue(page.check_login_page_loaded())
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
        home_page.check_home_page_loaded()
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
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.delete_site_if_exists(Variables.site_name)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.site_name)
        devices_page.click_site_name_popup_OK_button()
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.site_name))
        '''post-conditions'''
        devices_page.delete_site_from_gsv(Variables.site_name)
        print ("Test is passed")

    def test_05_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field")
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

    def test_06_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name")
        # site_name = "Default Site"
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.site_default_site)
        devices_page.click_site_name_popup_OK_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
        '''post-conditions'''
        devices_page.click_error_popup_Ok_button()
        devices_page.click_site_name_popup_system_button_close()
        print ("Test is passed")

    def test_07_create_site_with_fifty_one_symbol(self):
        print ("\n" + str(test_title(6)))
        login_page = LoginPage(self.driver)
        home_page = login_page.login()
        home_page.check_home_page_loaded()
        home_page.close_popups()
        devices_page = home_page.click_devices_menu_button()
        devices_page.check_devices_page_loaded()
        devices_page.delete_site_if_exists(Variables.site_name_max)
        devices_page.click_global_site_view_site()
        devices_page.click_new_site_button()
        devices_page.enter_site_name(Variables.site_name_fifty_one_symbols)
        devices_page.click_site_name_popup_OK_button()
        self.assertFalse(devices_page.check_if_site_is_in_gsv(Variables.site_name_fifty_one_symbols))
        self.assertTrue(devices_page.check_if_site_is_in_gsv(Variables.site_name_max))
        '''post-conditions'''
        devices_page.delete_site_from_gsv(Variables.site_name_max)
        print ("Test is passed")



    def tearDown(self):
        # time.sleep(1)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())