
from _base_page.base_actions import BaseActions


class SubscriptionHasExpitredPopup(BaseActions):

    BODY = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"

    def click_system_button_close(self):
        self._click_system_button_close(SubscriptionHasExpitredPopup.BODY)
        # self._click_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED + "/*" + Locators.SYS_BTN_CLOSE)
        # self.wait_for_element_not_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)

    # def close_popup(self):
    #     cond = self._is_element_present(SubscriptionHasExpitredPopup.BODY)
    #     if cond:
    #         self._click_system_button_close()
    #     else:
    #         pass


class TermsAndConditionsPopup(BaseActions):

    BODY = "//span[text()='Terms and Conditions']/ancestor::div[contains(@id,'WRP')]"
    BTN_I_AGREE = "//span[text()='I Agree']"
    BTN_I_DO_NOT_AGREE = "//span[text()='I Do Not Agree']"

    def click_button_i_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_AGREE)
        self.wait_for_element_not_present(TermsAndConditionsPopup.BODY)

    def click_button_i_do_not_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_DO_NOT_AGREE)

    def click_system_button_close(self):
        self._click_system_button_close(TermsAndConditionsPopup.BODY)

    def close_popup_if_exists(self):
        cond = self._is_element_present(TermsAndConditionsPopup.BODY)
        if cond:
            self.click_button_i_agree()
        else:
            pass


class AreYouSurePopup(BaseActions):

    BODY = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"

    def click_button_ok(self):
        self._click_button_ok(AreYouSurePopup.BODY)

    def click_system_button_close(self):
       self._click_system_button_close(AreYouSurePopup.BODY)
        # self._click_element(AreYouSurePopup.SYSTEM_BUTTON_CLOSE)
        # self.wait_for_element_not_present(AreYouSurePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(AreYouSurePopup.BODY)

    def click_button_no(self):
        self._click_button_no(AreYouSurePopup.BODY)

    def click_button_yes(self):
        self._click_button_yes(AreYouSurePopup.BODY)

    def check_popup_is_present(self):
        # cond = self.wait_for_element_present(AreYouSurePopup.BODY)
        cond = self._is_element_present(AreYouSurePopup.BODY)
        return True if cond else False


class UnableToRemovePopup(BaseActions):

    BODY =  "//span[text()='Unable to remove']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(UnableToRemovePopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(UnableToRemovePopup.BODY)
        # self.wait_for_element_present(UnableToRemovePopup.BODY)
        # cond1 = self._is_element_present(UnableToRemovePopup.BUTTON_OK)
        # cond2 = self._is_element_present(UnableToRemovePopup.BUTTON_Ok)
        # if cond1:
        #     self._click_element(UnableToRemovePopup.BUTTON_OK)
        # elif cond2:
        #     self._click_element(UnableToRemovePopup.BUTTON_Ok)
        # self.wait_for_element_not_present(UnableToRemovePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(UnableToRemovePopup.BODY)
        # self._click_element(UnableToRemovePopup.SYSTEM_BUTTON_CLOSE)
        # self.wait_for_element_not_present(UnableToRemovePopup.BODY)


class ErrorPopup(BaseActions):

    BODY = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ErrorPopup.BODY)
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ErrorPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(ErrorPopup.BODY)


