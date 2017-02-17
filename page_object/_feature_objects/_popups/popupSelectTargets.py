
from _base_page.base_actions import BaseActions


class SelectTargetsPopup(BaseActions):

    BODY = "//span[text()='Select Targets']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(SelectTargetsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SelectTargetsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Select Targets")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(SelectTargetsPopup.BODY)
        self.wait_for_element_not_present(SelectTargetsPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(SelectTargetsPopup.BODY)
        self.wait_for_element_not_present(SelectTargetsPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SelectTargetsPopup.BODY)
        self.wait_for_element_not_present(SelectTargetsPopup.BODY)

    def click_button_add_members(self):
        self._click_button_cancel(SelectTargetsPopup.BODY)
        self.wait_for_element_not_present(SelectTargetsPopup.BODY)






