
from _settings.settings import Settings
from _feature_objects.popups import *
from pageMain import MainPage
from _base_page.base_elements import BaseElements



class LoginPage(TermsAndConditionsPopup, SubscriptionHasExpitredPopup, ErrorPopup):

    BUTTON_SIGN_IN = "//span[text()='Sign In']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    FIELD_PASSWORD = "//input[@type='password']"
    FIELD_USERNAME = "//input[@type='text']"

    def login(self):
        try:
            self.check_login_page_loaded()
            TermsAndConditionsPopup.close_popup_if_exists(self)
            self.enter_username(Settings.username)
            self.enter_password(Settings.password)
            self.click_sign_in_button()
            cond1 = self._is_element_present(ErrorPopup.FRAME)
            cond2 = self._is_element_present(SubscriptionHasExpitredPopup.FRAME)
            if cond1:
                print Settings.username + " or " + Settings.password + " are incorrect"
            elif cond2:
                SubscriptionHasExpitredPopup.click_system_button_close(self)
            else:
                pass
            # self.wait_for_element_present(BaseElements._RIBBON_BAR)
            # self.wait_for_elements_present(BaseElements._PANEL)
            return MainPage(self.driver)
        except Exception as e:
            print "Login is not successful ", e

    def enter_username(self, username = Settings.username):
        self._find_element(LoginPage.FIELD_USERNAME).send_keys(username)

    def enter_password(self, password = Settings.password):
        self._find_element(LoginPage.FIELD_PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        self._click_element(LoginPage.BUTTON_SIGN_IN)

    def check_login_page_loaded(self):
        self.wait_for_element_present(BaseElements._LOGIN_PAGE_LOGO)
        cond1 = self._is_element_present(LoginPage.BUTTON_SIGN_IN)
        cond2 = self._is_element_present(LoginPage.FIELD_USERNAME)
        cond3 = self._is_element_present(LoginPage.FIELD_PASSWORD)
        return True if (cond1 and cond2 and cond3) else False
