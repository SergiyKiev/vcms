
from _base_page.base_actions import BaseActions
from _feature_objects.featurePopupColumnSetDesigner import ColumnSetDesignerPopup


class ConfigurationPopup(BaseActions):

    BODY = "//span[text()='Configuration']/ancestor::div[contains(@id,'WRP')]"
    TEXT_FIELD_NAME = BODY + "/*//input"
    BUTTON_NEW = BODY + "//span[text()='New']/ancestor::div[contains(@class,'Button')]"
    COLUMN_SET_DROP_DOWN_LIST = BODY + "/following::div[@class='ComboBox-PopupWindow']"
    DROP_DOWN_APPLIED_VALUE = BODY + "/*//div[contains(@class,'ComboBox-Container')]/*//span[@data-vwg_appliedvalue]"
    TAB_IP_ADDRESS = "//span[text()='IP Address Ranges'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_SITE = "//span[text()='Site'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_VREPS = "//span[text()='vReps'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(ConfigurationPopup.BODY)
        return True if cond else False

    def check_name_text_field_disabled(self):
        cond = self._is_element_disabled(ConfigurationPopup.TEXT_FIELD_NAME)
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ConfigurationPopup.BODY)

    def click_button_new(self):
        self._click_element(ConfigurationPopup.BUTTON_NEW)
        self._is_element_present(ColumnSetDesignerPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ConfigurationPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Configure a site")
        return True if cond else False

    def click_icon_restore(self):
        self._click_element(ConfigurationPopup.BODY)
        self.wait_for_element_not_present(ConfigurationPopup.DROP_DOWN_APPLIED_VALUE)

    def click_system_button_close(self):
        self._click_system_button_close(ConfigurationPopup.BODY)

    def click_column_set_dropdown_button(self):
        self._click_system_button_drop_down(ConfigurationPopup.BODY)
        self.wait_for_element_present(ConfigurationPopup.COLUMN_SET_DROP_DOWN_LIST)

    def select_columnset_in_drop_down_list(self, columnsetname):
        self.click_column_set_dropdown_button()
        self.scroll_list_to_top()
        row = "//table[contains(@id,'VWGVL_')]/*//tr"
        scroll = "//div[contains(@id,'VWGVLSC_')]/div"
        scroll_height = self._find_element(scroll).size['height']
        row_height = self._find_element(row).size['height']
        rows_number = scroll_height / row_height
        # print "DROP-DOWN: list_height, one row height, number of rows are: ", scroll_height, row_height, rows_number
        element = ConfigurationPopup.COLUMN_SET_DROP_DOWN_LIST + "/*//span[text()='" + columnsetname + "']"
        i = 0
        visible_rows = 8
        one_scroll = row_height * visible_rows
        step = one_scroll
        while i <= rows_number:
            cond = self._is_element_not_present(element)
            if cond:
                self.scroll_list_down(step)
                step += one_scroll
                i += visible_rows
            else:
                break
        # self._click_element(BaseElements._DROP_DOWN_LIST + "/*//span[text()='" + columnsetname + "']")
        self._click_element(element)
        self.wait_for_element_not_present(ConfigurationPopup.COLUMN_SET_DROP_DOWN_LIST)

    def check_columnset_is_selected_from_drop_down_list(self, columnsetname):
        cond = self._is_element_present(ConfigurationPopup.DROP_DOWN_APPLIED_VALUE + "[text()='" + columnsetname + "']")
        return True if cond else False

    def click_configuration_popup_site_tab(self):
        self._click_element(ConfigurationPopup.TAB_SITE)
        self.wait_for_element_selected(ConfigurationPopup.TAB_SITE)

    def click_configuration_popup_ip_address_ranges_tab(self):
        self._click_element(ConfigurationPopup.TAB_IP_ADDRESS)
        self.wait_for_element_selected(ConfigurationPopup.TAB_IP_ADDRESS)

    def click_configuration_popup_vreps_tab(self):
        self._click_element(ConfigurationPopup.TAB_VREPS)
        self.wait_for_element_selected(ConfigurationPopup.TAB_VREPS)

    def enter_text_into_name_text_field(self, sitename):
        self._click_element(ConfigurationPopup.TEXT_FIELD_NAME)
        self._find_element(ConfigurationPopup.TEXT_FIELD_NAME).send_keys(sitename)

    def get_name_text_field_value(self):
        actual_attribute_value = self.get_attribute_value(ConfigurationPopup.TEXT_FIELD_NAME, "value")
        print ("The actual value in the Name textfield is: " + actual_attribute_value)
        return actual_attribute_value