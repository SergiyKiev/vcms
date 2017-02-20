
from _base_page.base_actions import BaseActions
from _feature_objects._popups.popupSelectTargets import SelectTargetsPopup
from _feature_objects._popups.popupUserConfiguration import UserConfigurationPopup


class AdminAccountsPopup(BaseActions):

    BODY = "//span[text()='Admin Accounts']/ancestor::div[contains(@id,'WRP')]"
    BUTTON_ADD_MEMBERS = BODY + "/*//span[text()='Add Members']/ancestor::div[contains(@class,'Button')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    FIELD_GROUP_NAME = BODY + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_popup_is_present(self):
        cond = self._is_element_present(AdminAccountsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(AdminAccountsPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(AdminAccountsPopup.BODY)
        self._wait_for_element_not_present(AdminAccountsPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(AdminAccountsPopup.BODY)
        self._wait_for_element_not_present(AdminAccountsPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(AdminAccountsPopup.BODY)
        self._wait_for_element_not_present(AdminAccountsPopup.BODY)

    def click_button_add_members(self):
        self._click_element(AdminAccountsPopup.BUTTON_ADD_MEMBERS)
        self._wait_for_element_present(SelectTargetsPopup.BODY)

    def enter_text_into_group_name_text_field(self, text = None):
        self._find_element(AdminAccountsPopup.FIELD_GROUP_NAME).send_keys(text)

    def click_button_add(self):
        self._click_button_add(AdminAccountsPopup.BODY)
        self._wait_for_element_present(UserConfigurationPopup.BODY)







