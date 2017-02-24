#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import unittest

from _feature_objects.feature_left_menu import *
from _feature_objects.feature_ribbon_bar import *
from _feature_objects.feature_screen import *
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
        self.logger.info("[Test start]")
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        # left_menu_devices = LeftMenuDevices(self.driver)
        # left_menu_devices.open_menu_devices()
        # left_menu_devices.expand_global_site_view_tree()

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
        self.logger.info("TEST PASSED!!!")

    # def test_open_left_menus(self):
    #     print ("\n" + "TC#xxxx. Open left side menus")
    #     left_menu = BaseLeftMenu(self.driver)
    #     left_menu.menu_devices()
    #     left_menu.menu_administration()
    #     left_menu.menu_password_reset()
    #     left_menu.menu_reporting()
    #     left_menu.menu_tasks()
    #     # left_menu.open_menu_password_reset()
    #     print ("TEST PASSED!!!" + "\n")

    def test_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup")
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        print ("TEST PASSED!!!" + "\n")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name")
        sitename = "New site #9101"
        site_name_popup = SiteNamePopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.delete_site_if_exists(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        print ("TEST PASSED!!!" + "\n")

    def test_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field")
        left_menu_devices = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.click_button_cancel()
        self.assertFalse(site_name_popup.check_popup_is_present())
        print ("TEST PASSED!!!" + "\n")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name")
        sitename = "Default Site"
        left_menu_devices = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        error_popup = ErrorPopup(self.driver)
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(error_popup.check_popup_is_present())
        error_popup.click_button_ok()
        self.assertFalse(error_popup.check_popup_is_present())
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.click_system_button_close()
        self.assertFalse(site_name_popup.check_popup_is_present())
        print ("TEST PASSED!!!" + "\n")

    def test_create_site_with_fifty_one_symbols(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        fifty_symbols_name = "51symbols51symbols51symbols51symbols51symbols!<ok>"
        fifty_one_symbols_name = fifty_symbols_name + "1"
        left_menu_devices = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.delete_site_if_exists(fifty_symbols_name)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        left_menu_devices.delete_site_if_exists(fifty_one_symbols_name)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(fifty_one_symbols_name))
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.enter_text_into_name_text_field(fifty_one_symbols_name)
        site_name_popup.click_button_ok()
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(fifty_one_symbols_name))
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        left_menu_devices.delete_site_from_global_site_view_tree(fifty_symbols_name)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        print ("TEST PASSED!!!" + "\n")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
        sitename = "Site #9118"
        subsitename_one = sitename + "-01"
        subsitename_two = sitename + "-02"
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.delete_site_if_exists(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.create_new_site(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.create_new_subsite(sitename, subsitename_one)
        self.assertTrue(left_menu_devices.check_subsite_is_in_parent_site(sitename, subsitename_one))
        left_menu_devices.create_new_subsite(sitename, subsitename_two)
        self.assertTrue(left_menu_devices.check_subsite_is_in_parent_site(sitename, subsitename_two))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        print ("TEST PASSED!!!" + "\n")

    def tearDown(self):
        base_actions = BaseActions(self.driver)
        base_actions._close_help_window()
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
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        print ("TEST PASSED!!!" + "\n")

    def test_open_configuration_popup_from_global_site_view(self):
        print ("\n" + "TC#9228. Devices screen. Open Configuration popup from the Global Site View")
        configuration_popup = ConfigurationPopup(self.driver)
        site_tab = SiteTab(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        self.assertFalse(configuration_popup.check_tabs_panel_is_present())
        self.assertTrue(site_tab.check_name_text_field_disabled())
        self.assertEqual("Global Site View", site_tab.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        print ("TEST PASSED!!!" + "\n")

    def test_open_configuration_popup_from_default_site(self):
        print ("\n" + "TC#9230. Devices screen. Open Configuration popup from the Default Site main label")
        left_menu_devices = LeftMenuDevices(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        site_tab = SiteTab(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        self.assertTrue(site_tab.check_name_text_field_disabled())
        self.assertEqual("Default Site", site_tab.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        print ("TEST PASSED!!!" + "\n")

    def test_open_configuration_popup_from_created_site(self):
        print ("\n" + "TC#9236. Devices screen. Open Configuration popup from the created site")
        sitename = "Site#9236"
        ribbon_bar = RibbonBar(self.driver)
        site_tab = SiteTab(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(
            configuration_popup._is_element_present(configuration_popup.TAB_SITE))  # add verification method to class
        self.assertFalse(configuration_popup._is_element_disabled(
            site_tab.FIELD_NAME))  # add verification method to class
        self.assertEqual(sitename, site_tab.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        print ("TEST PASSED!!!" + "\n")

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
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        site_tab = SiteTab(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.delete_site_if_exists(sitename + modifed)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename + modifed))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertFalse(site_tab.check_name_text_field_disabled())
        self.assertEqual(sitename, site_tab.get_name_text_field_value())
        site_tab.enter_text_into_name_text_field(modifed)
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename + modifed))
        left_menu_devices.click_site_in_global_site_view_tree(sitename + modifed)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertEqual(sitename + modifed, site_tab.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        left_menu_devices.delete_site_from_global_site_view_tree(sitename + modifed)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename + modifed))
        left_menu_devices.delete_site_if_exists(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        print ("TEST PASSED!!!" + "\n")

    def test_configuration_popup_open_column_set_designer_popup(self):
        print ("\n" + "TC#9238. Devices screen. Configuration popup. Open Column Set Designer popup")
        configuration_popup = ConfigurationPopup(self.driver)
        column_set_designer = ColumnSetDesignerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        site_tab = SiteTab(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        site_tab.click_button_new()
        self.assertTrue(configuration_popup.check_popup_is_present())
        column_set_designer.click_system_button_close()
        self.assertFalse(column_set_designer.check_popup_is_present())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        print ("TEST PASSED!!!" + "\n")

    def test_configuration_popup_apply_column_set(self):
        print ("\n" + "TC#9239. Devices screen. Configuration popup. Apply Column set to the site")
        sitename = "Site#9239"
        columnset1 = "ColumnSet#9239-01"
        columnset2 = "test1"
        columns_list1 = ["Device Name", "OS Name", "Caption", "IP Address"]
        columns_list2 = ["Device Name", "Device ID", "Domain", "Site", "User Name"]
        left_menu_devices = LeftMenuDevices(self.driver)
        site_tab = SiteTab(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.click_global_site_view_label()
        ribbon_bar.click_tab_view()
        self.assertTrue(ribbon_bar.check_button_edit_or_create_is_present())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_popup_is_present())
        column_sets_popup.delete_columnset_if_exists(columnset1)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnset1))
        column_sets_popup.delete_columnset_if_exists(columnset2)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnset2))
        column_sets_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_popup_is_present())
        column_set_designer_popup.create_columnset(columnset1, columns_list1)
        self.assertFalse(column_set_designer_popup.check_popup_is_present())
        self.assertTrue(column_sets_popup.check_is_columnset_present(columnset1))
        column_sets_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_popup_is_present())
        column_set_designer_popup.create_columnset(columnset2, columns_list2)
        self.assertFalse(column_set_designer_popup.check_popup_is_present())
        self.assertTrue(column_sets_popup.check_is_columnset_present(columnset2))
        column_sets_popup.click_button_ok()
        self.assertFalse(column_sets_popup.check_popup_is_present())
        ribbon_bar.click_tab_home()
        self.assertTrue(ribbon_bar.check_button_exit_is_present())
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        site_tab.select_columnset_in_drop_down_list(columnset1)
        self.assertTrue(site_tab.check_columnset_is_selected_from_drop_down_list(columnset1))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(devices_screen.check_columns_are_present(columns_list1))
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        site_tab.select_columnset_in_drop_down_list(columnset2)
        self.assertTrue(site_tab.check_columnset_is_selected_from_drop_down_list(columnset2))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(devices_screen.check_columns_are_present(columns_list2))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        print ("TEST PASSED!!!" + "\n")

    def test_configuration_popup_create_column_set(self):
        print ("\n" + "TC#9999. Devices screen. Configuration popup. Create column set")
        sitename = "Site#9999"
        columnsetname = "ColumnSet#9999-01"
        columns_list = ["Device Name", "Device ID", "Domain", "Site"]
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        site_tab = SiteTab(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_tab_view()
        self.assertTrue(ribbon_bar.check_button_edit_or_create_is_present())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_popup_is_present())
        column_sets_popup.delete_columnset_if_exists(columnsetname)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnsetname))
        column_sets_popup.click_button_ok()
        self.assertFalse(column_sets_popup.check_popup_is_present())
        ribbon_bar.click_tab_home()
        self.assertTrue(ribbon_bar.check_button_exit_is_present())
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        site_tab.click_button_new()
        self.assertTrue(column_set_designer_popup.check_popup_is_present())
        column_set_designer_popup.create_columnset(columnsetname, columns_list)
        self.assertFalse(column_set_designer_popup.check_popup_is_present())
        site_tab.select_columnset_in_drop_down_list(columnsetname)
        self.assertTrue(site_tab.check_columnset_is_selected_from_drop_down_list(columnsetname))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(devices_screen.check_columns_are_present(columns_list))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        print ("TEST PASSED!!!" + "\n")

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
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.expand_global_site_view_tree()

    def test_delete_created_site_from_global_site_view_tree(self):
        self.logger.info("TC#9607. Devices screen. Delete created site from Global Site View tree")
        sitename = "Test#9607"
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        self.logger.info("TEST PASSED!!!")

    def test_delete_default_site_from_global_site_view_tree(self):
        self.logger.info("TC#8888. Devices screen. Delete Default site from Global Site View tree")
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        unable_to_remove_popup = UnableToRemovePopup(self.driver)
        left_menu_devices.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(unable_to_remove_popup.check_popup_is_present())
        unable_to_remove_popup.click_button_ok()
        self.assertTrue(left_menu_devices.check_default_site_is_in_global_site_view_tree())
        self.logger.info("TEST PASSED!!!")

    def test_delete_subsite_from_site_tree(self):
        self.logger.info("TC#3333. Devices screen. Delete subsite from Global Site View tree")
        sitename = "TC#3333"
        subsitename = "TC#3333-01"
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu_devices.delete_site_if_exists(sitename)
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.create_new_subsite(sitename, subsitename)
        self.assertTrue(left_menu_devices.check_subsite_is_in_parent_site(sitename, subsitename))
        left_menu_devices.click_subsite_in_site_tree(sitename, subsitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu_devices.check_subsite_is_in_parent_site(sitename, subsitename))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.logger.info("TEST PASSED!!!")

    def test_delete_site_with_subsite(self):
        self.logger.info("TC#0000. Devices screen. Delete site with subsite from Global Site View tree")
        sitename = "TC#0000"
        subsitename = "TC#0000-01"
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu_devices.delete_site_if_exists(sitename)
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.create_new_subsite(sitename, subsitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(subsitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu_devices.check_subsite_is_in_parent_site(sitename, subsitename))
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        self.logger.info("TEST PASSED!!!")

    def test_cancel_site_deletion_from_global_site_view(self):
        self.logger.info("TC#1111. Devices screen. Cancel site deletion")
        sitename = "TC#1111"
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_cancel()
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.logger.info("TEST PASSED!!!")

    def test_open_are_you_sure_popup(self):
        self.logger.info("TC#2222. Devices screen. Open Are you sure popup")
        sitename = "TC#2222"
        left_menu_devices = LeftMenuDevices(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_system_button_close()
        self.assertFalse(are_you_sure_popup.check_popup_is_present())
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.logger.info("TEST PASSED!!!")

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
    logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    logger.addHandler(console)

    @classmethod
    def setUpClass(cls):
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
        self.logger.info("TEST PASSED!!!")

    def test_help_link_on_reset_password_popup(self):
        self.logger.info("TC#0000: Check help link on Password Reset popup")
        expected_header = "Reset Password"
        login_page = LoginPage(self.driver)
        reset_password_popup = ResetPasswordPopup(self.driver)
        login_page.click_reset_password_label()
        self.assertTrue(reset_password_popup.check_popup_is_present())
        reset_password_popup.click_icon_help()
        actual_header = reset_password_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, reset_password_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

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
    # logging.basicConfig(filename='D:\\python\\vcms\\vcms\\page_object\\_test_suites\\text_logs_help_links.log',
    #                     level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
    logger = logging.getLogger(__name__)
    # console = logging.StreamHandler()
    # logger.addHandler(console)

    @classmethod
    def setUpClass(cls):
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

    def test_H_help_link_on_home_screen(self):
        self.logger.info("TC#0000: Check help link on Home screen")
        expected_header = "Getting Started in CMS"
        left_menu = BaseLeftMenu(self.driver)
        home_screen = HomeScreen(self.driver)
        left_menu.open_menu_home()
        self.assertTrue(home_screen.check_screen_is_present())
        home_screen.click_icon_help()
        actual_header = home_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, home_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_T_help_link_on_tasks_screen(self):
        self.logger.info("TC#0000: Check help link on Tasks screen")
        expected_header = "Tasks"
        left_menu_tasks = BaseLeftMenu(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu_tasks.open_menu_tasks()
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        ribbon_bar.click_button_home()
        ribbon_bar.click_go_to_home_screen_menu_item()
        self.assertTrue(tasks_screen.check_screen_is_present())
        tasks_screen.click_icon_help()
        actual_header = tasks_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, tasks_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_R_help_link_on_reporting_screen(self):
        self.logger.info("TC#0000: Check help link on Reporting screen")
        expected_header = "Reporting"
        left_menu = BaseLeftMenu(self.driver)
        reporting_screen = ReportingScreen(self.driver)
        left_menu.open_menu_reporting()
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        ribbon_bar.click_button_home()
        ribbon_bar.click_go_to_home_screen_menu_item()
        self.assertTrue(reporting_screen.check_screen_is_present())
        self.assertTrue(left_menu.check_menu_reporting_is_opened())
        reporting_screen.click_icon_help()
        actual_header = reporting_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, reporting_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_P_help_link_on_software_and_patch_manager_screen(self):
        self.logger.info("TC#0000: Check help link on Reporting screen")
        expected_header = "Software / Patch Manager"
        left_menu = BaseLeftMenu(self.driver)
        software_and_patch_manager_screen = SoftwareAndPatchManagerScreen(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        ribbon_bar.click_button_home()
        ribbon_bar.click_go_to_home_screen_menu_item()
        self.assertTrue(software_and_patch_manager_screen.check_screen_is_present())
        software_and_patch_manager_screen.click_icon_help()
        actual_header = software_and_patch_manager_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, software_and_patch_manager_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_administration_screen(self):
        self.logger.info("TC#0000: Check help link on Administration screen")
        expected_header = "Administration"
        left_menu_administration = LeftMenuAdministration(self.driver)
        administration_screen = AdministrationScreen(self.driver)
        left_menu_administration.open_menu_administration()
        administration_screen.open_administration_screen()
        self.assertTrue(administration_screen.check_screen_is_present())
        administration_screen.click_icon_help()
        actual_header = administration_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, administration_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_endpoint_management_screen(self):
        self.logger.info("TC#0000: Check help link on Endpoint Management screen")
        expected_header = "Endpoint Management"
        left_menu_administration = LeftMenuAdministration(self.driver)
        endpoint_management_screen = EndpointManagementScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(endpoint_management_screen.check_screen_is_present())
        endpoint_management_screen.click_icon_help()
        actual_header = endpoint_management_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, endpoint_management_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_dynamically_managed_screen(self):
        self.logger.info("TC#0000: Check help link on Dynamically Managed screen")
        expected_header = "Endpoint Management"
        left_menu_administration = LeftMenuAdministration(self.driver)
        dynamically_managed_screen = DynamicallyManagedScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.expand_endpoint_management_tree()
        self.assertTrue(left_menu_administration.check_dynamically_managed_label_is_present())
        left_menu_administration.click_dynamically_managed_label()
        self.assertTrue(dynamically_managed_screen.check_screen_is_present())
        dynamically_managed_screen.click_icon_help()
        actual_header = dynamically_managed_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, dynamically_managed_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_excluded_devices_screen(self):
        self.logger.info("TC#0000: Check help link on Excluded Devices screen")
        expected_header = "Endpoint Management"
        left_menu_administration = LeftMenuAdministration(self.driver)
        excluded_devices_screen = ExcludedDevicesScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.expand_endpoint_management_tree()
        self.assertTrue(left_menu_administration.check_excluded_devices_label_is_present())
        left_menu_administration.click_excluded_devices_label()
        self.assertTrue(excluded_devices_screen.check_screen_is_present())
        excluded_devices_screen.click_icon_help()
        actual_header = excluded_devices_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, excluded_devices_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_unmanaged_devices_screen(self):
        self.logger.info("TC#0000: Check help link on Unmanaged Devices screen")
        expected_header = "Endpoint Management"
        left_menu_administration = LeftMenuAdministration(self.driver)
        unmanaged_devices_screen = UnmanagedDevicesScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.expand_endpoint_management_tree()
        self.assertTrue(left_menu_administration.check_excluded_devices_label_is_present())
        left_menu_administration.click_unmanaged_devices_label()
        self.assertTrue(unmanaged_devices_screen.check_screen_is_present())
        unmanaged_devices_screen.click_icon_help()
        actual_header = unmanaged_devices_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, unmanaged_devices_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_infrastructure_screen(self):
        self.logger.info("TC#0000: Check help link on Infrastructure screen")
        expected_header = "Endpoint Management"
        left_menu_administration = LeftMenuAdministration(self.driver)
        infrastructure_screen = InfrastructureScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.expand_endpoint_management_tree()
        self.assertTrue(left_menu_administration.check_infrastructure_label_is_present())
        left_menu_administration.click_infrastructure_label()
        self.assertTrue(infrastructure_screen.check_screen_is_present())
        infrastructure_screen.click_icon_help()
        actual_header = infrastructure_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, infrastructure_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_site_configuration_screen(self):
        self.logger.info("TC#0000: Check help link on Site Configuration screen")
        expected_header = "Site Management"
        left_menu_administration = LeftMenuAdministration(self.driver)
        site_configuration_screen = SiteConfigurationScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_site_management_label()
        self.assertTrue(site_configuration_screen.check_screen_is_present())
        site_configuration_screen.click_icon_help()
        actual_header = site_configuration_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_configuration_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_site_event_logs_screen(self):
        self.logger.info("TC#0000: Check help link on Event Logs screen")
        expected_header = "Logs"
        left_menu_administration = LeftMenuAdministration(self.driver)
        event_logs_screen =EventLogsScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_logs_label()
        self.assertTrue(event_logs_screen.check_screen_is_present())
        event_logs_screen.click_icon_help()
        actual_header = event_logs_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, event_logs_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_column_sets_screen(self):
        self.logger.info("TC#0000: Check help link on Column Sets screen")
        expected_header = "Column Sets"
        left_menu_administration = LeftMenuAdministration(self.driver)
        column_sets_screen =ColumnSetsScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_column_sets_label()
        self.assertTrue(column_sets_screen.check_screen_is_present())
        column_sets_screen.click_icon_help()
        actual_header = column_sets_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, column_sets_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_inventory_configuration_screen(self):
        self.logger.info("TC#0000: Check help link on Inventory Configuration screen")
        expected_header = "Inventory Scan Configuration"
        left_menu_administration = LeftMenuAdministration(self.driver)
        inventory_configuration_screen =InventoryConfigurationScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_inventory_scan_configuration_label()
        self.assertTrue(inventory_configuration_screen.check_screen_is_present())
        inventory_configuration_screen.click_icon_help()
        actual_header = inventory_configuration_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, inventory_configuration_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_vreps_screen(self):
        self.logger.info("TC#0000: Check help link on vReps screen")
        expected_header = "vReps"
        left_menu_administration = LeftMenuAdministration(self.driver)
        vreps_screen =VRepsScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_vreps_label()
        self.assertTrue(vreps_screen.check_screen_is_present())
        vreps_screen.click_icon_help()
        actual_header = vreps_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, vreps_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_maintenance_windows_screen(self):
        self.logger.info("TC#0000: Check help link on Maintenance Windows screen")
        expected_header = "Maintenance Windows"
        left_menu_administration = LeftMenuAdministration(self.driver)
        maintenance_screen = MaintenanceWindowsScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_maintenance_windows_label()
        self.assertTrue(maintenance_screen.check_screen_is_present())
        maintenance_screen.click_icon_help()
        actual_header = maintenance_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, maintenance_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_notifications_screen(self):
        self.logger.info("TC#0000: Check help link on Notifications screen")
        expected_header = "Notifications"
        left_menu_administration = LeftMenuAdministration(self.driver)
        notification_screen =NotificationsScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_notifications_label()
        self.assertTrue(notification_screen.check_screen_is_present())
        notification_screen.click_icon_help()
        actual_header = notification_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, notification_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_audit_log_screen(self):
        self.logger.info("TC#0000: Check help link on Audit Log screen")
        expected_header = "Audit Log"
        left_menu_administration = LeftMenuAdministration(self.driver)
        audit_log_screen =AuditLogScreen(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_audit_log_label()
        self.assertTrue(audit_log_screen.check_screen_is_present())
        audit_log_screen.click_icon_help()
        actual_header = audit_log_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, audit_log_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_admin_accounts_popup(self):
        self.logger.info("TC#0000: Check help link on Admin Accounts popup")
        expected_header = "Accounts"
        left_menu_administration = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        admin_accounts_popup = AdminAccountsPopup(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_present())
        ribbon_bar.click_button_accounts()
        self.assertTrue(admin_accounts_popup.check_popup_is_present())
        admin_accounts_popup.click_icon_help()
        actual_header = admin_accounts_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, admin_accounts_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_user_configuration_popup(self):
        self.logger.info("TC#0000: Check help link on User Configuration popup")
        expected_header = "Create"
        left_menu_administration = LeftMenuAdministration(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        admin_accounts_popup = AdminAccountsPopup(self.driver)
        user_configuration_popup = UserConfigurationPopup(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_present())
        ribbon_bar.click_button_accounts()
        self.assertTrue(admin_accounts_popup.check_popup_is_present())
        admin_accounts_popup.click_button_add()
        self.assertTrue(user_configuration_popup.check_popup_is_present())
        user_configuration_popup.click_icon_help()
        actual_header = user_configuration_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, user_configuration_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_configure_exclusions_popup(self):
        self.logger.info("TC#0000: Check help link on Configure Exclusions popup")
        expected_header = "Exclusions"
        left_menu_administration = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_present())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_present())
        configure_exclusions_popup.click_icon_help()
        actual_header = configure_exclusions_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, configure_exclusions_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_exclude_site_popup(self):
        self.logger.info("TC#0000: Check help link on Exclude Site popup")
        expected_header = "Exclude Site"
        left_menu_administration = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        exclude_site_popup = ExcludeSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_present())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_present())
        configure_exclusions_popup.click_tree_label_sites()
        # self.assertTrue(configure_exclusions_popup.check_sites_tab_is_opened())
        configure_exclusions_popup.click_sites_tab_button_add()
        self.assertTrue(exclude_site_popup.check_popup_is_present())
        exclude_site_popup.click_icon_help()
        actual_header = exclude_site_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, exclude_site_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_exclude_device_popup(self):
        self.logger.info("TC#0000: Check help link on Exclude Device popup")
        expected_header = "Exclude Device"
        left_menu_administration = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        exclude_device_popup = ExcludeDevicePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_present())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_present())
        configure_exclusions_popup.click_tree_label_device_name()
        configure_exclusions_popup.click_device_name_tab_button_add()
        self.assertTrue(exclude_device_popup.check_popup_is_present())
        exclude_device_popup.click_icon_help()
        actual_header = exclude_device_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, exclude_device_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_exclude_ip_address_popup(self):
        self.logger.info("TC#0000: Check help link on Exclude IP Address popup")
        expected_header = "Exclude IP Address"
        left_menu_administration = LeftMenuAdministration(self.driver)
        configure_exclusions_popup = ConfigureExclusionsPopup(self.driver)
        exclude_ip_address_popup = ExcludeIPAddressPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_configuration_box_is_present())
        ribbon_bar.click_button_exclusions()
        self.assertTrue(configure_exclusions_popup.check_popup_is_present())
        configure_exclusions_popup.click_tree_label_ip_address()
        configure_exclusions_popup.click_ip_address_tab_button_add()
        self.assertTrue(exclude_ip_address_popup.check_popup_is_present())
        exclude_ip_address_popup.click_icon_help()
        actual_header = exclude_ip_address_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, exclude_ip_address_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_discover_devices_popup(self):
        self.logger.info("TC#0000: Check help link on Discover Devices popup (Administration)")
        expected_header = "Discovery"
        left_menu_administration = LeftMenuAdministration(self.driver)
        discover_devices_popup = DiscoverDevicesPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_endpoint_management_label()
        self.assertTrue(ribbon_bar.check_button_discover_is_present())
        ribbon_bar.click_button_discover()
        self.assertTrue(discover_devices_popup.check_popup_is_present())
        discover_devices_popup.click_icon_help()
        actual_header = discover_devices_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, discover_devices_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_site_config_popup(self):
        self.logger.info("TC#0000: Check help link on Site Config popup")
        expected_header = "Create" #THIS SHOULD BE SITE CONFIGURATION...
        left_menu_administration = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_site_management_label()
        self.assertTrue(ribbon_bar.check_config_box_is_present())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_present())
        site_config_popup.click_icon_help()
        actual_header = site_config_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_config_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_site_name_popup(self):
        self.logger.info("TC#0000: Check help link on Site Name popup (Administration)")
        expected_header = "Create a site"
        left_menu_administration = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_site_management_label()
        self.assertTrue(ribbon_bar.check_config_box_is_present())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_present())
        site_config_popup.click_global_site_view_label()
        site_config_popup.click_button_add_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.click_icon_help()
        actual_header = site_name_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_name_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_ip_address_popup(self):
        self.logger.info("TC#0000: Check help link on IP Address popup (Administration)")
        expected_header = "IP Address Range"
        sitename = "HelpTest"
        left_menu_administration = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        ip_address_popup = IPAddressPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_site_management_label()
        self.assertTrue(ribbon_bar.check_config_box_is_present())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_present())
        site_config_popup.create_site_if_not_exists(sitename)
        self.assertTrue(site_config_popup.check_site_is_in_global_site_view_tree(sitename))
        site_config_popup.click_site_in_global_site_view_tree(sitename)
        site_config_popup.click_button_add_ip_range()
        self.assertTrue(ip_address_popup.check_popup_is_present())
        ip_address_popup.click_icon_help()
        actual_header = ip_address_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ip_address_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_A_help_link_on_move_site_popup(self):
        self.logger.info("TC#0000: Check help link on Move Site popup (Administration)")
        expected_header = "Move a site or device"
        sitename = "HelpTest"
        left_menu_administration = LeftMenuAdministration(self.driver)
        site_config_popup = SiteConfigPopup(self.driver)
        move_site_popup = MoveSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_administration.open_menu_administration()
        self.assertTrue(left_menu_administration.check_menu_administration_is_opened())
        left_menu_administration.click_site_management_label()
        self.assertTrue(ribbon_bar.check_config_box_is_present())
        ribbon_bar.click_button_add()
        self.assertTrue(site_config_popup.check_popup_is_present())
        site_config_popup.create_site_if_not_exists(sitename)
        self.assertTrue(site_config_popup.check_site_is_in_global_site_view_tree(sitename))
        site_config_popup.click_button_move_site()
        self.assertTrue(move_site_popup.check_popup_is_present())
        move_site_popup.click_icon_help()
        actual_header = move_site_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, move_site_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_select_dashboard_popup(self):
        self.logger.info("TC#0000: Check help link on Select Dashboard popup")
        expected_header = "Select Dashboard"
        ribbon_bar = RibbonBar(self.driver)
        select_dashboard_popup = SelectDashboardPopup(self.driver)
        ribbon_bar.click_button_home()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_change_home_screen_menu_item()
        self.assertTrue(select_dashboard_popup.check_popup_is_present())
        select_dashboard_popup.click_icon_help()
        actual_header = select_dashboard_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, select_dashboard_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_user_settings_popup(self):
        self.logger.info("TC#0000: Check help link on User Settings popup")
        expected_header = "User Settings"
        ribbon_bar = RibbonBar(self.driver)
        user_settings_popup = UserSettingsPopup(self.driver)
        ribbon_bar.click_button_admin_user()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_settings_menu_item()
        self.assertTrue(user_settings_popup.check_popup_is_present())
        user_settings_popup.click_icon_help()
        actual_header = user_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, user_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_ribbon_bar(self):
        self.logger.info("TC#0000: Check help link on Ribbon bar")
        expected_header = "CMS Quick Help Videos"
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_button_console_guide()
        actual_header = ribbon_bar._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ribbon_bar._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_subscription_popup(self):
        self.logger.info("TC#0000: Check help link on Subscription popup")
        expected_header = "Subscriptions"
        subscription_popup = SubscriptionsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_button_subscriptions()
        self.assertIsNotNone(subscription_popup.check_popup_is_present()) #VERIFY THIS ASSERTION
        subscription_popup.click_icon_help()
        actual_header = subscription_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, subscription_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_settings_popup(self):
        self.logger.info("TC#0000: Check help link on Settings popup")
        expected_header = "Settings"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_settings_popup_content_services_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Content Services tab")
        expected_header = "Content Services"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_content_services_label()
        self.assertTrue(settings_popup.check_content_services_tab_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_settings_popup_email_settings_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Email Settings tab")
        expected_header = "Email Settings"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_email_settings_label()
        self.assertTrue(settings_popup.check_email_settings_tab_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_settings_popup_initial_setup_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Initial Setup tab")
        expected_header = "Initial Setup"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_initial_setup_label()
        self.assertTrue(settings_popup.check_initial_setup_tab_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_settings_popup_locale_options_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Locale Options tab")
        expected_header = "Locale Options"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_locale_options_label()
        self.assertTrue(settings_popup.check_locale_options_tab_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    @unittest.skip("Skip test_RB_help_link_on_settings_popup_inventory_tab. Inventory tab is opened too long\n")
    def test_RB_help_link_on_settings_popup_inventory_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Inventory tab")
        expected_header = "Inventory"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_inventory_label()
        self.assertTrue(settings_popup.check_inventory_tab_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_settings_popup_user_options_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - User Options tab")
        expected_header = "User Options"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_user_options_label()
        self.assertTrue(settings_popup.check_user_options_tab_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_settings_popup_audit_log_settings_tab(self):
        self.logger.info("TC#0000: Check help link on Settings popup - Audit Log Settings tab")
        expected_header = "Audit Log Settings"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_audit_log_settings_label()
        self.assertTrue(settings_popup.check_audit_log_settings_tab_is_present())
        settings_popup.click_icon_help()
        actual_header = settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_client_settings_popup(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup")
        expected_header = "Client"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_client_settings_popup_timers_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Timers tab")
        expected_header = "Timers"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_timers_tab()
        self.assertTrue(client_settings_popup.check_timers_tab_is_present())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_client_settings_popup_features_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Features tab")
        expected_header = "Features"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_features_label()
        self.assertTrue(client_settings_popup.check_features_tab_is_present())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_client_settings_popup_client_urls_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Client URLs tab")
        expected_header = "Client URLs"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_client_urls_label()
        self.assertTrue(client_settings_popup.check_client_urls_tab_is_present())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_client_settings_popup_reboot_ui_config_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Reboot UI Config tab")
        expected_header = "Reboot UI Config"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_reboot_ui_config_tab()
        self.assertTrue(client_settings_popup.check_reboot_ui_config_tab_is_present())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_client_settings_popup_client_proxy_settings_tab(self):
        self.logger.info("TC#0000: Check help link on Client Settings popup - Client Proxy Settings tab")
        expected_header = "Client Proxy Settings"
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_client_proxy_settings_tab()
        self.assertTrue(client_settings_popup.check_client_proxy_settings_tab_is_present())
        client_settings_popup.click_icon_help()
        actual_header = client_settings_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, client_settings_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_currency_popup(self):
        self.logger.info("TC#0000: Check help link on Currency popup")
        expected_header = "Currency"
        ribbon_bar = RibbonBar(self.driver)
        currency_popup = CurrencyPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_currency()
        self.assertTrue(currency_popup.check_popup_is_present())
        currency_popup.click_icon_help()
        actual_header = currency_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, currency_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_weight_display_popup(self):
        self.logger.info("TC#0000: Check help link on Weight Display popup")
        expected_header = "Imperial Metric"
        ribbon_bar = RibbonBar(self.driver)
        weight_display_popup = WeightDisplayPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_imperial_and_metric()
        self.assertTrue(weight_display_popup.check_popup_is_present())
        weight_display_popup.click_icon_help()
        actual_header = weight_display_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, weight_display_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_manufacturer_alias_popup(self):
        self.logger.info("TC#0000: Check help link on Manufacturer Alias popup")
        expected_header = "Manufacturers"
        ribbon_bar = RibbonBar(self.driver)
        manufacturer_alias_popup = ManufacturerAliasPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_makes()
        self.assertTrue(manufacturer_alias_popup.check_popup_is_present())
        manufacturer_alias_popup.click_icon_help()
        actual_header = manufacturer_alias_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, manufacturer_alias_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_model_alias_popup(self):
        self.logger.info("TC#0000: Check help link on Model Alias popup")
        expected_header = "Models"
        ribbon_bar = RibbonBar(self.driver)
        model_alias_popup = ModelAliasPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_models()
        self.assertTrue(model_alias_popup.check_popup_is_present())
        model_alias_popup.click_icon_help()
        actual_header = model_alias_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, model_alias_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_column_sets_popup(self):
        self.logger.info("TC#0000: Check help link on Column Set popup")
        expected_header = "Column Sets"
        ribbon_bar = RibbonBar(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_popup_is_present())
        column_sets_popup.click_icon_help()
        actual_header = column_sets_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, column_sets_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_RB_help_link_on_initial_setup_popup(self):
        self.logger.info("TC#0000: Check help link on Initial Setup popup")
        expected_header = "Initial Setup"
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        initial_setup_popup = InitialSetupPopup(self.driver)
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_initial_setup_label()
        self.assertTrue(settings_popup.check_initial_setup_tab_is_present())
        settings_popup.click_button_run_initial_setup()
        self.assertTrue(initial_setup_popup.check_popup_is_present())
        initial_setup_popup.click_icon_help()
        actual_header = initial_setup_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, initial_setup_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_devices_screen(self):
        self.logger.info("TC#0000: Check help link on Devices screen")
        expected_header = "Devices"
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_button_home()
        ribbon_bar.click_go_to_home_screen_menu_item()
        self.assertTrue(devices_screen.check_screen_is_present())
        devices_screen.click_icon_help()
        actual_header = devices_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, devices_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_queries_screen(self):
        self.logger.info("TC#0000: Check help link on Queries screen")
        expected_header = "Queries"
        left_menu_devices = LeftMenuDevices(self.driver)
        queries_screen =QueriesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_queries_label()
        queries_screen.click_icon_help()
        actual_header = queries_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, queries_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_groups_screen(self):
        self.logger.info("TC#0000: Check help link on Groups screen")
        expected_header = "Groups"
        left_menu_devices = LeftMenuDevices(self.driver)
        groups_screen =GroupsScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        groups_screen.click_icon_help()
        actual_header = groups_screen._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, groups_screen._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_site_name_popup(self):
        self.logger.info("TC#0000: Check help link on Site Name popup")
        expected_header = "Create a site"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = BaseLeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.click_icon_help()
        actual_header = site_name_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, site_name_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_configuration_popup(self):
        self.logger.info("TC#0000: Check help link on Configuration popup")
        expected_header = "Configure a site"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = BaseLeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu_devices.open_global_site_view_tree()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        configuration_popup.click_icon_help()
        actual_header = configuration_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, configuration_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_ip_address_popup(self):
        self.logger.info("TC#0000: Check help link on IP Address popup")
        expected_header = "Add IP Address"
        sitename = "HelpTest"
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        ip_address_popup = IPAddressPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu_devices.open_menu_devices()
        self.assertTrue(left_menu_devices.check_menu_devices_is_opened())
        left_menu_devices.open_global_site_view_tree()
        left_menu_devices.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        configuration_popup.click_ip_address_ranges_tab()
        self.assertTrue(configuration_popup.check_tab_is_present())
        configuration_popup.click_button_add()
        self.assertTrue(ip_address_popup.check_popup_is_present())
        ip_address_popup.click_icon_help()
        actual_header = ip_address_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ip_address_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_move_site_popup(self):
        self.logger.info("TC#0000: Check help link on Move Site popup")
        expected_header = "Move a site or device"
        sitename = "HelpTest"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = BaseLeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        move_site_popup = MoveSitePopup(self.driver)
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_opened())
        left_menu_devices.create_site_if_not_exists(sitename)
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_move()
        self.assertTrue(move_site_popup.check_popup_is_present())
        move_site_popup.click_icon_help()
        actual_header = move_site_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, move_site_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_query_designer_popup(self):
        self.logger.info("TC#0000: Check help link on Query Designer popup")
        expected_header = "Queries"
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        query_designer_popup = QueryDesignerPopup(self.driver)
        left_menu_devices.open_menu_devices()
        self.assertTrue(left_menu_devices.check_menu_devices_is_opened())
        left_menu_devices.click_queries_label()
        self.assertTrue(ribbon_bar.check_queries_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(query_designer_popup.check_popup_is_present())
        query_designer_popup.click_icon_help()
        actual_header = query_designer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, query_designer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_condition_editor_popup(self):
        self.logger.info("TC#0000: Check help link on Condition Editor popup")
        expected_header = "Create a Query"
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        query_designer_popup = QueryDesignerPopup(self.driver)
        condition_editor_popup = ConditionEditorPopup(self.driver)
        left_menu_devices.open_menu_devices()
        self.assertTrue(left_menu_devices.check_menu_devices_is_opened())
        left_menu_devices.click_queries_label()
        self.assertTrue(ribbon_bar.check_queries_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(query_designer_popup.check_popup_is_present())
        query_designer_popup.click_button_add()
        self.assertTrue(condition_editor_popup.check_popup_is_present())
        condition_editor_popup.click_icon_help()
        actual_header = condition_editor_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, condition_editor_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_new_group_popup(self):
        self.logger.info("TC#0000: Check help link on New Group popup")
        expected_header = "Create a Group"
        ribbon_bar = RibbonBar(self.driver)
        new_group_popup = NewGroupPopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_new_group_menu_item()
        self.assertTrue(new_group_popup.check_popup_is_present())
        new_group_popup.click_icon_help()
        actual_header = new_group_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, new_group_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_select_targets_popup(self):
        self.logger.info("TC#0000: Check help link on Select Targets popup")
        expected_header = "Select Targets"
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        new_group_popup = NewGroupPopup(self.driver)
        select_targets_popup = SelectTargetsPopup(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_new_group_menu_item()
        self.assertTrue(new_group_popup.check_popup_is_present())
        new_group_popup.click_button_add_members()
        self.assertTrue(select_targets_popup.check_popup_is_present())
        select_targets_popup.click_icon_help()
        actual_header = select_targets_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, select_targets_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_new_folder_popup(self):
        self.logger.info("TC#0000: Check help link on New Folder popup")
        expected_header = "Create a Folder"
        ribbon_bar = RibbonBar(self.driver)
        new_folder_popup = NewFolderPopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_new_folder_menu_item()
        self.assertTrue(new_folder_popup.check_popup_is_present())
        new_folder_popup.click_icon_help()
        actual_header = new_folder_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, new_folder_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_edit_folder_popup(self):
        self.logger.info("TC#0000: Check help link on Edit Folder popup")
        expected_header = "Edit a folder"
        name = "Help Test"
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        edit_folder_popup = EditFolderPopup(self.driver)
        left_menu_devices.open_menu_devices()
        self.assertTrue(left_menu_devices.check_menu_devices_is_opened())
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        left_menu_devices.create_group_folder_if_not_exists(name)
        self.assertTrue(left_menu_devices.check_folder_is_in_groups_tree(name))
        left_menu_devices.click_group_in_groups_tree(name)
        self.assertTrue(ribbon_bar.check_button_edit_folder_is_present())
        ribbon_bar.click_button_edit_folder()
        self.assertTrue(edit_folder_popup.check_popup_is_present())
        edit_folder_popup.click_icon_help()
        actual_header = edit_folder_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, edit_folder_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_inventory_view_popup(self):
        self.logger.info("TC#0000: Check help link on Inventory View popup")
        expected_header = "Inventory"
        device = Variables.vrep
        inventory_view_popup = InventoryViewPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_inventory_box_is_present())
        ribbon_bar.click_button_inventory()
        ribbon_bar.click_view_menu_item()
        self.assertTrue(inventory_view_popup.check_popup_is_present(device))
        inventory_view_popup.click_icon_help()
        actual_header = inventory_view_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, inventory_view_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_on_demand_inventory_scan_popup(self):
        self.logger.info("TC#0000: Check help link on On Demand Inventory Scan popup")
        expected_header = "On Demand Inventory Scan"
        device = Variables.vrep
        on_demand_inventory_scan_popup = OnDemandInventoryScanPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_inventory_box_is_present())
        ribbon_bar.click_button_inventory()
        ribbon_bar.click_on_demand_menu_item()
        self.assertTrue(on_demand_inventory_scan_popup.check_popup_is_present())
        on_demand_inventory_scan_popup.click_icon_help()
        actual_header = on_demand_inventory_scan_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, on_demand_inventory_scan_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_wake_up_popup(self):
        self.logger.info("TC#0000: Check help link on Wake on LAN popup")
        expected_header = "Wake Up"
        device = Variables.vrep
        wake_on_lan_popup = WakeOnLANPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_button_wake_up_is_present())
        ribbon_bar.click_button_wake_up()
        self.assertTrue(wake_on_lan_popup.check_popup_is_present())
        wake_on_lan_popup.click_icon_help()
        actual_header = wake_on_lan_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, wake_on_lan_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_move_device_popup(self):
        self.logger.info("TC#0000: Check help link on Move Device popup")
        expected_header = "Move a site or device"
        device = Variables.vrep
        move_device_popup = MoveDevicePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_site_management_box_is_present())
        ribbon_bar.click_button_move_device()
        self.assertTrue(move_device_popup.check_popup_is_present())
        move_device_popup.click_icon_help()
        actual_header = move_device_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, move_device_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_patch_manager_popup(self):
        self.logger.info("TC#0000: Check help link on Patch Manager popup")
        expected_header = "Software Updates"
        device = Variables.vrep
        patch_manager_popup = PatchManagerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_button_patch_manager_is_present())
        ribbon_bar.click_button_patch_manager()
        self.assertTrue(patch_manager_popup.check_popup_is_present())
        patch_manager_popup.click_icon_help()
        actual_header = patch_manager_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, patch_manager_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_reports_popup(self):
        self.logger.info("TC#0000: Check help link on Reports popup")
        expected_header = "Reports"
        device = Variables.vrep
        reports_popup = ReportsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_site_management_box_is_present())
        ribbon_bar.click_button_reports()
        self.assertTrue(reports_popup.check_popup_is_present())
        reports_popup.click_icon_help()
        actual_header = reports_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, reports_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_file_explorer_popup(self):
        self.logger.info("TC#0000: Check help link on File Explorer popup")
        expected_header = "File Explorer"
        device = Variables.vrep
        file_explorer_popup = FileExplorerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
        ribbon_bar.click_button_file_browser()
        self.assertTrue(file_explorer_popup.check_popup_is_present())
        file_explorer_popup.click_icon_help()
        actual_header = file_explorer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, file_explorer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_ping_result_popup(self):
        self.logger.info("TC#0000: Check help link on Ping Result popup")
        expected_header = "Ping Result"
        device = Variables.vrep
        ping_result_popup = PingResultPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
        ribbon_bar.click_button_ping()
        self.assertTrue(ping_result_popup.check_popup_is_present())
        ping_result_popup.click_icon_help()
        actual_header = ping_result_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, ping_result_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_process_explorer_popup(self):
        self.logger.info("TC#0000: Check help link on IP Process Explorer popup")
        expected_header = "Process Explorer"
        device = Variables.vrep
        process_explorer_popup = ProcessExplorerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
        ribbon_bar.click_button_process_viewer()
        self.assertTrue(process_explorer_popup.check_popup_is_present())
        process_explorer_popup.click_icon_help()
        actual_header = process_explorer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, process_explorer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_event_viewer_popup(self):
        self.logger.info("TC#0000: Check help link on Event Viewer popup")
        expected_header = "Event Viewer"
        device = Variables.vrep
        event_viewer_popup = EventViewerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
        ribbon_bar.click_button_event_viewer()
        self.assertTrue(event_viewer_popup.check_popup_is_present())
        event_viewer_popup.click_icon_help()
        actual_header = event_viewer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, event_viewer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def test_D_help_link_on_wmi_explorer_popup(self):
        self.logger.info("TC#0000: Check help link on WMI Explorer popup")
        expected_header = "Process Explorer"
        device = Variables.vrep
        wmi_explorer_popup = WMIExplorerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_screen.check_device_is_present(device))
        devices_screen.select_device_in_table(device)
        ribbon_bar.open_tab_tools()
        self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
        ribbon_bar.click_button_wmi_explorer()
        self.assertTrue(wmi_explorer_popup.check_popup_is_present())
        wmi_explorer_popup.click_icon_help()
        actual_header = wmi_explorer_popup._get_help_frame_header()
        self.assertEqual(expected_header, actual_header, wmi_explorer_popup._get_log_for_help_link(expected_header))
        self.logger.info("TEST PASSED!!!")

    def tearDown(self):
        base_actions = BaseActions(self.driver)
        base_actions._close_help_window()
        base_actions._close_popups()
        self.logger.info("[Test end]\n")

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("End testing\n")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())
    # logger.info('Started MainPageHelpLinks')
