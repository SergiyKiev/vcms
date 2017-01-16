import unittest
from selenium import webdriver
from pages import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time

class SiteCreation(unittest.TestCase):

    driver = None #global variable

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site creation (Suite ID: 9111)" + "\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        home_page = HomePage(cls.driver)
        devices_page = DevicesPage(cls.driver)
        login_page.open_page()
        login_page.login()
        home_page.close_popups()
        home_page.open_left_side_menu_devices()
        devices_page.click_global_site_view_label()

    def setUp(self):
        home_page = HomePage(self.driver)
        home_page.close_popups()
        # devices_page = home_page.open_left_side_menu_devices()
        # devices_page.check_devices_page_loaded()

    def test_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_label()
        devices_page.click_new_site_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed" + "\n")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name" + "\n")
        sitename = "New site #9101"
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(sitename)
        devices_page.click_global_site_view_label()
        devices_page.click_new_site_button()
        devices_page.enter_text_into_site_name_text_field(sitename)
        devices_page.click_site_name_popup_ok_button()
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(sitename))
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_label()
        devices_page.click_new_site_button()
        devices_page.click_site_name_popup_cancel_button()
        self.assertTrue(devices_page.is_element_not_present(Locators.POPUP_SITE_NAME))
        print ("Test is passed" + "\n")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name" + "\n")
        sitename = "Default Site"
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_label()
        devices_page.click_new_site_button()
        devices_page.enter_text_into_site_name_text_field(sitename)
        devices_page.click_site_name_popup_ok_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_ERROR))
        devices_page.click_error_popup_ok_button()
        devices_page.click_site_name_popup_system_button_close()
        print ("Test is passed" + "\n")

    def test_create_site_with_fifty_one_symbols(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(Variables.fifty_symbols_name)
        devices_page.click_global_site_view_label()
        devices_page.click_new_site_button()
        devices_page.enter_text_into_site_name_text_field(Variables.fifty_one_symbols_name)
        devices_page.click_site_name_popup_ok_button()
        self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_one_symbols_name))
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(Variables.fifty_symbols_name))
        devices_page.delete_site_from_global_site_view_tree(Variables.fifty_symbols_name)
        print ("Test is passed" + "\n")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree" + "\n")
        sitename = "Site #9118"
        subsitename_one = sitename + "-01"
        subsitename_two = sitename + "-02"
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(sitename)
        devices_page.create_new_site(sitename)
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(sitename))
        devices_page.create_new_subsite(sitename, subsitename_one)
        self.assertTrue(devices_page.check_subsite_is_in_parent_site(sitename, subsitename_one))
        devices_page.create_new_subsite(sitename, subsitename_two)
        self.assertTrue(devices_page.check_subsite_is_in_parent_site(sitename, subsitename_two))
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    # def tearDown(self):
    #     page = HomePage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration (Suite ID: 9112)" + "\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        home_page = HomePage(cls.driver)
        devices_page = DevicesPage(cls.driver)
        login_page.open_page()
        login_page.login()
        home_page.close_popups()
        home_page.open_left_side_menu_devices()
        devices_page.click_global_site_view_label()


    def setUp(self):
        home_page = HomePage(self.driver)
        home_page.close_popups()
        # devices_page = home_page.open_left_side_menu_devices()
        # devices_page.check_devices_page_loaded()

    def test_open_configuration_popup(self):
        print ("\n" + "TC#9601. Devices page. Open 'Configuration' popup" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_label()
        devices_page.click_config_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_CONFIGURATION))
        devices_page.click_configuration_popup_system_button_close()
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_global_site_view(self):
        print ("\n" + "TC#9228. Devices page. Open Configuration popup from the Global Site View" + "\n")
        print ("\n" + "Login to console. Go to the start point" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_global_site_view_label()
        devices_page.click_config_button()
        self.assertFalse(devices_page.check_configuration_popup_loaded())
        self.assertTrue(devices_page.check_name_text_feild_disabled())
        self.assertEqual("Global Site View", devices_page.get_configuration_popup_name_text_field_value())
        devices_page.click_configuration_popup_system_button_close()
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_default_site(self):
        print ("\n" + "TC#9230. Devices page. Open Configuration popup from the Default Site main label" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_default_site_in_global_site_view_tree()
        devices_page.click_config_button()
        self.assertTrue(devices_page.check_configuration_popup_loaded())
        self.assertTrue(devices_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_))
        self.assertEqual("Default Site", devices_page.get_configuration_popup_name_text_field_value())
        devices_page.click_configuration_popup_system_button_close()
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_created_site(self):
        print ("\n" + "TC#9236. Devices page. Open Configuration popup from the created site" + "\n")
        sitename = "Site#9236"
        devices_page = DevicesPage(self.driver)
        devices_page.create_site_if_not_exists(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_config_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL))
        self.assertFalse(devices_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_))
        self.assertEqual(sitename, devices_page.get_configuration_popup_name_text_field_value())
        devices_page.click_configuration_popup_system_button_close()
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    # def tearDown(self):
    #     page = HomePage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration_SiteTab(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration - Site tab (Suite ID: 9234)")
        print ("\n" + "Login to console. Go to the start point" + "\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        home_page = HomePage(cls.driver)
        devices_page = DevicesPage(cls.driver)
        login_page.open_page()
        login_page.login()
        home_page.close_popups()
        home_page.open_left_side_menu_devices()
        devices_page.click_global_site_view_label()


    def setUp(self):
        home_page = HomePage(self.driver)
        home_page.close_popups()
        # devices_page = home_page.open_left_side_menu_devices()
        # devices_page.check_devices_page_loaded()

    def test_open_left_side_menus(self):
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_left_side_menu_home()
        left_side_menu.open_left_side_menu_devices()
        left_side_menu.open_left_side_menu_administration()
        left_side_menu.open_left_side_menu_tasks()
        left_side_menu.open_left_side_menu_reporting()
        left_side_menu.open_left_side_menu_software_and_patch_manager()
        left_side_menu.open_left_side_menu_password_reset()

    def test_configuration_popup_change_site_name(self):
        print ("\n" + "TC#9237. Devices page. Configuration popup. Change site name" + "\n")
        sitename = "Site#9237"
        modifed = "_modifed"
        devices_page = DevicesPage(self.driver)
        devices_page.create_site_if_not_exists(sitename)
        devices_page.delete_site_if_exists(sitename + modifed)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_config_button()
        self.assertFalse(devices_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_))
        self.assertEqual(sitename, devices_page.get_configuration_popup_name_text_field_value())
        devices_page.enter_text_into_configuration_popup_name_text_field(modifed)
        devices_page.click_system_button_close()
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(sitename + modifed))
        devices_page.click_site_in_global_site_view_tree(sitename + modifed)
        devices_page.click_config_button()
        self.assertEqual(sitename + modifed, devices_page.get_configuration_popup_name_text_field_value())
        devices_page.click_system_button_close()
        devices_page.delete_site_from_global_site_view_tree(sitename + modifed)
        devices_page.delete_site_if_exists(sitename)
        print ("Test is passed" + "\n")

    def test_configuration_popup_open_column_set_designer_popup(self):
        print ("\n" + "TC#9238. Devices page. Configuration popup. Open Column Set Designer popup" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_default_site_in_global_site_view_tree()
        devices_page.click_config_button()
        devices_page.click_configuration_popup_button_new()
        self.assertTrue(devices_page.check_column_set_designer_popup_is_present())
        devices_page.click_column_set_popup_system_button_close()
        devices_page.click_configuration_popup_system_button_close()
        print ("Test is passed" + "\n")

    def test_configuration_popup_apply_column_set(self):
        print ("\n" + "TC#9239. Devices page. Configuration popup. Apply Column set to the site" + "\n")
        sitename = "Site#9239"
        columnset1 = "ColumnSet#9239-01"
        columnset2 = "ColumnSet#9239-02"
        devices_page = DevicesPage(self.driver)
        devices_page.open_column_sets_popup_from_ribbon_bar()
        devices_page.delete_columnset_in_column_sets_popup_if_exist(columnset1)
        devices_page.delete_columnset_in_column_sets_popup_if_exist(columnset2)
        devices_page.create_columnset_in_column_sets_popup(columnset1, Variables.columns_list1)
        devices_page.create_columnset_in_column_sets_popup(columnset2, Variables.columns_list2)
        devices_page.click_column_sets_popup_button_ok()
        devices_page.create_site_if_not_exists(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_config_button()
        devices_page.select_columnset_from_configuration_popup_column_set_dropdown_list(columnset1)
        devices_page.click_configuration_popup_system_button_close()
        self.assertTrue(devices_page.check_columns_are_presented_in_devices_list_header(Variables.columns_list1))
        devices_page.click_config_button()
        devices_page.select_columnset_from_configuration_popup_column_set_dropdown_list(columnset1)
        devices_page.click_configuration_popup_system_button_close()
        self.assertTrue(devices_page.check_columns_are_presented_in_devices_list_header(Variables.columns_list1))
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")



    # def tearDown(self):
    #     page = HomePage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration_IpAddressRangesTab(unittest.TestCase):

    pass

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration - IP Address Ranges tab (Suite ID: 9234)" + "\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        home_page = HomePage(cls.driver)
        devices_page = DevicesPage(cls.driver)
        login_page.open_page()
        login_page.login()
        home_page.close_popups()
        home_page.open_left_side_menu_devices()
        devices_page.click_global_site_view_label()


    def setUp(self):
        home_page = HomePage(self.driver)
        home_page.close_popups()
        # devices_page = home_page.open_left_side_menu_devices()
        # devices_page.check_devices_page_loaded()

    # def tearDown(self):
    #     page = HomePage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteDeletion(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site deletion (Suite ID: 9114)" + "\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        home_page = HomePage(cls.driver)
        devices_page = DevicesPage(cls.driver)
        login_page.open_page()
        login_page.login()
        home_page.close_popups()
        home_page.open_left_side_menu_devices()
        devices_page.click_global_site_view_label()

    def setUp(self):
        home_page = HomePage(self.driver)
        home_page.close_popups()
        # devices_page = home_page.open_left_side_menu_devices()
        # devices_page.check_devices_page_loaded()

    def test_delete_created_site_from_global_site_view_tree(self):
        print ("\n" + "TC#9607. Devices page. Delete created site from Global Site View tree" + "\n")
        sitename = "Test#9607"
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(sitename)
        devices_page.click_global_site_view_label()
        devices_page.create_new_site(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_delete_button()
        devices_page.click_are_you_sure_popup_button_ok()
        self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_delete_default_site_from_global_site_view_tree(self):
        print ("\n" + "TC#----. Devices page. Delete Default site from Global Site View tree" + "\n")
        devices_page = DevicesPage(self.driver)
        devices_page.click_default_site_in_global_site_view_tree()
        devices_page.click_delete_button()
        self.assertTrue(devices_page.is_element_present(Locators.POPUP_UNABLE_TO_REMOVE))
        devices_page.click_unable_to_remove_popup_ok_button()
        self.assertTrue(devices_page.is_element_present(Locators.LABEL_DEFAULT_SITE))
        print ("Test is passed" + "\n")

    def test_delete_subsite_from_site_tree(self):
        print ("\n" + "TC#----. Devices page. Delete subsite from Global Site View tree" + "\n")
        sitename = "TC#____"
        subsitename = "TC#____-01"
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(sitename)
        devices_page.create_new_site(sitename)
        devices_page.create_new_subsite(sitename, subsitename)
        devices_page.click_subsite_in_site_tree(sitename, subsitename)
        devices_page.click_delete_button()
        devices_page.click_are_you_sure_popup_button_ok()
        self.assertFalse(devices_page.check_subsite_is_in_parent_site(sitename, subsitename))
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_delete_site_with_subsite(self):
        print ("\n" + "TC#----. Devices page. Delete site with subsite from Global Site View tree" + "\n")
        sitename = "TC#____"
        subsitename = "TC#____-01"
        devices_page = DevicesPage(self.driver)
        devices_page.delete_site_if_exists(sitename)
        devices_page.create_new_site(sitename)
        devices_page.create_new_subsite(sitename, subsitename)
        devices_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(devices_page.check_subsite_is_in_parent_site(sitename, subsitename))
        self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(sitename))

    def test_cancel_site_deletion_from_global_site_view(self):
        print ("\n" + "TC#1111. Devices page. Cancel site deletion" + "\n")
        sitename = "TC#1111"
        devices_page = DevicesPage(self.driver)
        devices_page.create_site_if_not_exists(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_delete_button()
        devices_page.click_are_you_sure_popup_button_cancel()
        self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(sitename))
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_open_are_you_sure_popup(self):
        print ("\n" + "TC#2222. Devices page. Open Are you sure popup" + "\n")
        sitename = "TC#2222"
        devices_page = DevicesPage(self.driver)
        devices_page.create_site_if_not_exists(sitename)
        devices_page.click_site_in_global_site_view_tree(sitename)
        devices_page.click_delete_button()
        self.assertTrue(devices_page.check_are_you_sure_popup_is_present())
        devices_page.click_are_you_sure_popup_system_button_close()
        devices_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    # def tearDown(self):
    #     page = HomePage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# class SiteRelocation(unittest.TestCase):
#
    # driver = None
    #
    # @classmethod
    # def setUpClass(cls):
    #     print ("\n" + "Test suite: Site deletion (Suite ID: 9114)" + "\n")
    #     cls.driver = webdriver.Chrome()
    #     # cls.driver = webdriver.Firefox()
    #     cls.driver.maximize_window()
    #     cls.driver.get(Settings.baseUrl)
    #     WebDriverWait(cls.driver, 120).until(EC.presence_of_element_located((By.XPATH, Locators.BTN_SIGN_IN)))
    #     login_page = LoginPage(cls.driver)
    #     login_page.login()
    #     home_page = HomePage(cls.driver)
    #     home_page.close_popups()
    #     devices_page = home_page.open_left_side_menu_devices()
    #     devices_page.check_devices_page_loaded()
    #     devices_page.click_global_site_view_label()
    #
    # def setUp(self):
    #     home_page = HomePage(self.driver)
    #     home_page.close_popups()
    #     # devices_page = home_page.open_left_side_menu_devices()
    #     # devices_page.check_devices_page_loaded()
    #
    # def test_delete_created_site_from_global_site_view_tree(self):
    #     print ("\n" + "TC#9607. Devices page. Delete created site from Global Site View tree" + "\n")
    #     sitename = "Test#9607"
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.delete_site_if_exists(sitename)
    #     devices_page.click_global_site_view_label()
    #     devices_page.create_new_site(sitename)
    #     devices_page.click_site_in_global_site_view_tree(sitename)
    #     devices_page.click_delete_button()
    #     devices_page.click_are_you_sure_popup_button_ok()
    #     self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(sitename))
    #     print ("Test is passed" + "\n")
    #
    # def test_delete_default_site_from_global_site_view_tree(self):
    #     print ("\n" + "TC#----. Devices page. Delete Default site from Global Site View tree" + "\n")
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.click_default_site_in_global_site_view_tree()
    #     devices_page.click_delete_button()
    #     self.assertTrue(devices_page.is_element_present(Locators.POPUP_UNABLE_TO_REMOVE))
    #     devices_page.click_unable_to_remove_popup_ok_button()
    #     self.assertTrue(devices_page.is_element_present(Locators.LABEL_DEFAULT_SITE))
    #     print ("Test is passed" + "\n")
    #
    # def test_delete_subsite_from_site_tree(self):
    #     print ("\n" + "TC#----. Devices page. Delete subsite from Global Site View tree" + "\n")
    #     sitename = "TC#____"
    #     subsitename = "TC#____-01"
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.create_site_if_not_exists(sitename)
    #     devices_page.create_subsite_if_not_exists(sitename, subsitename)
    #     devices_page.click_subsite_in_site_tree(sitename, subsitename)
    #     devices_page.click_delete_button()
    #     devices_page.click_are_you_sure_popup_button_ok()
    #     self.assertFalse(devices_page.check_subsite_is_in_parent_site(sitename, subsitename))
    #     devices_page.delete_site_from_global_site_view_tree(sitename)
    #     print ("Test is passed" + "\n")
    #
    # def test_delete_site_with_subsite(self):
    #     print ("\n" + "TC#----. Devices page. Delete site with subsite from Global Site View tree" + "\n")
    #     sitename = "TC#____"
    #     subsitename = "TC#____-01"
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.create_site_if_not_exists(sitename)
    #     devices_page.create_subsite_if_not_exists(sitename, subsitename)
    #     devices_page.delete_site_from_global_site_view_tree(sitename)
    #     self.assertFalse(devices_page.check_subsite_is_in_parent_site(sitename, subsitename))
    #     self.assertFalse(devices_page.check_site_is_in_global_site_view_tree(sitename))
    #
    # def test_cancel_site_deletion_from_global_site_view(self):
    #     print ("\n" + "TC#1111. Devices page. Cancel site deletion" + "\n")
    #     sitename = "TC#1111"
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.create_site_if_not_exists(sitename)
    #     devices_page.click_site_in_global_site_view_tree(sitename)
    #     devices_page.click_delete_button()
    #     devices_page.click_are_you_sure_popup_system_button_close()
    #     self.assertTrue(devices_page.check_site_is_in_global_site_view_tree(sitename))
    #     devices_page.delete_site_from_global_site_view_tree(sitename)
    #     print ("Test is passed" + "\n")
    #
    # def test_open_are_you_sure_popup(self):
    #     print ("\n" + "TC#2222. Devices page. Open Are you sure popup" + "\n")
    #     sitename = "TC#2222"
    #     devices_page = DevicesPage(self.driver)
    #     devices_page.create_site_if_not_exists(sitename)
    #     devices_page.click_site_in_global_site_view_tree(sitename)
    #     devices_page.click_delete_button()
    #     self.assertTrue(devices_page.is_element_present(Locators.POPUP_ARE_YOU_SURE))
    #     devices_page.click_are_you_sure_popup_button_ok()
    #     print ("Test is passed" + "\n")
    #
    # # def tearDown(self):
    # #     page = HomePage(self.driver)
    # #     page.close_popups()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())