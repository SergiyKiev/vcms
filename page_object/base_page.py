from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import *
from settings import Settings


# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, driver, base_url=Settings.baseUrl):
        self.base_url = base_url
        self.driver = driver
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, PageConstants.LOADING_ANIMATION_BOX)))

    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, PageConstants.LOADING_ANIMATION_BOX)))

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
