
from _base_page.base_actions import BaseActions
from _locators.locators import Locators

class DevicesTab(BaseActions):

    FRAME = "//span[text()='Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]/parent::div"
    TAB_HEADER = "//span[text()='Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    TABLE_HEADER = FRAME + "/*//div[contains(@id,'HEADER')]"
    TABLE_LIST = FRAME + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_LIST + "/*//tr"
    SEARCH_FIELD = TAB_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def select_device_in_table(self, *name):
        self.wait_for_element_present(DevicesTab.FRAME)
        row = DevicesTab.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)

    def click_icon_refresh(self):
        self._click_icon_refresh(DevicesTab.TAB_HEADER)

    def click_icon_search(self):
        self._click_icon_search(DevicesTab.TAB_HEADER)

    def enter_text_into_search_field(self, text = None):
        self._find_element(DevicesTab.SEARCH_FIELD).send_keys(text)

    def check_is_tab_present(self):
        try:
            cond = self._is_element_present(DevicesTab.FRAME)
            return True if cond else False
        except Exception as e:
            print "Step failed: ", e

    def check_is_device_present(self, *name):
        cond = self._is_element_present(DevicesTab.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr")
        return True if cond else False



