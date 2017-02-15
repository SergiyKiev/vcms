
from _base_page.base_actions import BaseActions


class EditFolderPopup(BaseActions):

    BODY = "//span[text()='Edit Folder']/ancestor::div[contains(@id,'WRP')]"
    FIELD_EDIT_FOLDER = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._is_element_present(EditFolderPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EditFolderPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Edit Folder")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(EditFolderPopup.BODY)
        self.wait_for_element_not_present(EditFolderPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(EditFolderPopup.BODY)
        self.wait_for_element_not_present(EditFolderPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(EditFolderPopup.BODY)
        self.wait_for_element_not_present(EditFolderPopup.BODY)

    def enter_text_into_edit_folder_text_field(self, name):
        self._find_element(EditFolderPopup.FIELD_EDIT_FOLDER).send_keys(name)







