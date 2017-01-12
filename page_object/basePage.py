from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from settings import Settings
from locators import Locators
from selenium import webdriver


class BasePage(object):

    def __init__(self, driver, base_url=Settings.baseUrl):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 120
        self.timeout_request = 2
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.wait_request = WebDriverWait(self.driver, self.timeout_request)
        # self.loading_waiter = Locators.LOADING_SCREEN_VISIBLE

    # def open(self):
    #     self.driver.get(Settings.baseUrl)
    #     WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, Locators.BTN_SIGN_IN)))

    def find_element_self(self, locator):
        try:
            # time.sleep(1)
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            print locator + " is not found"
            return None

    def find_elements_self(self, locator):
        try:
            # time.sleep(1)
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            return None

    def click_element(self, locator):
        try:
            elem = self.find_element_self(locator)
            if elem:
                elem.click()
                time.sleep(2)
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
                print "OK"
                return True
        except NoSuchElementException:
            print locator + " is not clickable"
            return False

    def wait_for_element_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is presented"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_elements_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is presented"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_not_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))
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
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + Locators.SELECTED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + Locators.SELECTED)))
            # print locator + " is selected"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_disabled(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + Locators.DISABLED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + Locators.DISABLED)))
            # print locator + " is disabled"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_visible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
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
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))
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
            self.wait_request.until(EC.presence_of_element_located((By.XPATH, locator + Locators.SELECTED)))
            self.wait_request.until(EC.visibility_of_element_located((By.XPATH, locator + Locators.SELECTED)))
            # print locator + " element is selected. True"
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def is_element_disabled(self, locator):
        try:
            self.wait_request.until(EC.presence_of_element_located((By.XPATH, locator + Locators.DISABLED)))
            self.wait_request.until(EC.visibility_of_element_located((By.XPATH, locator + Locators.DISABLED)))
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
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
        cond = self.is_element_present(Locators.POPUP_)
        i = 0
        while i < 10:
            i += 1
            if cond:
                self.click_element(Locators.POPUP_ + "[last()]/*" + Locators.SYS_BTN_CLOSE)
                print "All popups are closed"
                return True
            else:
                pass

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    # def get_attribute_value(self, locator, expected_attribute_value):
    #     try:
    #         region_item = self.find_element_self(locator)
    #         acutual_attribute_value = region_item.get_attribute('value')
    #         print acutual_attribute_value
    #         return True if expected_attribute_value in acutual_attribute_value else False
    #     except TimeoutException:
    #         return False

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



