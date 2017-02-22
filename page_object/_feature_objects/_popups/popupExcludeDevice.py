
from _base_page.base_actions import BaseActions


class ExcludeDevicePopup(BaseActions):

    BODY = "//span[text()='Exclude Device'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._is_element_present(ExcludeDevicePopup.BODY)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(ExcludeDevicePopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(ExcludeDevicePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ExcludeDevicePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ExcludeDevicePopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ExcludeDevicePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclude Device")
        return True if cond else False
