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
        self.timeout = 60
        self.wait = WebDriverWait(self.driver, self.timeout)

    # def open(self):
    #     self.driver.get(Settings.baseUrl)
    #     WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, Locators.BUTTON_SIGN_IN)))

    def find_element(self, locator):
        try:
            # time.sleep(1)
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element_by_xpath(locator)
        except (NoSuchElementException, TimeoutException):
            return None

    def click_element(self, locator):
        elem = self.find_element(locator)
        if elem:
            elem.click()
            time.sleep(1)
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            return True
        else:
            return False

    def is_element_present(self, locator):
        try:
            # time.sleep(1)
            # self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def is_element_not_present(self, locator):
        try:
            # time.sleep(1)
            # self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            WebDriverWait(self.driver, 1).until_not(EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return True

    def is_element_selected(self, locator):
        try:
            # time.sleep(1)
            # self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREEN_VISIBLE)))
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, locator + Locators.TEXT_SELECTED)))
            return True
        except TimeoutException:
            return False

    def close_popups(self):
        cond = self.is_element_present(Locators.POPUP)
        i = 0
        while i < 10:
            i += 1
            if cond:
                self.click_element(Locators.POPUP + "[last()]/*" + Locators.BUTTON_SYSTEM_CLOSE)
                return True
            else: break
        return True

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, locator):
        element = self.find_element(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()



