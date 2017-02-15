
from _base_page.base_actions import BaseActions


class MaintenanceWindowsPage(BaseActions):

    PAGE_HEADER = "//span[text()='Maintenance Windows']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_START = TABLE_HEADER + "/*//span[contains(text(),'Start')]"
    HEADER_LENGTH = TABLE_HEADER + "/*//span[contains(text(),'Length')]"
    HEADER_RECURRENCE = TABLE_HEADER + "/*//span[contains(text(),'Recurrence')]"
    HEADER_DAYS = TABLE_HEADER + "/*//span[contains(text(),'Days')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_NAME = "/td[1]"
    CELL_START = "/td[3]"
    CELL_LENGTH = "/td[5]"
    CELL_RECURRENCE = "/td[7]"
    CELL_DAYS = "/td[9]"

    def check_page_is_present(self):
        cond = self._is_element_present(MaintenanceWindowsPage.PAGE_HEADER)
        return True if cond else False

    def check_maintenance_window_is_present(self, name):
        row = MaintenanceWindowsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(MaintenanceWindowsPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Maintenance Windows")
        return True if cond else False

    def select_maintenance_window_in_table(self, name):
        row = MaintenanceWindowsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)







