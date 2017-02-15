
from _base_page.base_actions import BaseActions


class InventoryConfigurationPage(BaseActions):

    PAGE_HEADER = "//span[text()='Inventory Configuration']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    SEARCH_FIELD = PAGE_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_INVENTORY_TEMPLATE = TABLE_HEADER + "/*//span[contains(text(),'Inventory')]"
    HEADER_FREQUENCY = TABLE_HEADER + "/*//span[contains(text(),'Frequency')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_INVENTORY_TEMPLATE = "/td[1]"
    CELL_FREQUENCY = "/td[3]"

    def check_page_is_present(self):
        cond = self._is_element_present(InventoryConfigurationPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_search(self):
        self._click_icon_search(InventoryConfigurationPage.PAGE_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(InventoryConfigurationPage.SEARCH_FIELD).send_keys(text)

    def check_inventory_is_present(self, name):
        row = InventoryConfigurationPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(InventoryConfigurationPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Inventory Scan Configuration")
        return True if cond else False

    def select_inventory_in_table(self, name):
        row = InventoryConfigurationPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)




