
from _base_page.base_actions import BaseActions


class InventoryViewPopup(BaseActions):

    # def __init__(self, name=None):
    #     super(Base, self). __init__()
    #     self.device_name = name

    #CONSTANTS
    BODY = "//div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self, name):
        element = "//span[text()='" + name + "']/ancestor::div[contains(@id,'WRP')]"
        cond = self._is_element_present(element)
        # cond = self._is_element_present(InventoryViewPopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(InventoryViewPopup.BODY)

    def click_button_close(self):
        self._click_button_close(InventoryViewPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(InventoryViewPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(InventoryViewPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Inventory")
        return True if cond else False

    def click_label_in_left_side_tree(self, label):
        elem = InventoryViewPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + label + "']"
        self._click_element(elem)
        self.wait_for_element_selected(elem + InventoryViewPopup.ELEMENT_LABEL)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(InventoryViewPopup.LEFT_SIDE_TREE)

    def check_text_is_in_list_view(self, text):
        cond = self._is_element_present(InventoryViewPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False