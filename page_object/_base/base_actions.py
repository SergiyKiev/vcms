import time

from _base.base_elements import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BaseActions(Base):

    def _close_popups(self):
        cond = self._is_element_present(BaseElements.POPUP)
        if cond:
            i = 0
            while i < 10:
                i += 1
                # self.wait_for_screen_is_unlocked()
                self._get_popup_error_messages()
                system_button_close = self._is_element_present(BaseElements.POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
                button_close = self._is_element_present(BaseElements.POPUP + BaseElements.BUTTON_CLOSE)
                if system_button_close:
                    self._click_system_button_close(BaseElements.POPUP)
                    # time.sleep(1)
                    self.logger.debug("Popup #" + str(i) +  " is closed.")
                elif button_close:
                    self._click_button_close(BaseElements.POPUP)
                    self.logger.debug("PopupBase without system button close is closed. PLEASE, ADD SYSTEM BUTTON CLOSE")
                else:
                    break

    def _click_label(self, locator, name=None):
        self._click_element(locator)
        self._wait_for_element_selected(locator)

    def _click_button_edit(self, locator):
        self._click_element(locator + BaseElements.BUTTON_EDIT)

    def _click_button_ok(self, locator):
        try:
            button_ok_uppercase = locator + BaseElements.BUTTON_OK_UPPERCASE
            button_ok_lowercase = locator + BaseElements.BUTTON_OK_LOWERCASE
            cond1 = self._is_element_present(button_ok_uppercase)
            cond2 = self._is_element_present(button_ok_lowercase)
            if cond1:
                self._click_element(button_ok_uppercase)
            elif cond2:
                self._click_element(button_ok_lowercase)
            self._wait_for_element_not_present(locator)
        except NoSuchElementException:
            self.logger.exception("Button 'OK(Ok)' is not found")

    def _click_button_no(self, locator):
        self._click_element(locator + BaseElements.BUTTON_NO)
        self._wait_for_element_not_present(locator)

    def _click_button_yes(self, locator):
        self._click_element(locator + BaseElements.BUTTON_YES)
        self._wait_for_element_not_present(locator)

    def _click_button_cancel(self, locator):
        try:
            button_cancel_uppercase = locator + BaseElements.BUTTON_CANCEL_UPPERCASE
            button_cancel_lowercase = locator + BaseElements.BUTTON_CANCEL_LOWERCASE
            cond1 = self._is_element_present(button_cancel_uppercase)
            cond2 = self._is_element_present(button_cancel_lowercase)
            if cond1:
                self._click_element(button_cancel_uppercase)
            elif cond2:
                self._click_element(button_cancel_lowercase)
            self._wait_for_element_not_present(locator)
        except NoSuchElementException:
            self.logger.exception("Button 'CANCEL(Cancel)' is not found")

    def _click_button_next(self, locator):
        time.sleep(1)
        self._click_element(locator + BaseElements.BUTTON_NEXT)

    def _click_button_previous(self, locator):
        self._click_element(locator + BaseElements.BUTTON_PREVIOUS)

    def _click_button_finish(self, locator):
        self._click_element(locator + BaseElements.BUTTON_FINISH)

    def _click_button_open(self, locator):
        self._click_element(locator + BaseElements.BUTTON_OPEN)

    def _click_button_close(self, locator):
        self._click_element(locator + BaseElements.BUTTON_CLOSE)
        # self._wait_for_element_not_present(locator)

    def _click_button_add(self, locator):
        self._click_element(locator + BaseElements.BUTTON_ADD)

    def _click_button_new(self, locator):
        self._click_element(locator + BaseElements.BUTTON_NEW)

    def _click_button_delete(self, locator):
        self._click_element(locator + BaseElements.BUTTON_DELETE)

    def _click_icon_help(self, locator):
        try:
            self._click_element(locator + BaseElements.ICON_HELP)
            self.wait_webelement.until(lambda d: len(d.window_handles) == 2)
        except TimeoutException:
            self.logger.exception("WAITING: Help window is NOT found after " + str(self.timeout_webelement) + " seconds")

    def _click_icon_restore(self, locator):
        self._wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_RESTORE)

    def _click_icon_refresh(self, locator):
        self._wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_REFRESH)

    def _click_icon_search(self, locator):
        self._wait_for_element_present(locator)
        self._click_element(locator + BaseElements.ICON_SEARCH)

    def _click_system_button_close(self, locator):
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_CLOSE)
        # self._wait_for_element_not_present(locator)

    def _click_system_button_maximize(self, locator):
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_MAXIMIZE)
        time.sleep(2)
        self._wait_for_element_present(locator + BaseElements.SYS_BUTTON_RESTORE_DOWN)

    def _click_system_button_drop_down(self, locator):
        self.hover(locator + BaseElements.SYSTEM_BUTTON_DROP_DOWN)
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_DROP_DOWN)

    def _check_help_frame_header(self, expected_header_name):
        cond = self._is_element_present(BaseElements.HELP_FRAME_HEADER + "[text()='" + expected_header_name + "']")
        return True if cond else False

    def _get_popup_error_messages(self):
        cond = self._is_element_present(BaseElements.POPUP_ERROR)
        if cond:
            elements = self._find_all_elements(BaseElements.POPUP_ERROR)
            for element in elements:
                message = element.text
                self.logger.error("TEST FAILED. Error popup message: " + str(message))

    def _get_help_frame_header(self):
        try:
            handles = self.driver.window_handles
            self.wait_webelement.until(lambda d: len(d.window_handles) == 2)
            help_window = handles[1]
            self.driver.switch_to_window(help_window)
            self.wait_webelement.until(lambda d: d.title != "")
            title = self.driver.title
            self.logger.info("Help window is opened. Title is: " + str(title))
            self._wait_for_element_present(BaseElements.HELP_FRAME_MAIN)
            self._wait_for_element_present(BaseElements.HELP_FRAME_TOC)
            self.driver.switch_to_frame(self._find_element(BaseElements.HELP_FRAME_MAIN))
            time.sleep(1)
            cond = self._is_element_present(BaseElements.HELP_FRAME_HEADER)
            error = self._is_element_present(BaseElements.HELP_FRAME_HEADER_ERROR)
            print "Header " + str(cond) + ". Error " + str(error)
            if cond:
                header = self._get_text(BaseElements.HELP_FRAME_HEADER)
                return str(header)
            elif error:
                error_header = self._get_text(BaseElements.HELP_FRAME_HEADER_ERROR)
                return str(error_header)
        except NoSuchElementException:
            massage1 = self._find_element("//*[@id='main-message']/h1").text
            massage2 = self._find_element("//*[@id='main-message']/div[2]").text
            return self.logger.error("HELP LINK IS UNAVAILABLE. Massage: " + massage1 + massage2)
        except TimeoutException:
            return self.logger.error("Help window is not opened")
        except IndexError:
            return self.logger.error("Help window is not found")
        except Exception as e:
            return  self.logger.exception("Help window is not found" + str(e))

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
        self.driver.switch_to_window(main_window)

    def _expand_list(self, locator):
        try:
            element = self._find_element(locator + BaseElements.ARROW_EXPAND)
            self.driver.execute_script("arguments[0].click();", element)
            # cond = self._wait_for_element_not_present(locator + BaseElements.ARROW_EXPAND)
            # if cond:
            #     return True
            # else:
            #     return False
        except Exception as e:
            print "Massage: ", e

    def _expand_all_lists(self, locator):
        self._wait_for_element_present(locator)
        elements = self._find_all_elements(locator + BaseElements.ARROW_EXPAND)
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)
            # self._wait_for_element_not_present(locator + BaseElements.ARROW_EXPAND)

    def _collaps_list(self, locator):
        try:
            element = self._find_element(locator + BaseElements.ARROW_COLLAPSE)
            self.driver.execute_script("arguments[0].click();", element)
            # self._wait_for_element_not_present(locator + BaseElements.ARROW_COLLAPSE)
        except Exception as e:
            print "Massage: ", e

    def _collaps_all_lists(self, locator):
        self._wait_for_element_present(locator)
        elements = self._find_all_elements(locator + BaseElements.ARROW_COLLAPSE)
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)
            # self._wait_for_element_not_present(locator + BaseElements.ARROW_COLLAPSE)

    def _get_list_view(self, locator):
        tree_view = locator + BaseElements.TREE_VIEW
        cond = self._is_element_present(tree_view)
        return tree_view if cond else None

    def _check_condition(self, locator):
        cond = self._is_element_present(locator)
        return True if cond else False

    def _set_log_msg_for_true_or_false(self, cond=True, true_msg=None, false_msg=None):
        if cond:
            self.logger.debug(true_msg)
            return True
        else:
            self.logger.error("TEST FAILED. " + false_msg)
            return False

    def _get_log_for_help_link(self, expected_header_name):
        try:
            cond1 = self._is_element_present(BaseElements.HELP_FRAME_HEADER + "[text()='" + expected_header_name + "']")
            cond2 = self._is_element_present(BaseElements.HELP_FRAME_HEADER)
            cond3 = self._is_element_present(BaseElements.HELP_FRAME_HEADER_SERVER_ERROR)
            if cond1:
                current_header_name = self._find_element(BaseElements.HELP_FRAME_HEADER).text
                result = "Expected header: " + expected_header_name \
                         + " == Actual header: " + str(current_header_name)
                self.logger.info(result)
            elif cond2:
                current_header = self._find_element(BaseElements.HELP_FRAME_HEADER).text
                error_message = "TEST FAILED: Expected header: " + expected_header_name \
                                + " !=  Actual header: " + str(current_header)
                self.logger.error(error_message)
            elif cond3:
                error = self._find_element(BaseElements.HELP_FRAME_HEADER_SERVER_ERROR).text
                error_text1 = self._find_element("//*[@id='content']/div/fieldset/h2").text
                # error_text2 = self._find_element("//*[@id='content']/div/fieldset/h3").text
                self.logger.error("TEST FAILED. Header: " + str(error) + ". Message: " + str(error_text1))
                # self.logger.error("Error message: " + str(error_text1))
                # self.logger.error(str(error_text2))
        except NoSuchElementException:
            massage1 = self._find_element("//*[@id='main-message']/h1").text
            massage2 = self._find_element("//*[@id='main-message']/div[2]").text
            self.logger.exception("Help link is NOT available.\nMassage: " + str(massage1) + str(massage2))
        except TimeoutException:
            self.logger.error("Help window is NOT opened")
        except IndexError:
            help_window = 'null'
            self.logger.exception("Help window is NOT found " + str(help_window))

