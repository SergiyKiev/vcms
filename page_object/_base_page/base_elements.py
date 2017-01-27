import time
from _base_page.base import Base
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException


class Buttons(Base):

    BTN_EDIT = "//img[@alt='Edit']"
    BTN_EDIT_by_text = "//span[text()='Edit']"
    BUTTON_OK = "/*//span[text()='OK']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    BUTTON_Ok = "/*//span[text()='Ok']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    SYSTEM_BUTTON_CLOSE = "/*//div[@title='Close']"

    def button_edit(self, locator):
        try:
            cond1 = self.is_element_present(locator + "/*" + Buttons.BTN_EDIT)
            cond2 = self.is_element_present(locator + "/*" + Buttons.BTN_EDIT_by_text)
            if cond1:
                return self._find_element(locator + "/*" + Buttons.BTN_EDIT)
            elif cond2:
                return self._find_element(locator + "/*" + Buttons.BTN_EDIT_by_text)

        except NoSuchElementException:
                print "Button Edit for " + locator +  " is not found"

    def click_ok(self, locator):
        self.wait_for_element_present(locator)
        try:
            cond1 = self.is_element_present(locator + Buttons.BUTTON_OK)
            cond2 = self.is_element_present(locator + Buttons.BUTTON_Ok)
            if cond1:
                self._click_element(locator + Buttons.BUTTON_OK)
            elif cond2:
                self._click_element(locator + Buttons.BUTTON_Ok)
            self.wait_for_element_not_present(locator)
        except Exception as e:
            print "Button is not found ", e

    def click_system_close(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + Buttons.SYSTEM_BUTTON_CLOSE)
        self.wait_for_element_not_present(locator)
