
from _base_page.base_actions import BaseActions
from _base_page.base_elements import BaseElements


class ColumnSetDesignerPopup(BaseActions):
    #CONSTANTS
    BODY = "//span[text()='Column Set Designer']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    BUTTON_ADD = BODY + "/*//span[text()='Add >>']/ancestor::div[contains(@class,'Button')]"
    BUTTON_REMOVE = BODY + "/*//span[text()='<< Remove']/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_UP = BODY + BaseElements.BUTTON_ARROW_UP
    BUTTON_ARROW_DOWN = BODY + BaseElements.BUTTON_ARROW_DOWN
    TEXT_FIELD_NAME = BODY  + "/*//div[2]/input"
    TEXT_FIELD_DESCRIPTION = BODY  + "/*//div[1]/input"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_NODE_BOX = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ColumnSetDesignerPopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ColumnSetDesignerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ColumnSetDesignerPopup.BODY)

    def click_button_add(self, columnname):
        self._click_element(ColumnSetDesignerPopup.BUTTON_ADD)
        self.wait_for_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")

    def click_icon_help(self):
        self._click_icon_help(ColumnSetDesignerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ColumnSetDesignerPopup.BODY)

    def click_system_button_maximize(self):
        self._click_system_button_maximize(ColumnSetDesignerPopup.BODY)

    def enter_text_into_text_field_name(self, columnsetname):
        self._find_element(ColumnSetDesignerPopup.TEXT_FIELD_NAME).send_keys(columnsetname)

    def enter_text_into_text_field_description(self, text):
        self._find_element(ColumnSetDesignerPopup.TEXT_FIELD_DESCRIPTION).send_keys(text)

    def click_column_in_left_side_tree(self, columnname):
        elem = ColumnSetDesignerPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + columnname + "']"
        self._click_element(elem)
        self.wait_for_element_selected(elem + ColumnSetDesignerPopup.ELEMENT_NODE_BOX)

    def expand_all_left_side_trees(self):
        self.wait_for_element_present(ColumnSetDesignerPopup.BODY)
        elements = self._find_elements(ColumnSetDesignerPopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)

    def add_columns_to_list_view(self, columns_list):
        self.expand_all_left_side_trees()
        for columnname in list(columns_list):
            self.scroll_to_element(ColumnSetDesignerPopup.BODY + "/*//span[contains(text(),'" + columnname + "')]")
            self.click_column_in_left_side_tree(columnname)
            self.click_button_add(columnname)

    def check_is_columnname_in_list_view(self, columnname):
        cond = self._is_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")
        return True if cond else False

    def create_columnset(self, columnsetname=None, columns_list=None):
        self.click_system_button_maximize()
        self.enter_text_into_text_field_name(columnsetname)
        self.add_columns_to_list_view(columns_list)
        self.click_button_ok()