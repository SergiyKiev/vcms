from _base_page.base import Base
from _locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class LeftSideMenu(Base):

    # BTN - BUTTON. TITLE - main title on the page
    ICON_HOME = Locators.ICON_HOME
    ICON_DEVICES = Locators.ICON_DEVICES
    ICON_ADMINISTRATION = Locators.ICON_ADMINISTRATION
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
        self.click_element(Locators.ICON_DEVICES)
        self.wait_for_element_present(Locators.LEFT_SIDE_MENU_DEVICES)
        self.wait_for_element_present("//" + Locators.EL_PAGE_HEADER_PANEL + Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_DEVICES)

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

    def open_menu_home(self):
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
            self.wait_for_element_present(self.ICON_DEVICES)
            cond = self.is_element_not_present(Locators.LEFT_SIDE_MENU_DEVICES + Locators.LEFT_SIDE_MENU_VISIBLE)
            if cond:
                self.click_icon_devices()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_administration(self):
        try:
            self.wait_for_element_present(self.ICON_ADMINISTRATION)
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_ADMINISTRATION + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_administration()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_tasks(self):
        self.wait_for_element_present(self.ICON_TASKS)
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_TASKS + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_tasks()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_reporting(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_REPORTING + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_reporting()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_software_and_patch_manager(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_SOFTWARE_AND_PATCH_MANAGER + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_software_and_patch_manager()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_menu_password_reset(self):
        try:
            cond = self.is_element_not_present(self.LEFT_SIDE_MENU_PASSWORD_RESET + self.MENU_IS_VISIBLE)
            if cond:
                self.click_icon_password_reset()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    # def check_main_page_loaded(self):
    #     cond = self.is_element_present(self.LEFT_SIDE_MENU_DEVICES + self.MENU_IS_VISIBLE)
    #     return True if cond else False

    def click_global_site_view_label(self):
        self.click_element(Locators.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_present(Locators.BTN_NEW_SITE)
        self.wait_for_element_selected(Locators.LABEL_GLOBAL_SITE_VIEW)
        # self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_CONTAINS_GLOBAL_SITE_VIEW)
        self.wait_for_element_not_present(Locators.BTN_DELETE)

    def click_default_site_in_global_site_view(self):
        self.click_element(Locators.LABEL_DEFAULT_SITE)
        self.wait_for_element_selected(Locators.LABEL_DEFAULT_SITE)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_CONTAINS_DEFAULT_SITE)

    def click_site_in_global_site_view_tree(self, sitename):
        elem1 = "//span[text()='" + sitename + "']"
        elem2 = "//span[contains(text(),'" + sitename + "')]"
        self.click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + elem1)
        self.wait_for_element_selected(elem1 + Locators.anc + Locators.EL_NODE_CONTAINER)
        self.wait_for_element_present(Locators.BTN_CONFIG)
        self.wait_for_element_present(Locators.BTN_NEW_SITE)
        # self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + elem2)

