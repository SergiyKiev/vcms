from base import Base
from locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time


class LeftSideMenu(Base):

    # BTN - BUTTON. TITLE - main title on the page
    ICON_HOME = Locators.BTN_ICON_HOME
    ICON_DEVICES = Locators.BTN_ICON_DEVICES
    ICON_ADMINISTRATION = Locators.BTN_ICON_ADMINISTRATION
    ICON_TASKS = Locators.BTN_ICON_TASKS
    ICON_REPORTING = Locators.BTN_ICON_REPORTING
    ICON_SOFT_AND_PATCH_MANAGER = Locators.BTN_ICON_SFT_AND_PTH_MANAGER
    ICON_PASSWORD_RESET = Locators.BTN_ICON_PASSWORD_RESET
    TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_WELCOME_TO_CLOUD_MANAGEMENT_SUITE
    # TITLE_DEVICES = Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_DEVICES
    TITLE_DEVICES = "//" + Locators.EL_PAGE_HEADER_PANEL + Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_DEVICES
    TITLE_ADMINISTRATION = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_ADMINISTRATION
    TITLE_TASKS = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_TASKS
    TITLE_REPORTING = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_REPORTING
    TITLE_SOFTWARE_AND_PATCH_MANAGER = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_SOFTWARE_AND_PATCH_MANAGER
    TITLE_PASSWORD_RESET = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_PASSWORD_RESET
    LEFT_SIDE_MENU_DEVICES = Locators.LEFT_SIDE_MENU_DEVICES
    LEFT_SIDE_MENU_ADMINISTRATION = Locators.LEFT_SIDE_MENU_ADMINISTRATION
    LEFT_SIDE_MENU_TASKS = Locators.LEFT_SIDE_MENU_TASKS
    LEFT_SIDE_MENU_REPORTING = Locators.LEFT_SIDE_MENU_REPORTING
    LEFT_SIDE_MENU_SOFTWARE_AND_PATCH_MANAGER = Locators.LEFT_SIDE_MENU_SOFT_AND_PATCH_MANAGER
    LEFT_SIDE_MENU_PASSWORD_RESET = Locators.LEFT_SIDE_MENU_PASSWORD_RESET
    MENU_IS_VISIBLE = Locators.LEFT_SIDE_MENU_VISIBLE

    def click_icon_home(self):
        self.click_element(self.ICON_HOME)
        cond = self.wait_for_element_present(self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
        return True if cond else False

    def click_icon_devices(self):
        self.click_element(self.ICON_DEVICES)
        self.wait_for_element_present(self.LEFT_SIDE_MENU_DEVICES)
        self.wait_for_element_present(self.TITLE_DEVICES)

    def click_icon_administration(self):
        self.click_element(self.ICON_ADMINISTRATION)
        self.wait_for_element_present(self.LEFT_SIDE_MENU_ADMINISTRATION)
        self.wait_for_element_present(self.TITLE_ADMINISTRATION)

    def click_icon_tasks(self):
        self.click_element(self.ICON_TASKS)
        self.wait_for_element_present(self.LEFT_SIDE_MENU_TASKS)
        self.wait_for_element_present(self.TITLE_TASKS)

    def click_icon_reporting(self):
        self.click_element(self.ICON_REPORTING)
        self.wait_for_element_present(self.LEFT_SIDE_MENU_REPORTING)
        self.wait_for_element_present(self.TITLE_REPORTING)

    def click_icon_software_and_patch_manager(self):
        self.click_element(self.ICON_SOFT_AND_PATCH_MANAGER)
        self.wait_for_element_present(self.LEFT_SIDE_MENU_SOFTWARE_AND_PATCH_MANAGER)
        self.wait_for_element_present(self.TITLE_SOFTWARE_AND_PATCH_MANAGER)

    def click_icon_password_reset(self):
        self.click_element(self.ICON_PASSWORD_RESET)
        self.wait_for_element_present(self.LEFT_SIDE_MENU_PASSWORD_RESET)
        self.wait_for_element_present(self.TITLE_PASSWORD_RESET)

    def open_left_side_menu_home(self):
        try:
            cond = self.is_element_not_present(self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
            if cond:
                self.click_icon_home()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_devices(self):
        try:
            self.wait_for_element_not_present(Locators.LEFT_SIDE_MENU_DEVICES)
            cond = self.is_element_not_present(Locators.LEFT_SIDE_MENU_DEVICES + Locators.LEFT_SIDE_MENU_VISIBLE)
            if cond:
                self.click_icon_devices()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_left_side_menu_administration(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_ADMINISTRATION + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_administration()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_left_side_menu_tasks(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_TASKS + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_tasks()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_left_side_menu_reporting(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_REPORTING + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_reporting()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_left_side_menu_software_and_patch_manager(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_SOFTWARE_AND_PATCH_MANAGER + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_software_and_patch_manager()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_left_side_menu_password_reset(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_PASSWORD_RESET + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_password_reset()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    # def check_devices_page_loaded(self):
    #     cond = self.is_element_present(self.LEFT_SIDE_MENU_DEVICES + self.MENU_IS_VISIBLE)
    #     return True if cond else False
