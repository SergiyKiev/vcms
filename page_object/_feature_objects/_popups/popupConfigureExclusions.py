
from _base_page.base_actions import BaseActions
from _feature_objects._popups.popupExcludeDevice import ExcludeDevicePopup
from _feature_objects._popups.popupExcludeIPAddress import ExcludeIPAddressPopup
from _feature_objects._popups.popupExcludeSite import ExcludeSitePopup


class ConfigureExclusionsPopup(BaseActions):

    BODY = "//span[text()='Configure Exclusions'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_MENU = BODY + "/*//div[@class='Common-Unselectable TreeView-Container']"
    # LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    # LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    # LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ConfigureExclusionsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ConfigureExclusionsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclusions")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ConfigureExclusionsPopup.BODY)
        self._wait_for_element_not_present(ConfigureExclusionsPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ConfigureExclusionsPopup.BODY)

    def click_label_in_left_side_tree(self, label):
        elem = ConfigureExclusionsPopup.LEFT_MENU + "/*//span[text()='" + str(label) + "']"
        self._click_element(elem)
        self._wait_for_element_selected(elem + ConfigureExclusionsPopup.ELEMENT_LABEL)

    def check_text_is_in_list_view(self, text):
        cond = self._is_element_present(ConfigureExclusionsPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False

    def select_item_in_table(self, item):
        self._wait_for_element_present(ConfigureExclusionsPopup.TABLE_ROW)
        row = ConfigureExclusionsPopup.TABLE_ROW + "/*//span[text()='" + item + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)

    def click_tree_label_sites(self):
        self.click_label_in_left_side_tree("Sites")

    def click_tree_label_ip_address(self):
        self.click_label_in_left_side_tree("IP Address")

    def click_tree_label_device_name(self):
        self.click_label_in_left_side_tree("Device Name")


class SitesTab(ConfigureExclusionsPopup):

    def click_button_add(self):
        self._click_button_add(ConfigureExclusionsPopup.TAB)
        self._wait_for_element_present(ExcludeSitePopup.BODY)

class IPAddressTab(ConfigureExclusionsPopup):

    def click_button_add(self):
        self._click_button_add(ConfigureExclusionsPopup.TAB)
        self._wait_for_element_present(ExcludeIPAddressPopup.BODY)

class DeviceNameTab(ConfigureExclusionsPopup):

    def click_button_add(self):
        self._click_button_add(ConfigureExclusionsPopup.TAB)
        self._wait_for_element_present(ExcludeDevicePopup.BODY)
