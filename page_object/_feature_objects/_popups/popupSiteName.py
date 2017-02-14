
from _base_page.base_actions import BaseActions


class SiteNamePopup(BaseActions):

    BODY = "//span[contains(text(),'Site') and contains(text(),'Name')]/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(SiteNamePopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(SiteNamePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SiteNamePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(SiteNamePopup.BODY)

    def check_popup_is_present(self):
        cond = self._is_element_present(SiteNamePopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SiteNamePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create a site")
        return True if cond else False
