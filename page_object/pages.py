from base import Page
from locators import *
from settings import Settings
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from variables import Variables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class LoginPage(Page):

    def check_login_page_loaded(self):
        cond = self.is_element_present(Locators.BUTTON_SIGN_IN)
        return True if cond else False

    def login(self):
        self.check_login_page_loaded()
        self.close_terms_and_conditions_popup()
        self.driver.implicitly_wait(5)
        self.enter_username()
        self.enter_password()
        self.click_sign_in_button()
        self.close_subscription_has_expired_popup()
        return HomePage(self.driver)

    def click_terms_and_conditions_popup_i_agree_button(self):
        self.click_element(Locators.POPUP_TERMS_AND_CONDITIONS + "/*" + Locators.BUTTON_I_AGREE)
        return True if self.find_element(Locators.POPUP_TERMS_AND_CONDITIONS) else False

    def close_terms_and_conditions_popup(self):
        cond = self.find_element(Locators.POPUP_TERMS_AND_CONDITIONS)
        if cond:
            self.click_terms_and_conditions_popup_i_agree_button()
        else:
            pass
        return True

    def close_subscription_has_expired_popup(self):
        # self.click_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED + "/*" + Locators.BUTTON_SYSTEM_CLOSE)
        # return True if self.find_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED) else False
        cond = self.find_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        if cond:
            self.close_subscription_has_expired_popup()
        else:
            pass
        return True

    def enter_username(self, username = Settings.username):
        self.find_element(Locators.FIELD_USERNAME).send_keys(username)
        return True

    def enter_password(self, password = Settings.password):
        self.find_element(Locators.FIELD_PASSWORD).send_keys(password)
        return True

    def click_sign_in_button(self):
        self.click_element(Locators.BUTTON_SIGN_IN)
        return HomePage(self.driver)

    def close_error_popup(self):
        self.click_element(Locators.POPUP_ERROR + "/*" + Locators.BUTTON_SYSTEM_CLOSE)
        return True if self.find_element(Locators.POPUP_ERROR) else False


class HomePage(Page):

    def check_home_page_loaded(self):
        cond = self.is_element_present(Locators.BUTTON_DEVICES)
        return True if cond else False

    def click_devices_menu_button(self):
        self.click_element(Locators.BUTTON_DEVICES)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.MENU_DEVICES)))
        return DevicesPage(self.driver)

    def open_devices_menu(self):
        cond = self.is_element_present(Locators.MENU_DEVICES)
        if cond:
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
        return True if (cond1 or cond2 or cond3) else False

    def click_new_site_button(self):
        self.click_element(Locators.BUTTON_NEW_SITE)
        cond = self.is_element_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def enter_site_name(self, sitename = Variables.siteName):
        self.find_element(Locators.POPUP_SITE_NAME + "/*" + Locators.FIELD).send_keys(sitename)
        return True

    def click_site_name_popup_OK_button(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BUTTON_OK)
        cond = self.wait.until_not(EC.presence_of_element_located((By.XPATH, Locators.POPUP_SITE_NAME)))
        return True if cond else False

    def click_site_name_popup_system_button_close(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BUTTON_SYSTEM_CLOSE)
        cond = self.wait.until_not(EC.presence_of_element_located((By.XPATH, Locators.POPUP_SITE_NAME)))
        return True if cond else False

    def click_site_in_global_site_view(self, sitename = Variables.siteName):
        self.click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        cond1 = self.is_element_selected("//span[text()='" + sitename + "']" + "/ancestor::div")
        cond2 = self.is_element_present(Locators.CONTAINER_HEADER_DEVICES_VIEW + "/*//span[contains(text(),'" + sitename + "'])")
        return True if (cond1 or cond2) else False

    def check_if_site_is_in_gsv(self, sitename = Variables.siteName): # gsv - Global Site View
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def click_delete_button(self):
        self.click_element(Locators.BUTTON_DELETE)
        cond = self.find_element(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_are_you_sure_OK_button(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BUTTON_OK)
        cond = self.is_element_not_present(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def delete_site_if_exists(self, sitename = Variables.siteName):
        try:
            elem = self.driver.find_element_by_xpath(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
            if elem:
                self.click_site_in_global_site_view(sitename)
                self.click_delete_button()
                self.click_are_you_sure_OK_button()
                self.wait.until_not(EC.presence_of_element_located((By.XPATH, Locators.POPUP_ARE_YOU_SURE)))
            else: pass
        except(NoSuchElementException):
            return True
        return True

    def delete_site_from_gsv(self, sitename = Variables.siteName):
        self.click_site_in_global_site_view(sitename)
        self.click_delete_button()
        self.click_are_you_sure_OK_button()
        self.wait.until_not(EC.presence_of_element_located((By.XPATH, Locators.POPUP_ARE_YOU_SURE)))
        cond = self.find_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def click_site_name_popup_cancel_button(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BUTTON_CANCEL)
        cond = self.is_element_not_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def click_error_popup_Ok_button(self):
        self.click_element(Locators.POPUP_ERROR + "/*" + Locators.BUTTON_Ok)
        cond = self.wait.until_not(EC.presence_of_element_located((By.XPATH, Locators.POPUP_ERROR)))
        return True if cond else False

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
