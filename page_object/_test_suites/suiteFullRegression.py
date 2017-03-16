#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import unittest
import time
from _feature_objects.feature_left_menu import *
from _feature_objects.feature_popup import *
from _feature_objects.feature_ribbon_bar import *
from _feature_objects.feature_screen import *
from _pages.pageEndUserAccessLogin import EndUserAccessLoginPage
from _pages.pageLogin import LoginPage
from _pages.pageMain import MainPage
from _test_suites._variables.variables import Variables
from selenium import webdriver


class SiteCreation(unittest.TestCase):

    driver = None  # global variable
    logger = logging.getLogger(__name__)

    @classmethod
    def setUpClass(cls):
        cls.logger.info("Start testing\n")
        cls.logger.info("TEST SUITE: Site creation (Suite ID: 9111)\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()
        main_page._close_popups()

    def setUp(self):
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        left_menu = LeftMenuDevices(self.driver)
        left_menu.open_menu_devices()
        left_menu.expand_global_site_view_list()
        self.logger.info("[Test start]")

    def test_open_left_menus(self):
        self.logger.info("TC#xxxx. Open left side menus")
        left_menu = BaseLeftMenu(self.driver)
        left_menu.open_menu_home()
        self.assertTrue(left_menu.check_menu_home_is_opened())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_menu_software_and_patch_manager_is_opened())
        # left_menu.open_menu_password_reset()
        # self.assertTrue(left_menu.check_menu_password_reset_is_opened())
        self.logger.info("TEST PASSED")

    def test_open_site_name_popup(self):
        self.logger.info("TC#9057. Open Site Name popup")
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_presented())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_presented())
        self.logger.info("TEST PASSED")

    def test_create_new_site_with_acceptable_name(self):
        self.logger.info("TC#9101. Create new site with acceptable name")
        sitename = "New site #9101"
        site_name_popup = SiteNamePopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.delete_site_if_exists(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_presented())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_presented())
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.delete_site_from_global_site_view_list(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        self.logger.info("TEST PASSED")

    def test_cancel_creating_site(self):
        self.logger.info("TC#9058. Cancel creating new site with empty text field")
        left_menu = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_presented())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_presented())
        site_name_popup.click_button_cancel()
        self.assertTrue(site_name_popup.check_popup_is_not_presented())
        self.logger.info("TEST PASSED")

    def test_create_site_with_duplicated_name(self):
        self.logger.info("TC#9107. Create new site with duplicated name")
        sitename = "Default Site"
        left_menu = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        error_popup = ErrorPopup(self.driver)
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_presented())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_presented())
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(error_popup.check_popup_is_presented())
        error_popup.click_button_ok()
        self.assertTrue(error_popup.check_popup_is_not_presented())
        self.assertTrue(site_name_popup.check_popup_is_presented())
        site_name_popup.click_system_button_close()
        self.assertTrue(site_name_popup.check_popup_is_not_presented())
        self.logger.info("TEST PASSED")

    def test_create_site_with_fifty_one_symbols(self):
        self.logger.info("TC#9104. Create site with name more than 50 symbols")
        fifty_symbols_name = "51symbols51symbols51symbols51symbols51symbols!<ok>"
        fifty_one_symbols_name = fifty_symbols_name + "1"
        left_menu = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.delete_site_if_exists(fifty_symbols_name)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(fifty_symbols_name))
        left_menu.delete_site_if_exists(fifty_one_symbols_name)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(fifty_one_symbols_name))
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_presented())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_presented())
        site_name_popup.enter_text_into_name_text_field(fifty_one_symbols_name)
        site_name_popup.click_button_ok()
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(fifty_one_symbols_name))
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(fifty_symbols_name))
        left_menu.delete_site_from_global_site_view_list(fifty_symbols_name)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(fifty_symbols_name))
        self.logger.info("TEST PASSED")

    def test_create_subsites_in_global_site_view_list(self):
        self.logger.info("TC#9118. Create subsites in the Global Site View tree")
        sitename = "Site #9118"
        subsitename_one = sitename + "-01"
        subsitename_two = sitename + "-02"
        left_menu = LeftMenuDevices(self.driver)
        left_menu.delete_site_if_exists(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.create_new_site(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.create_new_subsite(sitename, subsitename_one)
        self.assertTrue(left_menu.check_subsite_is_in_parent_site(sitename, subsitename_one))
        left_menu.create_new_subsite(sitename, subsitename_two)
        self.assertTrue(left_menu.check_subsite_is_in_parent_site(sitename, subsitename_two))
        left_menu.delete_site_from_global_site_view_list(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        self.logger.info("TEST PASSED")

    def tearDown(self):
        base_actions = BaseActions(self.driver)
        base_actions._close_popups()
        self.logger.info("[Test end]\n")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration((unittest.TestCase)):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: Site configuration (Suite ID: 9112)")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()
        left_menu = BaseLeftMenu(self.driver)
        left_menu.open_menu_devices()

    def test_open_configuration_popup(self):
        print ("\n" + "TC#9601. Devices screen. Open 'Configuration' popup")
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        print ("TEST PASSED" + "\n")

    def test_open_configuration_popup_from_global_site_view(self):
        print ("\n" + "TC#9228. Devices screen. Open Configuration popup from the Global Site View")
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        self.assertFalse(configuration_popup.check_tabs_panel_is_presented())
        self.assertTrue(configuration_popup.check_name_text_field_disabled())
        self.assertEqual("Global Site View", configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        print ("TEST PASSED" + "\n")

    def test_open_configuration_popup_from_default_site(self):
        print ("\n" + "TC#9230. Devices screen. Open Configuration popup from the Default Site main label")
        left_menu = LeftMenuDevices(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        self.assertTrue(configuration_popup.check_name_text_field_disabled())
        self.assertEqual("Default Site", configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        print ("TEST PASSED" + "\n")

    def test_open_configuration_popup_from_created_site(self):
        print ("\n" + "TC#9236. Devices screen. Open Configuration popup from the created site")
        sitename = "Site#9236"
        ribbon_bar = RibbonBar(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(
        configuration_popup._is_element_present(configuration_popup.TAB_SITE))  # add verification method to class
        self.assertFalse(configuration_popup._is_element_disabled(configuration_popup.FIELD_NAME))  # add verification method to class
        self.assertEqual(sitename, configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        left_menu.delete_site_from_global_site_view_list(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        print ("TEST PASSED" + "\n")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfigurationSiteTab((unittest.TestCase)):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: Site configuration - Site tab (Suite ID: 9234)")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()
        left_menu = BaseLeftMenu(self.driver)
        left_menu.open_menu_devices()

    def test_configuration_popup_change_site_name(self):
        print ("\n" + "TC#9237. Devices screen. Configuration popup. Change site name")
        sitename = "Site#9237"
        modifed = "_modifed"
        left_menu = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.delete_site_if_exists(sitename + modifed)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename + modifed))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertFalse(configuration_popup.check_name_text_field_disabled())
        self.assertEqual(sitename, configuration_popup.get_name_text_field_value())
        configuration_popup.enter_text_into_name_text_field(modifed)
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename + modifed))
        left_menu.click_site_in_global_site_view_list(sitename + modifed)
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertEqual(sitename + modifed, configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        left_menu.delete_site_from_global_site_view_list(sitename + modifed)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename + modifed))
        left_menu.delete_site_if_exists(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        print ("TEST PASSED" + "\n")

    def test_configuration_popup_open_column_set_designer_popup(self):
        print ("\n" + "TC#9238. Devices screen. Configuration popup. Open Column Set Designer popup")
        configuration_popup = ConfigurationPopup(self.driver)
        column_set_designer = ColumnSetDesignerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        left_menu.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        configuration_popup.click_button_new()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        column_set_designer.click_system_button_close()
        self.assertFalse(column_set_designer.check_popup_is_presented())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        print ("TEST PASSED" + "\n")

    def test_configuration_popup_apply_column_set(self):
        print ("\n" + "TC#9239. Devices screen. Configuration popup. Apply Column set to the site")
        sitename = "Site#9239"
        columnset1 = "ColumnSet#9239-01"
        columnset2 = "test1"
        columns_list1 = ["Device Name", "OS Name", "Caption", "IP Address"]
        columns_list2 = ["Device Name", "Device ID", "Domain", "Site", "User Name"]
        left_menu = LeftMenuDevices(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.click_global_site_view_label()
        ribbon_bar.click_tab_view()
        self.assertTrue(ribbon_bar.check_button_edit_or_create_is_presented())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_popup_is_presented())
        column_sets_popup.delete_columnset_if_exists(columnset1)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnset1))
        column_sets_popup.delete_columnset_if_exists(columnset2)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnset2))
        column_sets_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_popup_is_presented())
        column_set_designer_popup.create_columnset(columnset1, columns_list1)
        self.assertFalse(column_set_designer_popup.check_popup_is_presented())
        self.assertTrue(column_sets_popup.check_is_columnset_present(columnset1))
        column_sets_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_popup_is_presented())
        column_set_designer_popup.create_columnset(columnset2, columns_list2)
        self.assertFalse(column_set_designer_popup.check_popup_is_presented())
        self.assertTrue(column_sets_popup.check_is_columnset_present(columnset2))
        column_sets_popup.click_button_ok()
        self.assertFalse(column_sets_popup.check_popup_is_presented())
        ribbon_bar.click_tab_home()
        self.assertTrue(ribbon_bar.check_button_exit_is_presented())
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        configuration_popup.select_columnset_in_drop_down_list(columnset1)
        self.assertTrue(configuration_popup.check_columnset_is_selected_from_drop_down_list(columnset1))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        self.assertTrue(devices_screen.check_columns_are_present(columns_list1))
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        configuration_popup.select_columnset_in_drop_down_list(columnset2)
        self.assertTrue(configuration_popup.check_columnset_is_selected_from_drop_down_list(columnset2))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        self.assertTrue(devices_screen.check_columns_are_present(columns_list2))
        left_menu.delete_site_from_global_site_view_list(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        print ("TEST PASSED" + "\n")

    def test_configuration_popup_create_column_set(self):
        print ("\n" + "TC#9999. Devices screen. Configuration popup. Create column set")
        sitename = "Site#9999"
        columnsetname = "ColumnSet#9999-01"
        columns_list = ["Device Name", "Device ID", "Domain", "Site"]
        devices_screen = DevicesScreen(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_tab_view()
        self.assertTrue(ribbon_bar.check_button_edit_or_create_is_presented())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_popup_is_presented())
        column_sets_popup.delete_columnset_if_exists(columnsetname)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnsetname))
        column_sets_popup.click_button_ok()
        self.assertFalse(column_sets_popup.check_popup_is_presented())
        ribbon_bar.click_tab_home()
        self.assertTrue(ribbon_bar.check_button_exit_is_presented())
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        configuration_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_popup_is_presented())
        column_set_designer_popup.create_columnset(columnsetname, columns_list)
        self.assertFalse(column_set_designer_popup.check_popup_is_presented())
        configuration_popup.select_columnset_in_drop_down_list(columnsetname)
        self.assertTrue(configuration_popup.check_columnset_is_selected_from_drop_down_list(columnsetname))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_presented())
        self.assertTrue(devices_screen.check_columns_are_present(columns_list))
        left_menu.delete_site_from_global_site_view_list(sitename)
        print ("TEST PASSED" + "\n")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


@unittest.skip
class SiteConfigurationIpAddressRangesTab(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration - IP Address Ranges tab (Suite ID: 9234)")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()
        left_menu = BaseLeftMenu(self.driver)
        left_menu.open_menu_devices()

    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page._close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteDeletion(unittest.TestCase):

    driver = None
    logger = logging.getLogger(__name__)
    # console = logging.StreamHandler()
    # logger.addHandler(console)

    @classmethod
    def setUpClass(cls):
        cls.logger.info("Start testing\n")
        cls.logger.info("TEST SUITE: SITE DELETION (Suite ID: 9111)\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()
        main_page._close_popups()

    def setUp(self):
        self.logger.info("[Test start]")
        left_menu = LeftMenuDevices(self.driver)
        left_menu.open_menu_devices()
        left_menu.expand_global_site_view_list()

    def test_delete_created_site_from_global_site_view_list(self):
        self.logger.info("TC#9607. Devices screen. Delete created site from Global Site View tree")
        sitename = "Test#9607"
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_presented())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_presented())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        self.logger.info("TEST PASSED")

    def test_delete_default_site_from_global_site_view_list(self):
        self.logger.info("TC#8888. Devices screen. Delete Default site from Global Site View tree")
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        unable_to_remove_popup = UnableToRemovePopup(self.driver)
        left_menu.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_delete_is_presented())
        ribbon_bar.click_button_delete()
        self.assertTrue(unable_to_remove_popup.check_popup_is_presented())
        unable_to_remove_popup.click_button_ok()
        self.assertTrue(left_menu.check_default_site_is_in_global_site_view_list())
        self.logger.info("TEST PASSED")

    def test_delete_subsite_from_site_list(self):
        self.logger.info("TC#3333. Devices screen. Delete subsite from Global Site View tree")
        sitename = "TC#3333"
        subsitename = "TC#3333-01"
        left_menu = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu.delete_site_if_exists(sitename)
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.create_new_subsite(sitename, subsitename)
        self.assertTrue(left_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        left_menu.click_subsite_in_site_list(sitename, subsitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_presented())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_presented())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        left_menu.delete_site_from_global_site_view_list(sitename)
        self.logger.info("TEST PASSED")

    def test_delete_site_with_subsite(self):
        self.logger.info("TC#0000. Devices screen. Delete site with subsite from Global Site View tree")
        sitename = "TC#0000"
        subsitename = "TC#0000-01"
        left_menu = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu.delete_site_if_exists(sitename)
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.create_new_subsite(sitename, subsitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(subsitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_presented())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_presented())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        self.assertFalse(left_menu.check_site_is_in_global_site_view_list(sitename))
        self.logger.info("TEST PASSED")

    def test_cancel_site_deletion_from_global_site_view(self):
        self.logger.info("TC#1111. Devices screen. Cancel site deletion")
        sitename = "TC#1111"
        left_menu = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_presented())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_presented())
        are_you_sure_popup.click_button_cancel()
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.delete_site_from_global_site_view_list(sitename)
        self.logger.info("TEST PASSED")

    def test_open_are_you_sure_popup(self):
        self.logger.info("TC#2222. Devices screen. Open Are you sure popup")
        sitename = "TC#2222"
        left_menu = LeftMenuDevices(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_presented())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_presented())
        are_you_sure_popup.click_system_button_close()
        self.assertFalse(are_you_sure_popup.check_popup_is_presented())
        left_menu.delete_site_from_global_site_view_list(sitename)
        self.logger.info("TEST PASSED")

    def tearDown(self):
        base_actions = BaseActions(self.driver)
        base_actions._close_help_window()
        base_actions._close_popups()
        self.logger.info("[Test end]\n")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


@unittest.skip
class SiteRelocation(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: Site creation (Suite ID: 9111)")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()
        left_menu = BaseLeftMenu(self.driver)
        left_menu.open_menu_devices()

    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page._close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


@unittest.skip
class InventoryFeature(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: INVENTORY")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()
        main_page._close_popups()

    def setUp(self):
        self.logger.info("[Test start]")

    def test_inventory_view_folder_full_check(self):
        print ("\n" + "TC#7545: Devices: Inventory - Folder full check")
        main_page = MainPage(self.driver)
        left_menu = BaseLeftMenu(self.driver)


class LoginPageHelpLinks(unittest.TestCase):

    driver = None
    # logging.basicConfig(filename='D:\\python\\vcms\\vcms\\page_object\\_test_logs\\help_logs_login_page.log',
    #                     level=logging.INFO, format='%(asctime)-24s [%(levelname)-3s] %(message)s')
    # logger = logging.getLogger(__name__)
    # console = logging.StreamHandler()
    # logger.addHandler(console)

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='D:\\python\\vcms\\vcms\\page_object\\_test_logs\\help_logs_login_page.log',
                            level=logging.INFO, format='%(asctime)-24s [%(levelname)-3s] %(message)s')
        cls.logger = logging.getLogger("LoginPageHelpLinks")
        console = logging.StreamHandler()
        cls.logger.addHandler(console)
        cls.logger.info("Start testing\n")
        cls.logger.info("TEST SUITE: HELP LINKS ON LOGIN PAGE\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        login_page.check_login_page_loaded()
        login_page._close_popups()

    def setUp(self):
        self.logger.info("[Test start]")

    def test_help_link_on_login_page(self):
        self.logger.info("TC#0000: Check help link on Login page")
        expected_header = "Sign In"
        login_page = LoginPage(self.driver)
        login_page.click_icon_help()
        actual_header = login_page._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, login_page._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_help_link_on_reset_password_popup(self):
        self.logger.info("TC#0000: Check help link on Password Reset popup")
        expected_header = "Reset Password"
        login_page = LoginPage(self.driver)
        reset_password_popup = ResetPasswordPopup(self.driver)
        login_page.click_reset_password_label()
        self.assertTrue(reset_password_popup.check_popup_is_presented())
        reset_password_popup.click_icon_help()
        actual_header = reset_password_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, reset_password_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def tearDown(self):
        base_actions = BaseActions(self.driver)
        base_actions._close_help_window()
        base_actions._close_popups()
        self.logger.info("[Test end]\n")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class MainPageHelpLinks(unittest.TestCase):

    driver = None
    # logging.basicConfig(filename='D:\\python\\vcms\\vcms\\page_object\\_test_logs\\help_logs_main_page.log',
    #                     level=logging.INFO, format='%(asctime)-24s [%(levelname)-3s] %(message)s')
    # logger = logging.getLogger(__name__)
    # console = logging.StreamHandler()
    # logger.addHandler(console)

    @classmethod
    def setUpClass(cls):
        name = 'D:\\python\\vcms\\vcms\\page_object\\_test_logs\\help_logs_main_page.log'
        logging.basicConfig(filename=name, level=logging.INFO, format='%(asctime)-24s [%(levelname)-3s] %(message)s')
        cls.logger = logging.getLogger(__name__)
        console = logging.StreamHandler()
        cls.logger.addHandler(console)
        cls.logger.info("Start testing\n")
        cls.logger.info("TEST SUITE: HELP LINKS ON MAIN PAGE\n")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        main_page = MainPage(cls.driver)
        login_page.open_page()
        login_page.login()
        main_page.check_main_page_loaded()
        main_page._close_popups()
        # main_page.setup_for_help_tests()

    def setUp(self):
        self.logger.info("[Test start]")
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()

    def test_A_help_link_on_endpoint_management_screen(self):
        self.logger.info("TC#0000: Check help link on Endpoint Management screen")
        expected_header = "Endpoint Management"
        left_menu = LeftMenuAdministration(self.driver)
        endpoint_management_screen = EndpointManagementScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(endpoint_management_screen.check_screen_is_presented())
        endpoint_management_screen.click_icon_help()
        actual_header = endpoint_management_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, endpoint_management_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_dynamically_managed_screen(self):
        self.logger.info("TC#0000: Check help link on Dynamically Managed screen")
        expected_header = "Endpoint Management"
        left_menu = LeftMenuAdministration(self.driver)
        dynamically_managed_screen = DynamicallyManagedScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.expand_endpoint_management_list()
        self.assertTrue(left_menu.check_dynamically_managed_label_is_presented())
        left_menu.click_dynamically_managed_label()
        self.assertTrue(dynamically_managed_screen.check_screen_is_presented())
        dynamically_managed_screen.click_icon_help()
        actual_header = dynamically_managed_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, dynamically_managed_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_excluded_devices_screen(self):
        self.logger.info("TC#0000: Check help link on Excluded Devices screen")
        expected_header = "Endpoint Management"
        left_menu = LeftMenuAdministration(self.driver)
        excluded_devices_screen = ExcludedDevicesScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.expand_endpoint_management_list()
        self.assertTrue(left_menu.check_excluded_devices_label_is_presented())
        left_menu.click_excluded_devices_label()
        self.assertTrue(excluded_devices_screen.check_screen_is_presented())
        excluded_devices_screen.click_icon_help()
        actual_header = excluded_devices_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, excluded_devices_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_unmanaged_devices_screen(self):
        self.logger.info("TC#0000: Check help link on Unmanaged Devices screen")
        expected_header = "Endpoint Management"
        left_menu = LeftMenuAdministration(self.driver)
        unmanaged_devices_screen = UnmanagedDevicesScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.expand_endpoint_management_list()
        self.assertTrue(left_menu.check_excluded_devices_label_is_presented())
        left_menu.click_unmanaged_devices_label()
        self.assertTrue(unmanaged_devices_screen.check_screen_is_presented())
        unmanaged_devices_screen.click_icon_help()
        actual_header = unmanaged_devices_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, unmanaged_devices_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_infrastructure_screen(self):
        self.logger.info("TC#0000: Check help link on Infrastructure screen")
        expected_header = "Endpoint Management"
        left_menu = LeftMenuAdministration(self.driver)
        infrastructure_screen = InfrastructureScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.expand_endpoint_management_list()
        self.assertTrue(left_menu.check_infrastructure_label_is_presented())
        left_menu.click_infrastructure_label()
        self.assertTrue(infrastructure_screen.check_screen_is_presented())
        infrastructure_screen.click_icon_help()
        actual_header = infrastructure_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, infrastructure_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_site_configuration_screen(self):
        self.logger.info("TC#0000: Check help link on Site Configuration screen")
        expected_header = "Site Management"
        left_menu = LeftMenuAdministration(self.driver)
        site_configuration_screen = SiteConfigurationScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_site_management_label()
        self.assertTrue(site_configuration_screen.check_screen_is_presented())
        site_configuration_screen.click_icon_help()
        actual_header = site_configuration_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_configuration_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_site_event_logs_screen(self):
        self.logger.info("TC#0000: Check help link on Event Logs screen")
        expected_header = "Logs"
        left_menu = LeftMenuAdministration(self.driver)
        event_logs_screen =EventLogsScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_logs_label()
        self.assertTrue(event_logs_screen.check_screen_is_presented())
        event_logs_screen.click_icon_help()
        actual_header = event_logs_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, event_logs_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_column_sets_screen(self):
        self.logger.info("TC#0000: Check help link on Column Sets screen")
        expected_header = "Column Sets"
        left_menu = LeftMenuAdministration(self.driver)
        column_sets_screen = ColumnSetsScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_column_sets_label()
        self.assertTrue(column_sets_screen.check_screen_is_presented())
        column_sets_screen.click_icon_help()
        actual_header = column_sets_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, column_sets_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_inventory_configuration_screen(self):
        self.logger.info("TC#0000: Check help link on Inventory Configuration screen")
        expected_header = "Inventory Scan Configuration"
        left_menu = LeftMenuAdministration(self.driver)
        inventory_configuration_screen =InventoryConfigurationScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_inventory_scan_configuration_label()
        self.assertTrue(inventory_configuration_screen.check_screen_is_presented())
        inventory_configuration_screen.click_icon_help()
        actual_header = inventory_configuration_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, inventory_configuration_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_vreps_screen(self):
        self.logger.info("TC#0000: Check help link on vReps screen")
        expected_header = "vReps"
        left_menu = LeftMenuAdministration(self.driver)
        vreps_screen =VRepsScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_vreps_label()
        self.assertTrue(vreps_screen.check_screen_is_presented())
        vreps_screen.click_icon_help()
        actual_header = vreps_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, vreps_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_maintenance_windows_screen(self):
        self.logger.info("TC#0000: Check help link on Maintenance Windows screen")
        expected_header = "Maintenance Windows"
        left_menu = LeftMenuAdministration(self.driver)
        maintenance_screen = MaintenanceWindowsScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_maintenance_windows_label()
        self.assertTrue(maintenance_screen.check_screen_is_presented())
        maintenance_screen.click_icon_help()
        actual_header = maintenance_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, maintenance_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_notifications_screen(self):
        self.logger.info("TC#0000: Check help link on Notifications screen")
        expected_header = "Notifications"
        left_menu = LeftMenuAdministration(self.driver)
        notification_screen =NotificationsScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_notifications_label()
        self.assertTrue(notification_screen.check_screen_is_presented())
        notification_screen.click_icon_help()
        actual_header = notification_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, notification_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_audit_log_screen(self):
        self.logger.info("TC#0000: Check help link on Audit Log screen")
        expected_header = "Audit Log"
        left_menu = LeftMenuAdministration(self.driver)
        audit_log_screen =AuditLogScreen(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_audit_log_label()
        self.assertTrue(audit_log_screen.check_screen_is_presented())
        audit_log_screen.click_icon_help()
        actual_header = audit_log_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, audit_log_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_admin_accounts_popup(self):
        self.logger.info("TC#0000: Check help link on Admin Accounts popup")
        expected_header = "Accounts"
        left_menu = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        admin_accounts_popup = AdminAccountsPopup(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_presented())
        ribbon_bar.click_button_accounts()
        self.assertTrue(admin_accounts_popup.check_popup_is_presented())
        admin_accounts_popup.click_icon_help()
        actual_header = admin_accounts_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, admin_accounts_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_user_configuration_popup(self):
        self.logger.info("TC#0000: Check help link on User Configuration popup")
        expected_header = "Create"
        left_menu = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        admin_accounts_popup = AdminAccountsPopup(self.driver)
        user_configuration_popup = UserConfigurationPopup(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_presented())
        ribbon_bar.click_button_accounts()
        self.assertTrue(admin_accounts_popup.check_popup_is_presented())
        admin_accounts_popup.click_button_add()
        self.assertTrue(user_configuration_popup.check_popup_is_presented())
        user_configuration_popup.click_icon_help()
        actual_header = user_configuration_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, user_configuration_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_configure_exclusions_popup(self):
        self.logger.info("TC#0000: Check help link on Configure Exclusions popup")
        expected_header = "Exclusions"
        left_menu = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_presented())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_presented())
        configure_exclusions_popup.click_icon_help()
        actual_header = configure_exclusions_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, configure_exclusions_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_exclude_site_popup(self):
        self.logger.info("TC#0000: Check help link on Exclude Site popup")
        expected_header = "Exclude Site"
        left_menu = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        exclude_site_popup = ExcludeSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_presented())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_presented())
        configure_exclusions_popup.click_list_label_sites()
        # self.assertTrue(configure_exclusions_popup.check_sites_tab_is_opened())
        configure_exclusions_popup.click_sites_tab_button_add()
        self.assertTrue(exclude_site_popup.check_popup_is_presented())
        exclude_site_popup.click_icon_help()
        actual_header = exclude_site_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, exclude_site_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_exclude_device_popup(self):
        self.logger.info("TC#0000: Check help link on Exclude Device popup")
        expected_header = "Exclude Device"
        left_menu = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        exclude_device_popup = ExcludeDevicePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_presented())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_presented())
        configure_exclusions_popup.click_list_label_device_name()
        configure_exclusions_popup.click_device_name_tab_button_add()
        self.assertTrue(exclude_device_popup.check_popup_is_presented())
        exclude_device_popup.click_icon_help()
        actual_header = exclude_device_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, exclude_device_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_exclude_ip_address_popup(self):
        self.logger.info("TC#0000: Check help link on Exclude IP Address popup")
        expected_header = "Exclude IP Address"
        left_menu = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        exclude_ip_address_popup = ExcludeIPAddressPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_presented())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_presented())
        configure_exclusions_popup.click_list_label_ip_address()
        configure_exclusions_popup.click_ip_address_tab_button_add()
        self.assertTrue(exclude_ip_address_popup.check_popup_is_presented())
        exclude_ip_address_popup.click_icon_help()
        actual_header = exclude_ip_address_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, exclude_ip_address_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_discover_devices_popup(self):
        self.logger.info("TC#0000: Check help link on Discover Devices popup (Administration)")
        expected_header = "Discovery"
        left_menu = LeftMenuAdministration(self.driver)
        discover_devices_popup = DiscoverDevicesPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_button_discover_is_presented())
        ribbon_bar.click_button_discover()
        self.assertTrue(discover_devices_popup.check_popup_is_presented())
        discover_devices_popup.click_icon_help()
        actual_header = discover_devices_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, discover_devices_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_site_config_popup(self):
        self.logger.info("TC#0000: Check help link on Site Config popup")
        expected_header = "Create" #THIS SHOULD BE SITE CONFIGURATION...
        left_menu = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_site_management_label()
        self.assertTrue(ribbon_bar.check_box_config_is_presented())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_presented())
        site_config_popup.click_icon_help()
        actual_header = site_config_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_config_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_site_name_popup(self):
        self.logger.info("TC#0000: Check help link on Site Name popup (Administration)")
        expected_header = "Create a site"
        left_menu = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_site_management_label()
        self.assertTrue(ribbon_bar.check_box_config_is_presented())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_presented())
        site_config_popup.click_global_site_view_label()
        site_config_popup.click_button_add_site()
        self.assertTrue(site_name_popup.check_popup_is_presented())
        site_name_popup.click_icon_help()
        actual_header = site_name_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_name_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_ip_address_popup(self):
        self.logger.info("TC#0000: Check help link on IP Address popup (Administration)")
        expected_header = "IP Address Range"
        sitename = Variables.help_test
        left_menu = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        ip_address_popup = IPAddressPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_site_management_label()
        self.assertTrue(ribbon_bar.check_box_config_is_presented())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_presented())
        site_config_popup.create_site_if_not_exists(sitename)
        self.assertTrue(site_config_popup.check_site_is_in_global_site_view_list(sitename))
        site_config_popup.click_site_in_global_site_view_list(sitename)
        site_config_popup.click_button_add_ip_range()
        self.assertTrue(ip_address_popup.check_popup_is_presented())
        ip_address_popup.click_icon_help()
        actual_header = ip_address_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ip_address_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_move_site_popup(self):
        self.logger.info("TC#0000: Check help link on Move Site popup (Administration)")
        expected_header = "Move a site or device"
        sitename = Variables.help_test
        left_menu = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        move_site_popup = MoveSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_site_management_label()
        self.assertTrue(ribbon_bar.check_box_config_is_presented())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_presented())
        site_config_popup.create_site_if_not_exists(sitename)
        self.assertTrue(site_config_popup.check_site_is_in_global_site_view_list(sitename))
        site_config_popup.click_button_move_site()
        self.assertTrue(move_site_popup.check_popup_is_presented())
        move_site_popup.click_icon_help()
        actual_header = move_site_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, move_site_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_column_set_designer_popup(self):
        self.logger.info("TC#0000: Check help link on Column Set Designer popup (Administration)")
        expected_header = "Create" #IS NOT CORRECT
        left_menu = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_column_sets_label()
        self.assertTrue(ribbon_bar.check_box_column_sets_is_presented())
        ribbon_bar.click_button_new()
        self.assertTrue(column_set_designer_popup.check_popup_is_presented())
        column_set_designer_popup.click_icon_help()
        actual_header = column_set_designer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, column_set_designer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_edit_user_popup(self):
        self.logger.info("TC#0000: Check help link on Create User popup (Administration tab)")
        expected_header = "Edit User"
        left_menu = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        edit_user_popup = EditUserPopup(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_user_management_label()
        self.assertTrue(ribbon_bar.check_box_users_is_presented())
        ribbon_bar.click_button_add()
        self.assertTrue(edit_user_popup.check_popup_is_presented())
        edit_user_popup.click_icon_help()
        actual_header = edit_user_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, edit_user_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_inventory_configuration_popup(self):
        self.logger.info("TC#0000: Check help link on Inventory Configuration popup")
        expected_header = "Inventory Scan Configuration"
        left_menu = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        inventory_configuration_popup = InventoryConfigurationPopup(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_inventory_scan_configuration_label()
        self.assertTrue(ribbon_bar.check_box_inventory_is_presented())
        ribbon_bar.click_button_create()
        self.assertTrue(inventory_configuration_popup.check_popup_is_presented())
        inventory_configuration_popup.click_icon_help()
        actual_header = inventory_configuration_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, inventory_configuration_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_inventory_force_update_popup(self):
        self.logger.info("TC#0000: Check help link on Inventory Force Update popup")
        expected_header = "Force Update"
        left_menu = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        inventory_configuration_screen = InventoryConfigurationScreen(self.driver)
        inventory_force_update_popup = InventoryForceUpdatePopup(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_inventory_scan_configuration_label()
        self.assertTrue(ribbon_bar.check_box_inventory_is_presented())
        self.assertTrue(inventory_configuration_screen.check_inventory_is_presented("Full Scan"))
        inventory_configuration_screen.select_full_scan_inventory_in_table()
        self.assertTrue(ribbon_bar.check_button_force_update_is_enabled())
        ribbon_bar.click_button_force_update()
        self.assertTrue(inventory_force_update_popup.check_popup_is_presented())
        inventory_force_update_popup.click_icon_help()
        actual_header = inventory_force_update_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, inventory_force_update_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_A_help_link_on_maintenance_window_popup(self):
        self.logger.info("TC#0000: Check help link on Maintenance Window popup")
        expected_header = "Create"
        left_menu = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        maintenance_window_popup = MaintenanceWindowPopup(self.driver)
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_opened())
        left_menu.click_maintenance_windows_label()
        self.assertTrue(ribbon_bar.check_maintenance_windows_box_is_presented())
        ribbon_bar.click_button_add()
        self.assertTrue(maintenance_window_popup.check_popup_is_presented())
        maintenance_window_popup.click_icon_help()
        actual_header = maintenance_window_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, maintenance_window_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_queries_screen(self):
        self.logger.info("TC#0000: Check help link on Queries screen")
        expected_header = "Queries"
        left_menu = LeftMenuDevices(self.driver)
        queries_screen = QueriesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_queries_label()
        queries_screen.click_icon_help()
        actual_header = queries_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, queries_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_groups_screen(self):
        self.logger.info("TC#0000: Check help link on Groups screen")
        expected_header = "Groups"
        left_menu = LeftMenuDevices(self.driver)
        groups_screen =GroupsScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_groups_label()
        groups_screen.click_icon_help()
        actual_header = groups_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, groups_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_site_name_popup(self):
        self.logger.info("TC#0000: Check help link on Site Name popup")
        expected_header = "Create a site"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_presented())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_presented())
        site_name_popup.click_icon_help()
        actual_header = site_name_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_name_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_configuration_popup(self):
        self.logger.info("TC#0000: Check help link on Configuration popup")
        expected_header = "Configure a site"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = BaseLeftMenu(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.open_global_site_view_list()
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        configuration_popup.click_icon_help()
        actual_header = configuration_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, configuration_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_ip_address_popup(self):
        self.logger.info("TC#0000: Check help link on IP Address popup")
        expected_header = "Add IP Address"
        sitename = Variables.help_test
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        ip_address_popup = IPAddressPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.open_global_site_view_list()
        left_menu.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_list(sitename))
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_presented())
        configuration_popup.click_ip_address_ranges_tab()
        self.assertTrue(configuration_popup.check_tab_is_presented())
        configuration_popup.click_button_add()
        self.assertTrue(ip_address_popup.check_popup_is_presented())
        ip_address_popup.click_icon_help()
        actual_header = ip_address_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ip_address_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_move_site_popup(self):
        self.logger.info("TC#0000: Check help link on Move Site popup")
        expected_header = "Move a site or device"
        sitename = Variables.help_test
        ribbon_bar = RibbonBar(self.driver)
        left_menu = BaseLeftMenu(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        move_site_popup = MoveSitePopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.create_site_if_not_exists(sitename)
        left_menu.click_site_in_global_site_view_list(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_presented())
        ribbon_bar.click_button_move()
        self.assertTrue(move_site_popup.check_popup_is_presented())
        move_site_popup.click_icon_help()
        actual_header = move_site_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, move_site_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_query_designer_popup(self):
        self.logger.info("TC#0000: Check help link on Query Designer popup")
        expected_header = "Queries"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        query_designer_popup = QueryDesignerPopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.click_queries_label()
        self.assertTrue(ribbon_bar.check_queries_box_is_presented())
        ribbon_bar.click_button_new()
        ribbon_bar.click_menu_item_new_query()
        self.assertTrue(query_designer_popup.check_popup_is_presented())
        query_designer_popup.click_icon_help()
        actual_header = query_designer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, query_designer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_condition_editor_popup(self):
        self.logger.info("TC#0000: Check help link on Condition Editor popup")
        expected_header = "Create a Query"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        query_designer_popup = QueryDesignerPopup(self.driver)
        condition_editor_popup = ConditionEditorPopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.click_queries_label()
        self.assertTrue(ribbon_bar.check_queries_box_is_presented())
        ribbon_bar.click_button_new()
        ribbon_bar.click_menu_item_new_query()
        self.assertTrue(query_designer_popup.check_popup_is_presented())
        query_designer_popup.click_button_add()
        self.assertTrue(condition_editor_popup.check_popup_is_presented())
        condition_editor_popup.click_icon_help()
        actual_header = condition_editor_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, condition_editor_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_new_group_popup(self):
        self.logger.info("TC#0000: Check help link on New Group popup")
        expected_header = "Create a Group"
        ribbon_bar = RibbonBar(self.driver)
        new_group_popup = NewGroupPopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_presented())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_presented())
        ribbon_bar.click_menu_item_new_group()
        self.assertTrue(new_group_popup.check_popup_is_presented())
        new_group_popup.click_icon_help()
        actual_header = new_group_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, new_group_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_select_targets_popup(self):
        self.logger.info("TC#0000: Check help link on Select Targets popup (Devices)")
        expected_header = "Select Targets"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        new_group_popup = NewGroupPopup(self.driver)
        select_targets_popup = SelectTargetsPopup(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_presented())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_presented())
        ribbon_bar.click_menu_item_new_group()
        self.assertTrue(new_group_popup.check_popup_is_presented())
        new_group_popup.click_button_add_members()
        self.assertTrue(select_targets_popup.check_popup_is_presented())
        select_targets_popup.click_icon_help()
        actual_header = select_targets_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, select_targets_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_new_folder_popup(self):
        self.logger.info("TC#0000: Check help link on New Folder popup")
        expected_header = "Create a Folder"
        ribbon_bar = RibbonBar(self.driver)
        new_folder_popup = NewFolderPopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_presented())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_presented())
        ribbon_bar.click_menu_item_new_folder()
        self.assertTrue(new_folder_popup.check_popup_is_presented())
        new_folder_popup.click_icon_help()
        actual_header = new_folder_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, new_folder_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_edit_folder_popup(self):
        self.logger.info("TC#0000: Check help link on Edit Folder popup")
        expected_header = "Edit a folder"
        name = Variables.help_test
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        edit_folder_popup = EditFolderPopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_presented())
        left_menu.create_group_folder_if_not_exists(name)
        self.assertTrue(left_menu.check_folder_is_in_groups_list(name))
        left_menu.click_group_in_groups_list(name)
        self.assertTrue(ribbon_bar.check_button_edit_folder_is_presented())
        ribbon_bar.click_button_edit_folder()
        self.assertTrue(edit_folder_popup.check_popup_is_presented())
        edit_folder_popup.click_icon_help()
        actual_header = edit_folder_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, edit_folder_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_inventory_view_popup(self):
        self.logger.info("TC#0000: Check help link on Inventory View popup")
        expected_header = "Inventory"
        device = Variables.vrep
        inventory_view_popup = InventoryViewPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_box_inventory_is_presented())
        ribbon_bar.click_button_inventory()
        ribbon_bar.click_menu_item_view()
        self.assertTrue(inventory_view_popup.check_popup_is_presented(device))
        inventory_view_popup.click_icon_help()
        actual_header = inventory_view_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, inventory_view_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_on_demand_inventory_scan_popup(self):
        self.logger.info("TC#0000: Check help link on On Demand Inventory Scan popup")
        expected_header = "On Demand Inventory Scan"
        device = Variables.vrep
        on_demand_inventory_scan_popup = OnDemandInventoryScanPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_box_inventory_is_presented())
        ribbon_bar.click_button_inventory()
        ribbon_bar.click_menu_item_on_demand()
        self.assertTrue(on_demand_inventory_scan_popup.check_popup_is_presented())
        on_demand_inventory_scan_popup.click_icon_help()
        actual_header = on_demand_inventory_scan_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, on_demand_inventory_scan_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_wake_up_popup(self):
        self.logger.info("TC#0000: Check help link on Wake on LAN popup")
        expected_header = "Wake Up"
        device = Variables.vrep
        wake_on_lan_popup = WakeOnLANPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_button_wake_up_is_presented())
        ribbon_bar.click_button_wake_up()
        self.assertTrue(wake_on_lan_popup.check_popup_is_presented())
        wake_on_lan_popup.click_icon_help()
        actual_header = wake_on_lan_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, wake_on_lan_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_move_device_popup(self):
        self.logger.info("TC#0000: Check help link on Move Device popup")
        expected_header = "Move a site or device"
        device = Variables.vrep
        move_device_popup = MoveDevicePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_box_site_management_is_presented())
        ribbon_bar.click_button_move_device()
        self.assertTrue(move_device_popup.check_popup_is_presented())
        move_device_popup.click_icon_help()
        actual_header = move_device_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, move_device_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_patch_manager_popup(self):
        self.logger.info("TC#0000: Check help link on Patch Manager popup")
        expected_header = "Software Updates"
        device = Variables.vrep
        patch_manager_popup = PatchManagerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_button_patch_manager_is_presented())
        ribbon_bar.click_button_patch_manager()
        self.assertTrue(patch_manager_popup.check_popup_is_presented())
        patch_manager_popup.click_icon_help()
        actual_header = patch_manager_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, patch_manager_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_patch_component_details_popup(self):
        self.logger.info("TC#0000: Check help link on Patch Component Details popup")
        expected_header = "Patch Component Details"
        device = Variables.vrep
        patch = "KB3141501"
        patch_manager_popup = PatchManagerPopup(self.driver)
        patch_component_details_popup = PatchComponentDetailsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_button_patch_manager_is_presented())
        ribbon_bar.click_button_patch_manager()
        self.assertTrue(patch_manager_popup.check_popup_is_presented())
        patch_manager_popup.click_label_history()
        patch_manager_popup.enter_text_into_search_text_field_and_click_enter(patch)
        self.assertTrue(patch_manager_popup.check_patch_is_presented(patch))
        patch_manager_popup.click_patch_in_table(patch)
        self.assertTrue(patch_manager_popup.check_patch_components_table_is_presented())
        patch_manager_popup.click_first_component_in_table()
        self.assertTrue(patch_manager_popup.check_button_component_details_is_presented())
        patch_manager_popup.click_button_component_details()
        self.assertTrue(patch_component_details_popup.check_popup_is_presented())
        patch_component_details_popup.click_icon_help()
        actual_header = patch_component_details_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, patch_component_details_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_reports_popup(self):
        self.logger.info("TC#0000: Check help link on Reports popup")
        expected_header = "Reports"
        device = Variables.vrep
        reports_popup = ReportsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_box_site_management_is_presented())
        ribbon_bar.click_button_reports()
        self.assertTrue(reports_popup.check_popup_is_presented())
        reports_popup.click_icon_help()
        actual_header = reports_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, reports_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_end_user_access_popup(self):
        self.logger.info("TC#0000: Check help link on End User Access popup")
        expected_header = "End User Access"
        device = Variables.vrep
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        end_user_access_popup = EndUserAccessPopup(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_button_end_user_access_is_presented())
        ribbon_bar.click_button_end_user_access()
        self.assertTrue(end_user_access_popup.check_popup_is_presented())
        end_user_access_popup.click_icon_help()
        actual_header = end_user_access_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, end_user_access_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    # @unittest.skip("test_EUA_help_link_on_end_user_access_login_page\n")
    def test_EUA_help_link_on_end_user_access_login_page(self):
        self.logger.info("TC#0000: Check help link on End User Access login page")
        expected_header = "End User Access Page"
        end_user_access_login_page = EndUserAccessLoginPage(self.driver)
        end_user_access_login_page.open_page(url=Settings.endUserAccess)
        self.assertTrue(end_user_access_login_page.check_page_is_loaded())
        end_user_access_login_page.click_icon_help()
        actual_header = end_user_access_login_page._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, end_user_access_login_page._get_log_for_help_link(expected_header))
        base_actions = BaseActions(self.driver)
        base_actions._close_help_window()
        self.driver.back()
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_file_explorer_popup(self):
        self.logger.info("TC#0000: Check help link on File Explorer popup")
        expected_header = "File Explorer"
        device = Variables.vrep
        file_explorer_popup = FileExplorerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_box_computer_tools_is_presented())
        ribbon_bar.click_button_file_browser()
        self.assertTrue(file_explorer_popup.check_popup_is_presented())
        file_explorer_popup.click_icon_help()
        actual_header = file_explorer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, file_explorer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_ping_result_popup(self):
        self.logger.info("TC#0000: Check help link on Ping Result popup")
        expected_header = "Ping Result"
        device = Variables.vrep
        ping_result_popup = PingResultPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_box_computer_tools_is_presented())
        ribbon_bar.click_button_ping()
        self.assertTrue(ping_result_popup.check_popup_is_presented())
        ping_result_popup.click_icon_help()
        actual_header = ping_result_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ping_result_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_process_explorer_popup(self):
        self.logger.info("TC#0000: Check help link on IP Process Explorer popup")
        expected_header = "Process Explorer"
        device = Variables.vrep
        process_explorer_popup = ProcessExplorerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_box_computer_tools_is_presented())
        ribbon_bar.click_button_process_viewer()
        self.assertTrue(process_explorer_popup.check_popup_is_presented())
        process_explorer_popup.click_icon_help()
        actual_header = process_explorer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, process_explorer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_event_viewer_popup(self):
        self.logger.info("TC#0000: Check help link on Event Viewer popup")
        expected_header = "Event Viewer"
        device = Variables.vrep
        event_viewer_popup = EventViewerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_box_computer_tools_is_presented())
        ribbon_bar.click_button_event_viewer()
        self.assertTrue(event_viewer_popup.check_popup_is_presented())
        event_viewer_popup.click_icon_help()
        actual_header = event_viewer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, event_viewer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_D_help_link_on_wmi_explorer_popup(self):
        self.logger.info("TC#0000: Check help link on WMI Explorer popup")
        expected_header = "Process Explorer"
        device = Variables.vrep
        wmi_explorer_popup = WMIExplorerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_presented(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_box_computer_tools_is_presented())
        ribbon_bar.click_button_wmi_explorer()
        self.assertTrue(wmi_explorer_popup.check_popup_is_presented())
        wmi_explorer_popup.click_icon_help()
        actual_header = wmi_explorer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, wmi_explorer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_H_help_link_on_home_screen(self):
        self.logger.info("TC#0000: Check help link on Home screen")
        expected_header = "Getting Started in CMS"
        left_menu = BaseLeftMenu(self.driver)
        home_screen = HomeScreen(self.driver)
        left_menu.open_menu_home()
        self.assertTrue(home_screen.check_screen_is_presented())
        home_screen.click_icon_help()
        actual_header = home_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, home_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_H_help_link_on_devices_home_screen(self):
        self.logger.info("TC#0000: Check help link on Devices home screen")
        expected_header = "Devices"
        left_menu = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu.open_menu_devices()
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_button_home()
        ribbon_bar.click_menu_item_go_to_home_screen()
        self.assertTrue(devices_screen.check_screen_is_presented())
        devices_screen.click_icon_help()
        actual_header = devices_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, devices_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_H_help_link_on_administration_home_screen(self):
        self.logger.info("TC#0000: Check help link on Administration home screen")
        expected_header = "Administration"
        left_menu = LeftMenuAdministration(self.driver)
        administration_screen = AdministrationScreen(self.driver)
        left_menu.open_menu_administration()
        administration_screen.open_administration_screen()
        self.assertTrue(administration_screen.check_screen_is_presented())
        administration_screen.click_icon_help()
        actual_header = administration_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, administration_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_H_help_link_on_tasks_home_screen(self):
        self.logger.info("TC#0000: Check help link on Tasks home screen")
        expected_header = "Tasks"
        left_menu = BaseLeftMenu(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu.open_menu_tasks()
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        ribbon_bar.click_button_home()
        ribbon_bar.click_menu_item_go_to_home_screen()
        self.assertTrue(tasks_screen.check_screen_is_presented())
        tasks_screen.click_icon_help()
        actual_header = tasks_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, tasks_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_H_help_link_on_reporting_home_screen(self):
        self.logger.info("TC#0000: Check help link on Reporting home screen")
        expected_header = "Reporting"
        left_menu = BaseLeftMenu(self.driver)
        reporting_screen = ReportingScreen(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_presented())
        ribbon_bar.click_button_home()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_presented())
        ribbon_bar.click_menu_item_go_to_home_screen()
        self.assertTrue(reporting_screen.check_screen_is_presented())
        reporting_screen.click_icon_help()
        actual_header = reporting_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, reporting_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_H_help_link_on_software_and_patch_manager_home_screen(self):
        self.logger.info("TC#0000: Check help link on Software and Patch Manager home screen")
        expected_header = "Software / Patch Manager"
        left_menu = BaseLeftMenu(self.driver)
        software_and_patch_manager_screen = SoftwareAndPatchManagerScreen(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        ribbon_bar.click_button_home()
        ribbon_bar.click_menu_item_go_to_home_screen()
        self.assertTrue(software_and_patch_manager_screen.check_screen_is_presented())
        software_and_patch_manager_screen.click_icon_help()
        actual_header = software_and_patch_manager_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header,
                         software_and_patch_manager_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_my_dashboards_screen(self):
        self.logger.info("TC#0000: Check help link on My Dashboards screen")
        expected_header = "My Dashboards"
        left_menu = LeftMenuReporting(self.driver)
        my_dashboards_screen = MyDashboardsScreen(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_my_dashboards()
        self.assertTrue(my_dashboards_screen.check_screen_is_presented())
        my_dashboards_screen.click_icon_help()
        actual_header = my_dashboards_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, my_dashboards_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_my_reports_screen(self):
        self.logger.info("TC#0000: Check help link on My Reports screen")
        expected_header = "My Reports"
        left_menu = LeftMenuReporting(self.driver)
        my_reports_screen = MyReportsScreen(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_my_reports()
        self.assertTrue(my_reports_screen.check_screen_is_presented())
        my_reports_screen.click_icon_help()
        actual_header = my_reports_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, my_reports_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_shared_reports_screen(self):
        self.logger.info("TC#0000: Check help link on Shared Reports screen")
        expected_header = "Shared Reports"
        left_menu = LeftMenuReporting(self.driver)
        shared_reports_screen = SharedReportsScreen(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_shared_reports()
        self.assertTrue(shared_reports_screen.check_screen_is_presented())
        shared_reports_screen.click_icon_help()
        actual_header = shared_reports_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, shared_reports_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_queries_popup(self):
        self.logger.info("TC#0000: Check help link on Shared Reports screen")
        expected_header = "Queries"
        left_menu = LeftMenuReporting(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        queries_popup = QueriesPopup(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_shared_reports()
        self.assertTrue(ribbon_bar.check_button_create_is_presented())
        ribbon_bar.click_button_create()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_presented())
        ribbon_bar.click_menu_item_create_query_report()
        self.assertTrue(queries_popup.check_popup_is_presented())
        queries_popup.click_icon_help()
        actual_header = queries_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, queries_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_report_scheduler_popup(self):
        self.logger.info("TC#0000: Check help link on Report Scheduler popup")
        expected_header = "Report Scheduler"
        left_menu = LeftMenuReporting(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        shared_reports_screen = SharedReportsScreen(self.driver)
        report_scheduler_popup = ReportSchedlulerPopup(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_shared_reports()
        self.assertTrue(shared_reports_screen.check_report_is_presented())
        shared_reports_screen.select_single_report()
        self.assertTrue(ribbon_bar.check_create_schedule_button_is_enabled())
        ribbon_bar.click_button_create_schedule()
        self.assertTrue(report_scheduler_popup.check_popup_is_presented())
        report_scheduler_popup.click_icon_help()
        actual_header = report_scheduler_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, report_scheduler_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_saved_date_ranges_popup(self):
        self.logger.info("TC#0000: Check help link on Saved Date Ranges popup")
        expected_header = "Saved Date Ranges"
        left_menu = LeftMenuReporting(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        shared_reports_screen = SharedReportsScreen(self.driver)
        report_scheduler_popup = ReportSchedlulerPopup(self.driver)
        saved_date_ranges_popup = SavedDateRangesPopup(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_shared_reports()
        self.assertTrue(shared_reports_screen.check_report_is_presented())
        shared_reports_screen.select_single_report()
        self.assertTrue(ribbon_bar.check_create_schedule_button_is_enabled())
        ribbon_bar.click_button_create_schedule()
        self.assertTrue(report_scheduler_popup.check_popup_is_presented())
        report_scheduler_popup.click_button_open_data_range()
        self.assertTrue(saved_date_ranges_popup.check_popup_is_presented())
        saved_date_ranges_popup.click_icon_help()
        actual_header = saved_date_ranges_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, saved_date_ranges_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_baseline_popup(self):
        self.logger.info("TC#0000: Check help link on Baseline popup")
        expected_header = "Baseline"
        left_menu = LeftMenuReporting(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        shared_reports_screen = SharedReportsScreen(self.driver)
        report_scheduler_popup = ReportSchedlulerPopup(self.driver)
        saved_date_ranges_popup = SavedDateRangesPopup(self.driver)
        baseline_popup = BaselinePopup(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_shared_reports()
        self.assertTrue(shared_reports_screen.check_report_is_presented())
        shared_reports_screen.select_single_report()
        self.assertTrue(ribbon_bar.check_create_schedule_button_is_enabled())
        ribbon_bar.click_button_create_schedule()
        self.assertTrue(report_scheduler_popup.check_popup_is_presented())
        report_scheduler_popup.click_button_open_data_range()
        self.assertTrue(saved_date_ranges_popup.check_popup_is_presented())
        saved_date_ranges_popup.click_button_add()
        self.assertTrue(baseline_popup.check_popup_is_presented())
        baseline_popup.click_icon_help()
        actual_header = baseline_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, baseline_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_gadgets_directory_popup(self):
        self.logger.info("TC#0000: Check help link on Gadgets Directory popup")
        expected_header = "Gadgets Directory"
        left_menu = LeftMenuReporting(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        gadgets_directory_popup = GadgetsDirectoryPopup(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_my_dashboards()
        self.assertTrue(ribbon_bar.check_box_dashboards_is_enabled())
        left_menu.create_dashboard_if_not_exists()
        self.assertTrue(left_menu.check_dashboard_is_in_my_dashboards_list())
        left_menu.click_dashboard_in_my_dashboards_list()
        self.assertTrue(ribbon_bar.check_box_config_is_presented())
        ribbon_bar.click_button_add_gadget()
        self.assertTrue(gadgets_directory_popup.check_popup_is_presented())
        gadgets_directory_popup.click_icon_help()
        actual_header = gadgets_directory_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, gadgets_directory_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_R_help_link_on_dashboard_config_popup(self):
        self.logger.info("TC#0000: Check help link on Dashboard Config popup")
        expected_header = "Dashboard Config"
        left_menu = LeftMenuReporting(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        dashboard_config_popup = DashboardConfigPopup(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        left_menu.click_label_my_dashboards()
        self.assertTrue(ribbon_bar.check_box_dashboards_is_enabled())
        left_menu.create_dashboard_if_not_exists()
        self.assertTrue(left_menu.check_dashboard_is_in_my_dashboards_list())
        left_menu.click_dashboard_in_my_dashboards_list()
        self.assertTrue(ribbon_bar.check_box_config_is_presented())
        ribbon_bar.click_button_config()
        self.assertTrue(dashboard_config_popup.check_popup_is_presented())
        dashboard_config_popup.click_icon_help()
        actual_header = dashboard_config_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, dashboard_config_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_select_dashboard_popup(self):
        self.logger.info("TC#0000: Check help link on Select Dashboard popup")
        expected_header = "Select Dashboard"
        ribbon_bar = RibbonBar(self.driver)
        select_dashboard_popup = SelectDashboardPopup(self.driver)
        ribbon_bar.click_button_home()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_presented())
        ribbon_bar.click_menu_item_change_home_screen()
        self.assertTrue(select_dashboard_popup.check_popup_is_presented())
        select_dashboard_popup.click_icon_help()
        actual_header = select_dashboard_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, select_dashboard_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_user_settings_popup(self):
        self.logger.info("TC#0000: Check help link on User Settings popup")
        expected_header = "User Settings"
        ribbon_bar = RibbonBar(self.driver)
        user_settings_popup = UserSettingsPopup(self.driver)
        ribbon_bar.click_button_admin_user()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_presented())
        ribbon_bar.click_menu_item_settings()
        self.assertTrue(user_settings_popup.check_popup_is_presented())
        user_settings_popup.click_icon_help()
        actual_header = user_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, user_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_ribbon_bar(self):
        self.logger.info("TC#0000: Check help link on Ribbon bar")
        expected_header = "CMS Quick Help Videos"
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_button_console_guide()
        actual_header = ribbon_bar._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ribbon_bar._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_subscription_popup(self):
        self.logger.info("TC#0000: Check help link on Subscription popup")
        expected_header = "Subscriptions"
        subscription_popup = SubscriptionsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_button_subscriptions()
        self.assertIsNotNone(subscription_popup.check_popup_is_presented()) #VERIFY THIS ASSERTION
        subscription_popup.click_icon_help()
        actual_header = subscription_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, subscription_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_settings_popup(self):
        self.logger.info("TC#0000: Check help link on Settings popup")
        expected_header = "Settings"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_settings_popup_content_services_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Content Services tab")
        expected_header = "Content Services"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_content_services_label()
        self.assertTrue(settings_popup.check_content_services_tab_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_settings_popup_email_settings_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Email Settings tab")
        expected_header = "Email Settings"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_email_settings_label()
        self.assertTrue(settings_popup.check_email_settings_tab_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_settings_popup_initial_setup_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Initial Setup tab")
        expected_header = "Initial Setup"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_initial_setup_label()
        self.assertTrue(settings_popup.check_initial_setup_tab_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_settings_popup_locale_options_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Locale Options tab")
        expected_header = "Locale Options"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_locale_options_label()
        self.assertTrue(settings_popup.check_locale_options_tab_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    @unittest.skip("Skip test_RB_help_link_on_settings_popup_inventory_tab. Inventory tab is opened too long\n")
    def test_RB_help_link_on_settings_popup_inventory_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Inventory tab")
        expected_header = "Inventory"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_inventory_label()
        self.assertTrue(settings_popup.check_inventory_tab_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_settings_popup_user_options_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - User Options tab")
        expected_header = "User Options"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_user_options_label()
        self.assertTrue(settings_popup.check_user_options_tab_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_settings_popup_audit_log_settings_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Audit Log Settings tab")
        expected_header = "Audit Log Settings"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_audit_log_settings_label()
        self.assertTrue(settings_popup.check_audit_log_settings_tab_is_presented())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_client_settings_popup(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup")
        expected_header = "Client"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_presented())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_client_settings_popup_timers_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Timers tab")
        expected_header = "Timers"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_presented())
        client_settings_popup.click_timers_tab()
        self.assertTrue(client_settings_popup.check_timers_tab_is_presented())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_client_settings_popup_features_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Features tab")
        expected_header = "Features"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_presented())
        client_settings_popup.click_features_label()
        self.assertTrue(client_settings_popup.check_features_tab_is_presented())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_client_settings_popup_client_urls_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Client URLs tab")
        expected_header = "Client URLs"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_presented())
        client_settings_popup.click_client_urls_label()
        self.assertTrue(client_settings_popup.check_client_urls_tab_is_presented())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_client_settings_popup_reboot_ui_config_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Reboot UI Config tab")
        expected_header = "Reboot UI Config"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_presented())
        client_settings_popup.click_reboot_ui_config_tab()
        self.assertTrue(client_settings_popup.check_reboot_ui_config_tab_is_presented())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_client_settings_popup_client_proxy_settings_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Client Proxy Settings tab")
        expected_header = "Client Proxy Settings"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_presented())
        client_settings_popup.click_client_proxy_settings_tab()
        self.assertTrue(client_settings_popup.check_client_proxy_settings_tab_is_presented())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_currency_popup(self):
        self.logger.info("TC#0000: Check help link on Currency popup")
        expected_header = "Currency"
        ribbon_bar = RibbonBar(self.driver)
        currency_popup = CurrencyPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_presented())
        ribbon_bar.click_button_currency()
        self.assertTrue(currency_popup.check_popup_is_presented())
        currency_popup.click_icon_help()
        actual_header = currency_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, currency_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_weight_display_popup(self):
        self.logger.info("TC#0000: Check help link on Weight Display popup")
        expected_header = "Imperial Metric"
        ribbon_bar = RibbonBar(self.driver)
        weight_display_popup = WeightDisplayPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_presented())
        ribbon_bar.click_button_imperial_and_metric()
        self.assertTrue(weight_display_popup.check_popup_is_presented())
        weight_display_popup.click_icon_help()
        actual_header = weight_display_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, weight_display_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_manufacturer_alias_popup(self):
        self.logger.info("TC#0000: Check help link on Manufacturer Alias popup")
        expected_header = "Manufacturers"
        ribbon_bar = RibbonBar(self.driver)
        manufacturer_alias_popup = ManufacturerAliasPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_presented())
        ribbon_bar.click_button_makes()
        self.assertTrue(manufacturer_alias_popup.check_popup_is_presented())
        manufacturer_alias_popup.click_icon_help()
        actual_header = manufacturer_alias_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, manufacturer_alias_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_model_alias_popup(self):
        self.logger.info("TC#0000: Check help link on Model Alias popup")
        expected_header = "Models"
        ribbon_bar = RibbonBar(self.driver)
        model_alias_popup = ModelAliasPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_presented())
        ribbon_bar.click_button_models()
        self.assertTrue(model_alias_popup.check_popup_is_presented())
        model_alias_popup.click_icon_help()
        actual_header = model_alias_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, model_alias_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_column_sets_popup(self):
        self.logger.info("TC#0000: Check help link on Column Sets popup")
        expected_header = "Column Sets"
        ribbon_bar = RibbonBar(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        left_menu = LeftMenuDevices(self.driver)
        left_menu.open_menu_devices()
        left_menu.click_global_site_view_label()
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_presented())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_popup_is_presented())
        column_sets_popup.click_icon_help()
        actual_header = column_sets_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, column_sets_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_RB_help_link_on_initial_setup_popup(self):
        self.logger.info("TC#0000: Check help link on Initial Setup popup")
        expected_header = "Initial Setup"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        initial_setup_popup = InitialSetupPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_presented())
        settings_popup.click_initial_setup_label()
        self.assertTrue(settings_popup.check_initial_setup_tab_is_presented())
        settings_popup.click_button_run_initial_setup()
        self.assertTrue(initial_setup_popup.check_popup_is_presented())
        initial_setup_popup.click_icon_help()
        actual_header = initial_setup_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, initial_setup_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_applications_screen(self):
        self.logger.info("TC#0000: Check help link on Applications screen")
        expected_header = "Applications"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        applications_screen = ApplicationsScreen(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_applications_label()
        self.assertTrue(applications_screen.check_screen_is_presented())
        applications_screen.click_icon_help()
        actual_header = applications_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, applications_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_patch_manager_screen(self):
        self.logger.info("TC#0000: Check help link on Patch Manager screen")
        expected_header = "Patch Manager"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_patch_manager_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        patch_manager_screen.click_icon_help()
        actual_header = patch_manager_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, patch_manager_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_manage_install_media_screen(self):
        self.logger.info("TC#0000: Check help link on Manage Install Media screen")
        expected_header = "Media Manager"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        manage_install_media_screen = ManageInstallMediaScreen(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_patch_manager_label_is_presented())
        left_menu.expand_media_management_list()
        self.assertTrue(left_menu.check_my_patches_label_is_presented())
        left_menu.click_my_patches_label()
        self.assertTrue(manage_install_media_screen.check_screen_is_presented())
        manage_install_media_screen.click_icon_help()
        actual_header = manage_install_media_screen._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, manage_install_media_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_create_application_wizard_popup(self):
        self.logger.info("TC#0000: Check help link on Create Application Wizard popup")
        expected_header = "Create"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        create_application_wizard_popup = CreateApplicationWizardPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_applications_label()
        self.assertTrue(ribbon_bar.check_box_applications_is_presented())
        ribbon_bar.click_button_create()
        self.assertTrue(create_application_wizard_popup.check_popup_is_presented())
        create_application_wizard_popup.click_icon_help()
        actual_header = create_application_wizard_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, create_application_wizard_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_installers_popup(self):
        self.logger.info("TC#0000: Check help link on Installers popup")
        expected_header = "Installers"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        create_application_popup = CreateApplicationWizardPopup(self.driver)
        installers_popup = InstallersPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_applications_label()
        self.assertTrue(ribbon_bar.check_box_applications_is_presented())
        ribbon_bar.click_button_create()
        self.assertTrue(create_application_popup.check_popup_is_presented())
        create_application_popup.click_button_choose_installer_on_sever()
        self.assertTrue(installers_popup.check_popup_is_presented())
        installers_popup.click_icon_help()
        actual_header = installers_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, create_application_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_create_update_wizard_popup(self):
        self.logger.info("TC#0000: Check help link on Create Update Wizard popup")
        expected_header = "Create"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        create_update_wizard_popup = CreateUpdateWizardPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        ribbon_bar.click_button_create()
        self.assertTrue(create_update_wizard_popup.check_popup_is_presented())
        create_update_wizard_popup.click_icon_help()
        actual_header = create_update_wizard_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, create_update_wizard_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_advanced_editor_popup(self):
        self.logger.info("TC#0000: Check help link on Advanced Editor popup")
        expected_header = "Advanced Editor"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_pre_requisites_label()
        self.assertTrue(advanced_editor_popup.check_tab_pre_requisites_is_presented())
        advanced_editor_popup.click_icon_help()
        actual_header = advanced_editor_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, advanced_editor_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_pre_requisites_popup(self):
        self.logger.info("TC#0000: Check help link on Pre-Requisites popup")
        expected_header = "Pre-requisites"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        pre_requisites_popup = SelectPreRequisitesPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_pre_requisites_label()
        self.assertTrue(advanced_editor_popup.check_tab_pre_requisites_is_presented())
        advanced_editor_popup.click_button_add()
        self.assertTrue(pre_requisites_popup.check_popup_is_presented())
        pre_requisites_popup.click_icon_help()
        actual_header = pre_requisites_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, pre_requisites_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_select_install_media_popup(self):
        self.logger.info("TC#0000: Check help link on Select Install Media popup")
        expected_header = "Download Update"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        select_install_media_popup = SelectInstallMediaPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.click_button_add()
        self.assertTrue(select_install_media_popup.check_popup_is_presented())
        select_install_media_popup.click_icon_help()
        actual_header = select_install_media_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, select_install_media_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_component_popup(self):
        self.logger.info("TC#0000: Check help link on Component popup")
        expected_header = "Component"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_icon_help()
        actual_header = component_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, component_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_filters_popup(self):
        self.logger.info("TC#0000: Check help link on Filters popup")
        expected_header = "Filters"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        filters_popup = FiltersPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_button_edit_filters()
        self.assertTrue(filters_popup.check_popup_is_presented())
        filters_popup.click_icon_help()
        actual_header = filters_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, filters_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_existing_software_update_detection_popup(self):
        self.logger.info("TC#0000: Check help link on Existing Software Update Detection popup")
        expected_header = "Existing Software Update Detection"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        existing_software_update_detection_popup = ExistingSoftwareUpdateDetectionPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_button_edit_detectors()
        self.assertTrue(existing_software_update_detection_popup.check_popup_is_presented())
        existing_software_update_detection_popup.click_icon_help()
        actual_header = existing_software_update_detection_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header,
                         existing_software_update_detection_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_deployments_popup(self):
        self.logger.info("TC#0000: Check help link on Deployments popup")
        expected_header = "Deployments"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        deployments_popup = DeploymentsPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_button_edit_deployments()
        self.assertTrue(deployments_popup.check_popup_is_presented())
        deployments_popup.click_icon_help()
        actual_header = deployments_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, deployments_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_install_commands_popup(self):
        self.logger.info("TC#0000: Check help link on Install Commands popup")
        expected_header = "Install Commands"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        deployments_popup = DeploymentsPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        install_commands_popup = InstallCommandsPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_button_edit_deployments()
        self.assertTrue(deployments_popup.check_popup_is_presented())
        deployments_popup.click_install_commands_label()
        self.assertTrue(deployments_popup.check_tab_install_commands_is_presented())
        deployments_popup.click_button_edit_commands()
        self.assertTrue(install_commands_popup.check_popup_is_presented())
        install_commands_popup.click_icon_help()
        actual_header = install_commands_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, install_commands_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_uninstall_commands_popup(self):
        self.logger.info("TC#0000: Check help link on Uninstall Commands popup")
        expected_header = "Uninstall Commands"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        deployments_popup = DeploymentsPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        uninstall_commands_popup = UninstallCommandsPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_button_edit_deployments()
        self.assertTrue(deployments_popup.check_popup_is_presented())
        deployments_popup.click_uninstall_commands_label()
        self.assertTrue(deployments_popup.check_tab_uninstall_commands_is_presented())
        deployments_popup.click_button_edit_commands()
        self.assertTrue(uninstall_commands_popup.check_popup_is_presented())
        uninstall_commands_popup.click_icon_help()
        actual_header = uninstall_commands_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, uninstall_commands_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_superseding_patches_popup(self):
        self.logger.info("TC#0000: Check help link on Superseding Patches popup")
        expected_header = "Superseding Patches"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        superseding_patches_popup = SupersedingPatchesPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_button_view_details()
        self.assertTrue(superseding_patches_popup.check_popup_is_presented())
        superseding_patches_popup.click_icon_help()
        actual_header = superseding_patches_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, superseding_patches_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_select_superseding_patches_popup(self):
        self.logger.info("TC#0000: Check help link on Select Superseding Patches popup")
        expected_header = "Select Superseding Patches"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        advanced_editor_popup = AdvancedEditorPopup(self.driver)
        component_popup = ComponentPopup(self.driver)
        superseding_patches_popup = SupersedingPatchesPopup(self.driver)
        select_superseding_patches_popup = SelectSupersedingPatchesPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        patch_manager_screen.select_first_row_in_table()
        self.assertTrue(patch_manager_screen.check_first_row_is_selected())
        ribbon_bar.click_button_edit()
        self.assertTrue(advanced_editor_popup.check_popup_is_presented())
        advanced_editor_popup.click_components_label()
        self.assertTrue(advanced_editor_popup.check_tab_components_is_presented())
        advanced_editor_popup.select_first_row_in_table()
        self.assertTrue(advanced_editor_popup.check_first_row_is_selected())
        advanced_editor_popup.click_button_edit()
        self.assertTrue(component_popup.check_popup_is_presented())
        component_popup.click_button_view_details()
        self.assertTrue(superseding_patches_popup.check_popup_is_presented())
        superseding_patches_popup.click_button_edit()
        self.assertTrue(select_superseding_patches_popup.check_popup_is_presented())
        select_superseding_patches_popup.click_icon_help()
        actual_header = select_superseding_patches_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, select_superseding_patches_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_create_patch_group_popup(self):
        self.logger.info("TC#0000: Check help link on Create Patch Group popup")
        expected_header = "By Group"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        create_patch_group_popup = CreatePatchGroupPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.expand_patch_manager_list()
        self.assertTrue(left_menu.check_by_group_label_is_presented())
        left_menu.click_by_group_label()
        self.assertTrue(ribbon_bar.check_box_patch_groups_is_presented())
        ribbon_bar.click_button_create_group()
        self.assertTrue(create_patch_group_popup.check_popup_is_presented())
        create_patch_group_popup.click_icon_help()
        actual_header = create_patch_group_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, create_patch_group_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_select_patches_popup(self):
        self.logger.info("TC#0000: Check help link on Select Patches popup")
        expected_header = "By Group"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        create_patch_group_popup = CreatePatchGroupPopup(self.driver)
        select_patches_popup = SelectPatchesPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.expand_patch_manager_list()
        self.assertTrue(left_menu.check_by_group_label_is_presented())
        left_menu.click_by_group_label()
        self.assertTrue(ribbon_bar.check_box_patch_groups_is_presented())
        ribbon_bar.click_button_create_group()
        self.assertTrue(create_patch_group_popup.check_popup_is_presented())
        create_patch_group_popup.click_button_edit_members()
        self.assertTrue(select_patches_popup.check_popup_is_presented())
        select_patches_popup.click_icon_help()
        actual_header = select_patches_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, select_patches_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_edit_patch_group_popup(self):
        self.logger.info("TC#0000: Check help link on Edit Patch Group popup")
        expected_header = "By Group"
        name = Variables.help_test
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        edit_patch_group_popup = EditPatchGroupPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.expand_patch_manager_list()
        self.assertTrue(left_menu.check_by_group_label_is_presented())
        left_menu.click_by_group_label()
        self.assertTrue(ribbon_bar.check_box_patch_groups_is_presented())
        left_menu.create_patch_group_if_not_exists(name)
        self.assertTrue(left_menu.check_patch_group_is_in_by_group_list(name))
        left_menu.click_group_in_by_group_list(name)
        ribbon_bar.click_button_edit_group()
        self.assertTrue(edit_patch_group_popup.check_popup_is_presented())
        edit_patch_group_popup.click_icon_help()
        actual_header = edit_patch_group_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, edit_patch_group_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_query_designer_popup(self):
        self.logger.info("TC#0000: Check help link on Query Designer popup (Software/Patch Manger")
        expected_header = "Queries"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        query_designer = QueryDesignerPopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.expand_patch_manager_list()
        self.assertTrue(left_menu.check_by_group_label_is_presented())
        left_menu.click_by_query_rule_label()
        self.assertTrue(ribbon_bar.check_box_patch_query_rules_is_presented())
        ribbon_bar.click_button_create_query()
        self.assertTrue(query_designer.check_popup_is_presented())
        query_designer.click_icon_help()
        actual_header = query_designer._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, query_designer._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_patch_manager_settings_popup(self):
        self.logger.info("TC#0000: Check help link on Patch Manager Settings popup")
        expected_header = "Patch Manager Settings"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        patch_manager_settings_popup = PatchManagerSettingsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_tab_advanced_is_presented())
        self.assertTrue(ribbon_bar.check_box_updates_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_tab_advanced_is_presented())
        ribbon_bar.click_button_settings()
        self.assertTrue(patch_manager_settings_popup.check_popup_is_presented())
        patch_manager_settings_popup.click_icon_help()
        actual_header = patch_manager_settings_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, patch_manager_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_management_list_popup(self):
        self.logger.info("TC#0000: Check help link on Management Tree popup")
        expected_header = "Management Tree"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        patch_manager_screen = PatchMangerScreen(self.driver)
        management_list_popup = ManagementTreePopup(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(patch_manager_screen.check_screen_is_presented())
        patch_manager_screen.click_at_filter_field()
        self.assertTrue(management_list_popup.check_popup_is_presented())
        management_list_popup.click_icon_help()
        actual_header = management_list_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, management_list_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_scan_schedule_popup(self):
        self.logger.info("TC#0000: Check help link on Scan Schedule popup")
        expected_header = "Scan Schedule"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        scan_schedule_popup = ScanSchedulePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(ribbon_bar.check_box_move_to_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_tab_advanced_is_presented())
        ribbon_bar.click_button_to_be_checked()
        self.assertTrue(scan_schedule_popup.check_popup_is_presented())
        scan_schedule_popup.click_icon_help()
        actual_header = scan_schedule_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, scan_schedule_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_S_help_link_on_import_software_update_definition_popup(self):
        self.logger.info("TC#0000: Check help link on Import Software Update Definitions popup")
        expected_header = "Import Definition"
        left_menu = LeftMenuSoftwareAndPatchManager(self.driver)
        import_software_update_definition_popup = ImportSoftwareUpdateDefinitionsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_applications_label_is_presented())
        ribbon_bar.open_tab_advanced()
        self.assertTrue(ribbon_bar.check_tab_advanced_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(ribbon_bar.check_box_import_is_presented())
        ribbon_bar.click_button_import()
        self.assertTrue(import_software_update_definition_popup.check_popup_is_presented())
        import_software_update_definition_popup.click_icon_help()
        actual_header = import_software_update_definition_popup._get_help_frame_header()
        self.assertEqual(
           expected_header, actual_header, import_software_update_definition_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_scheduled_tasks_screen(self):
        self.logger.info("TC#0000: Check help link on Scheduled Tasks screen")
        expected_header = "Scheduled Tasks"
        left_menu = LeftMenuTasks(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.click_scheduled_tasks_label()
        self.assertTrue(tasks_screen.check_screen_is_presented())
        tasks_screen.click_icon_help()
        actual_header = tasks_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, tasks_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_discovery_tasks_screen(self):
        self.logger.info("TC#0000: Check help link on Discovery Tasks screen")
        expected_header = "Perform a Discovery to find all your devices"
        left_menu = LeftMenuTasks(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_discover_label()
        self.assertTrue(tasks_screen.check_screen_is_presented())
        tasks_screen.click_icon_help()
        actual_header = tasks_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, tasks_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_software_deployments_screen(self):
        self.logger.info("TC#0000: Check help link on Software Deployments screen")
        expected_header = "Software Deployment"
        left_menu = LeftMenuTasks(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_software_deployment_label_is_presented())
        left_menu.click_software_deployment_label()
        self.assertTrue(tasks_screen.check_screen_is_presented())
        tasks_screen.click_icon_help()
        actual_header = tasks_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, tasks_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_patch_manager_screen(self):
        self.logger.info("TC#0000: Check help link on Patch Manager screen")
        expected_header = "Patch Deployment"
        left_menu = LeftMenuTasks(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_patch_manager_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(tasks_screen.check_screen_is_presented())
        tasks_screen.click_icon_help()
        actual_header = tasks_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, tasks_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_discover_devices_popup(self):
        self.logger.info("TC#0000: Check help link on Discover Devices popup (Tasks)")
        expected_header = "Discovery"
        left_menu = LeftMenuTasks(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        discover_devices_popup = DiscoverDevicesPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_discover_label()
        self.assertTrue(ribbon_bar.check_box_discovery_task_is_presented())
        ribbon_bar.click_button_create()
        self.assertTrue(discover_devices_popup.check_popup_is_presented())
        discover_devices_popup.click_icon_help()
        actual_header = discover_devices_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, discover_devices_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_software_deployment_popup(self):
        self.logger.info("TC#0000: Check help link on Software Deployment popup (Tasks)")
        expected_header = "Software Deployment Wizard"
        left_menu = LeftMenuTasks(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        software_deployment_popup = SoftwareDeploymentPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_software_deployment_label_is_presented())
        left_menu.click_software_deployment_label()
        self.assertTrue(ribbon_bar.check_box_software_deployment_is_presented())
        ribbon_bar.click_button_create()
        self.assertTrue(software_deployment_popup.check_popup_is_presented())
        software_deployment_popup.click_icon_help()
        actual_header = software_deployment_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, software_deployment_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_patch_manager_scanning_popup(self):
        self.logger.info("TC#0000: Check help link on Patch Manager Scanning popup (Tasks)")
        expected_header = "Software Update Scanning"
        left_menu = LeftMenuTasks(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        patch_manager_scanning_popup = PatchManagerScanningPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_patch_manager_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(ribbon_bar.check_box_patch_manager_is_presented())
        ribbon_bar.click_button_scan()
        self.assertTrue(patch_manager_scanning_popup.check_popup_is_presented())
        patch_manager_scanning_popup.click_icon_help()
        actual_header = patch_manager_scanning_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, patch_manager_scanning_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_deploy_software_updates_popup(self):
        self.logger.info("TC#0000: Check help link on Deploy Software Updates popup (Tasks)")
        expected_header = "Deploy Software Updates"
        left_menu = LeftMenuTasks(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        deploy_software_updates_popup = DeploySoftwareUpdatesPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_patch_manager_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(ribbon_bar.check_box_patch_manager_is_presented())
        ribbon_bar.click_button_scan_and_deploy()
        self.assertTrue(deploy_software_updates_popup.check_popup_is_presented())
        deploy_software_updates_popup.click_icon_help()
        actual_header = deploy_software_updates_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, deploy_software_updates_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_scanned_addresses_popup(self):
        self.logger.info("TC#0000: Check help link on Scanned Addresses popup")
        expected_header = "Scanned Addresses"
        task_name = Variables.help_test_discovery_task
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        scanned_addresses_popup = ScannedAddressesPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_discover_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_label_addresses_to_scan_is_presented())
        screen_tasks.click_label_addresses_to_scan()
        self.assertTrue(scanned_addresses_popup.check_popup_is_presented())
        scanned_addresses_popup.click_icon_help()
        actual_header = scanned_addresses_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, scanned_addresses_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_discovered_devices_popup(self):
        self.logger.info("TC#0000: Check help link on Discovered Devices popup")
        expected_header = "Discovered Devices"
        task_name = Variables.help_test_discovery_task
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        discovered_devices_popup = DiscoverdDevicesPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_discover_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_label_devices_discovered_is_presented())
        screen_tasks.click_label_devices_discovered()
        self.assertTrue(discovered_devices_popup.check_popup_is_presented())
        discovered_devices_popup.click_icon_help()
        actual_header = discovered_devices_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, discovered_devices_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    def test_T_help_link_on_unknown_devices_popup(self):
        self.logger.info("TC#0000: Check help link on Unknown Devices popup")
        expected_header = "Unknown Devices"
        task_name = Variables.help_test_discovery_task
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        unknown_devices_popup = UnknownDevicesPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_discover_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_label_unknown_devices_is_presented())
        screen_tasks.click_label_unknown_devices()
        self.assertTrue(unknown_devices_popup.check_popup_is_presented())
        unknown_devices_popup.click_icon_help()
        actual_header = unknown_devices_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, unknown_devices_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    @unittest.skip("Skip test_T_help_link_on_successful_devices_popup.\n")
    def test_T_help_link_on_successful_devices_popup(self):
        self.logger.info("TC#0000: Check help link on Successful Devices popup")
        expected_header = "Successful Devices"
        task_name = Variables.help_test_scan_task
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        successful_devices_popup = SuccessfulDevicesPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_label_devices_successfully_scanned_is_presented())
        screen_tasks.click_label_devices_successfully_scannned()
        self.assertTrue(successful_devices_popup.check_popup_is_presented())
        successful_devices_popup.click_icon_help()
        actual_header = successful_devices_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, successful_devices_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    @unittest.skip("Skip test_T_help_link_on_devices_in_progress_popup.\n")
    def test_T_help_link_on_devices_in_progress_popup(self):
        self.logger.info("TC#0000: Check help link on Devices In Progress popup")
        expected_header = "Devices In Progress"
        task_name = Variables.help_test_scan_task
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        devices_in_progress_popup = DevicesInProgressPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_label_devices_still_to_be_done_is_presented())
        screen_tasks.click_label_devices_still_to_be_done()
        self.assertTrue(devices_in_progress_popup.check_popup_is_presented())
        devices_in_progress_popup.click_icon_help()
        actual_header = devices_in_progress_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, devices_in_progress_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    @unittest.skip("Skip test_T_help_link_on_failed_devices_popup.\n")
    def test_T_help_link_on_failed_devices_popup(self):
        self.logger.info("TC#0000: Check help link on Failed Devices popup")
        expected_header = "Failed Devices"
        task_name = Variables.help_test_scan_task
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        failed_devices_popup = FailedDevicesPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_label_devices_failed_to_patch_is_presented())
        screen_tasks.click_label_devices_failed_to_patch()
        self.assertTrue(failed_devices_popup.check_popup_is_presented())
        failed_devices_popup.click_icon_help()
        actual_header = failed_devices_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, failed_devices_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    @unittest.skip("Skip test_T_help_link_on_devices_with_partial_success_popup.\n")
    def test_T_help_link_on_devices_with_partial_success_popup(self):
        self.logger.info("TC#0000: Check help link on Devices with Partial Success popup")
        expected_header = "Devices with Partial Success"
        task_name = Variables.help_test_scan_task
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        devices_with_partial_success_popup = DevicesWithPartialSuccessPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_label_devices_partially_patched_is_presented())
        screen_tasks.click_label_devices_partially_patched()
        self.assertTrue(devices_with_partial_success_popup.check_popup_is_presented())
        devices_with_partial_success_popup.click_icon_help()
        actual_header = devices_with_partial_success_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, devices_with_partial_success_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

        "Devices with Partial Success"

    def test_T_help_link_on_patch_manager_popup(self):
        self.logger.info("TC#0000: Check help link on Patch Manager popup (Tasks)")
        expected_header = "Patch Manager"
        task_name = Variables.help_test_scan_task
        device = Variables.vrep
        left_menu = LeftMenuTasks(self.driver)
        screen_tasks = TasksScreen(self.driver)
        patch_manager_popup = PatchManagerPopup(self.driver)
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_opened())
        left_menu.expand_scheduled_tasks_list()
        self.assertTrue(left_menu.check_discover_label_is_presented())
        left_menu.click_patch_manager_label()
        self.assertTrue(screen_tasks.check_screen_is_presented())
        screen_tasks.search_task(task_name)
        self.assertTrue(screen_tasks.check_task_is_presented(task_name))
        screen_tasks.click_task_in_table(task_name)
        self.assertTrue(screen_tasks.check_tab_devices_is_presented())
        screen_tasks.click_tab_devices()
        self.assertTrue(screen_tasks.check_device_is_present_in_table(device))
        screen_tasks.click_device_in_table(device)
        self.assertTrue(screen_tasks.check_button_view_software_update_is_presented())
        screen_tasks.click_button_view_software_update_details()
        self.assertTrue(patch_manager_popup.check_popup_is_presented())
        patch_manager_popup.click_icon_help()
        actual_header = patch_manager_popup._get_help_frame_header()
        self.assertEqual(
            expected_header, actual_header, patch_manager_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED")

    # def test_create_and_config_site(self):
    #     self.logger.info("TC#0000: Create and config Site")
    #     main_page = MainPage(self.driver)
    #     cond = main_page.create_and_config_site()
    #     self.assertTrue(cond)
    #     self.logger.info("TEST PASSED")
    #
    # def test_run_discovery_task(self):
    #     self.logger.info("TC#0000: Run a Discovery task")
    #     main_page = MainPage(self.driver)
    #     cond = main_page.run_discovery_task_if_not_exists(Variables.help_test_discovery_task)
    #     self.assertTrue(cond)
    #     self.logger.info("TEST PASSED")

    # def test_run_scan_task(self):
    #     self.logger.info("TC#0000: Run a Patch Scan task")
    #     task_name = Variables.help_test_discovery_task
    #     device = Variables.vrep
    #     site_name = Variables.help_test
    #     main_page = MainPage(self.driver)
    #     cond = main_page.run_patch_scan_task_on_single_device_if_not_exists(task_name=task_name, site_name=site_name,
    #                                                                         device_name=device)
    #     self.assertTrue(cond)
    #     self.logger.info("TEST PASSED")

    def tearDown(self):
        base_actions = BaseActions(self.driver)
        base_actions._close_help_window()
        base_actions._close_popups()
        # left_menu = BaseLeftMenu(self.driver)
        # left_menu.open_menu_home()
        self.logger.info("[Test end]\n")

    @classmethod
    def tearDownClass(cls):
        cls.logger = logging.getLogger(__name__)
        cls.logger.info("End testing\n")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())
    # logger.info('Started MainPageHelpLinks')
