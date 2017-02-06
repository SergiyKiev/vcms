
import time
from _base_page.base_actions import BaseActions
from _locators.locators import Locators
from _base_page.base_elements import BaseElements
from selenium.webdriver.common.keys import Keys


class SubscriptionHasExpitredPopup(BaseActions):

    BODY = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"

    def click_system_button_close(self):
        self._click_system_button_close(SubscriptionHasExpitredPopup.BODY)
        # self._click_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED + "/*" + Locators.SYS_BTN_CLOSE)
        # self.wait_for_element_not_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)

    # def close_popup(self):
    #     cond = self._is_element_present(SubscriptionHasExpitredPopup.BODY)
    #     if cond:
    #         self._click_system_button_close()
    #     else:
    #         pass


class TermsAndConditionsPopup(BaseActions):

    BODY = "//span[text()='Terms and Conditions']/ancestor::div[contains(@id,'WRP')]"
    BTN_I_AGREE = "//span[text()='I Agree']"
    BTN_I_DO_NOT_AGREE = "//span[text()='I Do Not Agree']"

    def click_button_i_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_AGREE)
        self.wait_for_element_not_present(TermsAndConditionsPopup.BODY)

    def click_button_i_do_not_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_DO_NOT_AGREE)

    def click_system_button_close(self):
        self._click_system_button_close(TermsAndConditionsPopup.BODY)

    def close_popup_if_exists(self):
        cond = self._is_element_present(TermsAndConditionsPopup.BODY)
        if cond:
            self.click_button_i_agree()
        else:
            pass


class ColumnSetsPopup(BaseActions):

    BODY = "//span[contains(text(),'Column Sets')]/ancestor::div[contains(@id,'WRP')]"
    BUTTON_NEW = BODY + "/*//img[@alt='New']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT = BODY + "/*//img[@alt='Edit']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_COPY = BODY + "/*//img[@alt='Copy']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE = BODY + "/*//img[@alt='Delete']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SET_AS_DEFAULT = BODY + "/*//img[@alt='Set As Default']/ancestor::div[contains(@class,'RibbonBarButton')]"
    TABLE_HEADER_IS_DEFAULT = BODY + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Is Default')]"
    TABLE_HEADER_NAME = BODY + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Name')]"
    TABLE_HEADER_DESCRIPTION = BODY + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Description:')]"
    TABLE_HEADER_COLUMNS = BODY + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Columns')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"

    def click_button_ok(self):
        self._click_button_ok(ColumnSetsPopup.BODY)
        # self._click_element(self.BODY + "/*" + Locators.BTN_OK)
        # self.wait_for_element_not_present(self.BODY)

    def click_column_sets_popup_button_cancel(self):
        self._click_button_cancel(ColumnSetsPopup.BODY)

    def click_button_new(self):
        self._click_element(ColumnSetsPopup.BUTTON_NEW)
        self.wait_for_element_present(ColumnSetDesignerPopup.BODY)

    def click_column_sets_popup_button_edit(self):
        self._click_element(ColumnSetsPopup.BUTTON_EDIT)
        self.wait_for_element_present(ColumnSetDesignerPopup.BODY)

    def click_column_sets_popup_button_copy(self):
        self._click_element(ColumnSetsPopup.BUTTON_COPY)
        # self.wait_for_element_present(ColumnSetsPopup.TABLE_BODY + "/*//span[text()='Copy of " + columnsetname + "']")

    def click_button_delete(self):
        self._click_element(ColumnSetsPopup.BUTTON_DELETE)
        # self.wait_for_element_present(AreYouSurePopup.BODY)

    def click_column_sets_popup_button_set_as_default(self):
        self._click_element(ColumnSetsPopup.BUTTON_SET_AS_DEFAULT)

    def click_system_button_close(self):
        self._click_system_button_close(ColumnSetsPopup.BODY)

    def click_column_sets_popup_help_icon(self):
        self._click_icon_help(ColumnSetsPopup.BODY)

    def click_column_sets_popup_table_header_is_default(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_IS_DEFAULT)

    def click_column_sets_popup_table_header_name(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_NAME)

    def click_column_sets_popup_table_header_description(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_DESCRIPTION)

    def click_column_sets_popup_table_header_columns(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_COLUMNS)

    def click_columnset_in_table_list(self, columnsetname):
        element = ColumnSetsPopup.TABLE_BODY + "/*//span[text()='" + columnsetname + "']" + ColumnSetsPopup.TABLE_ROW
        self._click_element(element)
        self.wait_for_element_selected(element)

    def check_is_columnset_present(self, columsetname):
        cond = self._is_element_present(ColumnSetsPopup.TABLE_BODY + "/*//span[text()='" + columsetname  + "']")
        return True if cond else False

    def check_is_popup_present(self):
        cond = self._is_element_present(ColumnSetsPopup.BODY)
        return True if cond else False

    def delete_columnset_if_exists(self, columnsetname):
        elem = ColumnSetsPopup.TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
        cond = self._is_element_present(elem)
        if cond:
            ColumnSetsPopup.click_columnset_in_table_list(self, columnsetname)
            ColumnSetsPopup.click_button_delete(self)
            are_you_sure_popup = AreYouSurePopup(self.driver)
            are_you_sure_popup.click_button_yes()
            self.wait_for_element_not_present(elem)
        else:
            pass


class ColumnSetDesignerPopup(BaseActions):
    #CONSTANTS
    BODY = "//span[text()='Column Set Designer']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    BUTTON_CANCEL = BODY + "/*" + Locators.BTN_CANCEL
    BUTTON_ADD = BODY + "/*//span[text()='Add >>']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    BUTTON_REMOVE = BODY + "/*//span[text()='<< Remove']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    BUTTON_ARROW_UP = BODY + BaseElements.BUTTON_ARROW_UP
    BUTTON_ARROW_DOWN = BODY + BaseElements.BUTTON_ARROW_DOWN
    TEXT_FIELD_NAME = BODY  + "/*//div[2]/input"
    TEXT_FIELD_DESCRIPTION = BODY  + "/*//div[1]/input"
    LEFT_SIDE_TREE = BODY + "/*//" + Locators.EL_PADDING_BOX
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_SUBTREE_BOX
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_TREE_BOX
    ICON_HELP = BODY + "/*" + Locators.ICON_HELP
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_NODE_BOX = Locators.EL_TREE_BOX

    def check_is_popup_present(self):
        cond = self._is_element_present(ColumnSetDesignerPopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ColumnSetDesignerPopup.BODY)
        # self._click_element(ColumnSetDesignerPopup.BODY + "/*" + Locators.BTN_OK)
        # self.wait_for_element_not_present(ColumnSetDesignerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ColumnSetDesignerPopup.BODY)

    def click_button_add(self, columnname):
        self._click_element(ColumnSetDesignerPopup.BUTTON_ADD)
        self.wait_for_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")

    def click_system_button_close(self):
        self._click_system_button_close(ColumnSetDesignerPopup.BODY)

    def click_system_button_maximize(self):
        self._click_system_button_maximize(ColumnSetDesignerPopup.BODY)

    def enter_text_into_text_field_name(self, columnsetname):
        self._find_element(ColumnSetDesignerPopup.TEXT_FIELD_NAME).send_keys(columnsetname)

    def enter_text_into_text_field_description(self, text):
        self._find_element(ColumnSetDesignerPopup.TEXT_FIELD_DESCRIPTION).send_keys(text)

    def click_column_in_left_side_tree(self, columnname):
        elem = ColumnSetDesignerPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + columnname + "']"
        self._click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + self.ELEMENT_NODE_BOX)

    def expand_all_left_side_trees(self):
        self.wait_for_element_present(ColumnSetDesignerPopup.BODY)
        elements = self._find_elements(ColumnSetDesignerPopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)

    def add_columns_to_list_view(self, columns_list):
        self.expand_all_left_side_trees()
        for columnname in list(columns_list):
            self.scroll_to_element(ColumnSetDesignerPopup.BODY + "/*//span[contains(text(),'" + columnname + "')]")
            self.click_column_in_left_side_tree(columnname)
            self.click_button_add(columnname)

    def check_is_columnname_in_list_view(self, columnname):
        cond = self._is_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")
        return True if cond else False

    def create_columnset(self, columnsetname=None, columns_list=None):
        self.click_system_button_maximize()
        self.enter_text_into_text_field_name(columnsetname)
        self.add_columns_to_list_view(columns_list)
        self.click_button_ok()


class ConfigurationPopup(BaseActions):

    BODY = "//span[text()='Configuration']/ancestor::div[contains(@id,'WRP')]"
    TEXT_FIELD_NAME = BODY + "/*//input"
    BUTTON_NEW = BODY + "//span[text()='New']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    COLUMN_SET_DROP_DOWN_LIST = BODY + "/following::div[@class='ComboBox-PopupWindow']"
    DROP_DOWN_APPLIED_VALUE = BODY + "/*//div[contains(@class,'ComboBox-Container')]/*//span[@data-vwg_appliedvalue]"
    TAB_IP_ADDRESS = "//span[text()='IP Address Ranges'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_SITE = "//span[text()='Site'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_VREPS = "//span[text()='vReps'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"

    def check_is_popup_present(self):
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

class SiteNamePopup(BaseActions):

    BODY = "//span[contains(text(),'Site') and contains(text(),'Name')]/ancestor::div[contains(@id,'WRP')]"
    TEXT_FIELD_NAME = BODY + "/*//input"

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(SiteNamePopup.TEXT_FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(SiteNamePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SiteNamePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(SiteNamePopup.BODY)

    def check_is_popup_present(self):
        try:
            cond = self._is_element_present(SiteNamePopup.BODY)
            return True if cond else False
        except Exception as e:
            print "Step failed: ", e


class AreYouSurePopup(BaseActions):

    BODY = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"

    def click_button_ok(self):
        self._click_button_ok(AreYouSurePopup.BODY)
        # self.wait_for_element_present(AreYouSurePopup.BODY)
        # cond1 = self._is_element_present(AreYouSurePopup.BUTTON_OK)
        # cond2 = self._is_element_present(AreYouSurePopup.BUTTON_Ok)
        # if cond1:
        #     self._click_element(AreYouSurePopup.BUTTON_OK)
        # elif cond2:
        #     self._click_element(AreYouSurePopup.BUTTON_Ok)
        # self.wait_for_element_not_present(AreYouSurePopup.BODY)

    def click_system_button_close(self):
       self._click_system_button_close(AreYouSurePopup.BODY)
        # self._click_element(AreYouSurePopup.SYSTEM_BUTTON_CLOSE)
        # self.wait_for_element_not_present(AreYouSurePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(AreYouSurePopup.BODY)

    def click_button_no(self):
        self._click_button_no(AreYouSurePopup.BODY)

    def click_button_yes(self):
        self._click_button_yes(AreYouSurePopup.BODY)

    def check_is_popup_present(self):
        # cond = self.wait_for_element_present(AreYouSurePopup.BODY)
        cond = self._is_element_present(AreYouSurePopup.BODY)
        return True if cond else False


class UnableToRemovePopup(BaseActions):

    BODY =  "//span[text()='Unable to remove']/ancestor::div[contains(@id,'WRP')]"

    def check_is_popup_present(self):
        cond = self._is_element_present(UnableToRemovePopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(UnableToRemovePopup.BODY)
        # self.wait_for_element_present(UnableToRemovePopup.BODY)
        # cond1 = self._is_element_present(UnableToRemovePopup.BUTTON_OK)
        # cond2 = self._is_element_present(UnableToRemovePopup.BUTTON_Ok)
        # if cond1:
        #     self._click_element(UnableToRemovePopup.BUTTON_OK)
        # elif cond2:
        #     self._click_element(UnableToRemovePopup.BUTTON_Ok)
        # self.wait_for_element_not_present(UnableToRemovePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(UnableToRemovePopup.BODY)
        # self._click_element(UnableToRemovePopup.SYSTEM_BUTTON_CLOSE)
        # self.wait_for_element_not_present(UnableToRemovePopup.BODY)


class ErrorPopup(BaseActions):

    BODY = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')]"

    def check_is_popup_present(self):
        cond = self._is_element_present(ErrorPopup.BODY)
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ErrorPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(ErrorPopup.BODY)


class RemoveDevicesPopup(BaseActions):

    BODY = "//span[text()='Remove Devices']/ancestor::div[contains(@id,'WRP')]"
    CHECKBOX_KEEP_HIST_INFORM = BODY + "//span[contains(text(),'Keep')][@class='CheckBox-Label']/ancestor::tr/td[contains(@id,'TRG')]"

    def click_button_ok(self):
        self._click_button_ok(RemoveDevicesPopup.BODY)

    def click_system_button_close(self):
       self._click_system_button_close(RemoveDevicesPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(RemoveDevicesPopup.BODY)

    def check_is_popup_present(self):
        cond = self._is_element_present(RemoveDevicesPopup.BODY)
        return True if cond else False

    def check_keep_historical_information_check_box(self):
        self.wait_for_element_checked(RemoveDevicesPopup.BODY)
        self._click_element(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
        self.wait_for_element_checked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)

    def uncheck_keep_historical_information_check_box(self):
        self.wait_for_element_present(RemoveDevicesPopup.BODY)
        self._click_element(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
        self.wait_for_element_unchecked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)



