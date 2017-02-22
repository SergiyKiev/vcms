
from _base_page.base_actions import BaseActions


class CurrencyPopup(BaseActions):

    BODY = "//span[text()='Currency'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(CurrencyPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(CurrencyPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Currency")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(CurrencyPopup.BODY)
        self._wait_for_element_not_present(CurrencyPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(CurrencyPopup.BODY)
        self._wait_for_element_not_present(CurrencyPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(CurrencyPopup.BODY)








