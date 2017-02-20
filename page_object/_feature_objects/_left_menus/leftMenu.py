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
    ICON_HOME                    = "//td[contains(@style,'Home')]/ancestor::div[@class='PictureBox-Control']"

    '''NEW'''
    def click_icon_home(self):
        self._click_element(self.ICON_HOME)
        self._wait_for_element_not_present(self.ICON_HOME + BaseElements.GREY_COLOR)

    def open_menu_home(self):
        element = self.ICON_HOME + BaseElements.GREY_COLOR
        precond = self._is_element_present(element)
        if precond:
            self.click_icon_home()
        cond = self._is_element_not_present(element)
        return True if cond else False

    def menu_administration(self):
        left_menu = self._get_left_menu(self.ADMINISTRATION)
        return left_menu

    def menu_devices(self):
        left_menu = self._get_left_menu(self.DEVICES)
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

    def check_menu_devices_is_visible(self):
        cond = self._is_element_present(self.menu_devices())
        return True if cond else False

    def check_menu_administration_is_visible(self):
        cond = self._is_element_present(self.menu_administration())
        return True if cond else False

    def check_menu_tasks_is_visible(self):
        cond = self._is_element_present(self.menu_tasks())
        return True if cond else False

    def check_menu_reporting_is_visible(self):
        cond = self._is_element_present(self.menu_reporting())
        return True if cond else False

    def check_menu_software_and_patch_manager_is_visible(self):
        cond = self._is_element_present(self.menu_software_and_patch_manager())
        return True if cond else False

    def check_menu_password_reset_is_visible(self):
        cond = self._is_element_present(self.menu_password_reset())
        # print "CHECK METHOD RETURNS ", cond
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
    # def check_menu_devices_is_visible(self):
    #     cond = self._check_left_menu_visible(self.DEVICES)
    #     return True if cond else False
    #
    # def check_menu_administration_is_visible(self):
    #     cond = self._check_left_menu_visible(self.ADMINISTRATION)
    #     return True if cond else False
    #
    # def check_menu_tasks_is_visible(self):
    #     cond = self._check_left_menu_visible(self.TASKS)
    #     return True if cond else False
    #
    # def check_menu_reporting_is_visible(self):
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


