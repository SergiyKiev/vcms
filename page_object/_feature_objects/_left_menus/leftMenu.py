import time
from _base_page.base_actions import BaseActions
from _base_page.base_elements import BaseElements
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class LeftMenu(BaseActions):

    #ENUMERATION
    DEVICES                      = "Devices"
    ADMINISTRATION               = "Administration"
    TASKS                        = "Tasks"
    REPORTING                    = "Reporting"
    SOFTWARE_AND_PATCH_MANAGER   = "Software / Patch Manager"
    PASSWORD_RESET               = "Password Reset"
    HOME                         = "Homes"

    '''NEW'''
    def menu_home(self):
        left_menu = "//td[contains(@style,'" + self.HOME + "')]/ancestor::div[@class='PictureBox-Control']"
        return left_menu

    def menu_devices(self):
        left_menu = self._get_left_menu(self.DEVICES)
        return left_menu

    def menu_administration(self):
        left_menu = self._get_left_menu(self.ADMINISTRATION)
        return left_menu

    def menu_tasks(self):
        left_menu = self._get_left_menu(self.TASKS)
        return left_menu

    def menu_reporting(self):
        left_menu = self._get_left_menu(self.REPORTING)
        return left_menu

    def menu_software_and_patch_manager(self):
        left_menu = self._get_left_menu(self.SOFTWARE_AND_PATCH_MANAGER)
        return left_menu

    def menu_password_reset(self):
        left_menu = self._get_left_menu(self.PASSWORD_RESET)
        # print "Menu: ", left_menu
        return left_menu

    def click_icon_home(self):
        self._click_left_menu_icon(self.HOME)

    def click_icon_devices(self):
        self._click_left_menu_icon(self.DEVICES)

    def click_icon_administration(self):
        self._click_left_menu_icon(self.ADMINISTRATION)

    def click_icon_tasks(self):
        self._click_left_menu_icon(self.TASKS)

    def click_icon_reporting(self):
        self._click_left_menu_icon(self.REPORTING)

    def click_icon_software_and_patch_manager(self):
        self._click_left_menu_icon(self.SOFTWARE_AND_PATCH_MANAGER)

    def click_icon_password_reset(self):
        self._click_left_menu_icon(self.PASSWORD_RESET)

    def open_menu_home(self):
        element = "//span[text()='Home']/ancestor::div[@class='Label-Control']" + BaseElements.WHITE_COLOR
        i = 0
        while i < 2:
            i += 1
            cond = self._is_element_present(element)
            if cond:
                self.logger.debug("Left menu '" + self.HOME + "' is opened")
                break
            elif cond is None:
                self.logger.error("Failure. Left menu '" + self.HOME + "' is not found")
            elif i == 2:
                self.logger.error("Failure. Left menu '" + self.HOME + "' is not opened after " + str(i) + " attempts")
            else:
                self.click_icon_home()
                self._wait_for_element_present(
                    "//span[text()='Home']/ancestor::div[@class='Label-Control']" + BaseElements.WHITE_COLOR)

    def open_menu_devices(self):
        self._open_left_menu(self.DEVICES)

    def open_menu_administration(self):
        self._open_left_menu(self.ADMINISTRATION)

    def open_menu_tasks(self):
        self._open_left_menu(self.TASKS)

    def open_menu_reporting(self):
        self._open_left_menu(self.REPORTING)

    def open_menu_software_and_patch_manager(self):
        self._open_left_menu(self.SOFTWARE_AND_PATCH_MANAGER)

    def open_menu_password_reset(self):
        self._open_left_menu(self.PASSWORD_RESET)

    def check_menu_home_is_opened(self):
        cond = self._is_element_present(
            "//span[text()='Home']/ancestor::div[@class='Label-Control']" + BaseElements.WHITE_COLOR)
        msg_if_true = "Left menu '" + self.HOME + "' is opened"
        msg_if_false = "Left menu '" + self.HOME + "' is NOT opened"
        self._get_log_msg_for_true_or_false(cond, msg_if_true, msg_if_false)
        return True if cond else False

    def check_menu_devices_is_opened(self):
        cond = self._is_element_present(self.menu_devices())
        msg_if_true = "Left menu '" + self.DEVICES + "' is opened"
        msg_if_false = "Left menu '" + self.DEVICES + "' is NOT opened"
        self._get_log_msg_for_true_or_false(cond, msg_if_true, msg_if_false)
        return True if cond else False

    def check_menu_administration_is_opened(self):
        cond = self._is_element_present(self.menu_administration())
        msg_if_true = "Left menu '" + self.ADMINISTRATION + "' is opened"
        msg_if_false = "Left menu '" + self.ADMINISTRATION + "' is NOT opened"
        self._get_log_msg_for_true_or_false(cond, msg_if_true, msg_if_false)
        return True if cond else False

    def check_menu_tasks_is_opened(self):
        cond = self._is_element_present(self.menu_tasks())
        msg_if_true = "Left menu '" + self.TASKS + "' is opened"
        msg_if_false = "Left menu '" + self.TASKS + "' is NOT opened"
        self._get_log_msg_for_true_or_false(cond, msg_if_true, msg_if_false)
        return True if cond else False

    def check_menu_reporting_is_opened(self):
        cond = self._is_element_present(self.menu_reporting())
        msg_if_true = "Left menu '" + self.REPORTING + "' is opened"
        msg_if_false = "Left menu '" + self.REPORTING + "' is NOT opened"
        self._get_log_msg_for_true_or_false(cond, msg_if_true, msg_if_false)
        return True if cond else False

    def check_menu_software_and_patch_manager_is_opened(self):
        cond = self._is_element_present(self.menu_software_and_patch_manager())
        msg_if_true = "Left menu '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is opened"
        msg_if_false = "Left menu '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is NOT opened"
        self._get_log_msg_for_true_or_false(cond, msg_if_true, msg_if_false)
        return True if cond else False

    def check_menu_password_reset_is_opened(self):
        cond = self._is_element_present(self.menu_password_reset())
        msg_if_true = "Left menu '" + self.PASSWORD_RESET + "' is opened"
        msg_if_false = "Left menu '" + self.PASSWORD_RESET + "' is NOT opened"
        self._get_log_msg_for_true_or_false(cond, msg_if_true, msg_if_false)
        return True if cond else False

    '''OLD'''
    # def _check_left_menu_visible(self, locator):
    #     LEFT_MENU = "//span[text()='" + locator + "']/ancestor::div[contains(@style,'transform')]"
    #     cond = self._is_left_menu_visible(LEFT_MENU)
    #     return True if cond else False
    #
    # def _click_left_menu_icon(self, locator):
    #     icon = "//div[@title='" + locator + "']"
    #     self._click_element(icon)
    #     self._wait_for_element_not_present(icon + self.GREY_COLOR)
    #
    # def _open_left_menu(self, locator):
    #     cond = self._check_left_menu_visible(locator)
    #     if cond is not True:
    #         i = 0
    #         while i < 5:
    #             i += 1
    #             cond = self._check_left_menu_visible(locator)
    #             if cond is not True:
    #                 self._click_left_menu_icon(locator)
    #             else:
    #                 break
    #     cond = self._check_left_menu_visible(locator)
    #     return True if cond else False

    # def _click_left_menu_icon(self, locator):
    #     ICON = "//div[@title='" + locator + "']"
    #     self._click_element(ICON)
    #     self._wait_for_element_not_present(ICON + self.GREY_COLOR)
    #
    # def _check_left_menu_visible(self, locator):
    #     LEFT_MENU = "//span[text()='" + locator + "']/ancestor::div[contains(@style,'transform')]"
    #     cond = self._is_left_menu_visible(LEFT_MENU)
    #     return True if cond else False
    #
    # def _open_left_menu(self, locator):
    #     cond = self._check_left_menu_visible(locator)
    #     if cond is not True:
    #         i = 0
    #         while i < 5:
    #             i += 1
    #             cond = self._check_left_menu_visible(locator)
    #             if cond is not True:
    #                 self._click_left_menu_icon(locator)
    #             else:
    #                 break
    #     cond = self._check_left_menu_visible(locator)
    #     return True if cond else False
    #
    # def click_icon_home(self):
    #     self._click_element(self.ICON_HOME)
    #     self._wait_for_element_not_present(self.ICON_HOME + self.GREY_COLOR)
    #
    # def click_icon_devices(self):
    #     self._click_left_menu_icon(self.DEVICES)
    #
    # def click_icon_administration(self):
    #     self._click_left_menu_icon(self.ADMINISTRATION)
    #
    # def click_icon_tasks(self):
    #     self._click_left_menu_icon(self.TASKS)
    #
    # def click_icon_reporting(self):
    #     self._click_left_menu_icon(self.REPORTING)
    #
    # def click_icon_software_and_patch_manager(self):
    #     self._click_left_menu_icon(self.SOFTWARE_AND_PATCH_MANAGER)
    #
    # def click_icon_password_reset(self):
    #     self._click_left_menu_icon(self.PASSWORD_RESET)
    #
    # def open_menu_home(self):
    #     precond = self._is_element_present(self.ICON_HOME + self.GREY_COLOR)
    #     if precond:
    #         self.click_icon_home()
    #     cond = self._is_element_not_present(self.ICON_HOME + self.GREY_COLOR)
    #     return True if cond else False
    #
    # def open_menu_devices(self):
    #     self._open_left_menu("Devices")
    #
    # def open_menu_administration(self):
    #     self._open_left_menu("Administration")
    #
    # def open_menu_tasks(self):
    #     self._open_left_menu("Tasks")
    #
    # def open_menu_reporting(self):
    #     self._open_left_menu("Reporting")
    #
    # def open_menu_software_and_patch_manager(self):
    #     self._open_left_menu("Software / Patch Manager")
    #
    # def open_menu_password_reset(self):
    #     self._open_left_menu("Password Reset")
    #
    # def check_menu_devices_is_opened(self):
    #     cond = self._check_left_menu_visible(self.DEVICES)
    #     return True if cond else False
    #
    # def check_menu_administration_is_opened(self):
    #     cond = self._check_left_menu_visible(self.ADMINISTRATION)
    #     return True if cond else False
    #
    # def check_menu_tasks_is_opened(self):
    #     cond = self._check_left_menu_visible(self.TASKS)
    #     return True if cond else False
    #
    # def check_menu_reporting_is_opened(self):
    #     cond = self._check_left_menu_visible(self.REPORTING)
    #     return True if cond else False
    #
    # def check_menu_software_and_patch_manager_is_visible(self):
    #     cond = self._check_left_menu_visible(self.SOFTWARE_AND_PATCH_MANAGER)
    #     return True if cond else False
    #
    # def check_menu_password_reset_is_visible(self):
    #     cond = self._check_left_menu_visible(self.PASSWORD_RESET)
    #     return True if cond else False


