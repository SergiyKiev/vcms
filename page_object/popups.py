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

    def click_close_button(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_CLOSE)
        cond = self.is_element_not_present(Locators.POPUP_COLUMN_SETS)
        return True if cond else False

    def click_new_button(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_NEW)
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


class ColumnSetDesignerPopup(Base):
    pass





