from _base_page.base_actions import BaseActions


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