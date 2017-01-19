
import time
from _locators.locators import Locators
from _settings.settings import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base(object):

    #CONSTANTS
    FIELD_USERNAME = Locators.FIELD_USERNAME
    FIELD_PASSWORD = Locators.FIELD_PASSWORD
    LOADING_SCREEN_VISIBLE = Locators.LOADING_SCREEN_VISIBLE
    LOADING_SCREEN_VISIBLE_NEW = (By.XPATH, "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block']")
    POPUP_CONFIGURATION = Locators.POPUP
    POPUP_SYSTEM_BUTTON_CLOSE = Locators.POPUP + "/*" + Locators.SYS_BTN_CLOSE
    DISABLED = Locators.DISABLED
    SELECTED = Locators.SELECTED
    BUTTON_SIGN_IN = Locators.BTN_SIGN_IN
    EL_EXPAND_ARROW = Locators.EL_EXPAND_ARROW
    EL_COLLAPSE_ARROW = Locators.EL_COLLAPSE_ARROW
    EL_EMPTY_ARROW = Locators.EL_EMPTY_ARROW

    def __init__(self, driver, base_url=Settings.baseUrl):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 120
        self.timeout_request = 3
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.wait_request = WebDriverWait(self.driver, self.timeout_request)

    def _init_browser(self):
        pass
        # self.driver = webdriver.Chrome()

    def open_page(self):
        try:
            self.driver.maximize_window()
            self.driver.get(Settings.baseUrl)
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.FIELD_USERNAME)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.FIELD_PASSWORD)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.BUTTON_SIGN_IN)))
        except TimeoutException:
            print "Page is not loaded"

    def find_element_self(self, locator):
        try:
            time.sleep(1)
            self.wait.until_not(EC.visibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            print locator + " is not found"
            return None

    def find_elements_self(self, locator):
        try:
            time.sleep(1)
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            return None

    def click_element(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elem = self.find_element_self(locator)
            if elem is not None:
                elem.click()
                time.sleep(1)
                self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
                # print "CLICK " + locator
                return True
        except NoSuchElementException:
            print locator + " is not clickable"
            return False

    def hover_and_click_element(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elem = self.find_element_self(locator)
            if elem is not None:
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(elem).perform()
                time.sleep(1)
                actionChains.click(elem).perform()
                time.sleep(1)
                self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
                return True
        except NoSuchElementException:
            print locator + " is not clickable"
            return False

    def wait_for_element_present(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
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
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
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
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + self.SELECTED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + self.SELECTED)))
            # print locator + " is selected"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_disabled(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + self.DISABLED)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator + self.DISABLED)))
            # print locator + " is disabled"
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_visible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
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
        self.wait.until(EC.invisibility_of_element_located(self.LOADING_SCREEN_VISIBLE_NEW))
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
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def expand_tree(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator + Locators.ARROW_EXPAND )))
            element = self.find_element_self(locator)
            if element is not None:
                self.driver.execute_script("arguments[0].click();", element)
                # self.wait.until_not(EC.presence_of_element_located((By.XPATH, locator + Locators.ARROW_EXPAND)))
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print "Element not found"

    def scroll_up_drop_down_list(self):
        try:
            self.wait_for_element_present("//div[contains(@id,'VWGVLSC_')]")
            element = self.find_element_self("//div[contains(@id,'VWGVLSC_')]")
            self.hover("//table[contains(@id,'VWGVL_')]/*//tr")
            self.driver.execute_script("arguments[0].scrollTop = 0", element)
            self.wait_for_element_present("//table[contains(@id,'VWGVL_')]/*//tr[1][@data-vwgindex='0']")
            # self.find_element_self("//table[contains(@id,'VWGVL_')]/*//tr")
            # self.hover("//table[contains(@id,'VWGVL_')]/*//tr")
            # self.driver.execute_script("arguments[0].scrollTop = argument[1];", element, 150)
        except (NoSuchElementException, TimeoutException):
            print "Element not found"

    def scroll_down_drop_down_list(self, step):
        try:
            self.wait_for_element_present("//div[contains(@id,'VWGVLSC_')]")
            element1 = self.find_element_self("//table[contains(@id,'VWGVL_')]/*//tr")
            element = self.find_element_self("//div[contains(@id,'VWGVLSC_')]")
            self.hover("//table[contains(@id,'VWGVL_')]/*//tr")
            self.driver.execute_script("arguments[0].scrollTop = step", element, step)
        except Exception as e:
            print "error scrolling down web element", e


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

    # def click_button_edit(self, locator):
    #     try:
    #         cond1 = self.is_element_present(locator + "/*" + Locators.BTN_EDIT)
    #         cond2 = self.is_element_present(locator + "/*" + Locators.BTN_EDIT_by_text)
    #         if cond1:
    #             self.click_element(locator + "/*" + Locators.BTN_EDIT)
    #             self.wait_for_element_not_present(locator)
    #         elif cond2:
    #             self.click_element(locator + "/*" + Locators.BTN_EDIT_by_text)
    #             self.wait_for_element_not_present(locator)
    #     except NoSuchElementException:
    #             print "Button Edit for " + locator +  " is not found"

    # def click_ok(self, locator):
    #     try:
    #         cond1 = self.is_element_present(locator + "/*" + Locators.BTN_OK)
    #         cond2 = self.is_element_present(locator + "/*" + Locators.BTN_Ok)
    #         if cond1:
    #             self.click_element(locator + "/*" + Locators.BTN_OK)
    #             self.wait_for_element_not_present(locator)
    #         elif cond2:
    #             self.click_element(locator + "/*" + Locators.BTN_Ok)
    #             self.wait_for_element_not_present(locator)
    #     except NoSuchElementException:
    #         print "Button " + locator + "/*" + Locators.BTN_OK + " is not found"
    #         print "Button " + locator + "/*" + Locators.BTN_Ok + " is not found"
    #
    # def click_sytem_button_close(self, locator):
    #     self.click_element(locator + "/*" + Locators.SYS_BTN_CLOSE)
    #     self.wait_for_element_not_present(locator)

