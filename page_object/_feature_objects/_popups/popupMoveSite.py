import time
from _base_page.base_actions import BaseActions


class MoveSitePopup(BaseActions):

    BODY = "//span[text()='Move Site'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(MoveSitePopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(MoveSitePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Move a site or device")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(MoveSitePopup.BODY)
        self._wait_for_element_not_present(MoveSitePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(MoveSitePopup.BODY)
        self._wait_for_element_not_present(MoveSitePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(MoveSitePopup.BODY)







