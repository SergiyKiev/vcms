
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
        self.wait_for_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def click_column_sets_popup_button_edit(self):
        # self.click_button_edit(self.POPUP_COLUMN_SETS)
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_EDIT)
        self.wait_for_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)

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
    POPUP_COLUMN_SET_DESIGNER = Locators.POPUP_COLUMN_SET_DESIGNER
    CSD_BUTTON_OK = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_OK
    CSD_BUTTON_CANCEL = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_CANCEL
    CSD_BUTTON_ADD = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_ADD_right
    CSD_BUTTON_REMOVE = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_REMOVE_left
    CSD_BUTTON_ARROW_UP = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_ARROW_UP
    CSD_BUTTON_ARROW_DOWN = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_ARROW_DOWN
    # TEXT_FIELD_NAME = Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[2]/input"
    # TEXT_FIELD_DESCRIPTION = Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[1]/input"
    CSD_LEFT_SIDE_TREE = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_PADDING_CONTAINER
    CSD_LEFT_SIDE_SUBNODE = CSD_LEFT_SIDE_TREE + "/*//" + Locators.EL_SUBNODE_CONTAINER
    CSD_LEFT_SIDE_NODE = CSD_LEFT_SIDE_TREE + "/*//" + Locators.EL_NODE_CONTAINER
    CSD_ICON_HELP = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.ICON_HELP
    CSD_TABLE_HEADER_COLUMNS = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_COLUMNS
    CSD_TABLE_HEADER_DEFAULT_WIDTH = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_DEFAULT_WIDTH
    CSD_TABLE_HEADER_AGGREGATE = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_AGGREGATE
    CSD_TABLE_BODY = Locators.POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABLE_BODY
    CSD_ELEMENT_NODE_CONTAINER = Locators.EL_NODE_CONTAINER
    CSD_ARROW_EXPAND = Locators.ARROW_EXPAND

    def check_is_popup_present(self):
        cond = self.is_element_present(self.POPUP_COLUMN_SET_DESIGNER)
        return True if cond else False

    def click_button_ok(self):
        self.click_element(self.POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_OK)
        self.wait_for_element_not_present(self.POPUP_COLUMN_SET_DESIGNER)

    def click_button_cancel(self):
        self.click_element(self.CSD_BUTTON_CANCEL)
        self.wait_for_element_not_present(self.POPUP_COLUMN_SET_DESIGNER)

    def click_button_add(self, columnname):
        self.click_element(self.CSD_BUTTON_ADD)
        self.wait_for_element_present(self.CSD_TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")

    def click_system_button_close(self):
        self.click_element(Locators.POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def click_system_button_maximize(self):
        self.click_element(self.POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.SYS_BTN_MAXIMIZE)
        time.sleep(2)
        self.wait_for_element_present(Locators.SYS_BTN_RESTORE_DOWN)

    def enter_text_into_text_field_name(self, columnsetname):
        self.find_element_self(Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[2]/input").send_keys(columnsetname)

    def enter_text_into_text_field_description(self, text):
        self.find_element_self(Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[1]/input").send_keys(text)

    def click_column_in_left_side_tree(self, columnname):
        elem = self.CSD_LEFT_SIDE_SUBNODE + "/*//span[text()='" + columnname + "']"
        self.click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + self.CSD_ELEMENT_NODE_CONTAINER)

    def expand_all_left_side_lists(self):
        elements = self.find_elements_self(self.CSD_LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        for x in range(0, len(elements)):
            elem = self.CSD_LEFT_SIDE_TREE + "/div[" + str(x + 1) + "]/div/div[contains(@id,'VWGJOINT')]"
            self.expand_tree(elem)

    def add_columns_to_list_view(self, columns_list):
        self.expand_all_left_side_lists()
        for columnname in list(columns_list):
            self.click_column_in_left_side_tree(columnname)
            self.click_button_add(columnname)
            # self.check_is_columnname_in_list_view(columnname)

    def check_is_columnname_in_list_view(self, columnname):
        cond = self.is_element_present(self.CSD_TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")
        return True if cond else False


class ConfigurationPopup(Base):
    #CONSTANTS
    POPUP_CONFIGURATION = Locators.POPUP_CONFIGURATION
    TAB_PANEL = Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL
    TEXT_FIELD_NAME = Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_
    BUTTON_CLOSE = Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_CLOSE
    BUTTON_NEW = Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_NEW_by_text
    SYSTEM_BUTTON_CLOSE = Locators.POPUP_CONFIGURATION + "/*" + Locators.SYS_BTN_CLOSE
    SYSTEM_BUTTON_DROP_DOWN = Locators.POPUP_CONFIGURATION + "/*" + Locators.SYS_BTN_DROP_DOWN
    ICON_HELP = Locators.POPUP_CONFIGURATION + "/*" + Locators.ICON_HELP
    DROP_DOWN_LIST = "//" + Locators.EL_DROP_DOWN_LIST
    DROP_DOWN_CONTAINER = Locators.POPUP_CONFIGURATION + "/*//" + Locators.EL_DROP_DOWN_CONTAINER
    ICON_RESTORE = Locators.POPUP_CONFIGURATION + "/*" + Locators.ICON_RESTORE

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
        self.click_element(self.BUTTON_NEW)
        self.is_element_present(ColumnSetDesignerPopup.POPUP_COLUMN_SET_DESIGNER)

    def click_icon_help(self):
        self.click_element(self.ICON_HELP)

    def click_icon_restore(self):
        self.click_element(self.ICON_RESTORE)
        self.wait_for_element_not_present(self.ICON_RESTORE + "/following::span[@data-vwg_appliedvalue]")

    def click_system_button_close(self):
        self.click_element(self.SYSTEM_BUTTON_CLOSE)
        self.wait_for_element_not_present(self.POPUP_CONFIGURATION)

    def click_column_set_dropdown_button(self):
        self.hover(self.SYSTEM_BUTTON_DROP_DOWN)
        self.click_element(self.SYSTEM_BUTTON_DROP_DOWN)
        self.wait_for_element_present(self.DROP_DOWN_LIST)

    def select_columnset_in_configuration_popup_drop_down_list(self, columnsetname):
        self.click_column_set_dropdown_button()
        self.scroll_list_to_top()
        row = "//table[contains(@id,'VWGVL_')]/*//tr"
        scroll = "//div[contains(@id,'VWGVLSC_')]/div"
        scroll_height = self.find_element_self(scroll).size['height']
        row_height = self.find_element_self(row).size['height']
        rows_number = scroll_height / row_height
        print scroll_height, row_height, rows_number
        element = self.DROP_DOWN_LIST + "/*//span[text()='" + columnsetname + "']"
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
        self.click_element(self.DROP_DOWN_LIST + "/*//span[text()='" + columnsetname + "']")
        self.wait_for_element_not_present(self.DROP_DOWN_LIST)

    def enter_text_into_name_text_field(self, sitename):
        self.find_element_self(self.TEXT_FIELD_NAME).send_keys(sitename)
        self.click_element(self.TEXT_FIELD_NAME)

    def check_columnset_is_selected_from_drop_down_list(self, columnsetname):
        cond = self.wait_for_element_present(self.DROP_DOWN_CONTAINER + "/*//span[text()='" + columnsetname + "']")
        return True if cond else False

    def get_name_text_field_value(self):
        elem = self.TEXT_FIELD_NAME
        actual_attribute_value = self.get_attribute_value(elem, "value")
        print ("The actual Name text field value of the attribute 'value' is: " + actual_attribute_value)
        return actual_attribute_value


class NewSitePopup(Base):

    POPUP_SITE_NAME = Locators.POPUP_SITE_NAME

    def enter_text_into_name_text_field(self, sitename):
        self.find_element_self(self.POPUP_SITE_NAME + "/*" + Locators.FIELD_).send_keys(sitename)

    def click_button_ok(self):
        self.click_element(self.POPUP_SITE_NAME + "/*" + Locators.BTN_OK)
        self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)

    def click_system_button_close(self):
        self.click_element(self.POPUP_SITE_NAME + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)

    def click_button_cancel(self):
        self.click_element(self.POPUP_SITE_NAME + "/*" + Locators.BTN_CANCEL)
        self.wait_for_element_not_present(self.POPUP_SITE_NAME)

    def check_is_popup_present(self):
        cond = self.is_element_present(self.POPUP_SITE_NAME)
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
        # self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_OK)
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

