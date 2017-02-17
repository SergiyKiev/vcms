import time
from _base_page.base_actions import BaseActions
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
    GREY_COLOR                   = "[contains(@style,'#E8E8E8')]"

    def _click_left_menu(self, locator):
        ICON = "//div[@title='" + locator + "']"
        self._click_element(ICON)
        self._wait_for_element_not_present(ICON + self.GREY_COLOR)

    def _check_left_menu_visible(self, locator):
        LEFT_MENU = "//span[text()='" + locator + "']/ancestor::div[contains(@style,'transform')]"
        cond = self._is_left_menu_visible(LEFT_MENU)
        return True if cond else False

    def _open_left_menu(self, locator):
        cond = self._check_left_menu_visible(locator)
        if cond is not True:
            i = 0
            while i < 5:
                i += 1
                cond = self._check_left_menu_visible(locator)
                if cond is not True:
                    self._click_left_menu(locator)
                else:
                    break
        cond = self._check_left_menu_visible(locator)
        return True if cond else False

    def click_icon_home(self):
        self._click_element(self.ICON_HOME)
        self._wait_for_element_not_present(self.ICON_HOME + self.GREY_COLOR)

    def click_icon_devices(self):
        self._click_left_menu(self.DEVICES)

    def click_icon_administration(self):
        self._click_left_menu(self.ADMINISTRATION)

    def click_icon_tasks(self):
        self._click_left_menu(self.TASKS)

    def click_icon_reporting(self):
        self._click_left_menu(self.REPORTING)

    def click_icon_software_and_patch_manager(self):
        self._click_left_menu(self.SOFTWARE_AND_PATCH_MANAGER)

    def click_icon_password_reset(self):
        self._click_left_menu(self.PASSWORD_RESET)

    def open_menu_home(self):
        precond = self._is_element_present(self.ICON_HOME + self.GREY_COLOR)
        if precond:
            self.click_icon_home()
        cond = self._is_element_not_present(self.ICON_HOME + self.GREY_COLOR)
        return True if cond else False

    def open_menu_devices(self):
        self._open_left_menu("Devices")
        # cond = self._is_left_menu_visible(self.MENU_DEVICES)
        # if cond is not True:
        #     i = 0
        #     while i < 5:
        #         i += 1
        #         menu_visible = self._is_left_menu_visible(self.MENU_DEVICES)
        #         if menu_visible is not True:
        #             self.click_icon_devices()
        #         else:
        #             break
        #     # print "Left Menu is opened"

    def open_menu_administration(self):
        self._open_left_menu("Administration")

    def open_menu_tasks(self):
        self._open_left_menu("Tasks")

    def open_menu_reporting(self):
        self._open_left_menu("Reporting")

    def open_menu_software_and_patch_manager(self):
        self._open_left_menu("Software / Patch Manager")

    def open_menu_password_reset(self):
        self._open_left_menu("Password Reset")

    def check_menu_devices_is_visible(self):
        cond = self._check_left_menu_visible(self.DEVICES)
        return True if cond else False

    def check_menu_administration_is_visible(self):
        cond = self._check_left_menu_visible(self.ADMINISTRATION)
        return True if cond else False

    def check_menu_tasks_is_visible(self):
        cond = self._check_left_menu_visible(self.TASKS)
        return True if cond else False

    def check_menu_reporting_is_visible(self):
        cond = self._check_left_menu_visible(self.REPORTING)
        return True if cond else False

    def check_menu_software_and_patch_manager_is_visible(self):
        cond = self._check_left_menu_visible(self.SOFTWARE_AND_PATCH_MANAGER)
        return True if cond else False

    def check_menu_password_reset_is_visible(self):
        cond = self._check_left_menu_visible(self.PASSWORD_RESET)
        return True if cond else False


