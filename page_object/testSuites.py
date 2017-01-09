import unittest
from selenium import webdriver
from pages import *
from locators import Locators
from testTitles import test_title
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging


class SiteCreation(unittest.TestCase):

    driver = None #global variable

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site creation (Suite ID: 9111)" + "\n")
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
        print ("\n" + "TC#9057. Open Site Name popup" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_main_label()
        devices_page.click_new_site_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_SITE_NAME))
        print ("\n" + "Test is passed" + "\n")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(Variables.site_name)
        devices_page.click_global_site_view_main_label()
        devices_page.click_new_site_button()
        devices_page.enter_text_into_site_name_text_field(Variables.site_name)
        devices_page.click_site_name_popup_ok_button()
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.site_name))
        '''Post-conditions'''
        devices_page.delete_site_from_global_site_view_tree(Variables.site_name)
        print ("\n" + "Test is passed" + "\n")

    def test_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_main_label()
        devices_page.click_new_site_button()
        devices_page.click_site_name_popup_cancel_button()
        self.assertTrue(devices_page.is_element_not_present(Locators.POPUP_SITE_NAME))
        print ("\n" + "Test is passed" + "\n")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_main_label()
        devices_page.click_new_site_button()
        devices_page.enter_text_into_site_name_text_field(Variables.default_site_name)
        devices_page.click_site_name_popup_ok_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
        '''Post-conditions'''
        devices_page.click_error_popup_ok_button()
        devices_page.click_site_name_popup_system_button_close()
        print ("\n" + "Test is passed" + "\n")

    def test_create_site_with_fifty_one_symbols(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(Variables.fifty_symbols_name)
        devices_page.click_global_site_view_main_label()
        devices_page.click_new_site_button()
        devices_page.enter_text_into_site_name_text_field(Variables.fifty_one_symbols_name)
        devices_page.click_site_name_popup_ok_button()
        self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_one_symbols_name))
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_symbols_name))
        '''Post-conditions'''
        devices_page.delete_site_from_global_site_view_tree(Variables.fifty_symbols_name)
        print ("\n" + "Test is passed" + "\n")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(Variables.parent_site_name)
        devices_page.create_new_site(Variables.parent_site_name)
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.parent_site_name))
        time.sleep(5)
        devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_1_name)
        self.assertTrue(devices_page.check_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_1_name))
        time.sleep(5)
        devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_2_name)
        self.assertTrue(devices_page.check_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_2_name))
        '''Post-conditions'''
        devices_page.delete_site_from_global_site_view_tree(Variables.parent_site_name)
        print ("\n" + "Test is passed" + "\n")

    def tearDown(self):
        page = HomePage(self.driver)
        page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration (Suite ID: 9112)" + "\n")
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

    def test_open_configuration_popup(self):
        print ("\n" + "TC#9601. Open 'Configuration' popup" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_main_label()
        devices_page.click_config_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_CONFIGURATION))
        print ("\n" + "Test is passed" + "\n")

    def test_change_site_name_using_configuration_popup(self):
        print ("\n" + "TC#9237. Devices page. Change site name using Configuration popup" + "\n")
        sitename = "Site#9237"
        modifed = "_modifed"
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(sitename)
        devices_page.delete_site_if_exists(sitename + modifed)
        devices_page.create_new_site(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        time.sleep(2)
        devices_page.click_config_button()
        devices_page.enter_text_into_site_tab_name_text_field(modifed)
        devices_page.click_configuration_popup_close_button()
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(sitename + modifed))
        devices_page.delete_site_from_global_site_view_tree(sitename + modifed)
        devices_page.delete_site_if_exists(sitename)
        print ("\n" + "Test is passed" + "\n")

    def test_gui_configuration_popup_from_global_site_view_main_label(self): #gui - graf.user.int.
        print ("\n" + "TC#9228. Devices page. GUI: Configuration popup from the Global Site View main label" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_main_label()
        devices_page.click_config_button()
        self.assertTrue(devices_page.is_element_not_present(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL))
        self.assertTrue(devices_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD))
        print ("\n" + "Test is passed" + "\n")

    def test_gui_configuration_popup_from_default_site_label(self): #gui - graf.user.int.
        print ("\n" + "TC#9229. Devices page. GUI: Configuration popup from the Default Site main label" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_default_site_in_global_site_view_tree()
        devices_page.click_config_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL))
        self.assertTrue(devices_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD))
        devices_page.click_configuration_popup_ip_address_ranges_tab()
        self.assertFalse(devices_page.is_element_visible(Locators.TAB_IP_ADDRESS_RANGES_LIST_VIEW_CONTROL))
        self.assertFalse(devices_page.is_element_visible(Locators.TAB_IP_ADDRESS_RANGES_TOOL_BAR))
        devices_page.click_configuration_popup_close_button()
        print ("\n" + "Test is passed" + "\n")

    def test_gui_configuration_popup_from_created_site_label(self): #gui - graf.user.int.
        print ("\n" + "TC#9230. GUI: Devices page. Configuration popup from the created site" + "\n")
        sitename = "Site#9230"
        devices_page = DevicesPage(self.driver)
        devices_page.create_site_if_not_exists(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_config_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL))
        self.assertFalse(devices_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD))
        devices_page.click_configuration_popup_ip_address_ranges_tab()
        self.assertTrue(devices_page.is_element_visible(Locators.TAB_IP_ADDRESS_RANGES_TOOL_BAR))
        self.assertTrue(devices_page.is_element_visible(Locators.TAB_IP_ADDRESS_RANGES_LIST_VIEW_CONTROL))
        devices_page.click_configuration_popup_close_button()
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("\n" + "Test is passed" + "\n")

    # def test_create_site_with_duplicated_name(self):
    #     print ("\n" + "TC#9107. Create new site with duplicated name")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.click_global_site_view_main_label()
    #     devices_page.click_new_site_button()
    #     devices_page.enter_text_into_site_name_text_field(Variables.default_site_name)
    #     devices_page.click_site_name_popup_ok_button()
    #     self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
    #     '''Post-conditions'''
    #     devices_page.click_error_popup_ok_button()
    #     devices_page.click_site_name_popup_system_button_close()
    #     print ("\n" + "Test is passed" + "\n")
    #
    # def test_create_site_with_fifty_one_symbols(self):
    #     print ("\n" + "TC#9104. Create site with name more than 50 symbols")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.delete_site_if_exists(Variables.fifty_symbols_name)
    #     devices_page.click_global_site_view_main_label()
    #     devices_page.click_new_site_button()
    #     devices_page.enter_text_into_site_name_text_field(Variables.fifty_one_symbols_name)
    #     devices_page.click_site_name_popup_ok_button()
    #     self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_one_symbols_name))
    #     self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_symbols_name))
    #     '''Post-conditions'''
    #     devices_page.delete_site_from_global_site_view_tree(Variables.fifty_symbols_name)
    #     print ("\n" + "Test is passed" + "\n")
    #
    # def test_create_subsites_in_global_site_view_tree(self):
    #     print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.delete_site_if_exists(Variables.parent_site_name)
    #     devices_page.create_new_site(Variables.parent_site_name)
    #     self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.parent_site_name))
    #     devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_1_name)
    #     self.assertTrue(
    #         devices_page.check_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_1_name))
    #     devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_2_name)
    #     self.assertTrue(
    #         devices_page.check_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_2_name))
    #     '''Post-conditions'''
    #     devices_page.delete_site_from_global_site_view_tree(Variables.parent_site_name)
    #     print ("\n" + "Test is passed" + "\n")

    def tearDown(self):
        page = HomePage(self.driver)
        page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteDeletion(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site deletion (Suite ID: 9114)" + "\n")
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

    def test_delete_site_from_global_site_view(self):
        print ("\n" + "TC#9607. Delete created site from Global Site View tree" + "\n")
        sitename = "Test#9607"
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(sitename)
        devices_page.click_global_site_view_main_label()
        devices_page.create_new_site(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_delete_button()
        devices_page.click_are_you_sure_ok_button()
        self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(sitename))
        print ("\n" + "Test is passed" + "\n")

    # def test_create_new_site_with_acceptable_name(self):
    #     print ("\n" + "TC#9101. Create new site with acceptable name")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.delete_site_if_exists(Variables.site_name)
    #     devices_page.click_global_site_view_main_label()
    #     devices_page.click_new_site_button()
    #     devices_page.enter_text_into_site_name_text_field(Variables.site_name)
    #     devices_page.click_site_name_popup_ok_button()
    #     self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.site_name))
    #     '''Post-conditions'''
    #     devices_page.delete_site_from_global_site_view_tree(Variables.site_name)
    #     print ("\n" + "Test is passed" + "\n")
    #
    # def test_cancel_creating_site(self):
    #     print ("\n" + "TC#9058. Cancel creating new site with empty text field")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.click_global_site_view_main_label()
    #     devices_page.click_new_site_button()
    #     devices_page.click_site_name_popup_cancel_button()
    #     self.assertTrue(devices_page.is_element_not_present(Locators.POPUP_SITE_NAME))
    #     print ("\n" + "Test is passed" + "\n")
    #
    # def test_create_site_with_duplicated_name(self):
    #     print ("\n" + "TC#9107. Create new site with duplicated name")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.click_global_site_view_main_label()
    #     devices_page.click_new_site_button()
    #     devices_page.enter_text_into_site_name_text_field(Variables.default_site_name)
    #     devices_page.click_site_name_popup_ok_button()
    #     self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
    #     '''Post-conditions'''
    #     devices_page.click_error_popup_ok_button()
    #     devices_page.click_site_name_popup_system_button_close()
    #     print ("\n" + "Test is passed" + "\n")
    #
    # def test_create_site_with_fifty_one_symbols(self):
    #     print ("\n" + "TC#9104. Create site with name more than 50 symbols")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.delete_site_if_exists(Variables.fifty_symbols_name)
    #     devices_page.click_global_site_view_main_label()
    #     devices_page.click_new_site_button()
    #     devices_page.enter_text_into_site_name_text_field(Variables.fifty_one_symbols_name)
    #     devices_page.click_site_name_popup_ok_button()
    #     self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_one_symbols_name))
    #     self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_symbols_name))
    #     '''Post-conditions'''
    #     devices_page.delete_site_from_global_site_view_tree(Variables.fifty_symbols_name)
    #     print ("\n" + "Test is passed" + "\n")
    #
    # def test_create_subsites_in_global_site_view_tree(self):
    #     print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.delete_site_if_exists(Variables.parent_site_name)
    #     devices_page.create_new_site(Variables.parent_site_name)
    #     self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.parent_site_name))
    #     devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_1_name)
    #     self.assertTrue(
    #         devices_page.check_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_1_name))
    #     devices_page.create_subsite(Variables.parent_site_name, Variables.subsite_2_name)
    #     self.assertTrue(
    #         devices_page.check_subsite_is_in_parent_site(Variables.parent_site_name, Variables.subsite_2_name))
    #     '''Post-conditions'''
    #     devices_page.delete_site_from_global_site_view_tree(Variables.parent_site_name)
    #     print ("\n" + "Test is passed" + "\n")

    # def tearDown(self):
    #     page = HomePage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())