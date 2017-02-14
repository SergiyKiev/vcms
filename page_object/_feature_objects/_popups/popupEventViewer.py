
from _base_page.base_actions import BaseActions


class EventViewerPopup(BaseActions):

    BODY = "//span[text()='Event Viewer']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    TABLE_HEADER_TYPE = TABLE_HEADER + "/*//span[contains(text(),'Type')]"
    TABLE_HEADER_SIZE = TABLE_HEADER + "/*//span[contains(text(),'Size')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"


    def check_popup_is_present(self):
        cond = self._is_element_present(EventViewerPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EventViewerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Event Viewer")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(EventViewerPopup.BODY)
        self.wait_for_element_not_present(EventViewerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(EventViewerPopup.BODY)
        self.wait_for_element_not_present(EventViewerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(EventViewerPopup.BODY)
        self.wait_for_element_not_present(EventViewerPopup.BODY)

    def click_label_in_left_side_tree(self, label):
        elem = EventViewerPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + label + "']"
        self._click_element(elem)
        self.wait_for_element_selected(elem + EventViewerPopup.ELEMENT_LABEL)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(EventViewerPopup.LEFT_SIDE_TREE)

    def check_text_is_in_list_view(self, text):
        cond = self._is_element_present(EventViewerPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False

    def select_device_in_table(self, name):
        self.wait_for_element_present(EventViewerPopup.TABLE_ROW)
        row = EventViewerPopup.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)




