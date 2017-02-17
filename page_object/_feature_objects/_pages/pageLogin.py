
from _base_page.base_elements import BaseElements
from _feature_objects._pages.pageMain import MainPage
from _feature_objects._popups.popupTermsAndConditions import TermsAndConditionsPopup
from _feature_objects._popups.popupError import ErrorPopup
from _feature_objects._popups.popupSubscriptionHasExpired import *
from _settings.settings import Settings


class LoginPage(BaseActions):

    BODY = "//div[@id='VWG_Body']"
    BUTTON_SIGN_IN = "//span[text()='Sign In']/ancestor::div[contains(@class,'Button')]"
    FIELD_PASSWORD = "//input[@type='password']"
    FIELD_USERNAME = "//input[@type='text']"
    RESET_PASSWORD_LABEL = "//span[text()='Reset Password']/ancestor::div[contains(@class,'LinkLabel-Control')]"

    def login(self):
        try:
            self.check_login_page_loaded()
            terms_and_conditions_popup = TermsAndConditionsPopup(self.driver)
            terms_and_conditions_popup.close_popup_if_exists()
            self.enter_username(Settings.username)
            self.enter_password(Settings.password)
            self.click_sign_in_button()
            cond1 = self._is_element_present(ErrorPopup.BODY)
            cond2 = self._is_element_present(SubscriptionHasExpiredPopup.BODY)
            if cond1:
                elements = self._find_elements(BaseElements._POPUP + "/*//span[contains(@class,'Label-FontData')]")
                print "LOGIN IS FAILED. ERROR MESSAGE: "
                for element in elements:
                    error_text = element.text
                    print error_text
                    self.driver.quit()
            elif cond2:
                subscription_has_expired_popup = SubscriptionHasExpiredPopup(self.driver)
                subscription_has_expired_popup.click_system_button_close()
            self.wait_for_element_present(BaseElements._RIBBON_BAR)
            self.wait_for_element_present(BaseElements._LEFT_MENU)
            self.wait_for_element_not_present(BaseElements.LOADING_SCREEN_VISIBLE)
            return MainPage(self.driver)
        except Exception as e:
            print "LOGIN ERROR: ", e

    def enter_username(self, username = Settings.username):
        self._find_element(LoginPage.FIELD_USERNAME).send_keys(username)

    def enter_password(self, password = Settings.password):
        self._find_element(LoginPage.FIELD_PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        self._click_element(LoginPage.BUTTON_SIGN_IN)

    def check_login_page_loaded(self):
        cond1 = self._is_element_present(LoginPage.BUTTON_SIGN_IN)
        cond2 = self._is_element_present(LoginPage.FIELD_USERNAME)
        cond3 = self._is_element_present(LoginPage.FIELD_PASSWORD)
        return True if cond1 and cond2 and cond3 else False

    def click_icon_help(self):
        self._click_icon_help(LoginPage.BODY)

    def check_help_link_is_correct(self):
        # self._select_help_window()
        cond = self._check_help_frame_header("Sign In")
        return True if cond else False

    def click_reset_password_label(self):
        self._click_element(LoginPage.RESET_PASSWORD_LABEL)



