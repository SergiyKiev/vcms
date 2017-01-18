from page_object._settings.settings import Settings
from page_object._locators.locators import Locators
from page_object._feature_objects.popups import TermsAndConditionsPopup, SubscriptionHasExpitredPopup
from pageMain import MainPage


class LoginPage(TermsAndConditionsPopup, SubscriptionHasExpitredPopup):

    def login(self):
        self.check_login_page_loaded()
        TermsAndConditionsPopup.close_popup_if_exists(self)
        self.enter_username(Settings.username)
        self.enter_password(Settings.password)
        self.click_sign_in_button()
        cond1 = self.is_element_present(Locators.POPUP_ERROR)
        cond2 = self.is_element_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        if cond1:
            print Settings.username + " or " +  Settings.password + " are incorrect"
        elif cond2:
            SubscriptionHasExpitredPopup.close_popup(self)
            self.wait_for_element_present(Locators.BTN_EXIT)
        else:
            self.wait_for_element_present(Locators.BTN_EXIT)
        return MainPage(self.driver)

    def enter_username(self, username = Settings.username):
        self.find_element_self(Locators.FIELD_USERNAME).send_keys(username)

    def enter_password(self, password = Settings.password):
        self.find_element_self(Locators.FIELD_PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        self.click_element(Locators.BTN_SIGN_IN)

    def check_login_page_loaded(self):
        cond1 = self.is_element_present(Locators.BTN_SIGN_IN)
        cond2 = self.is_element_present(Locators.FIELD_USERNAME)
        cond3 = self.is_element_present(Locators.FIELD_PASSWORD)
        return True if (cond1 and cond2 and cond3) else False
