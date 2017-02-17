
from _base_page.base_actions import BaseActions


class FileExplorerPopup(BaseActions):

    BODY = "//span[text()='File Explorer']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(FileExplorerPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(FileExplorerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("File Explorer")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(FileExplorerPopup.BODY)
        self._wait_for_element_not_present(FileExplorerPopup.BODY)



