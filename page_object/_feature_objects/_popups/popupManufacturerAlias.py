
from _base_page.base_actions import BaseActions


class ManufacturerAliasPopup(BaseActions):

    BODY = "//span[text()='Manufacturer Alias']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(ManufacturerAliasPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ManufacturerAliasPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Manufacturers")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ManufacturerAliasPopup.BODY)
        self.wait_for_element_not_present(ManufacturerAliasPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ManufacturerAliasPopup.BODY)
        self.wait_for_element_not_present(ManufacturerAliasPopup.BODY)







