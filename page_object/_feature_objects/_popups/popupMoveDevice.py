
from _base_page.base_actions import BaseActions


class MoveDevicePopup(BaseActions):

    BODY = "//span[text()='Move Device']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"


    def check_popup_is_present(self):
        cond = self._is_element_present(MoveDevicePopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(MoveDevicePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Move a site or device")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(MoveDevicePopup.BODY)
        self._wait_for_element_not_present(MoveDevicePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(MoveDevicePopup.BODY)
        self._wait_for_element_not_present(MoveDevicePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(MoveDevicePopup.BODY)
        self._wait_for_element_not_present(MoveDevicePopup.BODY)

    def click_label_in_left_side_tree(self, label):
        elem = MoveDevicePopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + label + "']"
        self._click_element(elem)
        self._wait_for_element_selected(elem + MoveDevicePopup.ELEMENT_LABEL)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(MoveDevicePopup.LEFT_SIDE_TREE)
        # self._wait_for_element_present(MoveDevicePopup.PAGE_BODY)
        # elements = self._find_elements(MoveDevicePopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        # for element in elements:
        #     self.driver.execute_script("arguments[0].click();", element)

    def check_text_is_in_list_view(self, text):
        cond = self._is_element_present(MoveDevicePopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False

    def select_device_in_table(self, name):
        self._wait_for_element_present(MoveDevicePopup.TABLE_ROW)
        row = MoveDevicePopup.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)




