from base import Base
from locators import Locators


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

    def click_i_agree_button(self):
        self.click_element(Locators.POPUP_TERMS_AND_CONDITIONS + "/*" + Locators.BTN_I_AGREE)
        self.wait_for_element_not_present(Locators.POPUP_TERMS_AND_CONDITIONS)

    def close_popup(self):
        cond = self.is_element_present(Locators.POPUP_TERMS_AND_CONDITIONS)
        if cond:
            self.click_i_agree_button()
        else:
            pass


class ColumnSetsPopup(Base):
    # CONSTANTS
    POPUP_COLUMN_SETS = Locators.POPUP_COLUMN_SETS
    BUTTON_OK = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_OK
    BUTTON_CANCEL = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_CANCEL
    BUTTON_NEW = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_NEW
    BUTTON_EDIT = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_EDIT
    BUTTON_COPY = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_COPY
    BUTTON_DELETE = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_DELETE
    BUTTON_SET_AS_DEFAULT = Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_SET_AS_DEFAULT
    SYSTEM_BUTTON_CLOSE = Locators.POPUP_COLUMN_SETS + "/*" + Locators.SYS_BTN_CLOSE
    ICON_HELP = Locators.POPUP_COLUMN_SETS + "/*" + Locators.ICON_HELP
    TABLE_HEADER_IS_DEFAULT = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_IS_DEFAULT
    TABLE_HEADER_NAME = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_NAME
    TABLE_HEADER_DESCRIPTION = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_DESCRIPTION
    TABLE_HEADER_COLUMNS = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_COLUMNS
    TABLE_BODY = Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABLE_BODY

    def click_column_sets_popup_button_ok(self):
        self.click_ok(self.POPUP_COLUMN_SETS)
        # self.wait_for_element_not_present(self.POPUP_COLUMN_SETS)

    def click_column_sets_popup_button_cancel(self):
        self.click_element(self.BUTTON_CANCEL)
        self.wait_for_element_not_present(self.POPUP_COLUMN_SETS)

    def click_column_sets_popup_button_new(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_NEW)
        self.wait_for_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def click_column_sets_popup_button_edit(self):
        self.click_button_edit(self.POPUP_COLUMN_SETS)
        # self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_EDIT)
        self.wait_for_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def click_column_sets_popup_button_copy(self, columnsetname):
        elem = self.POPUP_COLUMN_SETS + "/*//span[text()='Copy of " + columnsetname + "']"
        self.click_element(self.BUTTON_COPY)
        self.wait_for_element_present(elem)

    def click_column_sets_popup_button_delete(self, columnsetname):
        self.click_element(self.BUTTON_DELETE)
        self.wait_for_element_present(AreYouSurePopup.POPUP_ARE_YOU_SURE)

    def click_column_sets_popup_button_set_as_default(self):
        self.click_element(self.BUTTON_SET_AS_DEFAULT)

    def click_column_sets_popup_system_button_close(self):
        self.click_sytem_button_close(self.POPUP_COLUMN_SETS)

    def click_column_sets_popup_help_icon(self):
        self.click_element(self.ICON_HELP)

    def click_column_sets_popup_table_header_is_default(self):
        self.click_element(self.TABLE_HEADER_IS_DEFAULT)

    def click_column_sets_popup_table_header_name(self):
        self.click_element(self.TABLE_HEADER_NAME)

    def click_column_sets_popup_table_header_description(self):
        self.click_element(self.TABLE_HEADER_DESCRIPTION)

    def click_column_sets_popup_table_header_columns(self):
        self.click_element(self.TABLE_HEADER_COLUMNS)

    def click_columnset_in_column_sets_popup_table_list(self, columnsetname):
        elem = self.TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
        self.click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + Locators.EL_LIST_ROW)

    def delete_columnset_in_column_sets_popup_if_exist(self, columnsetname):
        elem = self.TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
        cond = self.is_element_present(elem)
        if cond:
            self.click_columnset_in_column_sets_popup_table_list(elem)
            self.click_column_sets_popup_button_delete(columnsetname)
            AreYouSurePopup.click_ok(AreYouSurePopup.POPUP_ARE_YOU_SURE)
            self.wait_for_element_not_present(elem)
            return True
        else:
            pass


class ConfigurationPopup(Base):
    #CONSTANTS
    POPUP_CONFIGURATION = Locators.POPUP_CONFIGURATION
    TAB_PANEL = Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL
    TEXT_FIELD_NAME = Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_
    BUTTON_CLOSE = Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_CLOSE
    BUTTON_NEW = Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_NEW_by_text
    SYSTEM_BUTTON_CLOSE = Locators.POPUP_CONFIGURATION + "/*" + Locators.SYS_BTN_CLOSE
    SYSTEM_BUTTON_DROP_DOWN = Locators.SYS_BTN_DROP_DOWN
    ICON_HELP = Locators.POPUP_CONFIGURATION + "/*" + Locators.ICON_HELP
    DROP_DOWN_LIST = Locators.POPUP_CONFIGURATION + "/following::" + Locators.EL_DROP_DOWN_LIST
    DROP_DOWN_CONTAINER = Locators.POPUP_CONFIGURATION + "/*//" + Locators.EL_DROP_DOWN_CONTAINER

    def check_configuration_popup_loaded(self):
        cond = self.is_element_present(self.POPUP_CONFIGURATION)
        return True if cond else False

    def check_name_text_feild_disabled(self):
        cond = self.is_element_disabled(self.TEXT_FIELD_NAME)
        return True if cond else False

    def click_configuration_popup_button_close(self):
        self.click_element(self.BUTTON_CLOSE)
        self.is_element_not_present(self.POPUP_CONFIGURATION)

    def click_configuration_popup_button_new(self):
        self.click_element(self.BUTTON_NEW)
        self.is_element_present(ColumnSetDesignerPopup.POPUP_COLUMN_SET_DESIGNER)

    def click_configuration_popup_icon_help(self):
        self.click_element(self.ICON_HELP)

    def click_system_button_close(self):
        self.click_element(self.SYSTEM_BUTTON_CLOSE)
        self.wait_for_element_not_present(self.POPUP_CONFIGURATION)

    def click_column_set_dropdown_button(self):
        self.click_element(self.SYSTEM_BUTTON_DROP_DOWN)
        self.wait_for_element_present(self.DROP_DOWN_LIST)

    def click_columnset_in_configuration_popup_drop_down_list(self, columnsetname):
        self.click_element(self.DROP_DOWN_LIST + "/*//span[text()='" + columnsetname + "']")
        self.wait_for_element_not_present(self.DROP_DOWN_LIST)
        self.wait_for_element_present(self.DROP_DOWN_CONTAINER + "/*//span[text()='" + columnsetname + "']")

    def get_configuration_popup_name_text_field_value(self):
        elem = self.TEXT_FIELD_NAME
        actual_attribute_value = self.get_attribute_value(elem, "value")
        print ("The actual Name text field value of the attribute 'value' is: " + actual_attribute_value)
        return actual_attribute_value

    def enter_text_into_configuration_popup_name_text_field(self, sitename):
        self.find_element_self(self.TEXT_FIELD_NAME).send_keys(sitename)
        self.click_element(self.TEXT_FIELD_NAME)

    def check_configuration_popup_columnset_is_selected_from_drop_down_list(self, columnsetname):
        self.wait_for_element_present(self.DROP_DOWN_CONTAINER + "/*//span[text()='" + columnsetname + "']")


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


class ColumnSetDesignerPopup(Base):
    #CONSTANTS
    POPUP_COLUMN_SET_DESIGNER = Locators.POPUP_COLUMN_SET_DESIGNER
    BUTTON_OK = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_OK
    BUTTON_CANCEL = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_CANCEL
    BUTTON_ADD = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_ADD_right
    BUTTON_REMOVE = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_REMOVE_left
    BUTTON_ARROW_UP = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_ARROW_UP
    BUTTON_ARROW_DOWN = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.BTN_ARROW_DOWN
    # TEXT_FIELD_NAME = Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[2]/input"
    # TEXT_FIELD_DESCRIPTION = Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[1]/input"
    COLUMN_SET_DESIGNER_LEFT_SIDE_TREE = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_PADDING_CONTAINER
    COLUMN_SET_DESIGNER_LEFT_SIDE_SUBNODE = COLUMN_SET_DESIGNER_LEFT_SIDE_TREE + "/*//" + Locators.EL_SUBNODE_CONTAINER
    COLUMN_SET_DESIGNER_LEFT_SIDE_NODE = COLUMN_SET_DESIGNER_LEFT_SIDE_TREE + "/*//" + Locators.EL_NODE_CONTAINER
    ICON_HELP = POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.ICON_HELP
    TABLE_HEADER_COLUMNS = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_COLUMNS
    TABLE_HEADER_DEFAULT_WIDTH = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_DEFAULT_WIDTH
    TABLE_HEADER_AGGREGATE = POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_AGGREGATE
    TABLE_BODY = Locators.POPUP_COLUMN_SET_DESIGNER + "/*//" + Locators.EL_TABLE_BODY
    ELEMENT_NODE_CONTAINER = Locators.EL_NODE_CONTAINER

    def check_column_set_designer_popup_is_present(self):
        cond = self.is_element_present(self.POPUP_COLUMN_SET_DESIGNER)
        return True if cond else False

    def click_column_set_designer_popup_button_ok(self):
        self.click_ok(self.POPUP_COLUMN_SET_DESIGNER)

    def click_column_set_designer_popup_button_cancel(self):
        self.click_element(self.BUTTON_CANCEL)
        self.wait_for_element_not_present(self.POPUP_COLUMN_SET_DESIGNER)

    def click_column_set_designer_popup_button_add(self, columnname):
        self.click_element(self.BUTTON_ADD)
        self.wait_for_element_present(self.TABLE_BODY + "/*//span[text()='" + columnname + "']")

    def enter_text_into_column_set_designer_popup_text_field_name(self, columnsetname):
        self.find_element_self(Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[2]/input").send_keys(columnsetname)

    def enter_text_into_column_set_designer_popup_text_field_description(self, text):
        self.find_element_self(Locators.POPUP_COLUMN_SET_DESIGNER + "/*//div[1]/input").send_keys(text)

    def click_column_in_column_set_designer_left_side_tree(self, columnname):
        elem = self.COLUMN_SET_DESIGNER_LEFT_SIDE_SUBNODE + "/*//span[text()='" + columnname + "']"
        self.click_element(elem)
        self.wait_for_element_selected(elem + "/ancestor::" + self.ELEMENT_NODE_CONTAINER)

    def expand_all_column_set_designer_left_side_trees(self):
        elements = self.find_elements_self(self.COLUMN_SET_DESIGNER_LEFT_SIDE_TREE + "/div")
        x = []
        for element in elements:
            self.find_element_self(self.COLUMN_SET_DESIGNER_LEFT_SIDE_NODE)
            self.click_element(element)
            x.append(element)
            print x


    def add_columns_to_column_set_designer_list_view(self, columns_list = None):
        self.expand_all_column_set_designer_left_side_trees()
        for columnname in list(columns_list):
            self.click_column_in_column_set_designer_left_side_tree(columnname)
            self.expand_all_column_set_designer_left_side_trees()
            self.click_column_set_designer_popup_button_add(columnname)
            self.check_columnname_is_in_column_set_designer_list_view(columnname)

    def check_columnname_is_in_column_set_designer_list_view(self, columnname):
        cond = self.is_element_present(self.COLUMN_SET_DESIGNER_LEFT_SIDE_TREE + "/*//span[text()='" + columnname + "']")
        return True if cond else False


class AreYouSurePopup(Base):
    # CONSTANTS
    POPUP_ARE_YOU_SURE = Locators.POPUP_ARE_YOU_SURE
    BUTTON_CANCEL = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_CANCEL
    BUTTON_NO = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_NO
    # BUTTON_OK = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_OK
    # SYSTEM_BUTTON_CLOSE = Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.SYS_BTN_CLOSE

    def check_is_popup_present(self):
        cond = self.is_element_present(self.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_button_ok(self):
        self.click_ok(self.POPUP_ARE_YOU_SURE)
        # self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_OK)
        # self.wait_for_element_not_present(self.POPUP_ARE_YOU_SURE)

    def click_system_button_close(self):
        self.click_sytem_button_close(self.POPUP_ARE_YOU_SURE)
        # self.wait_for_element_not_present(self.POPUP_ARE_YOU_SURE)

    def click_button_cancel(self):
        self.click_element(self.BUTTON_CANCEL)
        self.wait_for_element_not_present(self.POPUP_ARE_YOU_SURE)

    def click_button_no(self):
        self.click_element(self.BUTTON_NO)
        self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)


class UnableToRemovePopup(Base):
    # CONSTANTS
    POPUP_UNABLE_TO_REMOVE = Locators.POPUP_UNABLE_TO_REMOVE
    # BUTTON_OK = Locators.POPUP_UNABLE_TO_REMOVE + "/*" + Locators.BTN_Ok
    SYSTEM_BUTTON_CLOSE = Locators.POPUP_UNABLE_TO_REMOVE + "/*" + Locators.SYS_BTN_CLOSE

    def check_unable_to_remove_popup_is_present(self):
        cond = self.is_element_present(self.POPUP_UNABLE_TO_REMOVE)
        return True if cond else False

    def click_unable_to_remove_popup_button_ok(self):
        self.click_ok(self.POPUP_UNABLE_TO_REMOVE)
        self.wait_for_element_not_present(self.POPUP_UNABLE_TO_REMOVE)

    def click_unable_to_remove_popup_system_button_close(self):
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
