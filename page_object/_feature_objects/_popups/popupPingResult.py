
from _base_page.base_actions import BaseActions


class PingResultPopup(BaseActions):

    BODY = "//span[text()='Ping Result'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(PingResultPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(PingResultPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Ping Result")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(PingResultPopup.BODY)




