
import time
from _base_page.base import Base
from _base_page.base_elements import *
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException


class BaseActions(Base):

    def _button_edit(self, locator):
        self._click_element(locator + BaseElements.BUTTON_EDIT)

    def _click_button_ok(self, locator=None):
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
        self._click_element(locator + BaseElements.BUTTON_NO)
        self.wait_for_element_not_present(locator)

    def _click_button_yes(self, locator):
        self._click_element(locator + BaseElements.BUTTON_YES)
        self.wait_for_element_not_present(locator)

    def _click_button_cancel(self, locator):
        self._click_element(locator + BaseElements.BUTTON_CANCEL)
        self.wait_for_element_not_present(locator)

    def _click_button_close(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.BUTTON_CLOSE)
        self.wait_for_element_not_present(locator)

    def _click_button_add(self, locator):
        self._click_element(locator + BaseElements.BUTTON_ADD)

    def _click_button_new(self, locator):
        self._click_element(locator + BaseElements.BUTTON_NEW)

    def _click_button_delete(self, locator):
        self._click_element(locator + BaseElements.BUTTON_DELETE)

    def _click_icon_help(self, locator):
        # self.wait_for_element_present(locator + BaseElements.ICON_HELP)
        self._click_element(locator + BaseElements.ICON_HELP)

    def _click_icon_restore(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_RESTORE)

    def _click_icon_refresh(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_REFRESH)

    def _click_icon_search(self, locator):
        self.wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_SEARCH)

    def _click_system_button_close(self, locator):
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
        cond = self._is_element_present(BaseElements._POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
        if cond:
            i = 0
            while i < 10:
                i += 1
                popup = self._is_element_present(BaseElements._POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
                if popup:
                    self._click_element(BaseElements._POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
                else:
                    break
            print "Popups are closed"
        else:
            pass

    def _check_help_frame_header(self, expected_header_name):
        self._select_help_window(expected_header_name)
        cond = self._is_element_present(BaseElements.HELP_FRAME_HEADER + "[text()='" + expected_header_name + "']")
        return True if cond else False
        # current_header_name = self._find_element(BaseElements.HELP_FRAME_HEADER).text
        # if current_header_name == expected_header_name:
        #     print "Link is correct: ", current_header_name
        #     return True
        # else:
        #     return False
        # elif current_header_name == BaseElements.HELP_FRAME_HEADER_GETTING_STARTED:
        #     default_text = self._find_element(BaseElements.HELP_FRAME_HEADER).text
        #     print "Link is incorrect: ", default_text
        #     return False
        # elif current_header_name == BaseElements.HELP_FRAME_HEADER_SERVER_ERROR:
        #     error_text = self._find_element("//h2").text
        #     print "Server error: ", error_text
        #     return False

    def _select_help_window(self, expected_header_name):
        try:
            handles = self.driver.window_handles
            self.wait_general.until(lambda d: len(d.window_handles) == 2)
            help_window = handles[1]
            self.driver.switch_to_window(help_window)
            self.wait_general.until(lambda d: d.title != "")
            title = self.driver.title
            print "\n" + "Title is: ", title
            self.driver.switch_to_frame(self.driver.find_element_by_name('FrameMain'))
            cond1 = self._is_element_present(BaseElements.HELP_FRAME_HEADER + "[text()='" + expected_header_name + "']")
            cond2 = self._is_element_present(BaseElements.HELP_FRAME_HEADER)
            cond3 = self._is_element_present(BaseElements.HELP_FRAME_HEADER_SERVER_ERROR)
            if cond1:
                current_header_name = self._find_element(BaseElements.HELP_FRAME_HEADER).text
                print "Link is correct. Actual header: ", current_header_name
                print "Expected header: ", expected_header_name
            elif cond2:
                current_header = self._find_element(BaseElements.HELP_FRAME_HEADER).text
                print "Link is incorrect. Actual header: ", current_header
                print "Expected header: ", expected_header_name
            elif cond3:
                error_header = self._find_element(BaseElements.HELP_FRAME_HEADER_SERVER_ERROR).text
                error_text1 = self._find_element("//*[@id='content']/div/fieldset/h2").text
                error_text2 = self._find_element("//*[@id='content']/div/fieldset/h3").text
                print "Link is incorrect. Header: ", error_header
                print "Error text: ", error_text1, error_text2
        except IndexError:
            help_window = 'null'
            print "Window is not found"

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