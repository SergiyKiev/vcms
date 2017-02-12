from _base_page.base_actions import BaseActions


class RemoveDevicesPopup(BaseActions):

    BODY = "//span[text()='Remove Devices']/ancestor::div[contains(@id,'WRP')]"
    CHECKBOX_KEEP_HIST_INFORM = BODY + "//span[contains(text(),'Keep')][@class='CheckBox-Label']/" \
                                       "ancestor::tr/td[contains(@id,'TRG')]"

    def click_button_ok(self):
        self._click_button_ok(RemoveDevicesPopup.BODY)

    def click_system_button_close(self):
       self._click_system_button_close(RemoveDevicesPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(RemoveDevicesPopup.BODY)

    def check_popup_is_present(self):
        cond = self._is_element_present(RemoveDevicesPopup.BODY)
        return True if cond else False

    def check_keep_historical_information_check_box(self):
        self.wait_for_element_checked(RemoveDevicesPopup.BODY)
        self._click_element(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
        self.wait_for_element_checked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)

    def uncheck_keep_historical_information_check_box(self):
        self.wait_for_element_present(RemoveDevicesPopup.BODY)
        self._click_element(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
        self.wait_for_element_unchecked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)