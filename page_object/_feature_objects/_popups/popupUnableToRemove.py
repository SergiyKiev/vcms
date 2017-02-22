
from _base_page.base_actions import BaseActions


class UnableToRemovePopup(BaseActions):

    BODY = "//span[text()='Unable to remove'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(UnableToRemovePopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(UnableToRemovePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(UnableToRemovePopup.BODY)