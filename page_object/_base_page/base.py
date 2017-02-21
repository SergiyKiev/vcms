
import time
from _settings.settings import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select


class Base(object):

    # logging.basicConfig(filename='D:\\python\\vcms\\vcms\\page_object\\_test_suites\\test_logs.log',
    #                     level=logging.INFO, format='%(asctime)-3s %(levelname)-3s %(message)s')
    logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    logger.addHandler(console)

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
    ARROW_EXPAND = "/*//div[contains(@style,'LTR1.gif')]"
    ARROW_COLLAPSE = "/*//div[contains(@style,'LTR0.gif')]"
    ARROW_EMPTY = "/*//div[contains(@style,'TreeViewEmpty')]"

    def __init__(self, driver, base_url=Settings.baseUrl):
        self.driver = driver
        self.base_url = base_url
        self.timeout_loading = 120
        self.timeout_condition = 1.5
        self.timeout_webelement = 10
        self.wait_webelement = WebDriverWait(self.driver, self.timeout_webelement)
        self.wait_condition = WebDriverWait(self.driver, self.timeout_condition)
        self.wait_loading = WebDriverWait(self.driver, self.timeout_loading)

    # def wait_for_action(self):
    #     try:
    #         i = 0
    #         while i <= 5:
    #             i += 1
    #             time.sleep(0.1)
    #             element = self.driver.find_element_by_xpath(Base.LOADING_ANIMATION_VISIBLE)
    #             print element
    #             if element is not None:
    #                 if i > 1:
    #                     print "Loading process is in progress ", element, str(i)
    #                 self.wait_loading.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOCKED_SCREEN)))
    #                 # self.wait_loading.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOCKED_SCREEN)))
    #             elif i == 5:
    #                 print "Loading process is stuck in progress after " + str(i * self.timeout_loading) + " seconds"
    #                 break
    #             else:
    #                 print "Loading process is finished"
    #                 break
    #     except Exception as e:
    #             print "System loading error\n" + str(e)

    '''Wait for action ACTUAL'''
    def wait_for_action(self):
        # time.sleep(0.2)
        # print "waiting..."
        self.wait_loading.until_not(EC.presence_of_element_located((By.XPATH, Base.LOADING_ANIMATION_VISIBLE )))
        self.wait_loading.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOCKED_SCREEN)))
        # time.sleep(0.1)
        self.wait_loading.until_not(EC.presence_of_element_located((By.XPATH, Base.LOADING_ANIMATION_VISIBLE)))
        self.wait_loading.until_not(EC.presence_of_element_located((By.XPATH, Base.LOADING_SCREEN_VISIBLE)))
        # self.wait_loading.until_not(EC.presence_of_element_located(
        #     (By.XPATH,"//*[@id='VWG_MaskedModalWindowBox'][contains(@style,'display: block')]")))
        # print "finish waiting"
        # cond = self._is_element_present(Base.LOADING_SCREEN_VISIBLE)
        # if cond is not True:
        #     self.logger.info("PAGE IS ACTIVE")
        # else:
        #     self.logger.critical("PAGE IS LOCKED: " + str(cond))

    def wait_for_not_loading(self):
        # time.sleep(0.3)
        self.wait_loading.until_not(EC.presence_of_element_located((By.XPATH, Base.ANIMATED_LOADER)))

    def open_page(self):
        try:
            self.driver.maximize_window()
            self.driver.get(Settings.baseUrl)
            self.logger.info("Instance is: " + str(Settings.baseUrl) + "\n")
            self.wait_loading.until(EC.presence_of_element_located((By.XPATH, Base.LOGIN_PAGE_LOGO)))
        except TimeoutException:
            self.logger.critical("Page is not loaded: " + str(Settings.baseUrl))
            return Exception
        except Exception as e:
            self.logger.critical("Service error: ", str(e))

    def _find_element(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            self.logger.error("FIND ELEMENT. Element " + locator + " is NOT found")
            return None
        except Exception as e:
            self.logger.critical("FIND ELEMENT. The element " + locator + " is NOT found\n. Message: " + str(e))
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
            self.logger.critical("FIND ELEMENT. The element " + locator + " is NOT found\n. Message: " + str(e))

    '''CUSTOM CLICK METHOD ACTUAL'''
    def _click_element(self, locator):
        try:
            # cond = self._is_element_present(locator)
            # if cond:
            self.wait_for_action()
            element = self._find_element(locator)
            if element:
                # self.wait_loading.until_not(
                #     EC.visibility_of_element_located((
                #         By.XPATH,"//*[@id='VWG_MaskedModalWindowBox'][contains(@style,'display: block')]")))
                # self.wait_webelement.until_not(
                #     EC.presence_of_element_located((
                #         By.XPATH,"//*[@id='VWG_MaskedModalWindowBox'][contains(@style,'display: block')]")))
                element.click()
                self.logger.debug("CLICK: " + str(locator))
                # self.logger.info("CLICK: " + str(locator))
            self.wait_for_action()
        except (NoSuchElementException, TimeoutException):
            self.logger.critical(
                "CLICK: Element " + locator + " is NOT found after " + str(self.timeout_webelement) + " seconds")
        except Exception as e:
            self.logger.critical("CLICK: Element " + locator + " is NOT clickable.\n" + str(e))
    #Click method (not actual)
    # def _click_element(self, locator):
    #     try:
    #         cond = self._wait_for_element_present(locator)
    #         if cond:
    #             self.wait_for_action()
    #             button = self._find_element(locator)
    #             button.click()
    #             self.wait_for_action()
    #             self.logger.debug("Click: " + str(locator))
    #             self.logger.info("Click: " + str(locator))
    #             # print "\n" + "CLICK:  ", locator
    #     except NoSuchElementException:
    #         # print "CLICK METHOD: " + locator + " is NOT found"
    #         self.logger.critical("METHOD 'Click element' " + locator + " is NOT found")
    #     except TimeoutException:
    #         # print "Element is not clickable after ", self.timeout_loading, "seconds"
    #         self.logger.critical("Element " + locator +  " is NOT clickable after ", self.timeout_webelement, "seconds")
    #     except Exception as e:
    #         # print "The element is not clickable in the reason of ", e
    #         self.logger.critical("The element " + locator + " is NOT clickable.\n" + str(e))

    def _hover_and_click_element(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator)))
            elem = self._find_element(locator)
            if elem is not None:
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(elem).perform()
                time.sleep(1)
                actionChains.click(elem).perform()
                time.sleep(1)
                self.wait_webelement.until(EC.invisibility_of_element_located((By.XPATH, Base.LOADING_ANIMATION_VISIBLE)))
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
        #     self.logger.critical("METHOD 'Wait for element present' is failed\n" + str(e))

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
            self.logger.critical("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "WAITING. Element " + locator + " is present after " + str(self.timeout_webelement) + " seconds")
            return False
            # except Exception as e:
        #     self.logger.critical("METHOD 'Wait for element not present' is failed\n" + str(e))

    def _wait_for_element_selected(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.logger.debug("WAITING. Element " + locator + " is selected.")
            return True
        except NoSuchElementException:
            self.logger.critical("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "WAITING. Element " + locator + " is NOT selected after " + str(self.timeout_webelement) + " seconds")
            return False

    def _wait_for_element_checked(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.logger.debug("Element " + locator + " is checked.")
            return True
        except NoSuchElementException:
            self.logger.critical("WAITING. Element " + locator + " is NOT found.")
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
            self.logger.critical("WAITING. Element " + locator + " is NOT found.")
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
            self.logger.critical("WAITING. Element " + locator + " is NOT found.")
            return False
        except TimeoutException:
            self.logger.error(
                "WAITING. Element " + locator + " is NOT disabled after " + str(self.timeout_webelement) + " seconds")
            return False

    def _is_element_present(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.logger.debug("CHECK. Element " + locator + " is present.")
            return True
        except NoSuchElementException:
            self.logger.critical("CHECK. Element " + locator + " is NOT found.")
            return None
        except TimeoutException:
            self.logger.debug(
                "CHECK. Element " + locator + " is NOT present after " + str(self.timeout_condition) + " seconds")
            return False

    def _is_element_not_present(self, locator):
        try:
            self.wait_condition.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_condition.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            self.logger.debug("CHECK. Element " + locator + " is NOT present.")
            return True
        except NoSuchElementException:
            self.logger.critical("CHECK. Element " + locator + " is NOT found.")
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
            self.logger.debug("CHECK. Element " + locator + " is NOT present.")
            return False

    def _get_text(self, locator):
        try:
            get = self._find_element(locator).text
            return get
        except Exception as e:
            print "Error finding the text of the element " , e

    def _send_keys_and_enter(self, locator, value):
        try:
            field = self._find_element(locator)
            field.self.send_keys(value)
            time.sleep(0.5)
            field.self.send_keys(Keys.ENTER)
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
            self.logger.critical("Error on scroll to top method.\n Message " + str(e))

    def scroll_list_down(self, step):
        try:
            element = self._find_element("//div[contains(@id,'VWGVLSC_')]")
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, step)
        except Exception as e:
            self.logger.critical("Error on scroll list down method.\n Message " + str(e))

    def scroll_to_element(self, locator):
        try:
            # self._wait_for_element_present(locator)
            element = self._find_element(locator)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        except Exception as e:
            self.logger.critical("Error on scroll to element method.\n Message " + str(e))
