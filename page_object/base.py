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
        self.timeout = 60
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self):
        self.driver.get(Settings.baseUrl)

    def find_element(self, locator):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        return self.driver.find_element_by_xpath(locator)
        #self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        # return self.wait.until(EC._find_element(By.XPATH, *locator))

        # try:
        #     elem = self.driver.find_element(By.XPATH, locator)
        #     if elem != True:
        #         self.wait.until(EC.presence_of_element_located(locator))
        # except NoSuchElementException:
        #     return self.driver.find_element(locator)

    def click_element(self, locator):
        try:
            elem = self.driver.find_element_by_xpath(locator)
            if elem:
                elem.click()
                self.driver.implicitly_wait(1)
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.LOADING_SCREE_INVISIBLE)))
            return True
        except(NoSuchElementException):
            return False

    def is_element_selected(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + Locators.SELECTED)))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        return True if self.driver.find_element_by_xpath(locator) else False

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()



