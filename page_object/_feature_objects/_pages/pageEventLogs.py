
from _base_page.base_actions import BaseActions



class EventLogsPage(BaseActions):

    PAGE_HEADER = "//span[text()='Event Logs']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    ROW1 = PAGE_HEADER + "//*[contains(@id,'HEADER')]/*//td[1]/following::*[contains(@id,'BODY')]/table/tbody/tr/td[1]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    HEADER_LOG_DATE = TABLE_HEADER + "/*//span[contains(text(),'Log Date')]"
    HEADER_COMPONENT = TABLE_HEADER + "/*//span[contains(text(),'Component')]"
    HEADER_DEVICE_NAME = TABLE_HEADER + "/*//span[contains(text(),'Device Name')]"
    HEADER_MESSAGE = TABLE_HEADER + "/*//span[contains(text(),'Message')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_LOG_DATE = "/td[1]"
    CELL_COMPONENT = "/td[3]"
    CELL_DEVICE_NAME = "/td[5]"
    CELL_IS_MESSAGE = "/td[7]"

    def check_page_is_present(self):
        cond = self._is_element_present(EventLogsPage.PAGE_HEADER)
        return True if cond else False

    def check_event_log_is_present(self, name):
        row = EventLogsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EventLogsPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Logs")
        return True if cond else False

    def select_event_log_in_table(self, name):
        row = EventLogsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)







