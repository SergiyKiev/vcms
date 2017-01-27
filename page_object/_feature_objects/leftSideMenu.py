from _base_page.base import Base
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time


class LeftSideMenu(Base):

    VISIBLE = "[contains(@style,'translate3d(0px, 0px, 0px)')]"
    GREY_COLOR = "[contains(@style,'#E8E8E8')]"
    ICON_HOME = "//td[contains(@style,'Home')]"
    ICON_HOME_GREY = ICON_HOME + "/ancestor::div[@class='PictureBox-Control']" + GREY_COLOR
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
    # TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_WELCOME_TO_CLOUD_MANAGEMENT_SUITE
    # # TITLE_DEVICES = Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_DEVICES
    # TITLE_DEVICES = "//" + Locators.EL_PAGE_HEADER_PANEL + Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_DEVICES
    # TITLE_ADMINISTRATION = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_ADMINISTRATION
    # TITLE_TASKS = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_TASKS
    # TITLE_REPORTING = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_REPORTING
    # TITLE_SOFTWARE_AND_PATCH_MANAGER = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_SOFTWARE_AND_PATCH_MANAGER
    # TITLE_PASSWORD_RESET = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_PASSWORD_RESET
    CONTAINER = "/ancestor::div[contains(@style,'transform')]"
    MENU_DEVICES = "//span[text()='Devices']" + CONTAINER
    MENU_ADMINISTRATION = "//span[text()='Administration']" + CONTAINER
    MENU_TASKS = "//span[text()='Tasks']" + CONTAINER
    MENU_REPORTING = "//span[text()='Reporting']" + CONTAINER
    MENU_SOFTWARE_AND_PATCH_MANAGER = "//span[text()='Software / Patch Manager']" + CONTAINER
    MENU_PASSWORD_RESET = "//span[text()='Password Reset']" + CONTAINER

    def click_icon_home(self):
        self._click_element(LeftSideMenu.ICON_HOME)
        self.wait_for_element_not_present(LeftSideMenu.ICON_HOME_GREY)

    def click_icon_devices(self):
        self._click_element(LeftSideMenu.ICON_DEVICES)
        self.wait_for_element_not_present(LeftSideMenu.ICON_DEVICES_GREY)

    def click_icon_administration(self):
        self._click_element(LeftSideMenu.ICON_ADMINISTRATION)
        self.wait_for_element_not_present(LeftSideMenu.ICON_ADMINISTRATION_GREY)

    def click_icon_tasks(self):
        self._click_element(LeftSideMenu.ICON_TASKS)
        self.wait_for_element_not_present(LeftSideMenu.ICON_TASKS_GREY)

    def click_icon_reporting(self):
        self._click_element(LeftSideMenu.ICON_REPORTING)
        self.wait_for_element_not_present(LeftSideMenu.ICON_REPORTING_GREY)

    def click_icon_software_and_patch_manager(self):
        self._click_element(LeftSideMenu.ICON_SOFT_AND_PATCH_MANAGER)
        self.wait_for_element_not_present(LeftSideMenu.ICON_SOFT_AND_PATCH_MANAGER_GREY)

    def click_icon_password_reset(self):
        self._click_element(LeftSideMenu.ICON_PASSWORD_RESET)
        self.wait_for_element_not_present(LeftSideMenu.ICON_PASSWORD_RESET_GREY)

    def open_menu_home(self):
        try:
            self.wait_for_element_present(LeftSideMenu.ICON_HOME)
            cond = self.is_element_present(LeftSideMenu.ICON_HOME_GREY)
            if cond:
                self.click_icon_home()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_devices(self):
        try:
            self.wait_for_element_present(LeftSideMenu.ICON_DEVICES)
            cond = self.is_element_not_present(LeftSideMenu.MENU_DEVICES + LeftSideMenu.VISIBLE)
            if cond:
                self.click_icon_devices()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_administration(self):
        try:
            self.wait_for_element_present(LeftSideMenu.ICON_ADMINISTRATION)
            cond = self.is_element_not_present(LeftSideMenu.MENU_ADMINISTRATION + LeftSideMenu.VISIBLE)
            if cond:
                self.click_icon_administration()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_tasks(self):
        try:
            self.wait_for_element_present(LeftSideMenu.ICON_TASKS)
            cond = self.is_element_not_present(LeftSideMenu.MENU_TASKS + LeftSideMenu.VISIBLE)
            if cond:
                self.click_icon_tasks()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_reporting(self):
        try:
            self.wait_for_element_present(LeftSideMenu.ICON_REPORTING)
            cond = self.is_element_not_present(LeftSideMenu.MENU_REPORTING + LeftSideMenu.VISIBLE)
            if cond:
                self.click_icon_reporting()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_software_and_patch_manager(self):
        try:
            self.wait_for_element_present(LeftSideMenu.ICON_SOFT_AND_PATCH_MANAGER)
            cond = self.is_element_not_present(LeftSideMenu.MENU_SOFTWARE_AND_PATCH_MANAGER + LeftSideMenu.VISIBLE)
            if cond:
                self.click_icon_software_and_patch_manager()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_password_reset(self):
        try:
            self.wait_for_element_present(LeftSideMenu.ICON_PASSWORD_RESET)
            cond = self.is_element_not_present(self.MENU_PASSWORD_RESET + self.VISIBLE)
            if cond:
                self.click_icon_password_reset()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def click_global_site_view_label(self):
        self._click_element(Locators.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_selected(Locators.LABEL_GLOBAL_SITE_VIEW)
        # self.wait_for_element_present(Locators.BTN_CONFIG)
        # self.wait_for_element_present(Locators.BTN_NEW_SITE)
        # self.wait_for_element_not_present(Locators.BTN_DELETE)

    def click_default_site_in_global_site_view(self):
        self._click_element(Locators.LABEL_DEFAULT_SITE)
        self.wait_for_element_selected(Locators.LABEL_DEFAULT_SITE)
        # self.wait_for_element_present(Locators.BTN_CONFIG)
        # self.wait_for_element_present(Locators.BTN_NEW_SITE)

    def click_site_in_global_site_view_tree(self, sitename):
        elem = "//span[text()='" + sitename + "']"
        self._click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + elem)
        self.wait_for_element_selected(elem + Locators.anc + Locators.EL_TREE_CONTAINER)

    def click_subsite_in_site_tree(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']"
        subsite_name = "//span[text()='" + subsitename + "']"
        contains_subsite_name = "//span[contains(text(),'" + subsitename + "')]"
        elem = site_name + "/following::div[contains(@style,'10LTR')]/*" + subsite_name
        self._click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + Locators.EL_TREE_CONTAINER)

    def check_menu_devices_is_visible(self):
        cond = self.is_element_present(LeftSideMenu.MENU_DEVICES + LeftSideMenu.VISIBLE)
        return True if cond else False

    def check_menu_tasks_is_visible(self):
        cond = self.is_element_present(LeftSideMenu.MENU_TASKS + LeftSideMenu.VISIBLE)
        return True if cond else False

    def check_menu_reporting_is_visible(self):
        cond = self.is_element_present(LeftSideMenu.MENU_REPORTING + LeftSideMenu.VISIBLE)
        return True if cond else False

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        cond = self.is_element_present("//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']")
        return True if cond else False


