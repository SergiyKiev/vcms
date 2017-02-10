
from _base_page.base_actions import BaseActions


class SelectDashboardPopup(BaseActions):

    BODY = "//span[text()='Select Dashboard']/ancestor::div[contains(@id,'WRP')]"
    _LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    _TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(SelectDashboardPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SelectDashboardPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Select Dashboard")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(SelectDashboardPopup.BODY)
        self.wait_for_element_not_present(SelectDashboardPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(SelectDashboardPopup.BODY)
        self.wait_for_element_not_present(SelectDashboardPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SelectDashboardPopup.BODY)
        self.wait_for_element_not_present(SelectDashboardPopup.BODY)







