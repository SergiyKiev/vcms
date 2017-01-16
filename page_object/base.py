from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from settings import *
from locators import Locators


class Base(object):

    #CONSTANTS
    FIELD_USERNAME = Locators.FIELD_USERNAME
    FIELD_PASSWORD = Locators.FIELD_PASSWORD
    LOADING_SCREEN_VISIBLE = Locators.LOADING_SCREEN_VISIBLE
    POPUP_CONFIGURATION = Locators.POPUP
    POPUP_SYSTEM_BUTTON_CLOSE = Locators.POPUP + "/*" + Locators.SYS_BTN_CLOSE
    DISABLED = Locators.DISABLED
    SELECTED = Locators.SELECTED
    BUTTON_SIGN_IN = Locators.BTN_SIGN_IN
    # EL_EXPAND_ARROW = Locators.EL_EXPAND_ARROW
    # EL_COLLAPSE_ARROW = Locators.EL_COLLAPSE_ARROW
    # EL_EMPTY_ARROW = Locators.EL_EMPTY_ARROW

    def __init__(self, driver, base_url=Settings.baseUrl):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.timeout_request = 2
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.wait_request = WebDriverWait(self.driver, self.timeout_request)

    def _init_browser(self):
        pass
        # self.driver = webdriver.Chrome()

    def open_page(self):
        self.driver.maximize_window()
        self.driver.get(Settings.baseUrl)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.FIELD_USERNAME)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.FIELD_PASSWORD)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.BUTTON_SIGN_IN)))

    def find_element_self(self, locator):
        try:
            self.wait.until_not(EC.visibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            print locator + " is not found"
            return None

    def find_elements_self(self, locator):
        try:
            # time.sleep(1)
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            return None

    def click_element(self, locator):
        try:
            time.sleep(2)
            elem = self.find_element_self(locator)
            if elem is not None:
                elem.click()
                time.sleep(1)
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
                # print "CLICK " + locator
                return True
        except NoSuchElementException:
            print locator + " is not clickable"
            return False

    def wait_for_element_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is presented"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_elements_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is presented"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_not_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is not presented"
            return True
        except NoSuchElementException:
            # print locator + " is not presented"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_selected(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + self.SELECTED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + self.SELECTED)))
            # print locator + " is selected"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_disabled(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + self.DISABLED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + self.DISABLED)))
            # print locator + " is disabled"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_visible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is visible"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def is_element_present(self, locator):
        try:
            self.wait_request.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_request.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " element is present. True"
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def is_element_not_present(self, locator):
        try:
            self.wait_request.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " element is not present. True"
            return True
        except NoSuchElementException:
            # print locator + " returns True"
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def is_element_selected(self, locator):
        try:
            self.wait_request.until(EC.presence_of_element_located((By.XPATH, locator + self.SELECTED)))
            self.wait_request.until(EC.visibility_of_element_located((By.XPATH, locator + self.SELECTED)))
            # print locator + " element is selected. True"
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def is_element_disabled(self, locator):
        try:
            self.wait_request.until(EC.presence_of_element_located((By.XPATH, locator + self.DISABLED)))
            self.wait_request.until(EC.visibility_of_element_located((By.XPATH, locator + self.DISABLED)))
            # print locator + " element is disabled. True"
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def is_element_visible(self, locator):
        try:
            self.wait_request.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " element is visible. True"
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def is_elements_visible(self, locator):
        try:
            self.wait_request.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            # print locator + " element is visible. True"
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def close_popups(self):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
        cond = self.is_element_present(self.POPUP_CONFIGURATION)
        i = 0
        while i < 10:
            i += 1
            if cond:
                self.click_element(self.POPUP_SYSTEM_BUTTON_CLOSE)
                print "All popups are closed"
                return True
            else:
                pass

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_attribute_value(self, locator, attribute_type = "value"):
        try:
            attribute_value = self.find_element_self(locator).get_attribute(attribute_type)
            # print locator + " has " + attribute_type
            return attribute_value
        except NoSuchElementException:
            print locator + " has no " + attribute_type
            return None

    def hover(self, locator):
        element = self.find_element_self(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # def expand_tree(self, locator):
    #     try:
    #         cond = self.is_element_present(locator + self.EL_EXPAND_ARROW)
    #         if cond:
    #             self.click_element(locator + self.EL_EXPAND_ARROW)
    #             self.wait_for_element_present(locator + self.EL_COLLAPSE_ARROW)
    #         else:
    #             pass
    #     except (NoSuchElementException, TimeoutException):
    #         print "Element not found"
    #
    # def collapse_tree(self, locator):
    #     try:
    #         cond = self.find_element_self(locator + self.EL_COLLAPSE_ARROW)
    #         if cond:
    #             self.click_element(locator + self.EL_COLLAPSE_ARROW)
    #             self.wait_for_element_present(locator + self.EL_EXPAND_ARROW)
    #         else:
    #             pass
    #     except (NoSuchElementException, TimeoutException):
    #         print "Element not found"
    #         # print locator + " is not found"

    def click_button_edit(self, locator):
        try:
            cond1 = self.is_element_present(locator + "/*" + Locators.BTN_EDIT)
            cond2 = self.is_element_present(locator + "/*" + Locators.BTN_EDIT_by_text)
            if cond1:
                self.click_element(locator + "/*" + Locators.BTN_EDIT)
                self.wait_for_element_not_present(locator)
            elif cond2:
                self.click_element(locator + "/*" + Locators.BTN_EDIT_by_text)
                self.wait_for_element_not_present(locator)
        except NoSuchElementException:
                print "Button Edit for " + locator +  " is not found"

    def click_button_ok(self, locator):
        try:
            cond1 = self.is_element_present(locator + "/*" + Locators.BTN_OK)
            cond2 = self.is_element_present(locator + "/*" + Locators.BTN_Ok)
            if cond1:
                self.click_element(locator + "/*" + Locators.BTN_OK)
                self.wait_for_element_not_present(locator)
            elif cond2:
                self.click_element(locator + "/*" + Locators.BTN_Ok)
                self.wait_for_element_not_present(locator)
        except NoSuchElementException:
            print "Button " + locator + "/*" + Locators.BTN_OK + " is not found"
            print "Button " + locator + "/*" + Locators.BTN_Ok + " is not found"

    def click_sytem_button_close(self, locator):
        self.click_element(locator + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(locator)

