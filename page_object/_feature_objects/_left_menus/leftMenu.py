import time
from _base_page.base_actions import BaseActions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class LeftMenu(BaseActions):
    "[contains(@style,'translate3d(0px, 0px, 0px)')]"
    #CONSTANTS
    LEFT_MENU_VISIBLE = "[contains(@style,'(0px, 0px, 0px)')]"
    GREY_COLOR = "/ancestor::div[@class='PictureBox-Control'][contains(@style,'#E8E8E8')]"
    LABEL = "div[contains(@class,'RowContainer')]"
    ICON_HOME = "//td[contains(@style,'Home')]/ancestor::div[@class='PictureBox-Control']"
    ICON_HOME_GREY = ICON_HOME + GREY_COLOR
    ICON_DEVICES = "//div[@title='Devices']"
    ICON_DEVICES_GREY = ICON_DEVICES + GREY_COLOR
    ICON_ADMINISTRATION = "//div[@title='Administration']"
    ICON_ADMINISTRATION_GREY = ICON_ADMINISTRATION + GREY_COLOR
    ICON_TASKS = "//div[@title='Tasks']"
    ICON_TASKS_GREY = ICON_TASKS + GREY_COLOR
    ICON_REPORTING = "//div[@title='Reporting']"
    ICON_REPORTING_GREY = ICON_REPORTING + GREY_COLOR
    ICON_SOFT_AND_PATCH_MANAGER = "//div[@title='Software / Patch Manager']"
    ICON_SOFT_AND_PATCH_MANAGER_GREY = ICON_SOFT_AND_PATCH_MANAGER + GREY_COLOR
    ICON_PASSWORD_RESET = "//div[@title='Password Reset']"
    ICON_PASSWORD_RESET_GREY = ICON_PASSWORD_RESET + GREY_COLOR
    MENU_DEVICES = "//span[text()='Devices']/ancestor::div[contains(@style,'transform')]"
    MENU_ADMINISTRATION = "//span[text()='Administration']/ancestor::div[contains(@style,'transform')]"
    MENU_TASKS = "//span[text()='Tasks']/ancestor::div[contains(@style,'transform')]"
    MENU_REPORTING = "//span[text()='Reporting']/ancestor::div[contains(@style,'transform')]"
    MENU_SOFTWARE_AND_PATCH_MANAGER = "//span[text()='Software / Patch Manager']/ancestor::div[contains(@style,'transform')]"
    MENU_PASSWORD_RESET = "//span[text()='Password Reset']/ancestor::div[contains(@style,'transform')]"

    def click_icon_home(self):
        self._click_element(LeftMenu.ICON_HOME)
        self.wait_for_element_not_present(LeftMenu.ICON_HOME_GREY)

    def click_icon_devices(self):
        self._click_element(LeftMenu.ICON_DEVICES)
        self.wait_for_element_not_present(LeftMenu.ICON_DEVICES_GREY)

    def click_icon_administration(self):
        self._click_element(LeftMenu.ICON_ADMINISTRATION)
        self.wait_for_element_not_present(LeftMenu.ICON_ADMINISTRATION_GREY)

    def click_icon_tasks(self):
        self._click_element(LeftMenu.ICON_TASKS)
        self.wait_for_element_not_present(LeftMenu.ICON_TASKS_GREY)

    def click_icon_reporting(self):
        self._click_element(LeftMenu.ICON_REPORTING)
        self.wait_for_element_not_present(LeftMenu.ICON_REPORTING_GREY)

    def click_icon_software_and_patch_manager(self):
        self._click_element(LeftMenu.ICON_SOFT_AND_PATCH_MANAGER)
        self.wait_for_element_not_present(LeftMenu.ICON_SOFT_AND_PATCH_MANAGER_GREY)

    def click_icon_password_reset(self):
        self._click_element(LeftMenu.ICON_PASSWORD_RESET)
        self.wait_for_element_not_present(LeftMenu.ICON_PASSWORD_RESET_GREY)

    def open_menu_home(self):
        try:
            self.wait_for_element_present(LeftMenu.ICON_HOME)
            cond = self._is_left_menu_visible(LeftMenu.ICON_HOME_GREY)
            if cond:
                pass
            else:
                self.click_icon_home()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_devices(self):
        cond = self._is_left_menu_visible(LeftMenu.MENU_DEVICES)
        if cond is not True:
            i = 0
            while i < 5:
                i += 1
                menu_visible = self._is_left_menu_visible(LeftMenu.MENU_DEVICES)
                if menu_visible is not True:
                    self.click_icon_devices()
                else:
                    break
            # print "Left Menu is opened"
        else:
            pass

    def open_menu_administration(self):
        try:
            self.wait_for_element_present(LeftMenu.ICON_ADMINISTRATION)
            cond = self._is_left_menu_visible(LeftMenu.MENU_ADMINISTRATION)
            if cond:
                pass
            else:
                self.click_icon_administration()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_tasks(self):
        try:
            self.wait_for_element_present(LeftMenu.ICON_TASKS)
            cond = self._is_left_menu_visible(LeftMenu.MENU_TASKS)
            if cond:
                pass
            else:
                self.click_icon_tasks()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_reporting(self):
        try:
            self.wait_for_element_present(LeftMenu.ICON_REPORTING)
            cond = self._is_left_menu_visible(LeftMenu.MENU_REPORTING)
            if cond:
                pass
            else:
                self.click_icon_reporting()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_software_and_patch_manager(self):
        try:
            self.wait_for_element_present(LeftMenu.ICON_SOFT_AND_PATCH_MANAGER)
            cond = self._is_left_menu_visible(LeftMenu.MENU_SOFTWARE_AND_PATCH_MANAGER)
            if cond:
                pass
            else:
                self.click_icon_software_and_patch_manager()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_password_reset(self):
        try:
            self.wait_for_element_present(LeftMenu.ICON_PASSWORD_RESET)
            cond = self._is_left_menu_visible(LeftMenu.MENU_PASSWORD_RESET)
            if cond:
                pass
            else:
                self.click_icon_password_reset()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def check_menu_devices_is_visible(self):
        cond = self._is_left_menu_visible(LeftMenu.MENU_DEVICES)
        return True if cond else False

    def check_menu_administration_is_visible(self):
        cond = self._is_left_menu_visible(LeftMenu.MENU_ADMINISTRATION)
        return True if cond else False

    def check_menu_tasks_is_visible(self):
        cond = self._is_left_menu_visible(LeftMenu.MENU_TASKS)
        return True if cond else False

    def check_menu_reporting_is_visible(self):
        cond = self._is_left_menu_visible(LeftMenu.MENU_REPORTING)
        return True if cond else False

    def check_menu_software_and_patch_manager_is_visible(self):
        cond = self._is_left_menu_visible(LeftMenu.MENU_SOFTWARE_AND_PATCH_MANAGER)
        return True if cond else False

    def check_menu_password_reset_is_visible(self):
        cond = self._is_left_menu_visible(LeftMenu.MENU_PASSWORD_RESET)
        return True if cond else False


