
from _base_page.base_actions import BaseActions


class AreYouSurePopup(BaseActions):

    # PAGE_BODY = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"
    ARE_YOU_SURE = "Are you sure?"

    def _set_popup(self, locator):
        body = "//span[text()='" + locator + "']/ancestor::div[contains(@id,'WRP')]"
        return body

    def _get_popup(self):
        body = self._set_popup(self.ARE_YOU_SURE)
        # print "Popup: ", body
        return body

    def click_button_ok(self):
        self._click_button_ok(self._get_popup())
        # self._click_button_ok(self.PAGE_BODY)

    def click_system_button_close(self):
       self._click_system_button_close(self._get_popup())
       # self._click_system_button_close(self.PAGE_BODY)

    def click_button_cancel(self):
        self._click_button_cancel(self._get_popup())
        # self._click_button_cancel(self.PAGE_BODY)

    def click_button_no(self):
        self._click_button_no(self._get_popup())
        # self._click_button_no(self.PAGE_BODY)

    def click_button_yes(self):
        self._click_button_yes(self._get_popup())
        # self._click_button_yes(self.PAGE_BODY)

    def check_popup_is_present(self):
        cond = self._is_element_present(self._get_popup())
        # cond = self._is_element_present(self.PAGE_BODY)
        return True if cond else False