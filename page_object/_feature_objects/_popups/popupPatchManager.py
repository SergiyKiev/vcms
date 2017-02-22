
from _base_page.base_actions import BaseActions


class PatchManagerPopup(BaseActions):
    #CONSTANTS
    BODY = "//span[text()='Patch Manager'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    SEARCH_FIELD = BODY + "/*//input"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(PatchManagerPopup.BODY)
        return True if cond else False

    def check_device_name_is_present(self, device_name):
        cond = self._is_element_present(PatchManagerPopup.BODY + "/*//span[text()='" + device_name + "']")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(PatchManagerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(PatchManagerPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(PatchManagerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Software Updates")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(PatchManagerPopup.BODY)

    def enter_text_into_search_text_field(self, text):
        self._find_element(PatchManagerPopup.SEARCH_FIELD).send_keys(text)

    def click_label_in_left_side_tree(self, label):
        elem = PatchManagerPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + label + "']"
        self._click_element(elem)
        self._wait_for_element_selected(elem + PatchManagerPopup.ELEMENT_LABEL)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(PatchManagerPopup.LEFT_SIDE_TREE)
