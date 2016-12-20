from base import Page
from constants import *
from settings import Settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.common.by import By
# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class LoginPage(Page):

    def check_page_loaded(self):
        #return True if self.driver.find_element_by_xpath(PageConstants.BUTTON_SIGN_IN) else False
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, PageConstants.BUTTON_SIGN_IN)))
        except TimeoutException:
            print "Page is not loaded"
        return True

    def enter_username(self):
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(*Settings.username)

    def enter_password(self):
        self.driver.find_element_by_xpath(PageConstants.FIELD_PASSWORD).send_keys(*Settings.password)

    def click_sign_in_button(self):
        self.driver.find_element_by_xpath(PageConstants.BUTTON_SIGN_IN).click()

    def login(self):
        self.enter_username()
        self.enter_password()
        self.click_sign_in_button()

    def login_with_valid_user(self):
        self.login()
        return HomePage(self.driver)


class HomePage(Page):
    pass

