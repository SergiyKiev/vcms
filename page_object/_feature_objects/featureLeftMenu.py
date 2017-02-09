from _base_page.base import Base
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time


class LeftMenu(Base):

    '''CONSTANTS'''
    LEFT_MENU_VISIBLE = "[contains(@style,'translate3d(0px, 0px, 0px)')]"
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
    LEFT_MENU_BOX = "/ancestor::div[contains(@style,'transform')]"
    MENU_DEVICES = "//span[text()='Devices']" + LEFT_MENU_BOX
    MENU_ADMINISTRATION = "//span[text()='Administration']" + LEFT_MENU_BOX
    MENU_TASKS = "//span[text()='Tasks']" + LEFT_MENU_BOX
    MENU_REPORTING = "//span[text()='Reporting']" + LEFT_MENU_BOX
    MENU_SOFTWARE_AND_PATCH_MANAGER = "//span[text()='Software / Patch Manager']" + LEFT_MENU_BOX
    MENU_PASSWORD_RESET = "//span[text()='Password Reset']" + LEFT_MENU_BOX
    LABEL = "div[contains(@class,'RowContainer')]"
    BOX_GLOBAL_SITE_VIEW = MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    BOX_ACTIVE_DIRECTORIES = MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    BOX_QUERIES = MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    BOX_GROUPS = MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[4]"
    TREE_GLOBAL_SITE_VIEW = BOX_GLOBAL_SITE_VIEW + "/div[contains(@class,'SubNodesContainer')]"
    TREE_ACTIVE_DIRECTORIES = BOX_ACTIVE_DIRECTORIES + "/div[contains(@class,'SubNodesContainer')]"
    TREE_QUERIES = BOX_QUERIES + "/div[contains(@class,'SubNodesContainer')]"
    TREE_GROUPS = BOX_GROUPS + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_GLOBAL_SITE_VIEW = BOX_GLOBAL_SITE_VIEW + "/div[contains(@class,'RowContainer')]"
    LABEL_ACTIVE_DIRECTORIES = BOX_ACTIVE_DIRECTORIES + "/div[contains(@class,'RowContainer')]"
    LABEL_QUERIES = BOX_QUERIES + "/div[contains(@class,'RowContainer')]"
    LABEL_GROUPS = BOX_GROUPS + "/div[contains(@class,'RowContainer')]"
    LABEL_DEFAULT_SITE = TREE_GLOBAL_SITE_VIEW + "/div/div/*//span[text()='Default Site']/ancestor::" + LABEL

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
        try:
            self.wait_for_element_present(LeftMenu.ICON_DEVICES)
            cond = self._is_left_menu_visible(LeftMenu.MENU_DEVICES)
            if cond:
                pass
            else:
                self.click_icon_devices()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

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

    def click_global_site_view_label(self):
        self.wait_for_element_present(LeftMenu.LABEL_GLOBAL_SITE_VIEW)
        self._click_element(LeftMenu.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_selected(LeftMenu.LABEL_GLOBAL_SITE_VIEW)

    def click_default_site_in_global_site_view(self):
        self._click_element(LeftMenu.LABEL_DEFAULT_SITE)
        self.wait_for_element_selected(LeftMenu.LABEL_DEFAULT_SITE)

    def click_site_in_global_site_view_tree(self, sitename):
        element = LeftMenu.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']/ancestor::" + LeftMenu.LABEL
        self._click_element(element)
        self.wait_for_element_selected(element)

    def click_subsite_in_site_tree(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::" + LeftMenu.LABEL
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::" + LeftMenu.LABEL
        element = LeftMenu.TREE_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        self._click_element(element)
        self.wait_for_element_selected(element)

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

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self._is_element_present(LeftMenu.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::" + LeftMenu.LABEL
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::" + LeftMenu.LABEL
        element = LeftMenu.TREE_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        cond = self._is_element_present(element)
        return True if cond else False

    def check_default_site_is_in_global_site_view_tree(self):
        cond = self._is_element_present(LeftMenu.LABEL_DEFAULT_SITE)
        return True if cond else False

    def expand_global_site_view_tree(self):
        self.wait_for_element_present(LeftMenu.LABEL_GLOBAL_SITE_VIEW)
        arrow_expand = self._is_element_present(LeftMenu.LABEL_GLOBAL_SITE_VIEW + Base.ARROW_EXPAND)
        if arrow_expand:
            self._expand_tree(LeftMenu.LABEL_GLOBAL_SITE_VIEW)
        else:
            pass




