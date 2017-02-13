
from _base_page.base_actions import BaseActions


class ModelAliasPopup(BaseActions):

    BODY = "//span[text()='Model Alias']/ancestor::div[contains(@id,'WRP')]"
    _LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    _TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(ModelAliasPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ModelAliasPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Models")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ModelAliasPopup.BODY)
        self.wait_for_element_not_present(ModelAliasPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ModelAliasPopup.BODY)
        self.wait_for_element_not_present(ModelAliasPopup.BODY)







