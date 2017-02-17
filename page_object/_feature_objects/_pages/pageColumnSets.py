import time
from _base_page.base_actions import BaseActions
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class ColumnSetsPage(BaseActions):

    PAGE_HEADER = "//span[text()='Column Sets']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    HEADER_IS_DEFAULT = TABLE_HEADER + "/*//span[contains(text(),'Is Default')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_DESCRIPTION = TABLE_HEADER + "/*//span[contains(text(),'Description')]"
    HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_IS_DEFAULT = "/td[1]" #NOT CORRECT
    CELL_NAME = "/td[3]"
    CELL_DESCRIPTION = "/td[5]"
    CELL_IS_COLUMNS = "/td[7]"

    def check_page_is_present(self):
        cond = self._is_element_present(ColumnSetsPage.PAGE_HEADER)
        return True if cond else False

    def check_column_set_is_present(self, name):
        row = ColumnSetsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ColumnSetsPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Column Sets")
        return True if cond else False

    def select_column_set_in_table(self, name):
        row = ColumnSetsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)







