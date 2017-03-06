import time
import logging

from _settings.settings import Settings
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base(object):

    '''CONSTANTS'''
    LOCKED_SCREEN = "//div[contains(@id,'VWG_Loading')][contains(@style,'display: block')]"
    LOADING_ANIMATION_VISIBLE = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block')]"
    LOADING_SCREEN_VISIBLE = "//div[@id='VWG_LoadingScreen'][contains(@style,'display: block')]"
    ANIMATED_LOADER = "//img[contains(@src,'Images.animated_loader')]"
    LEFT_MENU_VISIBLE = "[contains(@style,'(0px, 0px, 0px)')]"
    DISABLED = "[contains(@class,'Disabled')]"
    SELECTED = "[contains(@class,'Selected')]"
    CHECKED = "[contains(@style,'CheckBox1')]"
    UNCHECKED = "[contains(@style,'CheckBox0')]"
    LOGIN_PAGE_LOGO = "//img[contains(@src,'Images.CMS-Login')]"
    ARROW_EXPAND = "/div[contains(@style,'LTR1.gif')]"
    ARROW_COLLAPSE = "/div[contains(@style,'LTR0.gif')]"
    ARROW_EMPTY = "/div[contains(@style,'TreeViewEmpty')]"

    def __init__(self, driver, base_url=Settings.baseUrl, log_name="test_logs_base"):
        self.driver = driver
        self.base_url = base_url
        # self.log_name = log_name
        self.timeout_loading = 100
        self.timeout_condition = 1
        self.timeout_webelement = 10
        self.wait_webelement = WebDriverWait(self.driver, self.timeout_webelement)
        self.wait_condition = WebDriverWait(self.driver, self.timeout_condition)
        self.wait_loading = WebDriverWait(self.driver, self.timeout_loading)
        # self.logger = logging.getLogger(self.log_name)
        # self.console = logging.StreamHandler()
        # self.logger.addHandler(self.console)
        # logging.basicConfig(filename='E:\\python\\vcms\\vcms\\page_object\\_test_logs\\' + str(self.log_name) + '.log',
        #                     level=logging.INFO, format='%(asctime)-24s [%(levelname)-3s] %(message)s')  # KIPROV HOME

    '''LOGS'''
    # logging.basicConfig(filename='D:\\python\\vcms\\vcms\\page_object\\_test_suites\\test_logs.log',
    #                     level=logging.INFO, format='%(asctime)s [%(levelname)-3s] %(message)s') # KIPROV WORK
    logging.basicConfig(filename='E:\\python\\vcms\\vcms\\page_object\\_test_logs\\test_logs.log',
                        level=logging.INFO, format='%(asctime)-24s [%(levelname)-3s] %(message)s')  # KIPROV HOME
    logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    logger.addHandler(console)

    '''Wait for action ACTUAL'''
    def wait_for_screen_is_unlocked(self):
        i = 0
        imax = self.timeout_loading
        while i <= imax:
            i += 1
            time.sleep(0.3)
            self.wait_loading.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOCKED_SCREEN)))
            self.wait_loading.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOCKED_SCREEN)))
            # time.sleep(0.3)
            # event = self.driver.execute_script("return jQuery.active == 0")
            # if event:
            cond = self._is_element_not_present(Base.LOADING_SCREEN_VISIBLE)
            if cond:
                break
            elif i > imax:
                self.logger.error("Timeout exception for wait for screen is unlocked")
            else:
                time.sleep(0.5)
                print "waiting for screen is unlocked..." + str(i) + " times"

    def wait_for_loading_is_finished(self):
        time.sleep(2)
        i = 0
        imax = self.timeout_condition
        while i <= imax:
            self.wait_loading.until_not(EC.presence_of_element_located((By.XPATH, Base.ANIMATED_LOADER)))
            x = self.driver.execute_script("return jQuery.active == 0")
            if x:
                break
            elif i > imax:
                self.logger.exception("Timeout exception for wait for loading is finished")
            else:
                i += 1
                time.sleep(1)

    def open_page(self):
        try:
            self.driver.maximize_window()
            self.driver.get(Settings.baseUrl)
            self.logger.info("Instance is: " + str(Settings.baseUrl) + "\n")
            self.wait_loading.until(EC.presence_of_element_located((By.XPATH, Base.LOGIN_PAGE_LOGO)))
            cond = self._find_element(Base.LOGIN_PAGE_LOGO)
            if cond:
                return True
            else:
                title = self.get_title()
                self.logger.critical(str(title))
                self.driver.quit()
        except TimeoutException:
            self.logger.exception("Page is not loaded: " + str(Settings.baseUrl))
            return None
        except Exception as e:
            self.logger.exception("Service error: ", str(e))

    def _find_element(self, locator):
        try:
            self._wait_for_element_present(locator)
            element = self.driver.find_element(By.XPATH, locator)
            self.logger.debug("FIND ELEMENT. Element " + locator + " is found")
            return element
        except (NoSuchElementException, TimeoutException):
            self.logger.exception("FIND ELEMENT. Element " + locator + " is NOT found\n")
            title = self.get_title()
            if title == "Service Unavailable":
                self.logger.critical(str(title))
                self.driver.quit()
            return None
        except Exception as e:
            self.logger.exception("FIND ELEMENT. The element " + locator + " is NOT found\n. Message: " + str(e))
            return None

    def _find_elements(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            self.logger.error("FIND ELEMENT. Element " + locator + " is NOT found")
            return None
        except Exception as e:
            self.logger.exception("FIND ELEMENT. The element " + locator + " is NOT found\n. Message: " + str(e))

    def _click_element(self, locator):
        try:
            self.wait_for_screen_is_unlocked()
            # cond = self._is_element_present(Base.LOADING_ANIMATION_VISIBLE)
            # if cond:
            #     self.wait_for_screen_is_unlocked()
            #     print "SCREEN IS UNLOCKED..."
            element = self._find_element(locator)
            element.click()
            self.logger.debug("CLICK: " + str(locator))
            # print "CLICK: " + str(locator)
            # self.wait_for_screen_is_unlocked()
        except WebDriverException as e:
            if 'Other element would receive the click' in e.msg:
                print "SCREEN IS LOCKED..."
                time.sleep(0.5)
                self.wait_for_screen_is_unlocked()
                element = self._find_element(locator)
                element.click()
                # self.wait_for_screen_is_unlocked()
                # self.driver.execute_script('$("{sel}").click()'.format(sel=locator))
            else:
                self.logger.exception("CLICK: Element is NOT CLICKABLE.\n")
                print e.message
                raise
            # i = 0
            # imax = 20
            # while i <= imax:
            #     i += 1
            #     if i > imax:
            #         self.logger.exception(
            #             "CLICK: Element " + locator + " is NOT CLICKABLE after " + str(i) + " attempts.\n")
            #     elif 'Other element would receive the click' in e.msg:
            #         print "SCREEN IS LOCKED..." + str(i)
            #         self.wait_for_screen_is_unlocked()
            #         element = self._find_element(locator)
            #         element.click()
            #     # elif 'Element is not clickable at point' in e.msg:
            #     #     print "SCREEN IS LOCKED...."
            #     #     self.wait_for_screen_is_unlocked()
            #     #     self.driver.execute_script('$("{sel}").click()'.format(sel=locator))
            #     else:
            #         self.logger.exception("CLICK: Element is NOT CLICKABLE.\n")
            #         print e.message
        # except Exception as e:
        #     self.logger.exception("CLICK: Element is NOT CLICKABLE.\n")
        #     print e.message

    def _hover_and_click_element(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator)))
            element = self._find_element(locator)
            if element is not None:
                # time.sleep(15)
                event = 'click'  # or 'hover' or any other
                script = "$(arguments[0]).trigger('" + event + "')"
                self.driver.execute_script(script, element)
                self.driver.execute_script("arguments[0].click();", element)
                print "script is executed"
                self.wait_for_screen_is_unlocked()
                return True
        except NoSuchElementException:
            print locator + " is NOT clickable"
            return False

    def _wait_for_element_present(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.logger.debug("WAITING. Element " + locator + " is present.")
            return True
        except (NoSuchElementException, TimeoutException):
            self.logger.error(
                "WAITING. Element " + locator + " is NOT found after " + str(self.timeout_webelement) + " seconds")
            return False
        # except Exception as e:
        #     self.logger.exception("METHOD 'Wait for element present' is failed\n" + str(e))

    def _wait_for_elements_present(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            self.logger.debug("WAITING. Elements " + locator + " are present.")
            return True
        except (NoSuchElementException, TimeoutException):
            self.logger.error(
                "WAITING. Elements " + locator + " are not found after " + str(self.timeout_webelement) + " seconds")
            return False

    def _wait_for_element_not_present(self, locator):
        try:
            self.wait_webelement.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_webelement.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            self.logger.debug("WAITING. Element " + locator + " is NOT present.")
            return True
        except NoSuchElementException:
            self.logger.exception("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "WAITING. Element " + locator + " is present after " + str(self.timeout_webelement) + " seconds")
            return False
            # except Exception as e:
        #     self.logger.exception("METHOD 'Wait for element not present' is failed\n" + str(e))

    def _wait_for_element_selected(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.logger.debug("WAITING. Element " + locator + " is selected.")
            return True
        except NoSuchElementException:
            self.logger.exception("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.exception(
                "WAITING. Element " + locator + " is NOT selected after " + str(self.timeout_webelement) + " seconds")
            return False

    def _wait_for_element_checked(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.logger.debug("Element " + locator + " is checked.")
            return True
        except NoSuchElementException:
            self.logger.exception("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "Element " + locator + " is NOT checked after " + str(self.timeout_webelement) + " seconds")
            return False

    def _wait_for_element_unchecked(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            self.logger.debug("Element " + locator + " is unchecked.")
            return True
        except NoSuchElementException:
            self.logger.exception("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "Element " + locator + " is NOT unchecked after " + str(self.timeout_webelement) + " seconds")
            return False

    def _wait_for_element_disabled(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.logger.debug("WAITING. Element " + locator + " is disabled.")
            return True
        except NoSuchElementException:
            self.logger.exception("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "WAITING. Element " + locator + " is NOT disabled after " + str(self.timeout_webelement) + " seconds")
            return False

    def _wait_for_element_unabled(self, locator):
        try:
            self.wait_webelement.until_not(EC.presence_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.wait_webelement.until_not(EC.visibility_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.logger.debug("WAITING. Element " + locator + " is unabled.")
            return True
        except NoSuchElementException:
            self.logger.exception("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "WAITING. Element " + locator + " is NOT unabled after " + str(self.timeout_webelement) + " seconds")
            return False

    def _is_element_present(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.logger.debug("CHECK. Element " + locator + " is present.")
            return True
        except NoSuchElementException:
            self.logger.exception("CHECK. Element " + locator + " is NOT found.")
            return None
        except TimeoutException:
            self.logger.debug(
                "CHECK. Element " + locator + "' is NOT present after " + str(self.timeout_condition) + " seconds")
            return False

    def _is_element_not_present(self, locator):
        try:
            self.wait_condition.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_condition.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            self.logger.debug("CHECK. Element " + locator + "' is NOT present.")
            return True
        except NoSuchElementException:
            self.logger.exception("CHECK. Element " + locator + " is NOT found.")
            return None
        except TimeoutException:
            self.logger.debug(
                "CHECK. Element " + locator + " is present after " + str(self.timeout_condition) + " seconds")
            return False

    def _is_element_selected(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.logger.debug("CHECK. Element " + locator + " is selected.")
            return True
        except TimeoutException:
            self.logger.debug("CHECK. Element " + locator + " is NOT selected.")
            return False

    def _is_element_checked(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.logger.debug("CHECK. Element " + locator + " is checked.")
            return True
        except TimeoutException:
            self.logger.debug("CHECK. Element " + locator + " is NOT checked.")
            return False

    def _is_element_unchecked(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            self.logger.debug("CHECK. Element " + locator + " is unchecked.")
            return True
        except TimeoutException:
            self.logger.debug("CHECK. Element " + locator + " is NOT unchecked.")
            return False

    def _is_element_disabled(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.logger.debug("CHECK. Element " + locator + " is present.")
            return True
        except TimeoutException:
            self.logger.debug("CHECK. Element " + locator + " is NOT disabled.")
            return False

    def _is_tree_arrow_present(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.ARROW_EMPTY)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.ARROW_EMPTY)))
            self.logger.debug("CHECK. Element " + locator + " is present.")
            return True
        except TimeoutException:
            self.logger.debug("CHECK. Element " + locator + "' is NOT present.")
            return False

    def _get_text(self, locator):
        try:
            actual_text = self._find_element(locator).text
            return actual_text
        except Exception as e:
            print "Error finding the text of the element " , e

    def _send_keys_and_enter(self, locator, text):
        try:
            field = self._find_element(locator)
            field.send_keys(text)
            # time.sleep(0.5)
            field.send_keys(Keys.ENTER)
        except Exception as e:
            print "Error ", e

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def _get_attribute_value(self, locator, attribute_type ="value"):
        try:
            attribute_value = self._find_element(locator).get_attribute(attribute_type)
            return attribute_value
        except NoSuchElementException:
            print locator + " has no " + attribute_type
            return None

    def hover(self, locator):
        element = self._find_element(locator)
        self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def scroll_list_to_top(self):
        try:
            element = self._find_element("//div[contains(@id,'VWGVLSC_')]")
            self.driver.execute_script("arguments[0].scrollTop = 0", element)
            self._wait_for_element_present("//table[contains(@id,'VWGVL_')]/*//tr[1][@data-vwgindex='0']")
        except Exception as e:
            self.logger.exception("SCROLL. Error on scroll to top method.\n Message " + str(e))

    def scroll_list_down(self, step):
        try:
            element = self._find_element("//div[contains(@id,'VWGVLSC_')]")
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, step)
        except Exception as e:
            self.logger.exception("SCROLL. Error on scroll list down method.\n Message " + str(e))

    def scroll_to_element(self, locator):
        try:
            # self._wait_for_element_present(locator)
            element = self._find_element(locator)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        except Exception as e:
            self.logger.exception("SCROLL. Error on scroll to element method.\n Message " + str(e))
