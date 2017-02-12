import unittest

from _feature_objects._featureTabs.featureTabDevices import DevicesTab
from _feature_objects._feature_left_menus.featureLeftMenu import *
from _feature_objects.featureRibbonBar import *
from _pages.pageLogin import LoginPage
from _pages.pageMain import MainPage
from _variables.variables import *
from selenium import webdriver


class SmokeTest(unittest.TestCase):

    driver = None #global variable

    @classmethod
    def setUpClass(cls):
        print ("\n" + "TEST SUITE: Smoke test (Suite ID: )")
        cls.driver = webdriver.Chrome()
        login_page = LoginPage(cls.driver)
        login_page.open_page()
        main_page = login_page.login()
        main_page.check_main_page_loaded()

    def setUp(self):
        main_page = MainPage(self.driver)
        main_page._close_popups()

    def test_01_delete_devices_from_the_console(self):
        devices = Variables.devices_for_smoke_test
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page = MainPage(self.driver)
        remove_devices_popup = RemoveDevicesPopup(self.driver)
        tab_devices = DevicesTab(self.driver)
        left_menu.open_menu_devices()
        left_menu_devices.expand_global_site_view_tree()
        left_menu.click_global_site_view_label()
        # left_menu.click_site_in_global_site_view_tree(sitename)
        main_page.delete_devices_in_devices_tab_table(devices)

    # @unittest.skip
    # def test_install_vrep(self):
    #     pass
    #
    # @unittest.skip
    # def test_apply_vrep(self):
    #     pass
    #
    # @unittest.skip
    # def test_install_mresponder(self):
    #     pass
    #
    # @unittest.skip
    # def test_install_forceresident(self):
    #     pass


    def test_02_create_new_site(self):
        print ("\n" + "TC#9101. Create new site with acceptable name")
        sitename = Variables.site_for_smoke_test
        main_page = MainPage(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        left_menu = LeftMenu(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        main_page.delete_site_if_exists(sitename)
        left_menu.click_global_site_view_label()
        ribbon_bar.click_button_new_site()
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(left_menu.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    def test_create_ip_address_ranges(self):
        pass

    # @unittest.skip
    # def test_apply_vrep_to_site(self):
    #     pass
    #
    # @unittest.skip
    # def test_lock_devices_to_site(self):
    #     pass
    #
    # @unittest.skip
    # def test_create_discovery_task(self):
    #     pass
    #
    # @unittest.skip
    # def test_create_devices_groups(self):
    #     pass
    #
    # @unittest.skip
    # def test_create_patches_group(self):
    #     pass

    # def tearDown(self):
    #     page = MainPage(self.driver)
    #     page._close_popups()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)


