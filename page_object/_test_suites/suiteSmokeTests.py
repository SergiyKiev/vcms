
import unittest
from _variables.variables import *
from _pages.pageLogin import LoginPage
from _pages.pageMain import MainPage
from _feature_objects.popups import *
from _feature_objects.ribbonBar import *
from _feature_objects.leftSideMenu import *
from selenium import webdriver


class SmokeTest(unittest.TestCase):

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

    def test_install_vrep(self):
        pass

    def test_apply_vrep(self):
        pass

    def test_install_mresponder(self):
        pass

    def test_install_forceresident(self):
        pass

    def test_create_new_site(self):
        pass

    def test_create_ip_address_ranges(self):
        pass

    def test_apply_vrep_to_site(self):
        pass

    def test_lock_devices_to_site(self):
        pass

    def test_create_discovery_task(self):
        pass

    def test_create_devices_groups(self):
        pass

    def test_create_patches_group(self):
        pass

















if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())