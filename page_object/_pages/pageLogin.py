from _settings.settings import Settings
from _locators.locators import Locators
from _feature_objects.popups import TermsAndConditionsPopup, SubscriptionHasExpitredPopup
from pageMain import MainPage
from _feature_objects.ribbonBar import RibbonBar
from _feature_objects.leftSideMenu import LeftSideMenu


class LoginPage(TermsAndConditionsPopup, SubscriptionHasExpitredPopup):

    def login(self):
        try:
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
            else:
                pass
            self.wait_for_element_present(RibbonBar.BUTTON_EXIT)
            self.wait_for_element_present(LeftSideMenu.ICON_HOME)
            return MainPage(self.driver)
        except Exception as e:
            print "Login is not successful " ,e

    def enter_username(self, username = Settings.username):
        self._find_element(Locators.FIELD_USERNAME).send_keys(username)

    def enter_password(self, password = Settings.password):
        self._find_element(Locators.FIELD_PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        self._click_element(Locators.BTN_SIGN_IN)

    def check_login_page_loaded(self):
        cond1 = self.is_element_present(Locators.BTN_SIGN_IN)
        cond2 = self.is_element_present(Locators.FIELD_USERNAME)
        cond3 = self.is_element_present(Locators.FIELD_PASSWORD)
        return True if (cond1 and cond2 and cond3) else False
