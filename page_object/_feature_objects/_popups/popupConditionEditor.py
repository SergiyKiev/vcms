
from _base_page.base_actions import BaseActions


class ConditionEditorPopup(BaseActions):

    BODY = "//span[text()='Condition Editor']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(ConditionEditorPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ConditionEditorPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create a Query")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ConditionEditorPopup.BODY)
        self._wait_for_element_not_present(ConditionEditorPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ConditionEditorPopup.BODY)
        self._wait_for_element_not_present(ConditionEditorPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ConditionEditorPopup.BODY)
        self._wait_for_element_not_present(ConditionEditorPopup.BODY)







