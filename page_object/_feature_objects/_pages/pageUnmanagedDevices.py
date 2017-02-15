import time
from _base_page.base_actions import BaseActions
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class UnmanagedDevicesPage(BaseActions):

    PAGE_HEADER = "//span[text()='Unmanaged Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = PAGE_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_DEVICE_NAME = TABLE_HEADER + "/*//span[contains(text(),'Device Name')]"
    HEADER_DOMAIN = TABLE_HEADER + "/*//span[contains(text(),'Domain')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_IP_ADDRESS = TABLE_HEADER + "/*//span[contains(text(),'IP Address')]"
    HEADER_SITE = TABLE_HEADER + "/*//span[contains(text(),'Site')]"
    CELL_DEVICE_NAME = "/td[1]"
    CELL_DOMAIN = "/td[3]"
    CELL_IP_ADDRESS = "/td[5]"
    CELL_SITE = "/td[7]"
    CELL_SERVER = "/td[9]"
    CELL_OS_VERSION = "/td[11]"
    CELL_DATE_DISCOVERED = "/td[13]"

    def check_page_is_present(self):
        cond = self._is_element_present(UnmanagedDevicesPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(UnmanagedDevicesPage.PAGE_HEADER)

    def click_icon_search(self):
        self._click_icon_search(UnmanagedDevicesPage.PAGE_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(UnmanagedDevicesPage.SEARCH_FIELD).send_keys(text)

    def check_device_is_present(self, name):
        row = UnmanagedDevicesPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(UnmanagedDevicesPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = UnmanagedDevicesPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)







