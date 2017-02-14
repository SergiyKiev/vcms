
from _base_page.base_actions import BaseActions


class EndUserAccessPopup(BaseActions):

    BODY = "//span[text()=End User Access']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(EndUserAccessPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EndUserAccessPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("End User Access")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(EndUserAccessPopup.BODY)
        self.wait_for_element_not_present(EndUserAccessPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(EndUserAccessPopup.BODY)
        self.wait_for_element_not_present(EndUserAccessPopup.BODY)







