import unittest

from _base_page.downloadAndInstall import DownloadAndInstall
from _feature_objects._left_menus.leftMenu import *
from _feature_objects._left_menus.leftMenuDevices import LeftMenuDevices
from _feature_objects._pages.pageDevices import DevicesPage
from _feature_objects._pages.pageMain import MainPage
from _feature_objects.ribbonBar import *
from _feature_objects._pages.pageLogin import LoginPage
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
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_page = DevicesPage(self.driver)
        left_menu.open_menu_devices()
        left_menu_devices.expand_global_site_view_tree()
        left_menu_devices.click_global_site_view_label()
        # left_menu.click_site_in_global_site_view_tree(sitename)
        devices_page.delete_devices_in_devices_page_table(devices)

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
        site_name_popup = SiteNamePopup(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices.delete_site_if_exists(sitename)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.click_global_site_view_label()
        ribbon_bar.click_button_new_site()
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.assertTrue(left_menu_devices.check_site_is_in_global_site_view_tree(sitename))
        print ("Test is passed" + "\n")

    '''D0 NOT DELETE!!!'''
    # def test_add_vrep_to_the_console(self):
    #     name = "VKYV-DT-IK"
    #     main_page = MainPage(self.driver)
    #     devices_page = DevicesPage(self.driver)
    #     x = DownloadAndInstall(self.driver)
    #     main_page.delete_device_from_the_console()
    #     x.clean_up_device()
    #     x.download_agent()
    #     x.install_agent()
    #     devices_page.click_icon_refresh()
    #     devices_page.check_device_is_present(name)

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


