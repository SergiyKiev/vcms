
from _base_page.base_actions import BaseActions


class WakeOnLANPopup(BaseActions):

    BODY = "//span[text()='Wake on LAN'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(WakeOnLANPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(WakeOnLANPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Wake Up")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(WakeOnLANPopup.BODY)
        self._wait_for_element_not_present(WakeOnLANPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(WakeOnLANPopup.BODY)








