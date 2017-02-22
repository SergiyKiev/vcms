
from _base_page.base_actions import BaseActions


class WMIExplorerPopup(BaseActions):

    BODY = "//span[text()='WMI Explorer'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(WMIExplorerPopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(WMIExplorerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(WMIExplorerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(WMIExplorerPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(WMIExplorerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Process Explorer")
        return True if cond else False
