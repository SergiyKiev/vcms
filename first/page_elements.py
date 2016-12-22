
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import Constants
from base import Page


class PageElements(Page):

    def button (self, locator, condition):
        driver = self.driver
        try:
            elem = driver.find_element_by_xpath(locator)
            if elem:
                elem.click()
                driver.implicitly_wait(1)
                WebDriverWait(driver,60).until(EC.invisibility_of_element_located((By.ID, Constants.loadingAnimationBox)))
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, condition)))
        except NoSuchElementException:
            return True

    def text_field (self, locator, text):
        driver = self.driver
        try:
            elem = driver.find_element_by_xpath(locator)
            if elem:
                elem.send_keys(text)
                driver.implicitly_wait(1)
                WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.ID, Constants.loadingAnimationBox)))
        except NoSuchElementException:
            return True

