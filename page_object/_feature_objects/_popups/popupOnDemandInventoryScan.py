
from _base_page.base_actions import BaseActions


class OnDemandInventoryScanPopup(BaseActions):

    BODY = "//span[text()='On demand inventory scan'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    BUTTON_START_NOW = BODY + "/*//span[text()='Start Now']/ancestor::div[contains(@class,'RibbonBarButton')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(OnDemandInventoryScanPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(OnDemandInventoryScanPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("On Demand Inventory Scan")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(OnDemandInventoryScanPopup.BODY)
        self._wait_for_element_not_present(OnDemandInventoryScanPopup.BODY)

    def click_button_start_now(self):
        self._click_element(OnDemandInventoryScanPopup.BUTTON_START_NOW)

    def click_system_button_close(self):
        self._click_system_button_close(OnDemandInventoryScanPopup.BODY)








