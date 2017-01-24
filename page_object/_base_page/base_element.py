import time
from _base_page.base import Base
from _locators.locators import Locators
from _settings.settings import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BaseElement(Base):

    BTN_EDIT = "//img[@alt='Edit']"
    BTN_EDIT_by_text = "//span[text()='Edit']"

    def button_edit(self, locator):
        try:
            cond1 = self.is_element_present(locator + "/*" + BaseElement.BTN_EDIT)
            cond2 = self.is_element_present(locator + "/*" + BaseElement.BTN_EDIT_by_text)
            if cond1:
                return self._find_element(locator + "/*" + BaseElement.BTN_EDIT)
            elif cond2:
                return self._find_element(locator + "/*" + BaseElement.BTN_EDIT_by_text)

        except NoSuchElementException:
                print "Button Edit for " + locator +  " is not found"

    def click_ok(self, locator):
        try:
            cond1 = self.is_element_present(locator + "/*" + Locators.BTN_OK)
            cond2 = self.is_element_present(locator + "/*" + Locators.BTN_Ok)
            if cond1:
                self.click_element(locator + "/*" + Locators.BTN_OK)
                self.wait_for_element_not_present(locator)
            elif cond2:
                self.click_element(locator + "/*" + Locators.BTN_Ok)
                self.wait_for_element_not_present(locator)
        except NoSuchElementException:
            print "Button " + locator + "/*" + Locators.BTN_OK + " is not found"
            print "Button " + locator + "/*" + Locators.BTN_Ok + " is not found"

    def click_sytem_button_close(self, locator):
        self.click_element(locator + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(locator)
