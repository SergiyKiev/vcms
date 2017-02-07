
from _base_page.base_actions import BaseActions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from _locators.locators import Locators
import time

class HelpWindow(BaseActions):

    BODY = "//title[text()='ConsoleOperationGuide']"
    HEADER = "//h1[@id='topic_header_text']"
    SIGN_IN = "//h1[text()='Sign In']"
    HOME_TAB = "//h1[text()='Getting Started in CMS']"
    SERVER_ERROR = "//h1[text()='Server Error']"
    GETTING_STARTED = "//h1[text()='Getting Started in CMS']"

    def _check_help_window(self, locator):
        try:
            self.select_help_window()
            cond1 = self._is_element_present(locator)
            cond2 = self._is_element_present(HelpWindow.GETTING_STARTED)
            cond3 = self._is_element_present(HelpWindow.SERVER_ERROR)
            print cond1, cond2, cond3
            if cond1:
                text = self._find_element(locator).text
                print "Help link is correct: ", text
                return True
            elif cond2:
                text = self._find_element(HelpWindow.SIGN_IN).text
                print "Pass is incorrect: ", text
                return False
            elif cond3:
                text = self._find_element("//h2").text
                print "Server error: ", text
                return False
        except NoSuchElementException:
            print "No such element found: "

    def select_help_window(self):
        # time.sleep(7)
        # frame = self.driver.find_element_by_id('topic_header')
        # x = frame.text
        # print "\n" + x
        # self.driver.switch_to_window()
        window_before = self.driver.window_handles[0]
        print window_before
        window_after = self.driver.window_handles[1]
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)
        self.driver.switch_to_window(window_after)
        WebDriverWait(self.driver, 10).until(lambda d: d.title != "")
        title = self.driver.title
        print "Title is: " , title
        self.driver.switch_to_frame(self.driver.find_element_by_name('FrameMain'))

    def check_logon_page_help_window(self):
        cond = self._check_help_window(HelpWindow.SIGN_IN)
        return True if cond else False

    def check_home_tab_help_window(self):
        cond = self._check_help_window(HelpWindow.HOME_TAB)
        return True if cond else False


    def close_help_window(self):
       pass
