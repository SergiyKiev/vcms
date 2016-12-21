from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from settings import Settings

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):

    def __init__(self, driver, base_url=Settings.baseUrl):
        self.base_url = base_url
        self.driver = driver

    def open(self):
        self.driver.get(Settings.baseUrl)

    def find_element(self, xpath):
        return self.driver.find_element(xpath)

    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
