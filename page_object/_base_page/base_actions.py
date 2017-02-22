
import time

from _base_page import logs
from _base_page.base import Base
from _base_page.base_elements import *
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging


class BaseActions(Base):

    def _button_edit(self, locator):
        self._click_element(locator + BaseElements.BUTTON_EDIT)

    def _click_button_ok(self, locator):
        cond1 = self._is_element_present(locator + BaseElements.BUTTON_OK_1)
        cond2 = self._is_element_present(locator + BaseElements.BUTTON_OK_2)
        if cond1:
            self._click_element(locator + BaseElements.BUTTON_OK_1)
        elif cond2:
            self._click_element(locator + BaseElements.BUTTON_OK_2)
        self._wait_for_element_not_present(locator)

    def _click_button_no(self, locator):
        self._click_element(locator + BaseElements.BUTTON_NO)
        self._wait_for_element_not_present(locator)

    def _click_button_yes(self, locator):
        self._click_element(locator + BaseElements.BUTTON_YES)
        self._wait_for_element_not_present(locator)

    def _click_button_cancel(self, locator):
        cond1 = self._is_element_present(locator + BaseElements.BUTTON_CANCEL_1)
        cond2 = self._is_element_present(locator + BaseElements.BUTTON_CANCEL_2)
        if cond1:
            self._click_element(locator + BaseElements.BUTTON_OK_1)
        elif cond2:
            self._click_element(locator + BaseElements.BUTTON_OK_2)
        self._wait_for_element_not_present(locator)

    def _click_button_close(self, locator):
        self._click_element(locator + BaseElements.BUTTON_CLOSE)
        self._wait_for_element_not_present(locator)

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
            self.logger.error("WAITING: Help window is NOT found after " + str(self.timeout_webelement) + " seconds")

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
        self._wait_for_element_not_present(locator)

    def _click_system_button_maximize(self, locator):
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_MAXIMIZE)
        time.sleep(2)
        self._wait_for_element_present(locator + BaseElements.SYS_BUTTON_RESTORE_DOWN)

    def _click_system_button_drop_down(self, locator):
        self.hover(locator + BaseElements.SYSTEM_BUTTON_DROP_DOWN)
        self._click_element(locator + BaseElements.SYSTEM_BUTTON_DROP_DOWN)

    def _close_popups(self):
        # cond = self._is_element_present(BaseElements.POPUP)
        # if cond:
        #     elements = self._find_elements(BaseElements.POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
        #     for element in elements:
        #         error_popup = self._is_element_present(
        #             "//span[text()='Error'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]/*//span[contains(@class,'Label-FontData')]")
        #         if error_popup:
        #             print "error popup ", str(error_popup)
        #             text = self._get_text(
        #                 "//span[text()='Error'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]/*//span[contains(@class,'Label-FontData')]")
        #             self.logger.error("Error popup text is: " + str(text))
        #         elif element:
        #             print element
        #             self._click_element(BaseElements.POPUP + "[last()]" + BaseElements.SYSTEM_BUTTON_CLOSE)
        #         else:
        #             break
        #     button_close = self._is_element_present(BaseElements.POPUP + "[last()]" + BaseElements.BUTTON_CLOSE)
        #     if button_close:
        #         self._click_button_close("//div[contains(@id,'WRP')][last()]")
        #         print "button close ", button_close
        # if cond:
        #     i = 0
        #     while i < 10:
        #         i += 1
        #         system_button_close = self._is_element_present(BaseElements.POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
        #         button_close = self._is_element_present(BaseElements.POPUP + BaseElements.BUTTON_CLOSE)
        #         if system_button_close:
        #             self._click_system_button_close(BaseElements.POPUP)
        #         else:
        #             break
        cond = self._is_element_present(BaseElements.POPUP)
        if cond:
            i = 0
            while i < 10:
                i += 1
                self._get_error_popups_messages()
                system_button_close = self._is_element_present(BaseElements.POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
                button_close = self._is_element_present(BaseElements.POPUP + BaseElements.BUTTON_CLOSE)
                if system_button_close:
                    self._click_element(BaseElements.POPUP + BaseElements.SYSTEM_BUTTON_CLOSE)
                    # print "Popup #" + str(i) + " is closed: ", system_button_close
                elif button_close:
                    self._click_element(BaseElements.POPUP + BaseElements.BUTTON_CLOSE)
                    # print "Popup #" + str(i) + " is closed: ", button_close
                    # print "Popup without system button close is closed"
                    # self.logger.error("Popup without system button close is closed. PLEASE, ADD SYSTEM BUTTON CLOSE")
                else:
                    break

    def _check_help_frame_header(self, expected_header_name):
        cond = self._is_element_present(BaseElements.HELP_FRAME_HEADER + "[text()='" + expected_header_name + "']")
        return True if cond else False

    def _check_help_window_is_present(self, expected_header_name):
        cond = self._is_element_present(BaseElements.HELP_WINDOW_BODY)
        return True if cond else False

    def _get_error_popups_messages(self):
        cond = self._is_element_present(BaseElements.POPUP_ERROR)
        if cond:
            elements = self._find_elements(BaseElements.POPUP_ERROR)
            for element in elements:
                message = element.text
                self.logger.error("Test failed. Error popup message: " + str(message))

    def _get_help_frame_header(self):
        try:
            handles = self.driver.window_handles
            self.wait_webelement.until(lambda d: len(d.window_handles) == 2)
            help_window = handles[1]
            self.driver.switch_to_window(help_window)
            title = self.driver.title
            # print "Help window is opened. Title is: ", title
            self.logger.info("Help window is opened. Title is: " + str(title))
            self._wait_for_element_present(BaseElements.HELP_FRAME_MAIN)
            self._wait_for_element_present(BaseElements.HELP_FRAME_TOC)
            self.wait_webelement.until(lambda d: d.title != "")
            self.driver.switch_to_frame(self.driver.find_element_by_name('FrameMain'))
            cond = self._is_element_present(BaseElements.HELP_FRAME_HEADER)
            error = self._is_element_present(BaseElements.HELP_FRAME_HEADER_ERROR)
            if cond:
                header = self._get_text(BaseElements.HELP_FRAME_HEADER)
                return str(header)
            elif error:
                error_header = self._get_text(BaseElements.HELP_FRAME_HEADER_ERROR)
                return str(error_header)
        except NoSuchElementException:
            massage1 = self._find_element("//*[@id='main-message']/h1").text
            massage2 = self._find_element("//*[@id='main-message']/div[2]").text
            self.logger.error("HELP LINK IS UNAVAILABLE. Massage: " + massage1 + massage2)
            return "HELP LINK IS UNAVAILABLE. Massage: ", massage1, massage2
        except TimeoutException:
            self.logger.error("Help window is not opened")
            return ""
        except IndexError:
            help_window = 'null'
            self.logger.error("Help window is not found")
            return ""
        except Exception as e:
            self.logger.error("Help window is not found" + str(e))
            return ""

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

    # def _select_help_window(self, expected_header_name):
    #     try:
    #         handles = self.driver.window_handles
    #         self.wait_webelement.until(lambda d: len(d.window_handles) == 2)
    #         help_window = handles[1]
    #         self.driver.switch_to_window(help_window)
    #         self.wait_webelement.until(lambda d: d.title != "")
    #         title = self.driver.title
    #         print "Help window title is: ", title
    #         self.driver.switch_to_frame(self.driver.find_element_by_name('FrameMain'))
    #         cond1 = self._is_element_present(BaseElements.HELP_FRAME_HEADER + "[text()='" + expected_header_name + "']")
    #         cond2 = self._is_element_present(BaseElements.HELP_FRAME_HEADER)
    #         cond3 = self._is_element_present(BaseElements.HELP_FRAME_HEADER_SERVER_ERROR)
    #         if cond1:
    #             current_header_name = self._find_element(BaseElements.HELP_FRAME_HEADER).text
    #             print "Expected header: ", expected_header_name
    #             print "Actual header: ", current_header_name
    #         elif cond2:
    #             current_header = self._find_element(BaseElements.HELP_FRAME_HEADER).text
    #             print "Expected header: ", expected_header_name
    #             print "Link is incorrect. Actual header: ", current_header
    #         elif cond3:
    #             error_header = self._find_element(BaseElements.HELP_FRAME_HEADER_SERVER_ERROR).text
    #             error_text1 = self._find_element("//*[@id='content']/div/fieldset/h2").text
    #             error_text2 = self._find_element("//*[@id='content']/div/fieldset/h3").text
    #             print "Link is missed. Header: ", error_header
    #             print "Error text: ", error_text1, error_text2
    #         return title
    #     except NoSuchElementException:
    #         massage1 = self._find_element("//*[@id='main-message']/h1").text
    #         massage2 = self._find_element("//*[@id='main-message']/div[2]").text
    #         print "HELP LINK IS UNAVAILABLE. Massage: ", massage1, massage2
    #     except TimeoutException:
    #         print "Help window is not opened"
    #     except IndexError:
    #         help_window = 'null'
    #         print "Help window is not found"

    # def _close_help_windows(self):
    #     handles = self.driver.window_handles
    #     main_window = handles[0]
    #     for i in list(handles):
    #         if i == 0:
    #             continue
    #         else:
    #             help_window = handles[i]
    #             self.driver.switch_to_window(help_window)
    #             self.driver.close()
    #     self.driver.switch_to_window(main_window)
    #     print "Help windows are closed"

    def _expand_tree(self, locator):
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

    def _expand_all_trees(self, locator):
        self._wait_for_element_present(locator)
        elements = self._find_elements(locator + BaseElements.ARROW_EXPAND)
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)
            # self._wait_for_element_not_present(locator + BaseElements.ARROW_EXPAND)

    def _collaps_tree(self, locator):
        try:
            element = self._find_element(locator + BaseElements.ARROW_COLLAPSE)
            self.driver.execute_script("arguments[0].click();", element)
            # self._wait_for_element_not_present(locator + BaseElements.ARROW_COLLAPSE)
        except Exception as e:
            print "Massage: ", e

    def _collaps_all_trees(self, locator):
        self._wait_for_element_present(locator)
        elements = self._find_elements(locator + BaseElements.ARROW_COLLAPSE)
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)
            # self._wait_for_element_not_present(locator + BaseElements.ARROW_COLLAPSE)

    def _get_tree_view(self, locator):
        tree_view = locator + BaseElements.TREE_VIEW
        cond = self._is_element_present(tree_view)
        return tree_view if cond else None

    def _get_left_menu(self, name):
        left_menu = "//span[text()='" + str(name) + "']/ancestor::div[contains(@style,'translate3d(0px')]"
        return left_menu

    def _click_left_menu_icon(self, name):
        icon = "//div[@title='" + name + "']"
        icon_home = "//td[contains(@style,'" + name + "')]/ancestor::div[@class='PictureBox-Control']"
        cond = self._is_element_present(icon)
        if cond:
            self._click_element(icon)
            self._wait_for_element_not_present(str(icon) + BaseElements.GREY_COLOR)
        else:
            self._click_element(icon_home)
            self._wait_for_element_not_present(str(icon_home) + BaseElements.GREY_COLOR)

    def _open_left_menu(self, name):
        element = self._get_left_menu(name)
        i = 0
        while i < 2:
            i += 1
            cond = self._is_element_present(element)
            if cond:
                self.logger.info("Left menu '" + str(name) + "' is opened")
                break
            elif cond is None:
                self.logger.error("Failure. Left menu '" + str(name) + "' is not found")
                break
            elif i == 2:
                self.logger.error("Failure. Left menu '" + str(name) + "' is not opened after " + str(i) + " attempts")
                return False
            else:
                self._click_left_menu_icon(name)
                self._wait_for_element_present(element)
        #Another worked method
        # element = self._get_left_menu(name)
        # precond = self._is_element_present(element)
        # if precond is not True:
        #     i = 0
        #     while i < 5:
        #         i += 1
        #         cond = self._is_element_present(element)
        #         if cond is not True:
        #             self._click_left_menu_icon(name)
        #             self._wait_for_element_present(element)
        #             # print "Cond. WINDOW VISIBLE: ", cond
        #         else:
        #             break
        # postcond = self._is_element_present(element)
        # if postcond:
        #     self.logger.debug("Left menu '" + str(name) + "' is opened")
        #     return True
        # else:
        #     self.logger.error("Failure. Left menu '" + str(name) + "' is not opened")
        #     return False

    def _check_condition(self, locator):
        cond = self._is_element_present(locator)
        return True if cond else False

    def _get_log_msg_for_true_or_false(self, cond=True, true_msg=None, false_msg=None):
        # cond = self._check_condition(condition)
        if cond:
            self.logger.info(true_msg)
            return True
        else:
            self.logger.error(false_msg)
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
                error_message = "Test failed: Expected header: " + expected_header_name \
                                + " !=  Actual header: " +  str(current_header)
                self.logger.error(error_message)
            elif cond3:
                error = self._find_element(BaseElements.HELP_FRAME_HEADER_SERVER_ERROR).text
                error_text1 = self._find_element("//*[@id='content']/div/fieldset/h2").text
                # error_text2 = self._find_element("//*[@id='content']/div/fieldset/h3").text
                self.logger.error("Test failed. Header: " + str(error) + ". Message: " + str(error_text1))
                # self.logger.error("Error message: " + str(error_text1))
                # self.logger.error(str(error_text2))
        except NoSuchElementException:
            massage1 = self._find_element("//*[@id='main-message']/h1").text
            massage2 = self._find_element("//*[@id='main-message']/div[2]").text
            self.logger.critical("Help link is unavailable.\nMassage: " + str(massage1) + str(massage2))
        except TimeoutException:
            self.logger.error("Help window is not opened")
        except IndexError:
            help_window = 'null'
            self.logger.critical("Help window is not found " + str(help_window))


