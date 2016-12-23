from base import Page
from locators import *
from settings import Settings
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class LoginPage(Page):

    def check_login_page_loaded(self):
        return True if self.driver.find_element_by_xpath(Locators.BUTTON_SIGN_IN) else False

    def enter_username(self, username = Settings.username):
        self.find_element(Locators.FIELD_USERNAME).send_keys(username)
        return True

    def enter_password(self, password = Settings.password):
        self.driver.find_element_by_xpath(Locators.FIELD_PASSWORD).send_keys(password)
        return True

    def click_sign_in_button(self):
        self.click(Locators.BUTTON_SIGN_IN, Locators.BUTTON_EXIT)
        # self.driver.find_element_by_xpath(Locators.BUTTON_SIGN_IN).click()
        # time.sleep(10)
        # self.waiter(Locators.BUTTON_EXIT)
        return HomePage(self.driver)

    def login(self):
        self.enter_username()
        self.enter_password()
        self.click_sign_in_button()
        return HomePage(self.driver)


class HomePage(Page):

    def check_home_page_loaded(self):
        return True if self.driver.find_element_by_xpath(Locators.BUTTON_EXIT) else False

    def click_devices_menu_button(self):
        self.click(Locators.BUTTON_DEVICES, Locators.MENU_DEVICES)
        return DevicesPage(self.driver)
        # try:
        #     elem = self.driver.find_element_by_xpath(Locators.MENU_DEVICES)
        #     if elem:
        #         pass
        #     else:
        #         self.click(Locators.BUTTON_DEVICES, Locators.MENU_DEVICES)
        #         return DevicesPage(self.driver)
        # except(NoSuchElementException):
        #         return DevicesPage(self.driver)

class DevicesPage(Page):

    def check_devices_page_loaded(self):
        return True if self.find_element(Locators.MENU_DEVICES) else False

    def click_global_site_view_site(self):
        self.click(Locators.SITE_GLOBAL_SITE_VIEW, Locators.LABEL_GLOBAL_SITE_VIEW + Locators.SELECTED)
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, Locators.BUTTON_NEW_SITE)))
        return True if self.driver.find_element_by_xpath(Locators.LABEL_GLOBAL_SITE_VIEW + Locators.SELECTED) else False

    def click_new_site_button(self):
        self.click(Locators.BUTTON_NEW_SITE, Locators.POPUP_SITE_NAME)
        return self.driver.find_element_by_xpath(Locators.POPUP_SITE_NAME)

    def enter_site_name(self, sitename = Locators.SITE_NAME ):
        self.driver.find_element_by_xpath(Locators.POPUP_SITE_NAME + "/*" + Locators.FIELD).send_keys(sitename)
        return True

    def click_site_name_OK_button(self):
        self.click(Locators.POPUP_SITE_NAME + "/*" + Locators.BUTTON_OK,
                   Locators.TREE_GLOBAL_SITE_VIEW + "/*" + Locators.SITE_SITE_NAME)
        return self.driver.find_element_by_xpath(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + Locators.SITE_SITE_NAME)

class AdministrationPage(Page):
    pass


class TasksPage(Page):
    pass


class ReportingPage(Page):
    pass


class SoftwarePatchManagerPage(Page):
    pass


class PasswordReset(Page):
    pass
