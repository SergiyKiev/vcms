
from _base_page.base_actions import BaseActions


class ViewLogsPopup(BaseActions):

    BODY = "//span[contians(text(),'View Logs')]/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ViewLogsPopup.BODY)
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ViewLogsPopup.BODY)
        self.wait_for_element_not_present(ViewLogsPopup.BODY)







