
from _base_page.base_actions import BaseActions
from _locators.locators import Locators

class DevicesTab(BaseActions):

    BODY = "//span[text()='Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]/parent::div"
    TAB_HEADER = "//span[text()='Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = TAB_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def select_device_in_table(self, *name):
        self.wait_for_element_present(DevicesTab.BODY)
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
            cond = self._is_element_present(DevicesTab.BODY)
            return True if cond else False
        except Exception as e:
            print "Step failed: ", e

    def check_is_device_present(self, *name):
        cond = self._is_element_present(DevicesTab.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr")
        return True if cond else False

    def check_columns_are_present(self, columns_list):
        columnset = []
        for i in columns_list:
            elem = DevicesTab.TABLE_HEADER + "/*//span[contains(text(),'" + str(i) + "')]"
            cond = self._is_element_present(elem)
            if cond:
                columnset.append(i)
            else:
                pass
        print "Created column set is: ", columns_list
        print "Expected column set is : ", columnset
        if columnset == columns_list:
            pass
        else:
            print "Columnsets are not similar ", columns_list, columnset
        return True if columnset == columns_list else False

    def click_icon_help(self):
        self._click_icon_help(DevicesTab.TAB_HEADER)



