
from _base_page.base_actions import BaseActions


class ExcludeIPAddressPopup(BaseActions):

    BODY = "//span[text()='Exclude IP Address'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._is_element_present(ExcludeIPAddressPopup.BODY)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(ExcludeIPAddressPopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(ExcludeIPAddressPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ExcludeIPAddressPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ExcludeIPAddressPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ExcludeIPAddressPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclude IP Address")
        return True if cond else False
