
from _base_page.base_actions import BaseActions


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