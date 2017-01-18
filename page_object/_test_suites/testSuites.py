import unittest
from page_object._variables.variables import *
from page_object._pages.pageLogin import LoginPage
from page_object._pages.pageMain import MainPage
from page_object._feature_objects.popups import *
from page_object._feature_objects.ribbonBar import *
from page_object._feature_objects.leftSideMenu import *
from selenium import webdriver


class SiteCreation(unittest.TestCase):

    driver = None #global variable

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site creation (Suite ID: 9111)")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        # main_page = MainPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.close_popups()
        main_page.open_menu_devices()
        main_page.click_global_site_view_label()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page.close_popups()
        # main_page = main_page.open_menu_devices()
        # main_page.check_main_page_loaded()

    def test_open_site_name_popup(self):
        print ("\n" + "TC#9057. Open Site Name popup")
        main_page = MainPage(self.driver)
        new_site_popup = NewSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.click_global_site_view_label()
        ribbon_bar.click_button_new_site()
        self.assertTrue(new_site_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_create_new_site_with_acceptable_name(self):
        print ("\n" + "TC#9101. Create new site with acceptable name")
        sitename = "New site #9101"
        main_page = MainPage(self.driver)
        new_site_popup = NewSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.delete_site_if_exists(sitename)
        main_page.click_global_site_view_label()
        ribbon_bar.click_button_new_site()
        new_site_popup.enter_text_into_name_text_field(sitename)
        new_site_popup.click_button_ok()
        self.assertTrue(main_page.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_cancel_creating_site(self):
        print ("\n" + "TC#9058. Cancel creating new site with empty text field")
        main_page = MainPage(self.driver)
        new_site_popup = NewSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.click_global_site_view_label()
        ribbon_bar.click_button_new_site()
        new_site_popup.click_button_cancel()
        self.assertFalse(new_site_popup.check_is_popup_present())
        print ("Test is passed" + "\n")

    def test_create_site_with_duplicated_name(self):
        print ("\n" + "TC#9107. Create new site with duplicated name")
        sitename = "Default Site"
        main_page = MainPage(self.driver)
        new_site_popup = NewSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        error_popup = ErrorPopup(self.driver)
        main_page.click_global_site_view_label()
        ribbon_bar.click_button_new_site()
        new_site_popup.enter_text_into_name_text_field(sitename)
        new_site_popup.click_button_ok()
        self.assertTrue(main_page.is_element_present(Locators.POPUP_ERROR))
        error_popup.click_button_ok()
        new_site_popup.click_system_button_close()
        print ("Test is passed" + "\n")

    def test_create_site_with_fifty_one_symbols(self):
        print ("\n" + "TC#9104. Create site with name more than 50 symbols")
        main_page = MainPage(self.driver)
        new_site_popup = NewSitePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.delete_site_if_exists(Variables.fifty_symbols_name)
        main_page.click_global_site_view_label()
        ribbon_bar.click_button_new_site()
        new_site_popup.enter_text_into_name_text_field(Variables.fifty_one_symbols_name)
        new_site_popup.click_button_ok()
        self.assertFalse(main_page.check_site_is_in_global_site_view_tree(Variables.fifty_one_symbols_name))
        self.assertTrue(main_page.check_site_is_in_global_site_view_tree(Variables.fifty_symbols_name))
        main_page.delete_site_from_global_site_view_tree(Variables.fifty_symbols_name)
        print ("Test is passed" + "\n")

    def test_create_subsites_in_global_site_view_tree(self):
        print ("\n" + "TC#9118. Create subsites in the Global Site View tree")
        sitename = "Site #9118"
        subsitename_one = sitename + "-01"
        subsitename_two = sitename + "-02"
        main_page = MainPage(self.driver)
        main_page.delete_site_if_exists(sitename)
        main_page.create_new_site(sitename)
        self.assertTrue(main_page.check_site_is_in_global_site_view_tree(sitename))
        main_page.create_new_subsite(sitename, subsitename_one)
        self.assertTrue(main_page.check_subsite_is_in_parent_site(sitename, subsitename_one))
        main_page.create_new_subsite(sitename, subsitename_two)
        self.assertTrue(main_page.check_subsite_is_in_parent_site(sitename, subsitename_two))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration (Suite ID: 9112)")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        main_page = MainPage(cls.driver)
        main_page = MainPage(cls.driver)
        login_page.open_page()
        login_page.login()
        main_page.close_popups()
        main_page.open_menu_devices()
        main_page.click_global_site_view_label()


    def setUp(self):
        main_page = MainPage(self.driver)
        main_page.close_popups()
        # main_page = main_page.open_menu_devices()
        # main_page.check_main_page_loaded()

    def test_open_configuration_popup(self):
        print ("\n" + "TC#9601. Devices page. Open 'Configuration' popup")
        main_page = MainPage(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        main_page.click_global_site_view_label()
        main_page.click_button_config()
        self.assertTrue(main_page.is_element_present(Locators.POPUP_CONFIGURATION))
        configuration_popup.click_system_button_close()
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_global_site_view(self):
        print ("\n" + "TC#9228. Devices page. Open Configuration popup from the Global Site View")
        print ("Login to console. Go to the start point")
        main_page = MainPage(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        main_page.click_global_site_view_label()
        main_page.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        self.assertTrue(configuration_popup.check_name_text_feild_disabled())
        self.assertEqual("Global Site View", configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_default_site(self):
        print ("\n" + "TC#9230. Devices page. Open Configuration popup from the Default Site main label")
        main_page = MainPage(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.click_default_site_in_global_site_view_tree()
        ribbon_bar.click_button_config()
        self.assertTrue(configuration_popup.check_is_popup_present())
        self.assertTrue(configuration_popup.check_name_text_feild_disabled())
        self.assertEqual("Default Site", configuration_popup.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        print ("Test is passed" + "\n")

    def test_open_configuration_popup_from_created_site(self):
        print ("\n" + "TC#9236. Devices page. Open Configuration popup from the created site")
        sitename = "Site#9236"
        main_page = MainPage(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        main_page.click_site_in_global_site_view_tree(sitename)
        main_page.click_button_config()
        self.assertTrue(main_page.is_element_present(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL))
        self.assertFalse(main_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_))
        self.assertEqual(sitename, main_page.get_name_text_field_value())
        configuration_popup.click_system_button_close()
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration_SiteTab(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration - Site tab (Suite ID: 9234)")
        print ("\n" + "Login to console. Go to the start point")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        main_page = MainPage(cls.driver)
        main_page = MainPage(cls.driver)
        left_side_menu = LeftSideMenu(cls.driver)
        login_page.open_page()
        login_page.login()
        main_page.close_popups()
        left_side_menu.open_menu_devices()
        main_page.click_global_site_view_label()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page.close_popups()
        # main_page = main_page.open_menu_devices()
        # main_page.check_main_page_loaded()

    def test_open_left_side_menus(self):
        left_side_menu = LeftSideMenu(self.driver)
        left_side_menu.open_left_side_menu_home()
        left_side_menu.open_menu_devices()
        left_side_menu.open_left_side_menu_administration()
        left_side_menu.open_left_side_menu_tasks()
        left_side_menu.open_left_side_menu_reporting()
        left_side_menu.open_left_side_menu_software_and_patch_manager()
        # left_side_menu.open_left_side_menu_password_reset()

    def test_configuration_popup_change_site_name(self):
        print ("\n" + "TC#9237. Devices page. Configuration popup. Change site name")
        sitename = "Site#9237"
        modifed = "_modifed"
        main_page = MainPage(self.driver)
        main_page.create_site_if_not_exists(sitename)
        main_page.delete_site_if_exists(sitename + modifed)
        main_page.click_site_in_global_site_view_tree(sitename)
        main_page.click_button_config()
        self.assertFalse(main_page.is_element_disabled(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_))
        self.assertEqual(sitename, main_page.get_name_text_field_value())
        main_page.enter_text_into_configuration_popup_name_text_field(modifed)
        main_page.click_system_button_close()
        self.assertTrue(main_page.check_site_is_in_global_site_view_tree(sitename + modifed))
        main_page.click_site_in_global_site_view_tree(sitename + modifed)
        main_page.click_button_config()
        self.assertEqual(sitename + modifed, main_page.get_name_text_field_value())
        main_page.click_system_button_close()
        main_page.delete_site_from_global_site_view_tree(sitename + modifed)
        main_page.delete_site_if_exists(sitename)
        print ("Test is passed" + "\n")

    def test_configuration_popup_open_column_set_designer_popup(self):
        print ("\n" + "TC#9238. Devices page. Configuration popup. Open Column Set Designer popup")
        main_page = MainPage(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        main_page.click_default_site_in_global_site_view_tree()
        main_page.click_button_config()
        main_page.click_button_new()
        self.assertTrue(main_page.check_is_popup_present())
        main_page.click_column_set_popup_system_button_close()
        configuration_popup.click_system_button_close()
        print ("Test is passed" + "\n")

    def test_configuration_popup_apply_column_set(self):
        print ("\n" + "TC#9239. Devices page. Configuration popup. Apply Column set to the site")
        sitename = "Site#9239"
        columnset1 = "ColumnSet#9239-01"
        columnset2 = "ColumnSet#9239-02"
        main_page = MainPage(self.driver)
        column_sets_popup = ColumnSetsPopup(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.open_column_sets_popup_from_ribbon_bar()
        main_page.delete_columnset_if_exist(columnset1)
        main_page.delete_columnset_if_exist(columnset2)
        main_page.create_columnset(columnset1, Variables.columns_list1)
        main_page.create_columnset(columnset2, Variables.columns_list2)
        column_sets_popup.click_button_ok()
        ribbon_bar.click_tab_home()
        main_page.create_site_if_not_exists(sitename)
        main_page.click_site_in_global_site_view_tree(sitename)
        ribbon_bar.click_button_config()
        main_page.select_columnset_from_configuration_popup_column_set_dropdown_list(columnset1)
        configuration_popup.click_button_close()
        self.assertTrue(main_page.check_columns_are_presented_in_devices_list_header(Variables.columns_list1))
        ribbon_bar.click_button_config()
        main_page.select_columnset_from_configuration_popup_column_set_dropdown_list(columnset2)
        configuration_popup.click_button_close()
        self.assertTrue(main_page.check_columns_are_presented_in_devices_list_header(Variables.columns_list2))
        # main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")



    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page.close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class SiteConfiguration_IpAddressRangesTab(unittest.TestCase):

    pass

    driver = None

    @classmethod
    def setUpClass(cls):
        print ("\n" + "Test suite: Site configuration - IP Address Ranges tab (Suite ID: 9234)")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        main_page = MainPage(cls.driver)
        main_page = MainPage(cls.driver)
        login_page.open_page()
        login_page.login()
        main_page.close_popups()
        main_page.open_menu_devices()
        main_page.click_global_site_view_label()


    def setUp(self):
        main_page = MainPage(self.driver)
        main_page.close_popups()
        # main_page = main_page.open_menu_devices()
        # main_page.check_main_page_loaded()

    # def tearDown(self):
    #     page = MainPage(self.driver)
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
        main_page = MainPage(cls.driver)
        main_page = MainPage(cls.driver)
        login_page.open_page()
        login_page.login()
        main_page.close_popups()
        main_page.open_menu_devices()
        main_page.click_global_site_view_label()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page.close_popups()
        # main_page = main_page.open_menu_devices()
        # main_page.check_main_page_loaded()

    def test_delete_created_site_from_global_site_view_tree(self):
        print ("\n" + "TC#9607. Devices page. Delete created site from Global Site View tree")
        sitename = "Test#9607"
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.delete_site_if_exists(sitename)
        main_page.click_global_site_view_label()
        main_page.create_new_site(sitename)
        main_page.click_site_in_global_site_view_tree(sitename)
        ribbon_bar.click_delete_button()
        are_you_sure_popup.click_button_ok()
        self.assertFalse(main_page.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_delete_default_site_from_global_site_view_tree(self):
        print ("\n" + "TC#8888. Devices page. Delete Default site from Global Site View tree")
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        unable_to_remove_popup = UnableToRemovePopup(self.driver)
        main_page.click_default_site_in_global_site_view_tree()
        ribbon_bar.click_delete_button()
        self.assertTrue(unable_to_remove_popup.check_is_popup_present())
        unable_to_remove_popup.click_button_ok()
        self.assertTrue(main_page.is_element_present(Locators.LABEL_DEFAULT_SITE))
        print ("Test is passed" + "\n")

    def test_delete_subsite_from_site_tree(self):
        print ("\n" + "TC#3333. Devices page. Delete subsite from Global Site View tree")
        sitename = "TC#3333"
        subsitename = "TC#3333-01"
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.delete_site_if_exists(sitename)
        main_page.create_new_site(sitename)
        main_page.create_new_subsite(sitename, subsitename)
        main_page.click_subsite_in_site_tree(sitename, subsitename)
        ribbon_bar.click_delete_button()
        are_you_sure_popup.click_button_ok()
        self.assertFalse(main_page.check_subsite_is_in_parent_site(sitename, subsitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_delete_site_with_subsite(self):
        print ("\n" + "TC#0000. Devices page. Delete site with subsite from Global Site View tree")
        sitename = "TC#0000"
        subsitename = "TC#0000-01"
        main_page = MainPage(self.driver)
        main_page.delete_site_if_exists(sitename)
        main_page.create_new_site(sitename)
        main_page.create_new_subsite(sitename, subsitename)
        main_page.delete_site_from_global_site_view_tree(sitename)
        self.assertFalse(main_page.check_subsite_is_in_parent_site(sitename, subsitename))
        self.assertFalse(main_page.check_site_is_in_global_site_view_tree(sitename))

    def test_cancel_site_deletion_from_global_site_view(self):
        print ("\n" + "TC#1111. Devices page. Cancel site deletion")
        sitename = "TC#1111"
        main_page = MainPage(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        main_page.create_site_if_not_exists(sitename)
        main_page.click_site_in_global_site_view_tree(sitename)
        ribbon_bar.click_delete_button()
        are_you_sure_popup.click_button_cancel()
        self.assertTrue(main_page.check_site_is_in_global_site_view_tree(sitename))
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    def test_open_are_you_sure_popup(self):
        print ("\n" + "TC#2222. Devices page. Open Are you sure popup")
        sitename = "TC#2222"
        main_page = MainPage(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.create_site_if_not_exists(sitename)
        main_page.click_site_in_global_site_view_tree(sitename)
        ribbon_bar.click_delete_button()
        self.assertTrue(are_you_sure_popup.check_is_popup_present())
        are_you_sure_popup.click_system_button_close()
        main_page.delete_site_from_global_site_view_tree(sitename)
        print ("Test is passed" + "\n")

    # def tearDown(self):
    #     page = MainPage(self.driver)
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
    #     main_page = MainPage(cls.driver)
    #     main_page.close_popups()
    #     main_page = main_page.open_menu_devices()
    #     main_page.check_main_page_loaded()
    #     main_page.click_global_site_view_label()
    #
    # def setUp(self):
    #     main_page = MainPage(self.driver)
    #     main_page.close_popups()
    #     # main_page = main_page.open_menu_devices()
    #     # main_page.check_main_page_loaded()
    #
    # def test_delete_created_site_from_global_site_view_tree(self):
    #     print ("\n" + "TC#9607. Devices page. Delete created site from Global Site View tree" + "\n")
    #     sitename = "Test#9607"
    #     main_page = MainPage(self.driver)
    #     main_page.delete_site_if_exists(sitename)
    #     main_page.click_global_site_view_label()
    #     main_page.create_new_site(sitename)
    #     main_page.click_site_in_global_site_view_tree(sitename)
    #     main_page.click_delete_button()
    #     main_page.click_ok()
    #     self.assertFalse(main_page.check_site_is_in_global_site_view_tree(sitename))
    #     print ("Test is passed" + "\n")
    #
    # def test_delete_default_site_from_global_site_view_tree(self):
    #     print ("\n" + "TC#----. Devices page. Delete Default site from Global Site View tree" + "\n")
    #     main_page = MainPage(self.driver)
    #     main_page.click_default_site_in_global_site_view_tree()
    #     main_page.click_delete_button()
    #     self.assertTrue(main_page.is_element_present(Locators.POPUP_UNABLE_TO_REMOVE))
    #     main_page.click_unable_to_remove_popup_ok_button()
    #     self.assertTrue(main_page.is_element_present(Locators.LABEL_DEFAULT_SITE))
    #     print ("Test is passed" + "\n")
    #
    # def test_delete_subsite_from_site_tree(self):
    #     print ("\n" + "TC#----. Devices page. Delete subsite from Global Site View tree" + "\n")
    #     sitename = "TC#____"
    #     subsitename = "TC#____-01"
    #     main_page = MainPage(self.driver)
    #     main_page.create_site_if_not_exists(sitename)
    #     main_page.create_subsite_if_not_exists(sitename, subsitename)
    #     main_page.click_subsite_in_site_tree(sitename, subsitename)
    #     main_page.click_delete_button()
    #     main_page.click_ok()
    #     self.assertFalse(main_page.check_subsite_is_in_parent_site(sitename, subsitename))
    #     main_page.delete_site_from_global_site_view_tree(sitename)
    #     print ("Test is passed" + "\n")
    #
    # def test_delete_site_with_subsite(self):
    #     print ("\n" + "TC#----. Devices page. Delete site with subsite from Global Site View tree" + "\n")
    #     sitename = "TC#____"
    #     subsitename = "TC#____-01"
    #     main_page = MainPage(self.driver)
    #     main_page.create_site_if_not_exists(sitename)
    #     main_page.create_subsite_if_not_exists(sitename, subsitename)
    #     main_page.delete_site_from_global_site_view_tree(sitename)
    #     self.assertFalse(main_page.check_subsite_is_in_parent_site(sitename, subsitename))
    #     self.assertFalse(main_page.check_site_is_in_global_site_view_tree(sitename))
    #
    # def test_cancel_site_deletion_from_global_site_view(self):
    #     print ("\n" + "TC#1111. Devices page. Cancel site deletion" + "\n")
    #     sitename = "TC#1111"
    #     main_page = MainPage(self.driver)
    #     main_page.create_site_if_not_exists(sitename)
    #     main_page.click_site_in_global_site_view_tree(sitename)
    #     main_page.click_delete_button()
    #     main_page.click_system_button_close()
    #     self.assertTrue(main_page.check_site_is_in_global_site_view_tree(sitename))
    #     main_page.delete_site_from_global_site_view_tree(sitename)
    #     print ("Test is passed" + "\n")
    #
    # def test_open_are_you_sure_popup(self):
    #     print ("\n" + "TC#2222. Devices page. Open Are you sure popup" + "\n")
    #     sitename = "TC#2222"
    #     main_page = MainPage(self.driver)
    #     main_page.create_site_if_not_exists(sitename)
    #     main_page.click_site_in_global_site_view_tree(sitename)
    #     main_page.click_delete_button()
    #     self.assertTrue(main_page.is_element_present(Locators.POPUP_ARE_YOU_SURE))
    #     main_page.click_ok()
    #     print ("Test is passed" + "\n")
    #
    # # def tearDown(self):
    # #     page = MainPage(self.driver)
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