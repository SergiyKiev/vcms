
from _feature_objects.feature_popup import *
from _feature_objects.feature_screen import *
from _feature_objects.feature_left_menu import *
from _test_suites._variables.variables import Variables


class EndUserAccessLoginPage(BaseActions):


    BODY = "//div[@id='VWG_Body']"
    BUTTON_SIGN_IN = "//span[text()='Sign In']/ancestor::div[contains(@class,'Button')]"
    FIELD_PASSWORD = "//input[@type='password']"
    FIELD_DEVICENAME = "//input[@type='text']"

    def check_page_is_loaded(self):
        try:
            cond = self._is_element_present(ErrorPopup.BODY)
            cond1 = self._is_element_present(self.BUTTON_SIGN_IN)
            cond2 = self._is_element_present(self.FIELD_DEVICENAME)
            cond3 = self._is_element_present(self.FIELD_PASSWORD)
            if cond:
                elements = self._find_elements(BaseElements.POPUP + "/*//span[contains(@class,'Label-FontData')]")
                self.logger.error("PAGE IS NOT OPENED. Error massage: ")
                for element in elements:
                    error_text = element.text
                    self.logger.error(str(error_text) + "\n")
                    self.driver.quit()
            elif cond1 and cond2 and cond3:
                self.logger.info("End User Access Login page is presented\n")
                return EndUserAccessLoginPage(self.driver)
            else:
                return False
        except Exception as e:
            self.logger.exception("END USER ACCESS LOGIN PAGE IS NOT LOADED\n")
            print e

    def click_icon_help(self):
        self._click_icon_help(self.BODY)
