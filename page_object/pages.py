from base import Page
from locators import *
from settings import Settings
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from variables import Variables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class LoginPage(Page):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver = webdriver.Firefox()
        self.driver.get(Settings.baseUrl)
        self.driver.implicitly_wait(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.BUTTON_SIGN_IN)))

    def check_login_page_loaded(self):
        cond = self.driver.find_element(Locators.BUTTON_SIGN_IN)
        return True if cond else False

    def enter_username(self, username = Settings.username):
        self.find_element(Locators.FIELD_USERNAME).send_keys(username)
        return True

    def enter_password(self, password = Settings.password):
        self.find_element(Locators.FIELD_PASSWORD).send_keys(password)
        return True

    def click_sign_in_button(self):
        self.click_element(Locators.BUTTON_SIGN_IN)
        return HomePage(self.driver)

    def login(self):
        self.enter_username()
        self.enter_password()
        self.click_sign_in_button()
        return HomePage(self.driver)


class HomePage(Page):

    def check_home_page_loaded(self):
        cond = self.is_element_present(Locators.BUTTON_EXIT)
        return True if cond else False

    def click_devices_menu_button(self):
        self.click_element(Locators.BUTTON_DEVICES)
        return DevicesPage(self.driver)

    def open_devices_menu(self):
        if self.is_element_present(Locators.MENU_DEVICES):
            return DevicesPage(self.driver)
        else:
            self.click_devices_menu_button()
            return DevicesPage(self.driver)


class DevicesPage(Page):

    def check_devices_page_loaded(self):
        cond = self.is_element_present(Locators.MENU_DEVICES)
        return True if cond else False

    def click_global_site_view_site(self):
        self.click_element(Locators.SITE_GLOBAL_SITE_VIEW)
        cond1 = self.is_element_present(Locators.BUTTON_NEW_SITE)
        cond2 = self.is_element_selected(Locators.LABEL_GLOBAL_SITE_VIEW)
        cond3 = self.is_element_present(Locators.CONTAINER_HEADER_DEVICES_VIEW + "/*" + Locators.TEXT_GLOBAL_SITE_VIEW)
        return True if cond1 | cond2 | cond3 else False

    def click_new_site_button(self):
        self.click_element(Locators.BUTTON_NEW_SITE)
        cond = self.is_element_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def enter_site_name(self):
        self.find_element(Locators.POPUP_SITE_NAME + "/*" + Locators.FIELD).send_keys(Variables.siteName)
        return True

    def click_site_name_popup_OK_button(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BUTTON_OK)
        cond = self.wait.until_not(EC.presence_of_element_located((By.XPATH, Locators.POPUP_SITE_NAME)))
        return True if cond else False

    def click_site_in_global_site_view(self):
        self.click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + Locators.TEXT_SITE_NAME)
        cond1 = self.is_element_selected(Locators.TEXT_SITE_NAME + "/ancestor::div")
        cond2 = self.is_element_present(Locators.CONTAINER_HEADER_DEVICES_VIEW + "/*//span[contains(text(),'" + Variables.siteName + "'])")
        return True if cond1 | cond2 else False

    def check_site_is_in_gsv(self): # gsv - Global Site View
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + Locators.TEXT_SITE_NAME)
        return True if cond else False

    def check_site_is_not_in_gsv(self): # gsv - Global Site View
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + Locators.TEXT_SITE_NAME)
        return False if cond else True

    def click_delete_button(self):
        self.click_element(Locators.BUTTON_DELETE)
        cond = self.find_element(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_are_you_sure_ok_button(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BUTTON_OK)
        cond = self.is_element_present(Locators.POPUP_ARE_YOU_SURE)
        return False if cond else True

    def delete_site_if_exists(self):
        try:
            elem = self.driver.find_element_by_xpath(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + Locators.TEXT_SITE_NAME)
            if elem:
                self.click_site_in_global_site_view()
                self.click_delete_button()
                self.click_are_you_sure_ok_button()
                self.wait.until_not(EC.presence_of_element_located((By.XPATH, Locators.POPUP_ARE_YOU_SURE)))
            else: pass
        except(NoSuchElementException):
            return True
        return True

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
