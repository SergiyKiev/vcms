from _base_page.base_actions import BaseActions
from _feature_objects._popups.popupAreYouSure import AreYouSurePopup
from _feature_objects._popups.popupColumnSetDesigner import ColumnSetDesignerPopup


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

    def check_popup_is_present(self):
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