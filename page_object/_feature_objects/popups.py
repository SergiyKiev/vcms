
import time
from _base_page.base_actions import BaseActions
from _locators.locators import Locators
from _base_page.base_elements import BaseElements
from selenium.webdriver.common.keys import Keys


class SubscriptionHasExpitredPopup(BaseActions):

    FRAME = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"

    def click_system_button_close(self):
        self._click_system_button_close(SubscriptionHasExpitredPopup.FRAME)
        # self._click_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED + "/*" + Locators.SYS_BTN_CLOSE)
        # self.wait_for_element_not_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)

    # def close_popup(self):
    #     cond = self._is_element_present(SubscriptionHasExpitredPopup.FRAME)
    #     if cond:
    #         self._click_system_button_close()
    #     else:
    #         pass


class TermsAndConditionsPopup(BaseActions):

    FRAME = "//span[text()='Terms and Conditions']/ancestor::div[contains(@id,'WRP')]"
    BTN_I_AGREE = "//span[text()='I Agree']"
    BTN_I_DO_NOT_AGREE = "//span[text()='I Do Not Agree']"

    def click_button_i_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_AGREE)
        self.wait_for_element_not_present(TermsAndConditionsPopup.FRAME)

    def click_button_i_do_not_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_DO_NOT_AGREE)

    def click_system_button_close(self):
        self._click_system_button_close(TermsAndConditionsPopup.FRAME)

    def close_popup_if_exists(self):
        cond = self._is_element_present(Locators.POPUP_TERMS_AND_CONDITIONS)
        if cond:
            self.click_button_i_agree()
        else:
            pass


class ColumnSetsPopup(BaseActions):

    FRAME = "//span[contains(text(),'Column Sets')]/ancestor::div[contains(@id,'WRP')]"
    BUTTON_NEW = FRAME + "/*//img[@alt='New']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT = FRAME + "/*//img[@alt='Edit']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_COPY = FRAME + "/*//img[@alt='Copy']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE = FRAME + "/*//img[@alt='Delete']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SET_AS_DEFAULT = FRAME + "/*//img[@alt='Set As Default']/ancestor::div[contains(@class,'RibbonBarButton')]"
    TABLE_HEADER_IS_DEFAULT = FRAME + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Is Default')]"
    TABLE_HEADER_NAME = FRAME + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Name')]"
    TABLE_HEADER_DESCRIPTION = FRAME + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Description:')]"
    TABLE_HEADER_COLUMNS = FRAME + "/*//div[contains(@id,'HEADER')]/*//span[contains(text(),'Columns')]"
    TABLE_BODY = FRAME + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"

    def click_button_ok(self):
        self._click_button_ok(ColumnSetsPopup.FRAME)
        # self._click_element(self.FRAME + "/*" + Locators.BTN_OK)
        # self.wait_for_element_not_present(self.FRAME)

    def click_column_sets_popup_button_cancel(self):
        self._click_button_cancel(ColumnSetsPopup.FRAME)

    def click_button_new(self):
        self._click_element(ColumnSetsPopup.BUTTON_NEW)
        self.wait_for_element_present(ColumnSetDesignerPopup.FRAME)

    def click_column_sets_popup_button_edit(self):
        # self.button_edit(self.POPUP_COLUMN_SETS)
        self._click_element(ColumnSetsPopup.BUTTON_EDIT)
        self.wait_for_element_present(ColumnSetDesignerPopup.FRAME)

    def click_column_sets_popup_button_copy(self):
        self._click_element(ColumnSetsPopup.BUTTON_COPY)
        # self.wait_for_element_present(ColumnSetsPopup.TABLE_BODY + "/*//span[text()='Copy of " + columnsetname + "']")

    def click_button_delete(self):
        self._click_element(ColumnSetsPopup.BUTTON_DELETE)
        # self.wait_for_element_present(AreYouSurePopup.FRAME)

    def click_column_sets_popup_button_set_as_default(self):
        self._click_element(ColumnSetsPopup.BUTTON_SET_AS_DEFAULT)

    def click_system_button_close(self):
        self._click_system_button_close(ColumnSetsPopup.FRAME)

    def click_column_sets_popup_help_icon(self):
        self._click_icon_help(ColumnSetsPopup.FRAME)

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


class ColumnSetDesignerPopup(BaseActions):
    #CONSTANTS
    FRAME = "//span[text()='Column Set Designer']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = FRAME + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = FRAME  + "/*//div[contains(@id,'VWGLVBODY')]"
    BUTTON_CANCEL = FRAME + "/*" + Locators.BTN_CANCEL
    BUTTON_ADD = FRAME + "/*//span[text()='Add >>']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    BUTTON_REMOVE = FRAME + "/*//span[text()='<< Remove']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    BUTTON_ARROW_UP = FRAME + BaseElements.BUTTON_ARROW_UP
    BUTTON_ARROW_DOWN = FRAME + BaseElements.BUTTON_ARROW_DOWN
    TEXT_FIELD_NAME = FRAME  + "/*//div[2]/input"
    TEXT_FIELD_DESCRIPTION = FRAME  + "/*//div[1]/input"
    LEFT_SIDE_TREE = FRAME + "/*//" + Locators.EL_PADDING_BOX
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_SUBTREE_BOX
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_TREE_BOX
    ICON_HELP = FRAME + "/*" + Locators.ICON_HELP
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_NODE_BOX = Locators.EL_TREE_BOX

    def check_is_popup_present(self):
        cond = self._is_element_present(ColumnSetDesignerPopup.FRAME)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ColumnSetDesignerPopup.FRAME)
        # self._click_element(ColumnSetDesignerPopup.FRAME + "/*" + Locators.BTN_OK)
        # self.wait_for_element_not_present(ColumnSetDesignerPopup.FRAME)

    def click_button_cancel(self):
        self._click_button_cancel(ColumnSetDesignerPopup.FRAME)

    def click_button_add(self, columnname):
        self._click_element(ColumnSetDesignerPopup.BUTTON_ADD)
        self.wait_for_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")

    def click_system_button_close(self):
        self._click_system_button_close(ColumnSetDesignerPopup.FRAME)

    def click_system_button_maximize(self):
        self._click_system_button_maximize(ColumnSetDesignerPopup.FRAME)

    def enter_text_into_text_field_name(self, columnsetname):
        self._find_element(ColumnSetDesignerPopup.TEXT_FIELD_NAME).send_keys(columnsetname)

    def enter_text_into_text_field_description(self, text):
        self._find_element(ColumnSetDesignerPopup.TEXT_FIELD_DESCRIPTION).send_keys(text)

    def click_column_in_left_side_tree(self, columnname):
        elem = ColumnSetDesignerPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + columnname + "']"
        self._click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + self.ELEMENT_NODE_BOX)

    def expand_all_left_side_trees(self):
        self.wait_for_element_present(ColumnSetDesignerPopup)
        elements = self._find_elements(ColumnSetDesignerPopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        for element in elements:
            self.driver.execute_script("arguments[0].click();", element)

    def add_columns_to_list_view(self, columns_list):
        self.expand_all_left_side_trees()
        for columnname in list(columns_list):
            self.scroll_to_element(ColumnSetDesignerPopup.FRAME + "/*//span[contains(text(),'" + columnname + "')]")
            self.click_column_in_left_side_tree(columnname)
            self.click_button_add(columnname)

    def check_is_columnname_in_list_view(self, columnname):
        cond = self._is_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")
        return True if cond else False


class ConfigurationPopup(BaseActions):

    FRAME = "//span[text()='Configuration']/ancestor::div[contains(@id,'WRP')]"
    TEXT_FIELD_NAME = FRAME + "/*//input"
    BUTTON_NEW = FRAME + "//span[text()='New']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    COLUMN_SET_DROP_DOWN_LIST = FRAME + "/following::div[@class='ComboBox-PopupWindow']"
    DROP_DOWN_APPLIED_VALUE = FRAME + "/*//div[contains(@class,'ComboBox-Container')]/*//span[@data-vwg_appliedvalue]"
    TAB_IP_ADDRESS = "//span[text()='IP Address Ranges'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_SITE = "//span[text()='Site'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_VREPS = "//span[text()='vReps'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"

    def check_is_popup_present(self):
        cond = self._is_element_present(ConfigurationPopup.FRAME)
        return True if cond else False

    def check_name_text_field_disabled(self):
        cond = self._is_element_disabled(ConfigurationPopup.TEXT_FIELD_NAME)
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ConfigurationPopup.FRAME)

    def click_button_new(self):
        self._click_element(ConfigurationPopup.BUTTON_NEW)
        self._is_element_present(ColumnSetDesignerPopup.FRAME)

    def click_icon_help(self):
        self._click_icon_help(ConfigurationPopup.FRAME)

    def click_icon_restore(self):
        self._click_element(ConfigurationPopup.FRAME)
        self.wait_for_element_not_present(ConfigurationPopup.DROP_DOWN_APPLIED_VALUE)

    def click_system_button_close(self):
        self._click_system_button_close(ConfigurationPopup.FRAME)

    def click_column_set_dropdown_button(self):
        self._click_system_button_drop_down(ConfigurationPopup.FRAME)
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

    FRAME = "//span[contains(text(),'Site') and contains(text(),'Name')]/ancestor::div[contains(@id,'WRP')]"
    TEXT_FIELD_NAME = FRAME + "/*//input"

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(SiteNamePopup.TEXT_FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(SiteNamePopup.FRAME)

    def click_system_button_close(self):
        self._click_system_button_close(SiteNamePopup.FRAME)

    def click_button_cancel(self):
        self._click_button_cancel(SiteNamePopup.FRAME)

    def check_is_popup_present(self):
        cond = self._is_element_present(SiteNamePopup.FRAME)
        return True if cond else False


class AreYouSurePopup(BaseActions):

    FRAME = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"

    def click_button_ok(self):
        self._click_button_ok(AreYouSurePopup.FRAME)
        # self.wait_for_element_present(AreYouSurePopup.FRAME)
        # cond1 = self._is_element_present(AreYouSurePopup.BUTTON_OK)
        # cond2 = self._is_element_present(AreYouSurePopup.BUTTON_Ok)
        # if cond1:
        #     self._click_element(AreYouSurePopup.BUTTON_OK)
        # elif cond2:
        #     self._click_element(AreYouSurePopup.BUTTON_Ok)
        # self.wait_for_element_not_present(AreYouSurePopup.FRAME)

    def click_system_button_close(self):
       self._click_system_button_close(AreYouSurePopup.FRAME)
        # self._click_element(AreYouSurePopup.SYSTEM_BUTTON_CLOSE)
        # self.wait_for_element_not_present(AreYouSurePopup.FRAME)

    def click_button_cancel(self):
        self._click_button_cancel(AreYouSurePopup.FRAME)

    def click_button_no(self):
        self._click_button_no(AreYouSurePopup.FRAME)

    def click_button_yes(self):
        self._click_button_yes(AreYouSurePopup.FRAME)

    def check_is_popup_present(self):
        cond = self._is_element_present(AreYouSurePopup.FRAME)
        return True if cond else False

class UnableToRemovePopup(BaseActions):

    FRAME =  "//span[text()='Unable to remove']/ancestor::div[contains(@id,'WRP')]"

    def check_is_popup_present(self):
        cond = self._is_element_present(UnableToRemovePopup.FRAME)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(UnableToRemovePopup.FRAME)
        # self.wait_for_element_present(UnableToRemovePopup.FRAME)
        # cond1 = self._is_element_present(UnableToRemovePopup.BUTTON_OK)
        # cond2 = self._is_element_present(UnableToRemovePopup.BUTTON_Ok)
        # if cond1:
        #     self._click_element(UnableToRemovePopup.BUTTON_OK)
        # elif cond2:
        #     self._click_element(UnableToRemovePopup.BUTTON_Ok)
        # self.wait_for_element_not_present(UnableToRemovePopup.FRAME)

    def click_system_button_close(self):
        self._click_system_button_close(UnableToRemovePopup.FRAME)
        # self._click_element(UnableToRemovePopup.SYSTEM_BUTTON_CLOSE)
        # self.wait_for_element_not_present(UnableToRemovePopup.FRAME)


class ErrorPopup(BaseActions):

    FRAME = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')]"

    def check_is_popup_present(self):
        cond = self._is_element_present(ErrorPopup.FRAME)
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ErrorPopup.FRAME)

    def click_button_ok(self):
        self._click_button_ok(ErrorPopup.FRAME)


