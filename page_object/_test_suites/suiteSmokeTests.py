
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














if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    # unittest.TextTestRunner(verbosity=2).run(suite())