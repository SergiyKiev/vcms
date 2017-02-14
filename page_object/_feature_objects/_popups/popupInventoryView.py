from _base_page.base import Base
from _base_page.base_actions import BaseActions
from _base_page.base_elements import BaseElements
from _locators.locators import Locators
from _variables.variables import Variables


class InventoryViewPopup(BaseActions):

    # def __init__(self, name=None):
    #     super(Base, self). __init__()
    #     self.device_name = name

    #CONSTANTS
    BODY = "//div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    BUTTON_ARROW_UP = BODY + BaseElements.BUTTON_ARROW_UP
    BUTTON_ARROW_DOWN = BODY + BaseElements.BUTTON_ARROW_DOWN
    LEFT_SIDE_TREE = BODY + "/*//" + Locators.EL_PADDING_BOX
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_SUBTREE_BOX
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_TREE_BOX
    ICON_HELP = BODY + "/*" + Locators.ICON_HELP
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_NODE_BOX = "/ancestor::div[contains(@class,'RowContainer')]"

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

    def click_item_in_left_side_tree(self, item):
        elem = InventoryViewPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + item + "']"
        self._click_element(elem)
        self.wait_for_element_selected(elem + InventoryViewPopup.ELEMENT_NODE_BOX)

    def expand_all_left_side_trees(self):
        self.wait_for_element_present(InventoryViewPopup.BODY)
        elements = self._find_elements(InventoryViewPopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)

    def check_text_is_in_list_view(self, text):
        cond = self._is_element_present(InventoryViewPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False
