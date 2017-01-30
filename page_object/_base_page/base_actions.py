
import time
from _base_page.base import Base
from _base_page.base_elements import *
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException


class BaseActions(Base):

    def _button_edit(self, locator):
        try:
            cond1 = self._is_element_present(locator + "/*" + BaseElements.BUTTON_EDIT)
            cond2 = self._is_element_present(locator + "/*" + BaseElements.BUTTON_EDIT_by_text)
            if cond1:
                return self._find_element(locator + "/*" + BaseElements.BUTTON_EDIT)
            elif cond2:
                return self._find_element(locator + "/*" + BaseElements.BUTTON_EDIT_by_text)

        except NoSuchElementException:
                print "Button Edit for " + locator +  " is not found"

    # def _click_button_new(self, locator=None):
    #     self.wait_for_element_present(locator)
    #     try:
    #         cond1 = self._is_element_present(locator + BaseElements.BUTTON_NEW)
    #         cond2 = self._is_element_present(locator + BaseElements.BUTTON_NEW_by_text)
    #         if cond1:
    #             self._click_element(locator + BaseElements.BUTTON_NEW)
    #         elif cond2:
    #             self._click_element(locator + BaseElements.BUTTON_NEW_by_text)
    #     except Exception as e:
    #         print "Button is not found ", e

    def _click_button_ok(self, locator=None):
        self.wait_for_element_present(locator)
        try:
            cond1 = self._is_element_present(locator + BaseElements.BUTTON_OK)
            cond2 = self._is_element_present(locator + BaseElements.BUTTON_Ok)
            if cond1:
                self._click_element(locator + BaseElements.BUTTON_OK)
            elif cond2:
                self._click_element(locator + BaseElements.BUTTON_Ok)
            self.wait_for_element_not_present(locator)
        except Exception as e:
            print "Button is not found ", e

    def _click_button_no(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.BUTTON_NO)
        self.wait_for_element_not_present(locator)

    def _click_button_yes(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.BUTTON_YES)
        self.wait_for_element_not_present(locator)

    def _click_button_cancel(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.BUTTON_CANCEL)
        self.wait_for_element_not_present(locator)

    def _click_button_close(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.BUTTON_CLOSE)
        self.wait_for_element_not_present(locator)

    def _click_icon_help(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_HELP)
        # self.wait_for_element_not_present(locator)

    def _click_icon_restore(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.BUTTON_RESTORE)
        # self.wait_for_element_not_present(locator)

    def _click_system_button_close(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_CLOSE)
        self.wait_for_element_not_present(locator)

    def _click_system_button_maximize(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_MAXIMIZE)
        time.sleep(2)
        self.wait_for_element_present(locator + BaseElements.SYS_BUTTON_RESTORE_DOWN)

    def _click_system_button_drop_down(self, locator):
        self.wait_for_element_present(locator)
        self.hover(locator + BaseElements.SYSTEM_BUTTON_DROP_DOWN)
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_DROP_DOWN)

    def _close_popups(self):
        cond = self._is_element_present(BaseElements._POPUP)
        i = 0
        while i < 10:
            i += 1
            if cond:
                self._click_element(BaseElements._POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
                print "All popups are closed"
                return True
            else:
                pass
