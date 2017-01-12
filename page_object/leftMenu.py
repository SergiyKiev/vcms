from base import Base
from locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class LeftSideMenu(Base):

    # def __init__(self):
    #     # PageBase.__init__(self, driver = self.driver)
    #     super(LeftSideMenu,self).__init__(self)
    #     # CONSTANTS
    #     self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_WELCOME_TO_CLOUD_MANAGEMENT_SUITE
    #     self.TITLE_DEVICES = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_DEVICES
    #     self.TITLE_ADMINISTRATION = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_ADMINISTRATION
    #     self.TITLE_TASKS = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_TASKS
    #     self.TITLE_REPORTING = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_REPORTING
    #     self.TITLE_SOFTWARE_AND_PATCH_MANAGER = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_SOFTWARE_AND_PATCH_MANAGER
    #     self.TITLE_PASSWORD_RESET = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_PASSWORD_RESET
    #     self.MENU_DEVICES = Locators.MENU_DEVICES
    #     self.MENU_ADMINISTRATION = Locators.MENU_ADMINISTRATION
    #     self.MENU_TASKS = Locators.MENU_TASKS
    #     self.MENU_REPORTING = Locators.MENU_REPORTING
    #     self.MENU_SOFTWARE_AND_PATCH_MANAGER = Locators.MENU_SOFT_AND_PATCH_MANAGER
    #     self.MENU_PASSWORD_RESET = Locators.MENU_PASSWORD_RESET
    #     self.BTN_ICON_HOME = Locators.BTN_ICON_HOME
    #     self.BTN_ICON_DEVICES = Locators.BTN_ICON_DEVICES
    #     self.BTN_ICON_ADMINISTRATION = Locators.BTN_ICON_ADMINISTRATION
    #     self.BTN_ICON_TASKS = Locators.BTN_ICON_TASKS
    #     self.BTN_ICON_REPORTING = Locators.BTN_ICON_REPORTING
    #     self.BTN_ICON_SOFT_AND_PATCH_MANAGER = Locators.BTN_ICON_SFT_AND_PTH_MANAGER
    #     self.BTN_ICON_PASSWORD_RESET = Locators.BTN_ICON_PASSWORD_RESET
    #     self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_WELCOME_TO_CLOUD_MANAGEMENT_SUITE
    #     self.TITLE_DEVICES = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_DEVICES
    #     self.TITLE_ADMINISTRATION = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_ADMINISTRATION
    #     self.TITLE_TASKS = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_TASKS
    #     self.TITLE_REPORTING = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_REPORTING
    #     self.TITLE_SOFTWARE_AND_PATCH_MANAGER = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_SOFTWARE_AND_PATCH_MANAGER
    #     self.TITLE_PASSWORD_RESET = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_PASSWORD_RESET
    #     self.MENU_DEVICES = Locators.MENU_DEVICES
    #     self.MENU_ADMINISTRATION = Locators.MENU_ADMINISTRATION
    #     self.MENU_TASKS = Locators.MENU_TASKS
    #     self.MENU_REPORTING = Locators.MENU_REPORTING
    #     self.MENU_SOFTWARE_AND_PATCH_MANAGER = Locators.MENU_SOFT_AND_PATCH_MANAGER
    #     self.MENU_PASSWORD_RESET = Locators.MENU_PASSWORD_RESET
    #     self.BTN_ICON_HOME = Locators.BTN_ICON_HOME
    #     self.BTN_ICON_DEVICES = Locators.BTN_ICON_DEVICES
    #     self.BTN_ICON_ADMINISTRATION = Locators.BTN_ICON_ADMINISTRATION
    #     self.BTN_ICON_TASKS = Locators.BTN_ICON_TASKS
    #     self.BTN_ICON_REPORTING = Locators.BTN_ICON_REPORTING
    #     self.BTN_ICON_SOFT_AND_PATCH_MANAGER = Locators.BTN_ICON_SFT_AND_PTH_MANAGER
    #     self.BTN_ICON_PASSWORD_RESET = Locators.BTN_ICON_PASSWORD_RESET

    # BTN - BUTTON. TITLE - main title on the page
    BTN_ICON_HOME = Locators.BTN_ICON_HOME
    BTN_ICON_DEVICES = Locators.BTN_ICON_DEVICES
    BTN_ICON_ADMINISTRATION = Locators.BTN_ICON_ADMINISTRATION
    BTN_ICON_TASKS = Locators.BTN_ICON_TASKS
    BTN_ICON_REPORTING = Locators.BTN_ICON_REPORTING
    BTN_ICON_SOFT_AND_PATCH_MANAGER = Locators.BTN_ICON_SFT_AND_PTH_MANAGER
    BTN_ICON_PASSWORD_RESET = Locators.BTN_ICON_PASSWORD_RESET
    TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_WELCOME_TO_CLOUD_MANAGEMENT_SUITE
    TITLE_DEVICES = Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_DEVICES
    TITLE_ADMINISTRATION = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_ADMINISTRATION
    TITLE_TASKS = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_TASKS
    TITLE_REPORTING = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_REPORTING
    TITLE_SOFTWARE_AND_PATCH_MANAGER = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_SOFTWARE_AND_PATCH_MANAGER
    TITLE_PASSWORD_RESET = "//" + Locators.EL_PAGE_HEADER_PANEL + "/*" + Locators.TEXT_PASSWORD_RESET
    LEFT_MENU_DEVICES = Locators.MENU_DEVICES
    LEFT_MENU_ADMINISTRATION = Locators.MENU_ADMINISTRATION
    LEFT_MENU_TASKS = Locators.MENU_TASKS
    LEFT_MENU_REPORTING = Locators.MENU_REPORTING
    LEFT_MENU_SOFTWARE_AND_PATCH_MANAGER = Locators.MENU_SOFT_AND_PATCH_MANAGER
    LEFT_MENU_PASSWORD_RESET = Locators.MENU_PASSWORD_RESET

    def click_home_left_menu_button(self):
        self.click_element(self.BTN_ICON_HOME)
        cond = self.wait_for_element_present(self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
        return True if cond else False

    def click_devices_left_menu_button(self):
        self.click_element(self.BTN_ICON_DEVICES)
        self.wait_for_element_present(self.LEFT_MENU_DEVICES)
        self.wait_for_element_present(self.TITLE_DEVICES)

    def click_administration_left_menu_button(self):
        self.click_element(self.BTN_ICON_ADMINISTRATION)
        self.wait_for_element_present(self.LEFT_MENU_ADMINISTRATION)
        self.wait_for_element_present(self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE)

    def click_tasks_left_menu_button(self):
        self.click_element(self.BTN_ICON_TASKS)
        self.wait_for_element_present(self.LEFT_MENU_TASKS)

    def click_reporting_left_menu_button(self):
        self.click_element(self.BTN_ICON_REPORTING)
        self.wait_for_element_present(self.LEFT_MENU_REPORTING)

    def click_software_and_patch_manager_left_menu_button(self):
        self.click_element(self.BTN_ICON_SOFT_AND_PATCH_MANAGER)
        self.wait_for_element_present(self.LEFT_MENU_SOFTWARE_AND_PATCH_MANAGER)

    def click_password_reset_left_menu_button(self):
        self.click_element(self.BTN_ICON_PASSWORD_RESET)
        self.wait_for_element_present(self.LEFT_MENU_PASSWORD_RESET)

    def open_home_left_menu(self):
        try:
            cond = self.is_element_not_present(self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
            if cond:
                self.click_home_left_menu_button()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_devices_left_menu(self):
        try:
            cond = self.is_element_not_present(self.LEFT_MENU_DEVICES)
            if cond:
                self.click_devices_left_menu_button()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_administration_left_menu(self):
        try:
            cond = self.is_element_not_present(self.LEFT_MENU_ADMINISTRATION)
            if cond:
                self.click_administration_left_menu_button()
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Object not found"
