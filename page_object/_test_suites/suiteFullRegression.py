
import unittest
from _variables.variables import *
from _pages.pageLogin import LoginPage
from _pages.pageMain import MainPage
from _feature_objects.featurePopups import *
from _feature_objects.featureRibbonBar import *
from _feature_objects.featureLeftSideMenu import *
from _feature_objects.featureTabs import *
from _feature_objects.featureHelp import *
from selenium import webdriver


class SiteCreation(unittest.TestCase):

    driver = None #global variable

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
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_menu_devices()
        left_side_menu.expand_global_site_view_tree()

    def test_open_left_side_menus(self):
        print ("\n" + "TC#xxxx. Open left side menus")
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_menu_home()
        left_side_menu.open_menu_devices()
        self.assertTrue(left_side_menu.check_menu_devices_is_visible())
        left_side_menu.open_menu_administration()
        self.assertTrue(left_side_menu.check_menu_administration_is_visible())
        left_side_menu.open_menu_tasks()
        self.assertTrue(left_side_menu.check_menu_tasks_is_visible())
        left_side_menu.open_menu_reporting()
        self.assertTrue(left_side_menu.check_menu_reporting_is_visible())
        left_side_menu.open_menu_software_and_patch_manager()
        self.assertTrue(left_side_menu.check_menu_software_and_patch_manager_is_visible())
        # left_side_menu.open_menu_password_reset()
        print ("Test is passed" + "\n")

    def test_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup")
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name")
        sitename = "New site #9101"
        main_page = MainPage(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.delete_site_if_exists(sitename)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        left_side_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_is_popup_present())
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field")
        left_side_menu = LeftSideMenu(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_side_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_is_popup_present())
        site_name_popup.click_button_cancel()
        self.assertFalse(site_name_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name")
        sitename = "Default Site"
        left_side_menu = LeftSideMenu(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        error_popup = ErrorPopup(self.driver)
        left_side_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_is_popup_present())
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(error_popup.check_is_popup_present())
        error_popup.click_button_ok()
        self.assertFalse(error_popup.check_is_popup_present())
        self.assertTrue(site_name_popup.check_is_popup_present())
        site_name_popup.click_system_button_close()
        self.assertFalse(site_name_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_create_site_with_fifty_one_symbols(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        fifty_symbols_name = "51symbols51symbols51symbols51symbols51symbols!<ok>"
        fifty_one_symbols_name = fifty_symbols_name + "1"
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.delete_site_if_exists(fifty_symbols_name)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        main_page.delete_site_if_exists(fifty_one_symbols_name)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(fifty_one_symbols_name))
        left_side_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_new_site_is_present())
        ribbon_bar.click_button_new_site()
        self.assertTrue(site_name_popup.check_is_popup_present())
        site_name_popup.enter_text_into_name_text_field(fifty_one_symbols_name)
        site_name_popup.click_button_ok()
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(fifty_one_symbols_name))
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        main_page.delete_site_from_global_site_view_tree(fifty_symbols_name)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(fifty_symbols_name))
        print ("Test is passed" + "\n")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
        sitename = "Site #9118"
        subsitename_one = sitename + "-01"
        subsitename_two = sitename + "-02"
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        main_page.delete_site_if_exists(sitename)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_new_site(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_new_subsite(sitename, subsitename_one)
        self.assertTrue(left_side_menu.check_subsite_is_in_parent_site(sitename, subsitename_one))
        main_page.create_new_subsite(sitename, subsitename_two)
        self.assertTrue(left_side_menu.check_subsite_is_in_parent_site(sitename, subsitename_two))
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
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
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_menu_devices()

    def test_open_configuration_popup(self):
        print ("\n" + "TC#9601. Devices page. Open 'Configuration' popup")
        main_page = MainPage(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_side_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_global_site_view(self):
        print ("\n" + "TC#9228. Devices page. Open Configuration popup from the Global Site View")
        configuration_popup = ConfigurationPopup(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_side_menu.click_global_site_view_label()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        self.assertTrue(configuration_popup.check_name_text_field_disabled())
        self.assertEqual("Global Site View", configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_default_site(self):
        print ("\n" + "TC#9230. Devices page. Open Configuration popup from the Default Site main label")
        left_side_menu = LeftSideMenu(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_side_menu.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        self.assertTrue(configuration_popup.check_name_text_field_disabled())
        self.assertEqual("Default Site", configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_created_site(self):
        print ("\n" + "TC#9236. Devices page. Open Configuration popup from the created site")
        sitename = "Site#9236"
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup._is_element_present(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL))
        self.assertFalse(configuration_popup._is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators._FIELD))
        self.assertEqual(sitename, configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
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
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_menu_devices()

    def test_configuration_popup_change_site_name(self):
        print ("\n" + "TC#9237. Devices page. Configuration popup. Change site name")
        sitename = "Site#9237"
        modifed = "_modifed"
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_if_exists(sitename + modifed)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename + modifed))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertFalse(configuration_popup.check_name_text_field_disabled())
        self.assertEqual(sitename, configuration_popup.get_name_text_field_value())
        configuration_popup.enter_text_into_name_text_field(modifed)
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename + modifed))
        left_side_menu.click_site_in_global_site_view_tree(sitename + modifed)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertEqual(sitename + modifed, configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        main_page.delete_site_from_global_site_view_tree(sitename + modifed)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename + modifed))
        main_page.delete_site_if_exists(sitename)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_configuration_popup_open_column_set_designer_popup(self):
        print ("\n" + "TC#9238. Devices page. Configuration popup. Open Column Set Designer popup")
        configuration_popup = ConfigurationPopup(self.driver)
        column_set_designer = ColumnSetDesignerPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        configuration_popup.click_button_new()
        self.assertTrue(configuration_popup.check_is_popup_present())
        column_set_designer.click_system_button_close()
        self.assertFalse(column_set_designer.check_is_popup_present())
        configuration_popup.click_system_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_configuration_popup_apply_column_set(self):
        print ("\n" + "TC#9239. Devices page. Configuration popup. Apply Column set to the site")
        sitename = "Site#9239"
        columnset1 = "ColumnSet#9239-01"
        columnset2 = "test1"
        columns_list1 = ["Device Name", "OS Name", "Caption", "IP Address"]
        columns_list2 = ["Device Name", "Device ID", "Domain", "Site", "User Name"]
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        devices_tab = DevicesTab(self.driver)
        left_side_menu.click_global_site_view_label()
        ribbon_bar.click_tab_view()
        self.assertTrue(ribbon_bar.check_button_edit_or_create_is_present())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_is_popup_present())
        column_sets_popup.delete_columnset_if_exists(columnset1)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnset1))
        column_sets_popup.delete_columnset_if_exists(columnset2)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnset2))
        column_sets_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_is_popup_present())
        column_set_designer_popup.create_columnset(columnset1, columns_list1)
        self.assertFalse(column_set_designer_popup.check_is_popup_present())
        self.assertTrue(column_sets_popup.check_is_columnset_present(columnset1))
        column_sets_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_is_popup_present())
        column_set_designer_popup.create_columnset(columnset2, columns_list2)
        self.assertFalse(column_set_designer_popup.check_is_popup_present())
        self.assertTrue(column_sets_popup.check_is_columnset_present(columnset2))
        column_sets_popup.click_button_ok()
        self.assertFalse(column_sets_popup.check_is_popup_present())
        ribbon_bar.click_tab_home()
        self.assertTrue(ribbon_bar.check_button_exit_is_present())
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        configuration_popup.select_columnset_in_drop_down_list(columnset1)
        self.assertTrue(configuration_popup.check_columnset_is_selected_from_drop_down_list(columnset1))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        self.assertTrue(devices_tab.check_columns_are_present(columns_list1))
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        configuration_popup.select_columnset_in_drop_down_list(columnset2)
        self.assertTrue(configuration_popup.check_columnset_is_selected_from_drop_down_list(columnset2))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
        self.assertTrue(devices_tab.check_columns_are_present(columns_list2))
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_configuration_popup_create_column_set(self):
        print ("\n" + "TC#9999. Devices page. Configuration popup. Create column set")
        sitename = "Site#9999"
        columnsetname = "ColumnSet#9999-01"
        columns_list = ["Device Name", "Device ID", "Domain", "Site"]
        main_page = MainPage(self.driver)
        devices_tab = DevicesTab(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        column_set_designer_popup = ColumnSetDesignerPopup(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        ribbon_bar.click_tab_view()
        self.assertTrue(ribbon_bar.check_button_edit_or_create_is_present())
        ribbon_bar.click_button_edit_or_create()
        self.assertTrue(column_sets_popup.check_is_popup_present())
        column_sets_popup.delete_columnset_if_exists(columnsetname)
        self.assertFalse(column_sets_popup.check_is_columnset_present(columnsetname))
        column_sets_popup.click_button_ok()
        self.assertFalse(column_sets_popup.check_is_popup_present())
        ribbon_bar.click_tab_home()
        self.assertTrue(ribbon_bar.check_button_exit_is_present())
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_config_is_present())
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        configuration_popup.click_button_new()
        self.assertTrue(column_set_designer_popup.check_is_popup_present())
        column_set_designer_popup.create_columnset(columnsetname, columns_list)
        self.assertFalse(column_set_designer_popup.check_is_popup_present())
        configuration_popup.select_columnset_in_drop_down_list(columnsetname)
        self.assertTrue(configuration_popup.check_columnset_is_selected_from_drop_down_list(columnsetname))
        configuration_popup.click_button_close()
        self.assertFalse(configuration_popup.check_is_popup_present())
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
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_menu_devices()

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
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_menu_devices()

    def test_delete_created_site_from_global_site_view_tree(self):
        print ("\n" + "TC#9607. Devices page. Delete created site from Global Site View tree")
        sitename = "Test#9607"
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_is_popup_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_delete_default_site_from_global_site_view_tree(self):
        print ("\n" + "TC#8888. Devices page. Delete Default site from Global Site View tree")
        ribbon_bar = RibbonBar(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        unable_to_remove_popup = UnableToRemovePopup(self.driver)
        left_side_menu.click_default_site_in_global_site_view()
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(unable_to_remove_popup.check_is_popup_present())
        unable_to_remove_popup.click_button_ok()
        self.assertTrue(left_side_menu.check_default_site_is_in_global_site_view_tree())
        print ("Test is passed" + "\n")

    def test_delete_subsite_from_site_tree(self):
        print ("\n" + "TC#3333. Devices page. Delete subsite from Global Site View tree")
        sitename = "TC#3333"
        subsitename = "TC#3333-01"
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_subsite_if_not_exists(sitename, subsitename)
        self.assertTrue(left_side_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        left_side_menu.click_subsite_in_site_tree(sitename, subsitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_is_popup_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_side_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_delete_site_with_subsite(self):
        print ("\n" + "TC#0000. Devices page. Delete site with subsite from Global Site View tree")
        sitename = "TC#0000"
        subsitename = "TC#0000-01"
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.delete_site_if_exists(sitename)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_subsite_if_not_exists(sitename, subsitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(subsitename))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_is_popup_present())
        are_you_sure_popup.click_button_ok()
        self.assertFalse(left_side_menu.check_subsite_is_in_parent_site(sitename, subsitename))
        self.assertFalse(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_cancel_site_deletion_from_global_site_view(self):
        print ("\n" + "TC#1111. Devices page. Cancel site deletion")
        sitename = "TC#1111"
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_is_popup_present())
        are_you_sure_popup.click_button_cancel()
        self.assertTrue(main_page.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_open_are_you_sure_popup(self):
        print ("\n" + "TC#2222. Devices page. Open Are you sure popup")
        sitename = "TC#2222"
        main_page = MainPage(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.create_site_if_not_exists(sitename)
        self.assertTrue(left_side_menu.check_site_is_in_global_site_view_tree(sitename))
        left_side_menu.click_site_in_global_site_view_tree(sitename)
        self.assertTrue(ribbon_bar.check_button_delete_is_present())
        ribbon_bar.click_button_delete()
        self.assertTrue(are_you_sure_popup.check_is_popup_present())
        are_you_sure_popup.click_system_button_close()
        self.assertFalse(are_you_sure_popup.check_is_popup_present())
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
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_menu_devices()

    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page._close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

@unittest.skip
class Invenotry(unittest.TestCase):

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
        left_side_menu = LeftSideMenu(self.driver)


class HelpLinks(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: HELP")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()

    def test_open_help_links(self):
        print ("\n" + "TC#0000: Open help links")
        login_page = LoginPage(self.driver)
        help_window = HelpWindow(self.driver)
        home_tab = HomeTab(self.driver)
        left_side_menu = LeftSideMenu(self.driver)
        login_page.click_icon_help()
        self.assertTrue(help_window.check_logon_page_help_window())
        # help_window.close_help_window()
        # main_page = login_page.login()
        # main_page.check_main_page_loaded()
        # home_tab.click_icon_help()
        # self.assertTrue(help_window.check_home_tab_help_window())
        # # help_window.close_help_window()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())