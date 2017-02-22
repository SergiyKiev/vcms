from _base_page.base_actions import BaseActions


class TermsAndConditionsPopup(BaseActions):
    BODY = "//span[text()='Terms and Conditions'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    BTN_I_AGREE = "//span[text()='I Agree']"
    BTN_I_DO_NOT_AGREE = "//span[text()='I Do Not Agree']"

    def click_button_i_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_AGREE)
        self._wait_for_element_not_present(TermsAndConditionsPopup.BODY)

    def click_button_i_do_not_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_DO_NOT_AGREE)

    def click_system_button_close(self):
        self._click_system_button_close(TermsAndConditionsPopup.BODY)

    def close_popup_if_exists(self):
        cond = self._is_element_present(TermsAndConditionsPopup.BODY)
        if cond:
            self.click_button_i_agree()
