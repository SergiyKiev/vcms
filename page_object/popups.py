from base import Base
from locators import Locators


class ColumnSetsPopup(Base):

    def click_ok_button(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_OK)
        cond = self.is_element_not_present(Locators.POPUP_COLUMN_SETS)
        return True if cond else False

    def click_cancel_button(self, locator):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_CANCEL)
        cond = self.is_element_not_present(Locators.POPUP_COLUMN_SETS)
        return True if cond else False

    def click_new_button(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_NEW)
        cond = self.is_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)
        return True if cond else False

    def click_edit_button(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_EDIT)
        cond = self.is_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)
        return True if cond else False

    def click_copy_button(self, columnsetname):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_COPY)

    def click_delete_button(self, columnsetname):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_DELETE)

    def click_set_as_default_button(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_SET_AS_DEFAULT)

    def click_system_button_close(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.SYS_BTN_CLOSE)
        cond = self.is_element_not_present(Locators.POPUP_COLUMN_SETS)
        return True if cond else False

    def click_help_icon(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_ICON_HELP)

    def click_is_default_table_header(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_TABEL_HEADER + "/*" + Locators.TEXT_CONTAINS_COLUMN_SETS)

    def click_name_table_header(self):
        self.click_element(Locators.POPUP_COLUMN_SETS)

    def click_description_table_header(self):
        self.click_element(Locators.POPUP_COLUMN_SETS)

    def click_columns_table_header(self):
        self.click_element(Locators.POPUP_COLUMN_SETS)


class ConfigurationPopup(Base):

    #CONSTANTS
    TAB_PANEL = Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_PANEL
    TEXT_FIELD_NAME = Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_
    BUTTON_CLOSE = Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_CLOSE
    BUTTON_ICON_HELP = Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_ICON_HELP
    BUTTON_NEW = Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_NEW_by_text

    def click_button_close(self):
        self.click_element(self.BUTTON_CLOSE)
        self.is_element_not_present(Locators.POPUP_COLUMN_SETS)

    def click_button_new(self):
        self.click_element(self.BUTTON_NEW)
        self.is_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def click_icon_help(self):
        self.click_element(self.BUTTON_ICON_HELP)

    def check_configuration_popup_loaded(self):
        cond = self.is_element_present(self.TAB_PANEL)
        return True if cond else False

    def check_name_text_feild_disabled(self):
        cond = self.is_element_disabled(self.TEXT_FIELD_NAME)
        return True if cond else False

    def get_name_text_field_value(self):
        elem = self.TEXT_FIELD_NAME
        actual_attribute_value = self.get_attribute_value(elem, "value")
        print ("The actual Name text field value of the attribute 'value' is: " + actual_attribute_value)
        return actual_attribute_value


class NewSitePopup(Base):
    pass


class ColumnSetDesignerPopup(Base):
    pass





