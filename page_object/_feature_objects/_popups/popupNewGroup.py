
from _base_page.base_actions import BaseActions
from _feature_objects._popups.popupSelectTargets import SelectTargetsPopup


class NewGroupPopup(BaseActions):

    BODY = "//span[text()='New Group']/ancestor::div[contains(@id,'WRP')]"
    BUTTON_ADD_MEMBERS = BODY + "/*//span[text()='Add Members']/ancestor::div[contains(@class,'Button')]"
    _LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    _TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(NewGroupPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(NewGroupPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create a new Group")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(NewGroupPopup.BODY)
        self.wait_for_element_not_present(NewGroupPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(NewGroupPopup.BODY)
        self.wait_for_element_not_present(NewGroupPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(NewGroupPopup.BODY)
        self.wait_for_element_not_present(NewGroupPopup.BODY)

    def click_button_add_members(self):
        self._click_element(NewGroupPopup.BUTTON_ADD_MEMBERS)
        self.wait_for_element_present(SelectTargetsPopup.BODY)







