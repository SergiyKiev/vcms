
import time
from _locators.locators import Locators
from _settings.settings import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Base(object):

    # CONSTANTS
    FIELD_USERNAME = "//input[@type='text']"
    FIELD_PASSWORD = "//input[@type='password']"
    BUTTON_SIGN_IN = "//span[text()='Sign In']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    # LOADING_SCREEN_VISIBLE = Locators.LOADING_SCREEN_VISIBLE
    LOADING_SCREEN_VISIBLE = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block']"
    POPUP = "//div[contains(@id,'WRP')][last()]"
    SYSTEM_BUTTON_CLOSE = "//div[contains(@id,'WRP')][last()]/*//div[@title='Close']"
    DISABLED = "[contains(@class,'Disabled')]"
    SELECTED = "[contains(@class,'Selected')]"
    ARROW_EXPAND = "div[contains(@style,'LTR1.gif')]"
    ARROW_COLLAPSE = "div[contains(@style,'LTR0.gif')]"
    ARROW_EMPTY = "div[contains(@style,'TreeViewEmpty')]"

    def __init__(self, driver, base_url=Settings.baseUrl):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 120
        self.timeout_request = 3
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.wait_request = WebDriverWait(self.driver, self.timeout_request)

    def open_page(self):
        try:
            self.driver.maximize_window()
            self.driver.get(Settings.baseUrl)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Base.FIELD_USERNAME)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, Base.FIELD_PASSWORD)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, Base.BUTTON_SIGN_IN)))
        except TimeoutException:
            print "Page is not loaded"
        except Exception as e:
            print "The reason is ", e

    def _find_element(self, locator):
        try:
            time.sleep(1)
            self.wait.until_not(EC.visibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            print locator + " is not found"
            return None
        except Exception as e:
            print "The element is not found in the reason of ", e

    def _find_elements(self, locator):
        try:
            time.sleep(1)
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            return None

    def click_element(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elem = self._find_element(locator)
            if elem is not None:
                elem.click()
                time.sleep(1)
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
                # print "CLICK " + locator
                return True
        except NoSuchElementException:
            print locator + " is not clickable"
            return False
        except Exception as e:
            print "The element is not clickable in the reason of ", e

    def hover_and_click_element(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elem = self._find_element(locator)
            if elem is not None:
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(elem).perform()
                time.sleep(1)
                actionChains.click(elem).perform()
                time.sleep(1)
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
                return True
        except NoSuchElementException:
            print locator + " is not clickable"
            return False

    def wait_for_element_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is presented"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False
        except Exception as e:
            print "After wait fol element present, false ", e

    def wait_for_elements_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            # print locator + " is presented"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_not_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
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
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + self.SELECTED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + self.SELECTED)))
            # print locator + " is selected"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_disabled(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + self.DISABLED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + self.DISABLED)))
            # print locator + " is disabled"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_visible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
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
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
        cond = self.is_element_present(Base.POPUP)
        i = 0
        while i < 10:
            i += 1
            if cond:
                self.click_element(Base.SYSTEM_BUTTON_CLOSE)
                print "All popups are closed"
                return True
            else:
                pass

    def get_text(self, locator):
        try:
            get = self._find_element(locator)
            return get.text()
        except Exception as e:
            print "Error finding the text of the element " , e

    def send_keys_and_enter(self, locator, value):
        try:
            field = self._find_element(locator)
            field.self.send_keys(value)
            time.sleep(1)
            field.self.send_keys(Keys.ENTER)
        except Exception as e:
            print "Error ", e

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_attribute_value(self, locator, attribute_type = "value"):
        try:
            attribute_value = self._find_element(locator).get_attribute(attribute_type)
            # attribute_value = self._find_element(locator).self.get_attribute(attribute_type)
            # print locator + " has " + attribute_type
            return attribute_value
        except NoSuchElementException:
            print locator + " has no " + attribute_type
            return None

    def hover(self, locator):
        element = self._find_element(locator)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def expand_tree(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + Locators.ARROW_EXPAND )))
            element = self._find_element(locator)
            if element is not None:
                self.driver.execute_script("arguments[0].click();", element)
                # self.wait.until_not(EC.presence_of_element_located((By.XPATH, locator + Locators.ARROW_EXPAND)))
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Element not found"

    def scroll_list_to_top(self):
        try:
            self.wait_for_element_present("//div[contains(@id,'VWGVLSC_')]")
            element = self._find_element("//div[contains(@id,'VWGVLSC_')]")
            # self.hover("//table[contains(@id,'VWGVL_')]/*//tr")
            self.driver.execute_script("arguments[0].scrollTop = 0", element)
            self.wait_for_element_present("//table[contains(@id,'VWGVL_')]/*//tr[1][@data-vwgindex='0']")
            # self._find_element("//table[contains(@id,'VWGVL_')]/*//tr")
            # self.hover("//table[contains(@id,'VWGVL_')]/*//tr")
            # self.driver.execute_script("arguments[0].scrollTop = argument[1];", element, 150)
        except (NoSuchElementException, TimeoutException):
            print "Element not found"

    def scroll_list_down(self, step):
        try:
            self.wait_for_element_present("//div[contains(@id,'VWGVLSC_')]")
            element1 = self._find_element("//table[contains(@id,'VWGVL_')]/*//tr")
            element = self._find_element("//div[contains(@id,'VWGVLSC_')]")
            # self.hover("//table[contains(@id,'VWGVL_')]/*//tr")
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, step)
        except Exception as e:
            print "error scrolling down web element", e

    def scroll_to_element(self, locator):
        try:
            self.wait_for_element_present(locator)
            element = self._find_element(locator)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        except Exception as e:
            print "error scrolling into view ", e


    # def collapse_tree(self, locator):
    #     try:
    #         cond = self._find_element(locator + self.EL_COLLAPSE_ARROW)
    #         if cond:
    #             self.click_element(locator + self.EL_COLLAPSE_ARROW)
    #             self.wait_for_element_present(locator + self.EL_EXPAND_ARROW)
    #         else:
    #             pass
    #     except (NoSuchElementException, TimeoutException):
    #         print "Element not found"
    #         # print locator + " is not found"

