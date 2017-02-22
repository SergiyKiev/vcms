
from _base_page.base_actions import BaseActions


class WeightDisplayPopup(BaseActions):

    BODY = "//span[text()='Weight Display'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(WeightDisplayPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(WeightDisplayPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Imperial Metric")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(WeightDisplayPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(WeightDisplayPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(WeightDisplayPopup.BODY)








