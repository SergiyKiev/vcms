
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
        self.wait_for_element_present(locator + BaseElements.ICON_HELP)
        self._click_element(locator + BaseElements.ICON_HELP)

    def _click_button_restore(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.BUTTON_RESTORE)

    def _click_icon_refresh(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_REFRESH)

    def _click_icon_search(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_SEARCH)

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
        try:
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
        except Exception as e:
            print "No such element: ", e

    def _check_help_frame_header(self, expected_header_name):
        # element = HelpWindow.HEADER + "[text()='" + header_name + "']"
        # cond1 = self._is_element_present(element)
        # cond2 = self._is_element_present(BaseElements.HELP_FRAME_TITLE_GETTING_STARTED)
        # cond3 = self._is_element_present(BaseElements.HELP_FRAME_TITLE_SERVER_ERROR)
        self._select_help_window()
        current_header_name = self._find_element(BaseElements.HELP_WINDOW_HEADER).text
        if current_header_name == expected_header_name:
            print "Link is correct: ", current_header_name
            return True
        elif current_header_name == BaseElements.HELP_FRAME_TITLE_GETTING_STARTED:
            default_text = self._find_element(BaseElements.HELP_WINDOW_HEADER).text
            print "Link is incorrect: ", default_text
            return False
        elif current_header_name == BaseElements.HELP_FRAME_TITLE_SERVER_ERROR:
            error_text = self._find_element("//h2").text
            print "Server error: ", error_text
            return False

    def _select_help_window(self):
        handles = self.driver.window_handles
        help_window = handles[1]
        # WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)
        self.driver.switch_to_window(help_window)
        self.wait_general.until(lambda d: d.title != "")
        title = self.driver.title
        print "Title is: " , title
        self.driver.switch_to_frame(self.driver.find_element_by_name('FrameMain'))
        header = self._find_element(BaseElements.HELP_WINDOW_HEADER).text
        # print "Header is: ", header

    def _close_help_window(self):
        handles = self.driver.window_handles
        main_window = handles[0]
        try:
            help_window = handles[1]
        except IndexError:
            help_window = 'null'
        if help_window != 'null':
            self.driver.switch_to_window(help_window)
            self.driver.close()
            print "Help window is closed"
        self.driver.switch_to_window(main_window)

    def _close_help_windows(self):
        handles = self.driver.window_handles
        main_window = handles[0]
        for i in list(handles):
            if i == 0:
                continue
            else:
                help_window = handles[i]
                self.driver.switch_to_window(help_window)
                self.driver.close()
        self.driver.switch_to_window(main_window)
        print "Help windows are closed"