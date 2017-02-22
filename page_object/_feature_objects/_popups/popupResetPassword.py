
from _base_page.base_actions import BaseActions


class ResetPasswordPopup(BaseActions):

    BODY = "//span[text()='Reset Password'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ResetPasswordPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ResetPasswordPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Reset Password")
        return True if cond else False