
from _base_page.base_actions import BaseActions


class Popup(BaseActions):

    def _set_popup(self, locator):
        body = "//span[text()='" + locator + "']/ancestor::div[contains(@id,'WRP')]"
        return body

    def _get_popup(self):
        body = self._set_popup(name)
        # print "Popup: ", body
        return body