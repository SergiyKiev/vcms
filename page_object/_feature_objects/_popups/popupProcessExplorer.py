
from _base_page.base_actions import BaseActions


class ProcessExplorerPopup(BaseActions):

    BODY = "//span[text()='Process Explorer']/ancestor::div[contains(@id,'WRP')]"
    TABS_PANEL = BODY + "/*//div[contains(@id,'VWGScrollable')]/div"
    TAB_PROCESSES = BODY + "/*//span[text()='Processes'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_SERVICES = BODY + "/*//span[text()='Services'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    BUTTON_OPEN = BODY + "/*//span[text()='...']/ancestor::div[contains(@class,'Button')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ProcessExplorerPopup.BODY)
        return True if cond else False

    def check_tabs_panel_is_present(self):
        cond = self._is_element_present(ProcessExplorerPopup.TABS_PANEL)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ProcessExplorerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ProcessExplorerPopup.BODY)

    def click_button_open(self):
        self._click_element(ProcessExplorerPopup.BUTTON_OPEN)

    def click_system_button_close(self):
        self._click_system_button_close(ProcessExplorerPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ProcessExplorerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Process Explorer")
        return True if cond else False

    def click_services_tab(self):
        self._click_element(ProcessExplorerPopup.TAB_SERVICES)
        self._wait_for_element_selected(ProcessExplorerPopup.TAB_SERVICES)

    def click_processes_tab(self):
        self._click_element(ProcessExplorerPopup.TAB_PROCESSES)
        self._wait_for_element_selected(ProcessExplorerPopup.TAB_PROCESSES)
