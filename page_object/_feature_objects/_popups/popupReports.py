
from _base_page.base_actions import BaseActions


class ReportsPopup(BaseActions):

    BODY = "//span[text()='Reports']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ReportsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ReportsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Reports")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ReportsPopup.BODY)
        self.wait_for_element_not_present(ReportsPopup.BODY)







