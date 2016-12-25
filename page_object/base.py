from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from settings import Settings
from locators import Locators

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):

    def __init__(self, driver, base_url=Settings.baseUrl):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self):
        self.driver.get(Settings.baseUrl)

    def find_element(self, locator):
        try:
            self.driver.implicitly_wait(10)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        except (NoSuchElementException , TimeoutException):
            return None
        return self.driver.find_element_by_xpath(locator)

    def click_element(self, locator):
        try:
            elem = self.find_element(locator)
            if elem:
                elem.click()
                self.driver.implicitly_wait(1)
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREE_INVISIBLE)))
        except NoSuchElementException:
            return False
        return True

    def is_element_present(self, locator):
        try:
            # self.driver.implicitly_wait(1)
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def is_element_selected(self, locator):
        # try:
        #     self.wait.until(EC.presence_of_element_located((By.XPATH, locator + Locators.SELECTED)))
        # except NoSuchElementException:
        #     return False
        # return True
        try:
            # self.driver.implicitly_wait(1)
            self.find_element(locator + Locators.SELECTED)
        except NoSuchElementException:
            return False
        return True

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, locator):
        element = self.find_element(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()



