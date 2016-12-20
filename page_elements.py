
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from login_page import BasePage

class BaseElement(object):

    def __init__(self, driver):
        self.driver = driver

class PageElements(BaseElement):

    def button (self, locator, condition, driver=None):

        try:
            elem = driver.find_element_by_xpath(locator)
            if elem:
                elem.click()
                self.driver.implicitly_wait(1)
                WebDriverWait(self.driver,60).until(EC.invisibility_of_element_located((By.ID, Locators.LOADING_ANIMATION_BOX)))
                WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, condition)))
        except NoSuchElementException:
            return True

    def text_field (self, locator, text):

        try:
            elem = self.driver.find_element_by_xpath(locator)
            if elem:
                elem.send_keys(text)
                self.driver.implicitly_wait(1)
                WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.ID, Locators.LOADING_ANIMATION_BOX)))
        except NoSuchElementException:
            return True

