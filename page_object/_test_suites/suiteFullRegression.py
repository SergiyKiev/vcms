import logging
import unittest

from _feature_objects.featureLeftMenu import *
from _feature_objects.featurePopupAreYouSure import AreYouSurePopup
from _feature_objects.featurePopupClientSettings import *
from _feature_objects.featurePopupColumnSetDesigner import ColumnSetDesignerPopup
from _feature_objects.featurePopupConfiguration import *
from _feature_objects.featurePopupCurrency import CurrencyPopup
from _feature_objects.featurePopupError import ErrorPopup
from _feature_objects.featurePopupIPAddress import IPAddressPopup
from _feature_objects.featurePopupManufacturerAlias import ManufacturerAliasPopup
from _feature_objects.featurePopupModelAlias import ModelAliasPopup
from _feature_objects.featurePopupResetPassword import ResetPasswordPopup
from _feature_objects.featurePopupSettings import *
from _feature_objects.featurePopupUnableToRemove import UnableToRemovePopup
from _feature_objects.featurePopupUserSettings import UserSettingsPopup
from _feature_objects.featureRibbonBar import *
from _feature_objects.featureTabs import *
from _pages.pageLogin import LoginPage
from _pages.pageMain import MainPage
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
        left_menu = LeftMenu(self.driver)
        left_menu.open_menu_devices()
        left_menu.expand_global_site_view_tree()

    def test_open_left_menus(self):
        print ("\n" + "TC#xxxx. Open left side menus")
        left_menu = LeftMenu(self.driver)
        left_menu.open_menu_home()
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        left_menu.open_menu_administration()
        self.assertTrue(left_menu.check_menu_administration_is_visible())
        left_menu.open_menu_tasks()
        self.assertTrue(left_menu.check_menu_tasks_is_visible())
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_visible())
        left_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_menu.check_menu_software_and_patch_manager_is_visible())
        # left_menu.open_menu_password_reset()
        print ("Test is passed" + "\n")

    def test_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup")
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        print ("Test is passed" + "\n")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name")
        sitename = "New site #9101"
        main_page = MainPage(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.delete_site_if_exists(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field")
        left_menu = LeftMenu(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.click_button_cancel()
        self.assertFalse(site_name_popup.check_popup_is_present())
        print ("Test is passed" + "\n")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name")
        sitename = "Default Site"
        left_menu = LeftMenu(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        error_popup = ErrorPopup(self.driver)
        left_menu.click_global_site_view_label()
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
        left_menu = LeftMenu(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.delete_site_if_exists(fifty_symbols_name)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        main_page.delete_site_if_exists(fifty_one_symbols_name)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(fifty_one_symbols_name))
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.enter_text_into_name_text_field(fifty_one_symbols_name)
        site_name_popup.click_button_ok()
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(fifty_one_symbols_name))
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        main_page.delete_site_from_global_site_view_tree(fifty_symbols_name)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        print ("Test is passed" + "\n")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
        sitename = "Site #9118"
        subsitename_one = sitename + "-01"
        subsitename_two = sitename + "-02"
        main_page = MainPage(self.driver)
        left_menu = LeftMenu(self.driver)
        main_page.delete_site_if_exists(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_new_site(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_new_subsite(sitename, subsitename_one)
        self.assertTrue(left_menu.check_subsite_is_in_parent_site(sitename, subsitename_one))
        main_page.create_new_subsite(sitename, subsitename_two)
        self.assertTrue(left_menu.check_subsite_is_in_parent_site(sitename, subsitename_two))
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
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
        main_page = MainPage(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_global_site_view_label()
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
        ip_address_ranges = IPAddressRangesTab(self.driver)
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_global_site_view_label()
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
        left_menu = LeftMenu(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        site_tab = SiteTab(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu.click_default_site_in_global_site_view()
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
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        site_tab = SiteTab(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu = LeftMenu(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(
            configuration_popup._is_element_present(configuration_popup.TAB_SITE))  # add verification method to class
        self.assertFalse(configuration_popup._is_element_disabled(
            site_tab.FIELD_NAME))  # add verification method to class
        self.assertEqual(sitename, site_tab.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
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
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        site_tab = SiteTab(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_if_exists(sitename + modifed)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename + modifed))
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertFalse(site_tab.check_name_text_field_disabled())
        self.assertEqual(sitename, site_tab.get_name_text_field_value())
        site_tab.enter_text_into_name_text_field(modifed)
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename + modifed))
        left_menu.click_site_in_global_site_view_tree(sitename + modifed)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertEqual(sitename + modifed, site_tab.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        main_page.delete_site_from_global_site_view_tree(sitename + modifed)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename + modifed))
        main_page.delete_site_if_exists(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_configuration_popup_open_column_set_designer_popup(self):
        print ("\n" + "TC#9238. Devices page. Configuration popup. Open Column Set Designer popup")
        configuration_popup = ConfigurationPopup(self.driver)
        column_set_designer = ColumnSetDesignerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        site_tab = SiteTab(self.driver)
        left_menu = LeftMenu(self.driver)
        left_menu.click_default_site_in_global_site_view()
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
        main_page = MainPage(self.driver)
        left_menu = LeftMenu(self.driver)
        site_tab = SiteTab(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        devices_tab = DevicesTab(self.driver)
        left_menu.click_global_site_view_label()
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
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        site_tab.select_columnset_in_drop_down_list(columnset1)
        self.assertTrue(site_tab.check_columnset_is_selected_from_drop_down_list(columnset1))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(devices_tab.check_columns_are_present(columns_list1))
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        site_tab.select_columnset_in_drop_down_list(columnset2)
        self.assertTrue(site_tab.check_columnset_is_selected_from_drop_down_list(columnset2))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_popup_is_present())
        self.assertTrue(devices_tab.check_columns_are_present(columns_list2))
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_configuration_popup_create_column_set(self):
        print ("\n" + "TC#9999. Devices page. Configuration popup. Create column set")
        sitename = "Site#9999"
        columnsetname = "ColumnSet#9999-01"
        columns_list = ["Device Name", "Device ID", "Domain", "Site"]
        main_page = MainPage(self.driver)
        devices_tab = DevicesTab(self.driver)
        left_menu = LeftMenu(self.driver)
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
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        left_menu.click_site_in_global_site_view_tree(sitename)
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
        self.assertTrue(devices_tab.check_columns_are_present(columns_list))
        main_page.delete_site_from_global_site_view_tree(sitename)
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
        left_menu = LeftMenu(self.driver)
        left_menu.open_menu_devices()

    def test_delete_created_site_from_global_site_view_tree(self):
        print ("\n" + "TC#9607. Devices page. Delete created site from Global Site View tree")
        sitename = "Test#9607"
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_menu = LeftMenu(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_delete_default_site_from_global_site_view_tree(self):
        print ("\n" + "TC#8888. Devices page. Delete Default site from Global Site View tree")
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        unable_to_remove_popup = UnableToRemovePopup(self.driver)
        left_menu.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(unable_to_remove_popup.check_popup_is_present())
        unable_to_remove_popup.click_button_ok()
        self.assertTrue(left_menu.check_default_site_is_in_global_site_view_tree())
        print ("Test is passed" + "\n")

    def test_delete_subsite_from_site_tree(self):
        print ("\n" + "TC#3333. Devices page. Delete subsite from Global Site View tree")
        sitename = "TC#3333"
        subsitename = "TC#3333-01"
        main_page = MainPage(self.driver)
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_subsite_if_not_exists(sitename, subsitename)
        self.assertTrue(left_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        left_menu.click_subsite_in_site_tree(sitename, subsitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_delete_site_with_subsite(self):
        print ("\n" + "TC#0000. Devices page. Delete site with subsite from Global Site View tree")
        sitename = "TC#0000"
        subsitename = "TC#0000-01"
        main_page = MainPage(self.driver)
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.delete_site_if_exists(sitename)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_subsite_if_not_exists(sitename, subsitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(subsitename))
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        self.assertFalse(left_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_cancel_site_deletion_from_global_site_view(self):
        print ("\n" + "TC#1111. Devices page. Cancel site deletion")
        sitename = "TC#1111"
        main_page = MainPage(self.driver)
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_button_cancel()
        self.assertTrue(main_page.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_open_are_you_sure_popup(self):
        print ("\n" + "TC#2222. Devices page. Open Are you sure popup")
        sitename = "TC#2222"
        main_page = MainPage(self.driver)
        left_menu = LeftMenu(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_popup_is_present())
        are_you_sure_popup.click_system_button_close()
        self.assertFalse(are_you_sure_popup.check_popup_is_present())
        main_page.delete_site_from_global_site_view_tree(sitename)
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
class InvenotryFeature(unittest.TestCase):
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

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()

    def test_help_link_on_home_tab(self):
        print ("\n" + "TC#0000: Check help link on home tab")
        left_menu = LeftMenu(self.driver)
        home_tab = HomeTab(self.driver)
        left_menu.open_menu_home()
        self.assertTrue(home_tab.check_tab_is_present())
        home_tab.click_icon_help()
        self.assertTrue(home_tab.check_help_link_is_correct())

    def test_help_link_on_devices_tab(self):
        print ("\n" + "TC#0000: Check help link on devices tab")
        left_menu = LeftMenu(self.driver)
        devices_tab = DevicesTab(self.driver)
        left_menu.open_menu_devices()
        devices_tab.click_icon_help()
        self.assertTrue(devices_tab.check_help_link_is_correct())

    def test_help_link_on_administration_tab(self):
        print ("\n" + "TC#0000: Check help link on administration tab")
        left_menu = LeftMenu(self.driver)
        administration_tab = AdministrationTab(self.driver)
        left_menu.open_menu_administration()
        administration_tab.click_icon_help()
        self.assertTrue(administration_tab.check_help_link_is_correct())

    def test_help_link_on_tasks_tab(self):
        print ("\n" + "TC#0000: Check help link on tasks tab")
        left_menu = LeftMenu(self.driver)
        tasks_tab = TasksTab(self.driver)
        left_menu.open_menu_tasks()
        tasks_tab.click_icon_help()
        self.assertTrue(tasks_tab.check_help_link_is_correct())

    def test_help_link_on_reporting_tab(self):
        print ("\n" + "TC#0000: Check help link on reporting tab")
        left_menu = LeftMenu(self.driver)
        reporting_tab = ReportingTab(self.driver)
        left_menu.open_menu_reporting()
        self.assertTrue(left_menu.check_menu_reporting_is_visible())
        reporting_tab.click_icon_help()
        self.assertTrue(reporting_tab.check_help_link_is_correct())

    def test_help_link_on_software_and_patch_manager_tab(self):
        print ("\n" + "TC#0000: Check help link on software and patch manager tab")
        left_menu = LeftMenu(self.driver)
        software_and_patch_manager_tab = SoftwareAndPatchManagerTab(self.driver)
        left_menu.open_menu_software_and_patch_manager()
        software_and_patch_manager_tab.click_icon_help()
        self.assertTrue(software_and_patch_manager_tab.check_help_link_is_correct())

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
        self.assertTrue(ribbon_bar.check_home_drop_down_list_is_present())
        ribbon_bar.click_change_home_screen_label()
        self.assertTrue(select_dashboard_popup.check_popup_is_present())
        select_dashboard_popup.click_icon_help()
        self.assertTrue(select_dashboard_popup.check_help_link_is_correct())

    def test_help_link_on_user_settings_popup(self):
        print ("\n" + "TC#0000: Check help link on User Settings popup")
        ribbon_bar = RibbonBar(self.driver)
        user_settings_popup = UserSettingsPopup(self.driver)
        ribbon_bar.click_button_admin_user()
        self.assertTrue(ribbon_bar.check_home_drop_down_list_is_present())
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
    #     self.assertTrue(inventory_tab.check_tab_is_present())
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
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        left_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_popup_is_present())
        site_name_popup.click_icon_help()
        self.assertTrue(site_name_popup.check_help_link_is_correct())

    def test_help_link_on_configuration_popup(self):
        print ("\n" + "TC#0000: Check help link on Configuration popup")
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        left_menu.click_global_site_view_label()
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
        main_page = MainPage(self.driver)
        ip_address_ranges_tab = IPAddressRangesTab(self.driver)
        ip_address_popup = IPAddressPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        main_page.create_site_if_not_exists(sitename)
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_popup_is_present())
        configuration_popup.click_ip_address_ranges_tab()
        self.assertTrue(ip_address_ranges_tab.check_tab_is_present())
        ip_address_ranges_tab.click_button_add()
        self.assertTrue(ip_address_ranges_tab.check_popup_is_present())
        configuration_popup.click_icon_help()
        self.assertTrue(ip_address_popup.check_help_link_is_correct())

    def test_help_link_on_move_site_popup(self):
        print ("\n" + "TC#0000: Check help link on Move Site popup")
        sitename = "HelpTest"
        ribbon_bar = RibbonBar(self.driver)
        left_menu = LeftMenu(self.driver)
        main_page = MainPage(self.driver)
        move_site_popup = MoveSitePopup(self.driver)
        ribbon_bar.open_tab_home()
        self.assertTrue(ribbon_bar.check_tab_home_is_present())
        left_menu.open_menu_devices()
        self.assertTrue(left_menu.check_menu_devices_is_visible())
        main_page.create_site_if_not_exists(sitename)
        left_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_move()
        self.assertTrue(move_site_popup.check_popup_is_present())
        move_site_popup.click_icon_help()
        self.assertTrue(move_site_popup.check_help_link_is_correct())

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
