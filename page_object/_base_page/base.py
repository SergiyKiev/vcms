
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
        self.timeout_condition = 2
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
        # print "finish waiting"
        # cond = self._is_element_not_present(Base.LOADING_SCREEN_VISIBLE)
        # if cond:
        #     self.logger.debug("PAGE IS UNLOCKED: " + str(cond))

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
            self.logger.error("Page is not loaded: " + str(Settings.baseUrl))
            return Exception
        except Exception as e:
            self.logger.error("Service error: ", str(e))

    def _find_element(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            self.logger.error(str(locator)+ " is not found")
            return None
        except Exception as e:
            self.logger.error("The element " + locator + " is not found\n " + str(e))

    def _find_elements(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            return self.driver.find_elements(By.XPATH, locator)
        except (NoSuchElementException, TimeoutException):
            return None
        except Exception as e:
            self.logger.error("The elements " + locator + " are not found ")
            print e

    '''CUSTOM CLICK METHOD ACTUAL'''
    def _click_element(self, locator):
        try:
            cond = self._wait_for_element_present(locator)
            if cond:
                self.wait_for_action()
                self._find_element(locator).click()
                self.wait_for_action()
                self.logger.debug("Click: " + str(locator))
                # self.logger.info("Click: " + str(locator))
        except NoSuchElementException:
            self.logger.error("METHOD 'Click element' " + locator + " is not found")
        except TimeoutException:
            self.logger.error("Element " + locator + " is not clickable after ", self.timeout_webelement, "seconds")
        except Exception as e:
            self.logger.error("The element " + locator + " is not clickable.\n" + str(e))
    '''CUSTOM CLICK METHOD NOT TEMP'''
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
    #         # print "CLICK METHOD: " + locator + " is not found"
    #         self.logger.error("METHOD 'Click element' " + locator + " is not found")
    #     except TimeoutException:
    #         # print "Element is not clickable after ", self.timeout_loading, "seconds"
    #         self.logger.error("Element " + locator +  " is not clickable after ", self.timeout_webelement, "seconds")
    #     except Exception as e:
    #         # print "The element is not clickable in the reason of ", e
    #         self.logger.error("The element " + locator + " is not clickable.\n" + str(e))

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
            print locator + " is not clickable"
            return False

    def _wait_for_element_present(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            self.logger.error("METHOD 'Wait for element present'. Element was not found after " + str(self.timeout_webelement) + " seconds: " + locator)
            return False
        except Exception as e:
            self.logger.error("METHOD 'Wait for element present' is failed\n" + str(e))

    def _wait_for_elements_present(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            self.wait_webelement.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            self.logger.error("METHOD 'Wait for elements present'. Elements were not found after " + str(self.timeout_webelement) + " seconds:  " + locator)
            return False
        except Exception as e:
            self.logger.error("METHOD 'Wait for elements present' is failed\n", str(e))

    def _wait_for_element_not_present(self, locator):
        try:
            self.wait_webelement.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_webelement.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except NoSuchElementException:
            return True
        except TimeoutException:
            self.logger.error("METHOD 'Wait for element not present'. Element is found after " + str(self.timeout_webelement) + " seconds:  " + locator)
            return False
        except Exception as e:
            self.logger.error("METHOD 'Wait for element not present' is failed\n" + str(e))

    def _wait_for_element_selected(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.SELECTED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.SELECTED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False
        except Exception as e:
            print "Wait for element selected, returns false ", e

    def _wait_for_element_checked(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.CHECKED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.CHECKED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def _wait_for_element_unchecked(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def _wait_for_element_disabled(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.DISABLED)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.DISABLED)))
            return True
        except TimeoutException:
            print locator + " returns False"
            return False

    def _wait_for_left_menu_visible(self, locator):
        try:
            self.wait_webelement.until(EC.presence_of_element_located((By.XPATH, locator + Base.LEFT_MENU_VISIBLE)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator + Base.LEFT_MENU_VISIBLE)))
            return True
        except TimeoutException:
            self.logger.error("Element is not visible: " + str(locator))
            return False

    def _wait_for_element_visible(self, locator):
        try:
            self.wait_loading.until_not(EC.presence_of_all_elements_located((By.XPATH, Base.LOCKED_SCREEN)))
            self.wait_loading.until_not(EC.visibility_of_any_elements_located((By.XPATH, Base.LOCKED_SCREEN)))
            self.wait_webelement.until(EC.visibility_of_element_located((By.XPATH, locator)))
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
        except Exception as e:
            print e
            return False

    def _is_element_not_present(self, locator):
        try:
            self.wait_condition.until_not(EC.presence_of_element_located((By.XPATH, locator)))
            self.wait_condition.until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except NoSuchElementException:
            return True
        except TimeoutException:
            return False
        except Exception as e:
            print e
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

    def _is_element_unchecked(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.UNCHECKED)))
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

    def _is_tree_arrow_present(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.ARROW_EMPTY)))
            self.wait_condition.until(EC.visibility_of_element_located((By.XPATH, locator + Base.ARROW_EMPTY)))
            return False
        except TimeoutException:
            return True

    def _is_left_menu_visible(self, locator):
        try:
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.LEFT_MENU_VISIBLE)))
            self.wait_condition.until(EC.presence_of_element_located((By.XPATH, locator + Base.LEFT_MENU_VISIBLE)))
            return True
        except TimeoutException:
            return False

    def _get_text(self, locator):
        try:
            get = self._find_element(locator).text
            return get
        except Exception as e:
            print "Error finding the text of the element " , e

    def send_keys_and_enter(self, locator, value):
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
        except (NoSuchElementException, TimeoutException):
            print "Element not found"

    def scroll_list_down(self, step):
        try:
            element = self._find_element("//div[contains(@id,'VWGVLSC_')]")
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, step)
        except Exception as e:
            print "error scrolling down web element", e

    def scroll_to_element(self, locator):
        try:
            # self._wait_for_element_present(locator)
            element = self._find_element(locator)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        except Exception as e:
            print "error scrolling into view ", e
