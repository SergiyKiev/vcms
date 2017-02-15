
from _base_page.base_actions import BaseActions


class NotificationsPage(BaseActions):

    PAGE_HEADER = "//span[text()='Notifications']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"

    def check_page_is_present(self):
        cond = self._is_element_present(NotificationsPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(NotificationsPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Notifications")
        return True if cond else False







