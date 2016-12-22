from base_page import Page
from constants import *
from settings import Settings
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.common.by import By
# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class LoginPage(Page):

    def check_page_loaded(self):
        pc = PageConstants
        return True if self.driver.find_element(By.ID, pc.LOADING_ANIMATION_BOX) else False
        # try:
        #     WebDriverWait(self.driver, 60).until(
        #         EC.presence_of_element_located((By.ID, pc.LOADING_ANIMATION_BOX)))
        # except TimeoutException:
        #     print "Page is not loaded"
        # return True

    def enter_username(self):
        pc = PageConstants
        self.text_field_type(pc.FIELD_USERNAME, Settings.username)
        # self.driver.find_element_by_xpath("//input[@type='text']").send_keys(*Settings.username)

    def enter_password(self):
        pc = PageConstants
        self.text_field_type(pc.FIELD_PASSWORD, Settings.password)
        # self.driver.find_element_by_xpath(pc.FIELD_PASSWORD).send_keys(*Settings.password)

    def click_sign_in_button(self):
        pc = PageConstants
        self.button_click(pc.BUTTON_SIGN_IN, pc.BUTTON_EXIT)
        # self.driver.find_element_by_xpath(pc.BUTTON_SIGN_IN).click()

    def login(self):
        self.enter_username()
        self.enter_password()
        self.click_sign_in_button()

    # def login_with_valid_user(self):
    #     self.login()
    #     return HomePage(self.driver)
    #

# class HomePage(Page):
#     pass

