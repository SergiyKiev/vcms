
from _base_page.base_actions import BaseActions


class SubscriptionHasExpiredPopup(BaseActions):

    BODY = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"

    def click_system_button_close(self):
        self._click_system_button_close(SubscriptionHasExpiredPopup.BODY)

    # def close_popup(self):
    #     cond = self._is_element_present(SubscriptionHasExpitredPopup.BODY)
    #     if cond:
    #         self._click_system_button_close()
    #     else:
    #         pass


