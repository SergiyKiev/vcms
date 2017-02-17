
from _base_page.base_actions import BaseActions


class IPAddressPopup(BaseActions):

    BODY = "//span[text()='IP Address']/ancestor::div[contains(@id,'WRP')]"
    FIELD_START = BODY + "/*//div[4]/input"
    FIELD_END = BODY + "/*//div[1]/input"

    def check_popup_is_present(self):
        cond = self._is_element_present(IPAddressPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(IPAddressPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("IP Address")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(IPAddressPopup.BODY)
        self._wait_for_element_not_present(IPAddressPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(IPAddressPopup.BODY)
        self._wait_for_element_not_present(IPAddressPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(IPAddressPopup.BODY)
        self._wait_for_element_not_present(IPAddressPopup.BODY)

    def enter_start_ip_address(self, ipaddress = "0.0.0.0"):
        self._find_element(IPAddressPopup.FIELD_START).send_keys(ipaddress)

    def enter_end_ip_address(self, ipaddress = "1.1.1.1"):
        self._find_element(IPAddressPopup.FIELD_END).send_keys(ipaddress)





