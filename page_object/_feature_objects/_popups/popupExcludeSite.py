
from _base_page.base_actions import BaseActions


class ExcludeSitePopup(BaseActions):

    BODY = "//span[text()='Exclude Site']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._is_element_present(ExcludeSitePopup.BODY)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(ExcludeSitePopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(ExcludeSitePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ExcludeSitePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ExcludeSitePopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ExcludeSitePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclude Site")
        return True if cond else False
