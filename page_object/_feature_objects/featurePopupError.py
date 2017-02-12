from _base_page.base_actions import BaseActions


class ErrorPopup(BaseActions):

    BODY = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ErrorPopup.BODY)
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ErrorPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(ErrorPopup.BODY)