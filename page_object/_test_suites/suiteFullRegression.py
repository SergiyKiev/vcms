
import logging
import unittest

from _feature_objects._left_menus.leftMenu import LeftMenu
from _feature_objects._left_menus.leftMenuDevices import LeftMenuDevices
from _feature_objects._pages.pageAdministration import AdministrationPage
from _feature_objects._pages.pageDevices import *
from _feature_objects._pages.pageGroups import GroupsPage
from _feature_objects._pages.pageHome import HomePage
from _feature_objects._pages.pageLogin import LoginPage
from _feature_objects._pages.pageMain import MainPage
from _feature_objects._pages.pageQueries import QueriesPage
from _feature_objects._pages.pageReporting import ReportingPage
from _feature_objects._pages.pageSoftwareAndPatchManger import SoftwareAndPatchManagerPage
from _feature_objects._pages.pageTasks import TasksPage
from _feature_objects._popups.popupConditionEditor import ConditionEditorPopup
from _feature_objects._popups.popupConfiguration import *
from _feature_objects._popups.popupError import ErrorPopup
from _feature_objects._popups.popupPatchManager import PatchManagerPopup
from _feature_objects._popups.popupQueryDesigner import QueryDesignerPopup
from _feature_objects._popups.popupResetPassword import ResetPasswordPopup
from _feature_objects._popups.popupSelectTargets import SelectTargetsPopup
from _feature_objects._popups.popupSettings import *
from _feature_objects._popups.popupClientSettings import *
from _feature_objects._ribbon_bar.ribbonBar import *
from _variables.variables import Variables
from selenium import webdriver

logging.basicConfig(level=logging.INFO)


class SiteCreation(unittest.TestCase):
    driver = None  # global variable

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
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.expand_global_site_view_tree()

    # def test_open_left_menus(self):
    #     print ("\n" + "TC#xxxx. Open left side menus")
    #     left_menu = LeftMenu(self.driver)
    #     left_menu.open_menu_home()
    #     left_menu.open_menu_devices()
    #     self.assertTrue(left_menu.check_menu_devices_is_visible())
    #     left_menu.open_menu_administration()
    #     self.assertTrue(left_menu.check_menu_administration_is_visible())
    #     left_menu.open_menu_tasks()
    #     self.assertTrue(left_menu.check_menu_tasks_is_visible())
    #     left_menu.open_menu_reporting()
    #     self.assertTrue(left_menu.check_menu_reporting_is_visible())
    #     left_menu.open_menu_software_and_patch_manager()
    #     self.assertTrue(left_menu.check_menu_software_and_patch_manager_is_visible())
    #     # left_menu.open_menu_password_reset()
    #     print ("Test is passed" + "\n")

    def test_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup")
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        print ("Test is passed" + "\n")

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
        print ("Test is passed" + "\n")

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
        print ("Test is passed" + "\n")

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
        print ("Test is passed" + "\n")

    def test_create_site_with_fifty_one_symbols(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        fifty_symbols_name = "51symbols51symbols51symbols51symbols51symbols!<ok>"
        fifty_one_symbols_name = fifty_symbols_name + "1"
        main_page = MainPage(self.driver)
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
        print ("Test is passed" + "\n")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
        sitename = "Site #9118"
        subsitename_one = sitename + "-01"
        subsitename_two = sitename + "-02"
        main_page = MainPage(self.driver)
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
        print ("Test is passed" + "\n")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration(unittest.TestCase):
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
        left_menu = LeftMenu(self.driver)
        left_menu.open_menu_devices()

    def test_open_configuration_popup(self):
        print ("\n" + "TC#9601. Devices page. Open 'Configuration' popup")
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_global_site_view(self):
        print ("\n" + "TC#9228. Devices page. Open Configuration popup from the Global Site View")
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
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_default_site(self):
        print ("\n" + "TC#9230. Devices page. Open Configuration popup from the Default Site main label")
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
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_created_site(self):
        print ("\n" + "TC#9236. Devices page. Open Configuration popup from the created site")
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
        print ("Test is passed" + "\n")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfigurationSiteTab(unittest.TestCase):
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
        left_menu = LeftMenu(self.driver)
        left_menu.open_menu_devices()

    def test_configuration_popup_change_site_name(self):
        print ("\n" + "TC#9237. Devices page. Configuration popup. Change site name")
        sitename = "Site#9237"
        modifed = "_modifed"
        main_page = MainPage(self.driver)
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
        print ("Test is passed" + "\n")

    def test_configuration_popup_open_column_set_designer_popup(self):
        print ("\n" + "TC#9238. Devices page. Configuration popup. Open Column Set Designer popup")
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
        print ("Test is passed" + "\n")

    def test_configuration_popup_apply_column_set(self):
        print ("\n" + "TC#9239. Devices page. Configuration popup. Apply Column set to the site")
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
        devices_page = DevicesPage(self.driver)
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
        self.assertTrue(devices_page.check_columns_are_present(columns_list1))
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        site_tab.select_columnset_in_drop_down_list(columnset2)
        self.assertTrue(site_tab.check_columnset_is_selected_from_drop_down_list(columnset2))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(devices_page.check_columns_are_present(columns_list2))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_configuration_popup_create_column_set(self):
        print ("\n" + "TC#9999. Devices page. Configuration popup. Create column set")
        sitename = "Site#9999"
        columnsetname = "ColumnSet#9999-01"
        columns_list = ["Device Name", "Device ID", "Domain", "Site"]
        main_page = MainPage(self.driver)
        devices_page = DevicesPage(self.driver)
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
        self.assertTrue(devices_page.check_columns_are_present(columns_list))
        left_menu_devices.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

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
        left_menu = LeftMenu(self.driver)
        left_menu.open_menu_devices()

    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page._close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteDeletion(unittest.TestCase):
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
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.expand_global_site_view_tree()

    def test_delete_created_site_from_global_site_view_tree(self):
        print ("\n" + "TC#9607. Devices page. Delete created site from Global Site View tree")
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
        print ("Test is passed" + "\n")

    def test_delete_default_site_from_global_site_view_tree(self):
        print ("\n" + "TC#8888. Devices page. Delete Default site from Global Site View tree")
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        unable_to_remove_popup = UnableToRemovePopup(self.driver)
        left_menu_devices.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(unable_to_remove_popup.check_popup_is_present())
        unable_to_remove_popup.click_button_ok()
        self.assertTrue(left_menu_devices.check_default_site_is_in_global_site_view_tree())
        print ("Test is passed" + "\n")

    def test_delete_subsite_from_site_tree(self):
        print ("\n" + "TC#3333. Devices page. Delete subsite from Global Site View tree")
        sitename = "TC#3333"
        subsitename = "TC#3333-01"
        main_page = MainPage(self.driver)
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
        print ("Test is passed" + "\n")

    def test_delete_site_with_subsite(self):
        print ("\n" + "TC#0000. Devices page. Delete site with subsite from Global Site View tree")
        sitename = "TC#0000"
        subsitename = "TC#0000-01"
        main_page = MainPage(self.driver)
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
        print ("Test is passed" + "\n")

    def test_cancel_site_deletion_from_global_site_view(self):
        print ("\n" + "TC#1111. Devices page. Cancel site deletion")
        sitename = "TC#1111"
        main_page = MainPage(self.driver)
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
        print ("Test is passed" + "\n")

    def test_open_are_you_sure_popup(self):
        print ("\n" + "TC#2222. Devices page. Open Are you sure popup")
        sitename = "TC#2222"
        main_page = MainPage(self.driver)
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
        print ("Test is passed" + "\n")

    def tearDown(self):
        pass

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
        left_menu = LeftMenu(self.driver)
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

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()

    def test_inventory_view_folder_full_check(self):
        print ("\n" + "TC#7545: Devices: Inventory - Folder full check")
        main_page = MainPage(self.driver)
        left_menu = LeftMenu(self.driver)


class LoginPageHelpLinks(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: HELP LINKS ON LOGIN PAGE")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        login_page.check_login_page_loaded()

    def setUp(self):
        login_page = LoginPage(self.driver)
        login_page._close_popups()

    def test_help_link_on_login_page(self):
        print ("\n" + "TC#0000: Check help link on login page")
        login_page = LoginPage(self.driver)
        login_page.click_icon_help()
        self.assertTrue(login_page.check_help_link_is_correct())

    def test_help_link_on_reset_password_popup(self):
        print ("\n" + "TC#0000: Check help link on password reset popup")
        login_page = LoginPage(self.driver)
        reset_password_popup = ResetPasswordPopup(self.driver)
        login_page.click_reset_password_label()
        self.assertTrue(reset_password_popup.check_popup_is_present())
        reset_password_popup.click_icon_help()
        self.assertTrue(reset_password_popup.check_help_link_is_correct())

    def tearDown(self):
        help_window = BaseActions(self.driver)
        help_window._close_help_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class MainPageHelpLinks(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: HELP LINKS ON MAIN PAGE")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        main_page = MainPage(cls.driver)
        login_page.open_page()
        login_page.login()
        main_page.check_main_page_loaded()
        # devices_page = DevicesPage(cls.driver)
        # desktop = DownloadAndInstall(cls.driver)
        # main_page._close_popups()
        # main_page.delete_single_device_in_devices_page_table(Variables.vrep)
        # desktop.clean_up_device()
        # desktop.download_agent()
        # desktop.install_agent()
        # devices_page.click_icon_refresh()
        # devices_page.check_device_is_present(Variables.vrep)

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()

    def test_help_link_on_home_page(self):
        print ("\n" + "TC#0000: Check help link on home page")
        left_menu = LeftMenu(self.driver)
        home_page = HomePage(self.driver)
        left_menu.open_menu_home()
        self.assertTrue(home_page.check_page_is_present())
        home_page.click_icon_help()
        self.assertTrue(home_page.check_help_link_is_correct())

    def test_help_link_on_devices_page(self):
        print ("\n" + "TC#0000: Check help link on Devices page")
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu_devices.open_menu_devices()
        devices_page.click_icon_help()
        self.assertTrue(devices_page.check_help_link_is_correct())

    def test_help_link_on_queries_page(self):
        print ("\n" + "TC#0000: Check help link on Queries page")
        left_menu_devices = LeftMenuDevices(self.driver)
        queries_page = QueriesPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_queries_label()
        queries_page.click_icon_help()
        self.assertTrue(queries_page.check_help_link_is_correct())

    def test_help_link_on_groups_page(self):
        print ("\n" + "TC#0000: Check help link on Groups page")
        left_menu_devices = LeftMenuDevices(self.driver)
        groups_page = GroupsPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        groups_page.click_icon_help()
        self.assertTrue(groups_page.check_help_link_is_correct())

    def test_help_link_on_administration_page(self):
        print ("\n" + "TC#0000: Check help link on administration page")
        left_menu = LeftMenu(self.driver)
        administration_page = AdministrationPage(self.driver)
        left_menu.open_menu_administration()
        administration_page.click_icon_help()
        self.assertTrue(administration_page.check_help_link_is_correct())

    def test_help_link_on_tasks_page(self):
        print ("\n" + "TC#0000: Check help link on tasks page")
        left_menu = LeftMenu(self.driver)
        tasks_page = TasksPage(self.driver)
        left_menu.open_menu_tasks()
        tasks_page.click_icon_help()
        self.assertTrue(tasks_page.check_help_link_is_correct())

    def test_help_link_on_reporting_page(self):
        print ("\n" + "TC#0000: Check help link on reporting page")
        left_menu = LeftMenu(self.driver)
        reporting_page = ReportingPage(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_visible())
        reporting_page.click_icon_help()
        self.assertTrue(reporting_page.check_help_link_is_correct())

    def test_help_link_on_software_and_patch_manager_page(self):
        print ("\n" + "TC#0000: Check help link on software and patch manager page")
        left_menu = LeftMenu(self.driver)
        software_and_patch_manager_page = SoftwareAndPatchManagerPage(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        software_and_patch_manager_page.click_icon_help()
        self.assertTrue(software_and_patch_manager_page.check_help_link_is_correct())

    def test_help_link_on_ribbon_bar_console_guide_button(self):
        print ("\n" + "TC#0000: Check help link on Ribbon bar - Console guide button")
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_console_guide()
        self.assertTrue(ribbon_bar.check_help_link_is_correct())

    def test_help_link_on_select_dashboard_popup(self):
        print ("\n" + "TC#0000: Check help link on Select Dashboard popup")
        ribbon_bar = RibbonBar(self.driver)
        select_dashboard_popup = SelectDashboardPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_home()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_change_home_screen_label()
        self.assertTrue(select_dashboard_popup.check_popup_is_present())
        select_dashboard_popup.click_icon_help()
        self.assertTrue(select_dashboard_popup.check_help_link_is_correct())

    def test_help_link_on_user_settings_popup(self):
        print ("\n" + "TC#0000: Check help link on User Settings popup")
        ribbon_bar = RibbonBar(self.driver)
        user_settings_popup = UserSettingsPopup(self.driver)
        ribbon_bar.click_button_admin_user()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_settings_label()
        self.assertTrue(user_settings_popup.check_popup_is_present())
        user_settings_popup.click_icon_help()
        self.assertTrue(user_settings_popup.check_help_link_is_correct())

    def test_help_link_on_subscription_popup(self):
        print ("\n" + "TC#0000: Check help link on Ribbon bar - Console guide button")
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_console_guide()
        self.assertTrue(ribbon_bar.check_help_link_is_correct())

    def test_help_link_on_settings_popup(self):
        print ("\n" + "TC#0000: Check help link on Settings popup")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_icon_help()
        self.assertTrue(settings_popup.check_help_link_is_correct())

    def test_help_link_on_settings_popup_content_services_tab(self):
        print ("\n" + "TC#0000: Check help link on Settings popup - Content Services tab")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        content_services_tab = ContentServicesTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_content_services_label()
        self.assertTrue(content_services_tab.check_tab_is_present())
        settings_popup.click_icon_help()
        self.assertTrue(content_services_tab.check_help_link_is_correct())

    def test_help_link_on_settings_popup_email_settings_tab(self):
        print ("\n" + "TC#0000: Check help link on Settings popup - Email Settings tab")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        email_settings_tab = EmailSettingsTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_email_settings_label()
        self.assertTrue(email_settings_tab.check_tab_is_present())
        settings_popup.click_icon_help()
        self.assertTrue(email_settings_tab.check_help_link_is_correct())

    def test_help_link_on_settings_popup_initial_setup_tab(self):
        print ("\n" + "TC#0000: Check help link on Settings popup - Initial Setup tab")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        initial_setup_tab = InitialSetupTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_initial_setup_label()
        self.assertTrue(initial_setup_tab.check_tab_is_present())
        settings_popup.click_icon_help()
        self.assertTrue(initial_setup_tab.check_help_link_is_correct())

    def test_help_link_on_settings_popup_locale_option_tab(self):
        print ("\n" + "TC#0000: Check help link on Settings popup - Locale Option tab")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        locale_option_tab = LocaleOptionsTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_locale_options_label()
        self.assertTrue(locale_option_tab.check_tab_is_present())
        settings_popup.click_icon_help()
        self.assertTrue(locale_option_tab.check_help_link_is_correct())

    # def test_help_link_on_settings_popup_inventory_tab(self):
    #     print ("\n" + "TC#0000: Check help link on Settings popup - Inventory tab")
    #     ribbon_bar = RibbonBar(self.driver)
    #     settings_popup = SettingsPopup(self.driver)
    #     inventory_tab = InventoryTab(self.driver)
    #     ribbon_bar.open_tab_home()
    #     self.assertTrue(ribbon_bar.check_tab_home_is_present())
    #     ribbon_bar.click_button_settings()
    #     self.assertTrue(settings_popup.check_popup_is_present())
    #     settings_popup.click_inventory_label()
    #     self.assertTrue(inventory_tab.check_page_is_present())
    #     settings_popup.click_icon_help()
    #     self.assertTrue(inventory_tab.check_help_link_is_correct())

    def test_help_link_on_settings_popup_user_options_tab(self):
        print ("\n" + "TC#0000: Check help link on Settings popup - User Options tab")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        user_options_tab = UserOptionsTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_user_options_label()
        self.assertTrue(user_options_tab.check_tab_is_present())
        settings_popup.click_icon_help()
        self.assertTrue(user_options_tab.check_help_link_is_correct())

    def test_help_link_on_settings_popup_audit_log_settings_tab(self):
        print ("\n" + "TC#0000: Check help link on Settings popup - Audit Log Settings tab")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        audit_log_settings_tab = AuditLogSettingsTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_audit_log_settings_label()
        self.assertTrue(audit_log_settings_tab.check_tab_is_present())
        settings_popup.click_icon_help()
        self.assertTrue(audit_log_settings_tab.check_help_link_is_correct())

    def test_help_link_on_client_settings_popup(self):
        print ("\n" + "TC#0000: Check help link on Client Settings popup")
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_icon_help()
        self.assertTrue(client_settings_popup.check_help_link_is_correct())

    def test_help_link_on_client_settings_popup_timers_tab(self):
        print ("\n" + "TC#0000: Check help link on Client Settings popup - Timers tab")
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        timers_tab = TimersTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_timers_tab()
        self.assertTrue(timers_tab.check_tab_is_present())
        client_settings_popup.click_icon_help()
        self.assertTrue(timers_tab.check_help_link_is_correct())

    def test_help_link_on_client_settings_popup_feature_tab(self):
        print ("\n" + "TC#0000: Check help link on Client Settings popup - Feature tab")
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        feature_tab = FeaturesTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_features_label()
        self.assertTrue(feature_tab.check_tab_is_present())
        client_settings_popup.click_icon_help()
        self.assertTrue(feature_tab.check_help_link_is_correct())

    def test_help_link_on_client_settings_popup_client_urls_tab(self):
        print ("\n" + "TC#0000: Check help link on Client Settings popup - Client URLs tab")
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        client_urls_tab = ClientUrlsTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_client_urls_label()
        self.assertTrue(client_urls_tab.check_tab_is_present())
        client_settings_popup.click_icon_help()
        self.assertTrue(client_urls_tab.check_help_link_is_correct())

    def test_help_link_on_client_settings_popup_reboot_ui_config_tab(self):
        print ("\n" + "TC#0000: Check help link on Client Settings popup - Reboot UI Config tab")
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        reboot_ui_config_tab = RebootUIConfigTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_reboot_ui_config_tab()
        self.assertTrue(reboot_ui_config_tab.check_tab_is_present())
        client_settings_popup.click_icon_help()
        self.assertTrue(reboot_ui_config_tab.check_help_link_is_correct())

    def test_help_link_on_client_settings_popup_client_proxy_settings_tab(self):
        print ("\n" + "TC#0000: Check help link on Client Settings popup - Client Proxy Settings tab")
        ribbon_bar = RibbonBar(self.driver)
        client_settings_popup = ClientSettingsPopup(self.driver)
        client_proxy_settings_tab = ClientProxySettingsTab(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_client()
        self.assertTrue(client_settings_popup.check_popup_is_present())
        client_settings_popup.click_client_proxy_settings_tab()
        self.assertTrue(client_proxy_settings_tab.check_tab_is_present())
        client_settings_popup.click_icon_help()
        self.assertTrue(client_proxy_settings_tab.check_help_link_is_correct())

    def test_help_link_on_site_name_popup(self):
        print ("\n" + "TC#0000: Check help link on Site Name popup")
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.click_icon_help()
        self.assertTrue(site_name_popup.check_help_link_is_correct())

    def test_help_link_on_configuration_popup(self):
        print ("\n" + "TC#0000: Check help link on Configuration popup")
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        configuration_popup.click_icon_help()
        self.assertTrue(configuration_popup.check_help_link_is_correct())

    def test_help_link_on_ip_address_popup(self):
        print ("\n" + "TC#0000: Check help link on IP Address popup")
        sitename = "HelpTest"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        main_page = MainPage(self.driver)
        ip_address_ranges_tab = IPAddressRangesTab(self.driver)
        ip_address_popup = IPAddressPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        left_menu_devices.create_site_if_not_exists(sitename)
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        configuration_popup.click_ip_address_ranges_tab()
        self.assertTrue(ip_address_ranges_tab.check_tab_is_present())
        ip_address_ranges_tab.click_button_add()
        self.assertTrue(ip_address_popup.check_popup_is_present())
        ip_address_popup.click_icon_help()
        self.assertTrue(ip_address_popup.check_help_link_is_correct())

    def test_help_link_on_move_site_popup(self):
        print ("\n" + "TC#0000: Check help link on Move Site popup")
        sitename = "HelpTest"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        main_page = MainPage(self.driver)
        move_site_popup = MoveSitePopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        left_menu_devices.create_site_if_not_exists(sitename)
        left_menu_devices.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_move()
        self.assertTrue(move_site_popup.check_popup_is_present())
        move_site_popup.click_icon_help()
        self.assertTrue(move_site_popup.check_help_link_is_correct())

    def test_help_link_on_query_designer_popup(self):
        print ("\n" + "TC#0000: Check help link on Query Designer popup")
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        query_designer_popup = QueryDesignerPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu_devices.open_menu_devices()
        self.assertTrue(left_menu_devices.check_menu_devices_is_visible())
        left_menu_devices.click_queries_label()
        self.assertTrue(ribbon_bar.check_queries_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(query_designer_popup.check_popup_is_present())
        query_designer_popup.click_icon_help()
        self.assertTrue(query_designer_popup.check_help_link_is_correct())

    def test_help_link_on_condition_editor_popup(self):
        print ("\n" + "TC#0000: Check help link on Condition Editor popup")
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        query_designer_popup = QueryDesignerPopup(self.driver)
        condition_editor_popup = ConditionEditorPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu_devices.open_menu_devices()
        self.assertTrue(left_menu_devices.check_menu_devices_is_visible())
        left_menu_devices.click_queries_label()
        self.assertTrue(ribbon_bar.check_queries_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(query_designer_popup.check_popup_is_present())
        query_designer_popup.click_button_add()
        self.assertTrue(condition_editor_popup.check_popup_is_present())
        condition_editor_popup.click_icon_help()
        self.assertTrue(condition_editor_popup.check_help_link_is_correct())

    def test_help_link_on_new_group_popup(self):
        print ("\n" + "TC#0000: Check help link on New Group popup")
        ribbon_bar = RibbonBar(self.driver)
        new_group_popup = NewGroupPopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_new_group_label()
        self.assertTrue(new_group_popup.check_popup_is_present())
        new_group_popup.click_icon_help()
        self.assertTrue(new_group_popup.check_help_link_is_correct())

    def test_help_link_on_select_targets_popup(self):
        print ("\n" + "TC#0000: Check help link on Select Targets popup")
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        new_group_popup = NewGroupPopup(self.driver)
        select_targets_popup = SelectTargetsPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_new_group_label()
        self.assertTrue(new_group_popup.check_popup_is_present())
        new_group_popup.click_button_add_members()
        self.assertTrue(select_targets_popup.check_popup_is_present())
        select_targets_popup.click_icon_help()
        self.assertTrue(select_targets_popup.check_help_link_is_correct())

    def test_help_link_on_new_folder_popup(self):
        print ("\n" + "TC#0000: Check help link on New Folder popup")
        ribbon_bar = RibbonBar(self.driver)
        new_folder_popup = NewFolderPopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        ribbon_bar.click_button_new()
        self.assertTrue(ribbon_bar.check_drop_down_list_is_present())
        ribbon_bar.click_new_folder_label()
        self.assertTrue(new_folder_popup.check_popup_is_present())
        new_folder_popup.click_icon_help()
        self.assertTrue(new_folder_popup.check_help_link_is_correct())

    def test_help_link_on_edit_folder_popup(self):
        print ("\n" + "TC#0000: Check help link on Edit Folder popup")
        name = "Help Test"
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        edit_folder_popup = EditFolderPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu_devices.open_menu_devices()
        self.assertTrue(left_menu_devices.check_menu_devices_is_visible())
        left_menu_devices.click_groups_label()
        self.assertTrue(ribbon_bar.check_groups_box_is_present())
        left_menu_devices.create_group_folder_if_not_exists(name)
        self.assertTrue(left_menu_devices.check_folder_is_in_groups_tree(name))
        left_menu_devices.click_group_in_groups_tree(name)
        self.assertTrue(ribbon_bar.check_button_edit_folder_is_present())
        ribbon_bar.click_button_edit_folder()
        self.assertTrue(edit_folder_popup.check_popup_is_present())
        edit_folder_popup.click_icon_help()
        self.assertTrue(edit_folder_popup.check_help_link_is_correct())

    def test_help_link_on_currency_popup(self):
        print ("\n" + "TC#0000: Check help link on Currency popup")
        ribbon_bar = RibbonBar(self.driver)
        currency_popup = CurrencyPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_currency()
        self.assertTrue(currency_popup.check_popup_is_present())
        currency_popup.click_icon_help()
        self.assertTrue(currency_popup.check_help_link_is_correct())

    def test_help_link_on_weight_display_popup(self):
        print ("\n" + "TC#0000: Check help link on Weight Display popup")
        ribbon_bar = RibbonBar(self.driver)
        weight_display_popup = WeightDisplayPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_imperial_and_metric()
        self.assertTrue(weight_display_popup.check_popup_is_present())
        weight_display_popup.click_icon_help()
        self.assertTrue(weight_display_popup.check_help_link_is_correct())

    def test_help_link_on_manufacturer_alias_popup(self):
        print ("\n" + "TC#0000: Check help link on Manufacturer Alias popup")
        ribbon_bar = RibbonBar(self.driver)
        manufacturer_alias_popup = ManufacturerAliasPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_makes()
        self.assertTrue(manufacturer_alias_popup.check_popup_is_present())
        manufacturer_alias_popup.click_icon_help()
        self.assertTrue(manufacturer_alias_popup.check_help_link_is_correct())

    def test_help_link_on_model_alias_popup(self):
        print ("\n" + "TC#0000: Check help link on Model Alias popup")
        ribbon_bar = RibbonBar(self.driver)
        model_alias_popup = ModelAliasPopup(self.driver)
        ribbon_bar.open_tab_view()
        self.assertTrue(ribbon_bar.check_tab_view_is_present())
        ribbon_bar.click_button_models()
        self.assertTrue(model_alias_popup.check_popup_is_present())
        model_alias_popup.click_icon_help()
        self.assertTrue(model_alias_popup.check_help_link_is_correct())

    def test_help_link_on_column_sets_popup(self):
        print ("\n" + "TC#0000: Check help link on Column Sets popup")
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
        self.assertTrue(column_sets_popup.check_help_link_is_correct())

    def test_help_link_on_initial_setup_popup(self):
        print ("\n" + "TC#0000: Check help link on Initial Setup popup")
        ribbon_bar = RibbonBar(self.driver)
        settings_popup = SettingsPopup(self.driver)
        initial_setup_tab = InitialSetupTab(self.driver)
        initial_setup_popup = InitialSetupPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        ribbon_bar.click_button_settings()
        self.assertTrue(settings_popup.check_popup_is_present())
        settings_popup.click_initial_setup_label()
        self.assertTrue(initial_setup_tab.check_tab_is_present())
        initial_setup_tab.click_button_run_initial_setup()
        self.assertTrue(initial_setup_popup.check_popup_is_present())
        initial_setup_popup.click_icon_help()
        self.assertTrue(initial_setup_popup.check_help_link_is_correct())

    def test_help_link_on_inventory_view_popup(self):
        print ("\n" + "TC#0000: Check help link on Inventory View popup")
        device = Variables.vrep
        inventory_view_popup = InventoryViewPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_page.check_device_is_present(device))
        devices_page.select_device_in_table(device)
        self.assertTrue(ribbon_bar.check_devices_tab_is_present())
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_inventory_box_is_present())
        ribbon_bar.click_button_inventory()
        ribbon_bar.click_view_label()
        self.assertTrue(inventory_view_popup.check_popup_is_present(device))
        inventory_view_popup.click_icon_help()
        self.assertTrue(inventory_view_popup.check_help_link_is_correct())

    def test_help_link_on_on_demand_inventory_scan_popup(self):
        print ("\n" + "TC#0000: Check help link on On Demand Inventory Scan popup")
        device = Variables.vrep
        on_demand_inventory_scan_popup = OnDemandInventoryScanPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_page.check_device_is_present(device))
        devices_page.select_device_in_table(device)
        self.assertTrue(ribbon_bar.check_devices_tab_is_present())
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_inventory_box_is_present())
        ribbon_bar.click_button_inventory()
        ribbon_bar.click_on_demand_label()
        self.assertTrue(on_demand_inventory_scan_popup.check_popup_is_present())
        on_demand_inventory_scan_popup.click_icon_help()
        self.assertTrue(on_demand_inventory_scan_popup.check_help_link_is_correct())

    def test_help_link_on_wake_up_popup(self):
        print ("\n" + "TC#0000: Check help link on Wake on LAN popup")
        device = Variables.vrep
        wake_on_lan_popup = WakeOnLANPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_page.check_device_is_present(device))
        devices_page.select_device_in_table(device)
        self.assertTrue(ribbon_bar.check_devices_tab_is_present())
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_button_wake_up_is_present())
        ribbon_bar.click_button_wake_up()
        self.assertTrue(wake_on_lan_popup.check_popup_is_present())
        wake_on_lan_popup.click_icon_help()
        self.assertTrue(wake_on_lan_popup.check_help_link_is_correct())

    def test_help_link_on_move_device_popup(self):
        print ("\n" + "TC#0000: Check help link on Move Device popup")
        device = Variables.vrep
        move_device_popup = MoveDevicePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_page.check_device_is_present(device))
        devices_page.select_device_in_table(device)
        self.assertTrue(ribbon_bar.check_devices_tab_is_present())
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_site_management_box_is_present())
        ribbon_bar.click_button_move_device()
        self.assertTrue(move_device_popup.check_popup_is_present())
        move_device_popup.click_icon_help()
        self.assertTrue(move_device_popup.check_help_link_is_correct())

    def test_help_link_on_patch_manager_popup(self):
        print ("\n" + "TC#0000: Check help link on Patch Manager popup")
        device = Variables.vrep
        patch_manager_popup = PatchManagerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_page.check_device_is_present(device))
        devices_page.select_device_in_table(device)
        self.assertTrue(ribbon_bar.check_devices_tab_is_present())
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_site_management_box_is_present())
        ribbon_bar.click_button_move_device()
        self.assertTrue(patch_manager_popup.check_popup_is_present())
        patch_manager_popup.click_icon_help()
        self.assertTrue(patch_manager_popup.check_help_link_is_correct())

    def test_help_link_on_reports_popup(self):
        print ("\n" + "TC#0000: Check help link on Reports popup")
        device = Variables.vrep
        reports_popup = ReportsPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        self.assertTrue(devices_page.check_device_is_present(device))
        devices_page.select_device_in_table(device)
        self.assertTrue(ribbon_bar.check_devices_tab_is_present())
        ribbon_bar.open_tab_devices()
        self.assertTrue(ribbon_bar.check_site_management_box_is_present())
        ribbon_bar.click_button_reports()
        self.assertTrue(reports_popup.check_popup_is_present())
        reports_popup.click_icon_help()
        self.assertTrue(reports_popup.check_help_link_is_correct())

    # def test_help_link_on_file_browser_popup(self):
    #     print ("\n" + "TC#0000: Check help link on File Browser popup")
    #     device = Variables.vrep
    #     file_expplorer_popup = FileExplorerPopup(self.driver)
    #     ribbon_bar = RibbonBar(self.driver)
    #     left_menu_devices = LeftMenuDevices(self.driver)
    #     devices_page = DevicesPage(self.driver)
    #     left_menu_devices.open_menu_devices()
    #     left_menu_devices.click_global_site_view_label()
    #     self.assertTrue(devices_page.check_device_is_present(device))
    #     devices_page.select_device_in_table(device)
    #     self.assertTrue(ribbon_bar.check_devices_tab_is_present())
    #     ribbon_bar.open_tab_tools()
    #     self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
    #     ribbon_bar.click_button_file_browser()
    #     self.assertTrue(file_expplorer_popup.check_popup_is_present())
    #     file_expplorer_popup.click_icon_help()
    #     self.assertTrue(file_expplorer_popup.check_help_link_is_correct())
    #
    # def test_help_link_on_ping_result_popup(self):
    #     print ("\n" + "TC#0000: Check help link on Ping Result popup")
    #     device = Variables.vrep
    #     ping_result_popup = PingResultPopup(self.driver)
    #     ribbon_bar = RibbonBar(self.driver)
    #     left_menu_devices = LeftMenuDevices(self.driver)
    #     devices_page = DevicesPage(self.driver)
    #     left_menu_devices.open_menu_devices()
    #     left_menu_devices.click_global_site_view_label()
    #     self.assertTrue(devices_page.check_device_is_present(device))
    #     devices_page.select_device_in_table(device)
    #     self.assertTrue(ribbon_bar.check_devices_tab_is_present())
    #     ribbon_bar.open_tab_tools()
    #     self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
    #     ribbon_bar.click_button_ping()
    #     self.assertTrue(ping_result_popup.check_popup_is_present())
    #     ping_result_popup.click_icon_help()
    #     self.assertTrue(ping_result_popup.check_help_link_is_correct())
    #
    # def test_help_link_on_process_viewer_popup(self):
    #     print ("\n" + "TC#0000: Check help link on Process Viewer popup")
    #     device = Variables.vrep
    #     process_explorer_popup = ProcessExplorerPopup(self.driver)
    #     ribbon_bar = RibbonBar(self.driver)
    #     left_menu_devices = LeftMenuDevices(self.driver)
    #     devices_page = DevicesPage(self.driver)
    #     left_menu_devices.open_menu_devices()
    #     left_menu_devices.click_global_site_view_label()
    #     self.assertTrue(devices_page.check_device_is_present(device))
    #     devices_page.select_device_in_table(device)
    #     self.assertTrue(ribbon_bar.check_devices_tab_is_present())
    #     ribbon_bar.open_tab_tools()
    #     self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
    #     ribbon_bar.click_button_process_viewer()
    #     self.assertTrue(process_explorer_popup.check_popup_is_present())
    #     process_explorer_popup.click_icon_help()
    #     self.assertTrue(process_explorer_popup.check_help_link_is_correct())
    #
    # def test_help_link_on_event_viewer_popup(self):
    #     print ("\n" + "TC#0000: Check help link on Event Viewer popup")
    #     device = Variables.vrep
    #     event_viewer_popup = EventViewerPopup(self.driver)
    #     ribbon_bar = RibbonBar(self.driver)
    #     left_menu_devices = LeftMenuDevices(self.driver)
    #     devices_page = DevicesPage(self.driver)
    #     left_menu_devices.open_menu_devices()
    #     left_menu_devices.click_global_site_view_label()
    #     self.assertTrue(devices_page.check_device_is_present(device))
    #     devices_page.select_device_in_table(device)
    #     self.assertTrue(ribbon_bar.check_devices_tab_is_present())
    #     ribbon_bar.open_tab_tools()
    #     self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
    #     ribbon_bar.click_button_event_viewer()
    #     self.assertTrue(event_viewer_popup.check_popup_is_present())
    #     event_viewer_popup.click_icon_help()
    #     self.assertTrue(event_viewer_popup.check_help_link_is_correct())
    #
    # def test_help_link_on_wmi_explorer_popup(self):
    #     print ("\n" + "TC#0000: Check help link on WMI Explorer popup")
    #     device = Variables.vrep
    #     wmi_explorer_popup = WMIExplorerPopup(self.driver)
    #     ribbon_bar = RibbonBar(self.driver)
    #     left_menu_devices = LeftMenuDevices(self.driver)
    #     devices_page = DevicesPage(self.driver)
    #     left_menu_devices.open_menu_devices()
    #     left_menu_devices.click_global_site_view_label()
    #     self.assertTrue(devices_page.check_device_is_present(device))
    #     devices_page.select_device_in_table(device)
    #     self.assertTrue(ribbon_bar.check_devices_tab_is_present())
    #     ribbon_bar.open_tab_tools()
    #     self.assertTrue(ribbon_bar.check_computer_tools_box_is_present())
    #     ribbon_bar.click_button_wmi_explorer()
    #     self.assertTrue(wmi_explorer_popup.check_popup_is_present())
    #     wmi_explorer_popup.click_icon_help()
    #     self.assertTrue(wmi_explorer_popup.check_help_link_is_correct())

    def tearDown(self):
        help_window = BaseActions(self.driver)
        help_window._close_help_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=1)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())
