
from _base_page.base_actions import BaseActions


class NewFolderPopup(BaseActions):

    BODY = "//span[text()='New Folder']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(NewFolderPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(NewFolderPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("New Folder")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(NewFolderPopup.BODY)
        self.wait_for_element_not_present(NewFolderPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(NewFolderPopup.BODY)
        self.wait_for_element_not_present(NewFolderPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(NewFolderPopup.BODY)
        self.wait_for_element_not_present(NewFolderPopup.BODY)

    def click_button_add_members(self):
        self._click_button_cancel(NewFolderPopup.BODY)
        self.wait_for_element_not_present(NewFolderPopup.BODY)







