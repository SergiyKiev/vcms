
from _base_page.base_actions import BaseActions
from _feature_objects._popups.popupConditionEditor import ConditionEditorPopup


class QueryDesignerPopup(BaseActions):

    BODY = "//span[text()='Query Designer']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(QueryDesignerPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(QueryDesignerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Queries")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(QueryDesignerPopup.BODY)
        self._wait_for_element_not_present(QueryDesignerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(QueryDesignerPopup.BODY)
        self._wait_for_element_not_present(QueryDesignerPopup.BODY)

    def click_button_add(self):
        self._click_button_add(QueryDesignerPopup.BODY)
        self._wait_for_element_present(ConditionEditorPopup.BODY)




