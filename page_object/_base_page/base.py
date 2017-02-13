
import time
from _settings.settings import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from _base_page.base_elements import *
from selenium.webdriver.support import select



class Base(object):

    '''CONSTANTS'''
    # LOGIN_PAGE_LOGO = "//img[contains(@src,'Images.CMS-Login')]"
    LOADING_VISIBLE = "//div[contains(@id,'VWG_Loading')][contains(@style,'display: block')]"
    LOADING_ANIMATION_VISIBLE = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block')]"
    LOADING_SCREEN_VISIBLE = "//div[@id='VWG_LoadingScreen'][contains(@style,'display: block')]"
    LEFT_MENU_VISIBLE = "[contains(@style,'(0px, 0px, 0px)')]"
    DISABLED = "[contains(@class,'Disabled')]"
    SELECTED = "[contains(@class,'Selected')]"
    CHECKED = "[contains(@style,'CheckBox1')]"
    UNCHECKED = "[contains(@style,'CheckBox0')]"
    ARROW_EXPAND = "/div[contains(@style,'LTR1.gif')]"
    ARROW_COLLAPSE = "/div[contains(@style,'LTR0.gif')]"
    ARROW_EMPTY = "/div[contains(@style,'TreeViewEmpty')]"


    def __init__(self, driver, base_url=Settings.baseUrl):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 120
        self.timeout_condition = 2
        self.wait_general = WebDriverWait(self.driver, self.timeout)
        self.wait_condition = WebDriverWait(self.driver, self.timeout_condition)

    def open_page(self):
        try:
            self.driver.maximize_window()
            self.driver.get(Settings.baseUrl)
            self.wait_for_element_present(BaseElements._LOGIN_PAGE_LOGO)
        except TimeoutException:
            print "Page is not loaded"
        except Exception as e:
            print "The reason is ", e

    def _find_element(self, locator):
        try:
            # # time.sleep(0.5)
            # # self.wait.until_not(EC.presence_of_element_located((By.XPATH, Base.LOADING_ANIMATION_VISIBLE)))
            # # self.wait.until_not(EC.presence_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            print locator + " is not found"
            return None
        except Exception as e:
            print "The element is not found ", e

    def _find_elements(self, locator):
        try:
            # time.sleep(0.5)
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait_general.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            return None
        except Exception as e:
            print "The elements are not found ", e

    def _click_element(self, locator):
        try:
            element = self._find_element(locator)
            if element is not None:
                # print "\n" + "CLICK:  ", locator
                time.sleep(0.8)
                self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
                self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
                self.wait_general.until(EC.element_to_be_clickable((By.XPATH, locator)))
                element.click()
                time.sleep(0.8)
                self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
                self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
                return True
        except NoSuchElementException:
            print locator + " is not found"
            return False
        except TimeoutException:
            print "Loading process timeout after clicking. Timeout set: ", self.timeout, "seconds"
            return False
        except Exception as e:
            print "The element is not clickable in the reason of ", e
            return False

    def hover_and_click_element(self, locator):
        try:
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator)))
            elem = self._find_element(locator)
            if elem is not None:
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(elem).perform()
                time.sleep(1)
                actionChains.click(elem).perform()
                time.sleep(1)
                self.wait_general.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_ANIMATION_VISIBLE)))
                return True
        except NoSuchElementException:
            print locator + " is not clickable"
            return False

    def wait_for_element_present(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            print "Element was not found after " +  str(self.timeout) + " seconds:  " + locator
            return False
        except Exception as e:
            print "Wait for element present, returns false ", e

    def wait_for_elements_present(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait_general.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_not_present(self, locator):
        try:
            # time.sleep(1)
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_general.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            # print locator + " is not presented"
            return True
        except NoSuchElementException:
            # print locator + " is not presented"
            return True
        except TimeoutException:
            print "Method returns false, " + locator + " is present"
            return False

    def wait_for_element_selected(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator + Base.SELECTED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_checked(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator + Base.CHECKED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_unchecked(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False



    def wait_for_element_disabled(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator + Base.DISABLED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_menu_visible(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator + Base.LEFT_MENU_VISIBLE)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator + Base.LEFT_MENU_VISIBLE)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def wait_for_element_visible(self, locator):
        try:
            self.wait_general.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOADING_VISIBLE)))
            self.wait_general.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def _is_element_present(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def _is_tree_arrow_present(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.ARROW_EMPTY)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.ARROW_EMPTY)))
            return False
        except TimeoutException:
            return True

    def _is_element_not_present(self, locator):
        try:
            self.wait_condition.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_condition.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except NoSuchElementException:
            return True
        except TimeoutException:
            # print locator + " returns False"
            return False

    def _is_element_selected(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.SELECTED)))
            return True
        except TimeoutException:
            return False

    def _is_element_checked(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.CHECKED)))
            return True
        except TimeoutException:
            return False

    def _is_element_disabled(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.DISABLED)))
            return True
        except TimeoutException:
            return False

    def _is_element_visible(self, locator):
        try:
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def _is_left_menu_visible(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.LEFT_MENU_VISIBLE)))
            return True
        except TimeoutException:
            return False

    def _is_elements_visible(self, locator):
        try:
            self.wait_condition.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # def _close_popups(self):
    #     cond = self._is_element_present(Base.POPUP)
    #     i = 0
    #     while i < 10:
    #         i += 1
    #         if cond:
    #             self._click_element(Base.TOP_SYSTEM_BUTTON_CLOSE)
    #             print "All popups are closed"
    #             return True
    #         else:
    #             pass

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
        self.wait_general.until(EC.presence_of_element_located((By.XPATH, locator)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def _expand_tree(self, locator):
        try:
            element = self._find_element(locator + Base.ARROW_EXPAND)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print "Massage: ", e

    def _collaps_tree(self, locator):
        try:
            element = self._find_element(locator + Base.ARROW_COLLAPSE)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print "Massage: ", e

    def scroll_list_to_top(self):
        try:
            self.wait_for_element_present("//div[contains(@id,'VWGVLSC_')]")
            element = self._find_element("//div[contains(@id,'VWGVLSC_')]")
            self.driver.execute_script("arguments[0].scrollTop = 0", element)
            self.wait_for_element_present("//table[contains(@id,'VWGVL_')]/*//tr[1][@data-vwgindex='0']")
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
