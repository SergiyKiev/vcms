
from _base_page.base_actions import BaseActions


class SubscriptionsPopup(BaseActions):

    BODY = "//span[text()='Subscriptions']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(SubscriptionsPopup.BODY)
        return self._find_element(SubscriptionsPopup.BODY) if cond else None

    def click_icon_help(self):
        self._click_icon_help(SubscriptionsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Subscriptions")
        return True if cond else False