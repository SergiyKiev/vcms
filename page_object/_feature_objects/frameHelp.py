
from _base_page.base_actions import BaseActions
from _locators.locators import Locators

class HelpFrame(BaseActions):

    BODY = "//title[text()='ConsoleOperationGuide']"

    def check_logon_page_help_is_resent(self):
        pass

    def select_help_frame(self):
        self.driver.switch_to_frame(HelpFrame.BODY)
