
import time
from _base_page.base import Base
from _locators.locators import Locators
from selenium.webdriver.common.keys import Keys


class SubscriptionHasExpitredPopup(Base):

    def click_system_button_close(self):
        self.click_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)

    def close_popup(self):
        cond = self.is_element_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        if cond:
            self.click_system_button_close()
        else:
            pass


class TermsAndConditionsPopup(Base):

    def click_button_i_agree(self):
        self.click_element(Locators.POPUP_TERMS_AND_CONDITIONS + "/*" + Locators.BTN_I_AGREE)
        self.wait_for_element_not_present(Locators.POPUP_TERMS_AND_CONDITIONS)

    def click_button_i_do_not_agree(self):
        self.click_element(Locators.POPUP_TERMS_AND_CONDITIONS + "/*" + Locators.BTN_I_DO_NOT_AGREE)

    def click_system_button_close(self):
        self.click_element(Locators.POPUP_TERMS_AND_CONDITIONS + "/*" + Locators.SYS_BTN_CLOSE)

    def close_popup_if_exists(self):
        cond = self.is_element_present(Locators.POPUP_TERMS_AND_CONDITIONS)
        if cond:
            self.click_button_i_agree()
        else:
            pass


class ColumnSetsPopup(Base):
    # CONSTANTS
    POPUP_COLUMN_SETS = Locators.POPUP_COLUMN_SETS
    CS_BUTTON_OK = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_OK
    CS_BUTTON_CANCEL = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_CANCEL
    CS_BUTTON_NEW = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_NEW
    CS_BUTTON_EDIT = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_EDIT
    CS_BUTTON_COPY = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_COPY
    CS_BUTTON_DELETE = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_DELETE
    CS_BUTTON_SET_AS_DEFAULT = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_SET_AS_DEFAULT
    CS_SYSTEM_BUTTON_CLOSE = Locators.POPUP_COLUMN_SETS + "/*" + Locators.SYS_BTN_CLOSE
    CS_ICON_HELP = Locators.POPUP_COLUMN_SETS + "/*" + Locators.ICON_HELP
    CS_TABLE_HEADER_IS_DEFAULT = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_IS_DEFAULT
    CS_TABLE_HEADER_NAME = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_NAME
    CS_TABLE_HEADER_DESCRIPTION = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_DESCRIPTION
    CS_TABLE_HEADER_COLUMNS = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_COLUMNS
    CS_TABLE_BODY = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABLE_BODY

    def click_button_ok(self):
        self.click_element(self.POPUP_COLUMN_SETS + "/*" + Locators.BTN_OK)
        self.wait_for_element_not_present(self.POPUP_COLUMN_SETS)

    def click_column_sets_popup_button_cancel(self):
        self.click_element(self.CS_BUTTON_CANCEL)
        self.wait_for_element_not_present(self.POPUP_COLUMN_SETS)

    def click_button_new(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_NEW)
        self.wait_for_element_present(ColumnSetDesignerPopup.FRAME)

    def click_column_sets_popup_button_edit(self):
        # self.cbutton_edit(self.POPUP_COLUMN_SETS)
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_EDIT)
        self.wait_for_element_present(ColumnSetDesignerPopup.FRAME)

    def click_column_sets_popup_button_copy(self, columnsetname):
        elem = self.POPUP_COLUMN_SETS + "/*//span[text()='Copy of " + columnsetname + "']"
        self.click_element(self.CS_BUTTON_COPY)
        self.wait_for_element_present(elem)

    def click_button_delete(self):
        self.click_element(self.CS_BUTTON_DELETE)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        self.wait_for_element_present(are_you_sure_popup.POPUP_ARE_YOU_SURE)

    def click_column_sets_popup_button_set_as_default(self):
        self.click_element(self.CS_BUTTON_SET_AS_DEFAULT)

    def click_system_button_close(self):
        self.click_element(self.POPUP_COLUMN_SETS + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(self.POPUP_COLUMN_SETS)

    def click_column_sets_popup_help_icon(self):
        self.click_element(self.CS_ICON_HELP)

    def click_column_sets_popup_table_header_is_default(self):
        self.click_element(self.CS_TABLE_HEADER_IS_DEFAULT)

    def click_column_sets_popup_table_header_name(self):
        self.click_element(self.CS_TABLE_HEADER_NAME)

    def click_column_sets_popup_table_header_description(self):
        self.click_element(self.CS_TABLE_HEADER_DESCRIPTION)

    def click_column_sets_popup_table_header_columns(self):
        self.click_element(self.CS_TABLE_HEADER_COLUMNS)

    def click_columnset_in_table_list(self, columnsetname):
        elem = self.CS_TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
        self.click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + Locators.EL_LIST_ROW)

    def check_is_columnset_present(self, columsetname):
        elem = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABLE_BODY + "/*//span[text()='" + columsetname  + "']"
        cond = self.is_element_present(elem)
        return True if cond else False


class ColumnSetDesignerPopup(Base):
    #CONSTANTS
    FRAME = "//span[text()='Column Set Designer']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = FRAME + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = FRAME  + "/*//div[contains(@id,'VWGLVBODY')]"
    BUTTON_OK = FRAME + "/*" + Locators.BTN_OK
    BUTTON_CANCEL = FRAME + "/*" + Locators.BTN_CANCEL
    BUTTON_ADD = FRAME + "/*" + Locators.BTN_ADD_right
    BUTTON_REMOVE = FRAME + "/*" + Locators.BTN_REMOVE_left
    BUTTON_ARROW_UP = FRAME + "/*" + Locators.BTN_ARROW_UP
    BUTTON_ARROW_DOWN = FRAME + "/*" + Locators.BTN_ARROW_DOWN
    # TEXT_FIELD_NAME = FRAME  + "/*//div[2]/input"
    # TEXT_FIELD_DESCRIPTION = FRAME  + "/*//div[1]/input"
    LEFT_SIDE_TREE = FRAME + "/*//" + Locators.EL_PADDING_CONTAINER
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_SUBTREE_CONTAINER
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//" + Locators.EL_TREE_CONTAINER
    ICON_HELP = FRAME + "/*" + Locators.ICON_HELP
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    ELEMENT_NODE_CONTAINER = Locators.EL_TREE_CONTAINER

    def check_is_popup_present(self):
        cond = self.is_element_present(ColumnSetDesignerPopup.FRAME)
        return True if cond else False

    def click_button_ok(self):
        self.click_element(ColumnSetDesignerPopup.FRAME + "/*" + Locators.BTN_OK)
        self.wait_for_element_not_present(ColumnSetDesignerPopup.FRAME)

    def click_button_cancel(self):
        self.click_element(self.BUTTON_CANCEL)
        self.wait_for_element_not_present(ColumnSetDesignerPopup.FRAME)

    def click_button_add(self, columnname):
        self.click_element(self.BUTTON_ADD)
        self.wait_for_element_present(self.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")

    def click_system_button_close(self):
        self.click_element(ColumnSetDesignerPopup.FRAME  + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(ColumnSetDesignerPopup.FRAME)

    def click_system_button_maximize(self):
        self.click_element(ColumnSetDesignerPopup.FRAME + "/*" + Locators.SYS_BTN_MAXIMIZE)
        time.sleep(2)
        self.wait_for_element_present(Locators.SYS_BTN_RESTORE_DOWN)

    def enter_text_into_text_field_name(self, columnsetname):
        self._find_element(ColumnSetDesignerPopup.FRAME  + "/*//div[2]/input").send_keys(columnsetname)

    def enter_text_into_text_field_description(self, text):
        self._find_element(ColumnSetDesignerPopup.FRAME  + "/*//div[1]/input").send_keys(text)

    def click_column_in_left_side_tree(self, columnname):
        elem = self.LEFT_SIDE_SUBNODE + "/*//span[text()='" + columnname + "']"
        self.click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + self.ELEMENT_NODE_CONTAINER)

    def expand_all_left_side_lists(self):
        elements = self._find_elements(self.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        for x in range(0, len(elements)):
            elem = self.LEFT_SIDE_TREE + "/div[" + str(x + 1) + "]/div/div[contains(@id,'VWGJOINT')]"
            self.expand_tree(elem)

    def add_columns_to_list_view(self, columns_list):
        self.expand_all_left_side_lists()
        for columnname in list(columns_list):
            self.click_column_in_left_side_tree(columnname)
            self.click_button_add(columnname)
            # self.check_is_columnname_in_list_view(columnname)

    def check_is_columnname_in_list_view(self, columnname):
        cond = self.is_element_present(self.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")
        return True if cond else False


class ConfigurationPopup(Base):
    #CONSTANTS
    POPUP_CONFIGURATION = "//span[text()='Configuration']/ancestor::div[contains(@id,'WRP')]"
    TAB_PANEL = POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL
    TEXT_FIELD_NAME = POPUP_CONFIGURATION + "/*" + Locators._FIELD
    BUTTON_CLOSE = POPUP_CONFIGURATION + "/*" + Locators.BTN_CLOSE
    BUTTON_NEW = POPUP_CONFIGURATION + "/*" + Locators.BTN_NEW_by_text
    SYSTEM_BUTTON_CLOSE = POPUP_CONFIGURATION + "/*" + Locators.SYS_BTN_CLOSE
    SYSTEM_BUTTON_DROP_DOWN = POPUP_CONFIGURATION + "/*" + Locators.SYS_BTN_DROP_DOWN
    ICON_HELP = POPUP_CONFIGURATION + "/*" + Locators.ICON_HELP
    DROP_DOWN_LIST = "//" + Locators.EL_DROP_DOWN_LIST
    DROP_DOWN_CONTAINER = POPUP_CONFIGURATION + "/*//" + Locators.EL_DROP_DOWN_CONTAINER
    ICON_RESTORE = POPUP_CONFIGURATION + "/*" + Locators.ICON_RESTORE

    def check_is_popup_present(self):
        cond = self.is_element_present(self.POPUP_CONFIGURATION)
        return True if cond else False

    def check_name_text_feild_disabled(self):
        cond = self.is_element_disabled(self.TEXT_FIELD_NAME)
        return True if cond else False

    def click_button_close(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_CLOSE)
        self.is_element_not_present(Locators.POPUP_CONFIGURATION)

    def click_button_new(self):
        self.click_element(ConfigurationPopup.BUTTON_NEW)
        self.is_element_present(ColumnSetDesignerPopup.FRAME)

    def click_icon_help(self):
        self.click_element(ConfigurationPopup.ICON_HELP)

    def click_icon_restore(self):
        self.click_element(ConfigurationPopup.ICON_RESTORE)
        self.wait_for_element_not_present(ConfigurationPopup.ICON_RESTORE + "/following::span[@data-vwg_appliedvalue]")

    def click_system_button_close(self):
        self.click_element(ConfigurationPopup.SYSTEM_BUTTON_CLOSE)
        self.wait_for_element_not_present(ConfigurationPopup.POPUP_CONFIGURATION)

    def click_column_set_dropdown_button(self):
        self.hover(ConfigurationPopup.SYSTEM_BUTTON_DROP_DOWN)
        self.click_element(ConfigurationPopup.SYSTEM_BUTTON_DROP_DOWN)
        self.wait_for_element_present(ConfigurationPopup.DROP_DOWN_LIST)

    def select_columnset_in_configuration_popup_drop_down_list(self, columnsetname):
        self.click_column_set_dropdown_button()
        self.scroll_list_to_top()
        row = "//table[contains(@id,'VWGVL_')]/*//tr"
        scroll = "//div[contains(@id,'VWGVLSC_')]/div"
        scroll_height = self._find_element(scroll).size['height']
        row_height = self._find_element(row).size['height']
        rows_number = scroll_height / row_height
        # print "DROP-DOWN: list_height, one row height, number of rows are: ", scroll_height, row_height, rows_number
        element = ConfigurationPopup.DROP_DOWN_LIST + "/*//span[text()='" + columnsetname + "']"
        i = 0
        visible_rows = 8
        one_scroll = row_height * visible_rows
        step = one_scroll
        while i <= rows_number:
            cond = self.is_element_not_present(element)
            if cond:
                self.scroll_list_down(step)
                step += one_scroll
                i += visible_rows
            else:
                break
        self.click_element(ConfigurationPopup.DROP_DOWN_LIST + "/*//span[text()='" + columnsetname + "']")
        self.wait_for_element_not_present(self.DROP_DOWN_LIST)

    def check_columnset_is_selected_from_drop_down_list(self, columnsetname):
            cond = self.wait_for_element_present(
                ConfigurationPopup.DROP_DOWN_CONTAINER + "/*//span[text()='" + columnsetname + "']")
            return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(ConfigurationPopup.TEXT_FIELD_NAME).send_keys(sitename)
        self.click_element(ConfigurationPopup.TEXT_FIELD_NAME)

    def get_name_text_field_value(self):
        elem = ConfigurationPopup.TEXT_FIELD_NAME
        actual_attribute_value = self.get_attribute_value(elem, "value")
        print ("The actual value in the Name textfield is: " + actual_attribute_value)
        return actual_attribute_value


class SiteNamePopup(Base):

    FRAME = "//span[contains(text(),'Site') and contains(text(),'Name')]/ancestor::div[contains(@id,'WRP')]"

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(SiteNamePopup.FRAME + "/*" + Locators._FIELD).send_keys(sitename)

    def click_button_ok(self):
        self.click_element(SiteNamePopup.FRAME + "/*" + Locators.BTN_OK)
        self.wait_for_element_not_present(SiteNamePopup.FRAME)

    def click_system_button_close(self):
        self.click_element(SiteNamePopup.FRAME + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(SiteNamePopup.FRAME)

    def click_button_cancel(self):
        self.click_element(SiteNamePopup.FRAME + "/*" + Locators.BTN_CANCEL)
        self.wait_for_element_not_present(SiteNamePopup.FRAME)

    def check_is_popup_present(self):
        cond = self.is_element_present(SiteNamePopup.FRAME)
        return True if cond else False


class AreYouSurePopup(Base):
    # CONSTANTS
    POPUP_ARE_YOU_SURE = Locators.POPUP_ARE_YOU_SURE
    BUTTON_CANCEL = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_CANCEL
    BUTTON_NO = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_NO
    BUTTON_YES = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_YES
    BUTTON_OK = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_OK
    # SYSTEM_BUTTON_CLOSE = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.SYS_BTN_CLOSE

    def check_is_popup_present(self):
        cond = self.is_element_present(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_button_ok(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_OK)
        self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)

    def click_system_button_close(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)

    def click_button_cancel(self):
        self.click_element(self.BUTTON_CANCEL)
        self.wait_for_element_not_present(self.POPUP_ARE_YOU_SURE)

    def click_button_no(self):
        self.click_element(self.BUTTON_NO)
        self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)

    def click_button_yes(self):
        self.click_element(self.BUTTON_YES)
        self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)


class UnableToRemovePopup(Base):
    # CONSTANTS
    POPUP_UNABLE_TO_REMOVE = Locators.POPUP_UNABLE_TO_REMOVE
    BUTTON_OK = Locators.POPUP_UNABLE_TO_REMOVE + "/*" + Locators.BTN_Ok
    SYSTEM_BUTTON_CLOSE = Locators.POPUP_UNABLE_TO_REMOVE + "/*" + Locators.SYS_BTN_CLOSE

    def check_is_popup_present(self):
        cond = self.is_element_present(self.POPUP_UNABLE_TO_REMOVE)
        return True if cond else False

    def click_button_ok(self):
        self.click_element(self.BUTTON_OK)
        self.wait_for_element_not_present(self.POPUP_UNABLE_TO_REMOVE)

    def click_system_button_close(self):
        self.click_element(self.SYSTEM_BUTTON_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)


class ErrorPopup(Base):

    POPUP_ERROR = Locators.POPUP_ERROR

    def click_system_button_close(self):
        self.click_element(self.POPUP_ERROR + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(self.POPUP_ERROR)

    def click_button_ok(self):
        self.click_element(self.POPUP_ERROR + "/*" + Locators.BTN_Ok)
        self.wait_for_element_not_present(self.POPUP_ERROR)

    def check_is_popup_present(self):
        cond = self.is_element_present(self.POPUP_ERROR)
        return True if cond else False

