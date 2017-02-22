from _base_page.base_actions import BaseActions

class ConnectingPopup(BaseActions):

    CONNECTING = "//span[text()='Connecting....'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    PING = "//span[text()='Ping....'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def _check_popup_is_present(self, name):
        global BODY
        NAME = "//span[text()='" + str(name) + "'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
        PARTIAL_NAME = "//span[contains(text(),'" + name + "')][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
        full_name = self._is_element_present(NAME)
        partial_name = self._is_element_present(PARTIAL_NAME)
        if full_name:
            BODY = NAME
        elif partial_name:
            BODY = PARTIAL_NAME
        cond = self._is_element_present(BODY)
        return str(BODY) if cond else None

    def check_popup_is_present(self):
        cond = self._check_popup_is_present("Connecting")
        return True if cond is not None else False

    def _get_popup(self):
        name = self._check_popup_is_present("Connecting")
        return str(name) if name is not None else None

    def click_button_close(self):
        self._click_button_close(self._get_popup())
        self._wait_for_element_not_present(self._get_popup())



