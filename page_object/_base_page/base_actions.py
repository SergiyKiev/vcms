import time
from _base_page.base import Base
from _base_page.base_elements import *
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException


class BaseActions(Base):

    BTN_EDIT = "//img[@alt='Edit']"
    BTN_EDIT_by_text = "//span[text()='Edit']"

    def _button_edit(self, locator):
        try:
            cond1 = self.is_element_present(locator + "/*" + BaseActions.BTN_EDIT)
            cond2 = self.is_element_present(locator + "/*" + BaseActions.BTN_EDIT_by_text)
            if cond1:
                return self._find_element(locator + "/*" + BaseActions.BTN_EDIT)
            elif cond2:
                return self._find_element(locator + "/*" + BaseActions.BTN_EDIT_by_text)

        except NoSuchElementException:
                print "Button Edit for " + locator +  " is not found"

    def _click_button_ok(self, locator):
        self.wait_for_element_present(locator)
        try:
            cond1 = self.is_element_present(locator + BaseElements.BUTTON_OK)
            cond2 = self.is_element_present(locator + BaseElements.BUTTON_Ok)
            if cond1:
                self._click_element(locator + BaseElements.BUTTON_OK)
            elif cond2:
                self._click_element(locator + BaseElements.BUTTON_Ok)
            self.wait_for_element_not_present(locator)
        except Exception as e:
            print "Button is not found ", e

    def _click_system_button_close(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_CLOSE)
        self.wait_for_element_not_present(locator)

    def _close_popups(self):
        cond = self.is_element_present(BaseElements._POPUP)
        i = 0
        while i < 10:
            i += 1
            if cond:
                self._click_element(BaseElements.POPUP_SYSTEM_BUTTON_CLOSE)
                print "All popups are closed"
                return True
            else:
                pass
