import time
from _base.base_actions import BaseActions
from _base.base_elements import BaseElements


class BasePopup(BaseActions):

    def _set_popup(self, name):
        locator = "//span[text()='" + str(name) + "']" \
                                    "[@dir='LTR'][contains(@style,'White')]/ancestor::div[contains(@id,'WRP')][last()]"
        # locator = "//span[text()='" + str(name) + "'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
        return str(locator)

    def _set_popup_header(self, set_popup_method):
        locator = str(set_popup_method) + "/div[@class='Panel-Control']"
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else None

    def _set_popup_table_header(self, set_screen_method): #INPUT SCREEN METHOD FOR CURRENT SCREEN
        locator = str(set_screen_method) + BaseElements.TABLE_HEADER
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else None

    def _set_popup_table_body(self, set_screen_method):
        locator = str(set_screen_method) + BaseElements.TABLE_BODY
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else None



class AdminAccountsPopup(BaseActions):

    BODY = "//span[text()='Admin Accounts'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    BUTTON_ADD_MEMBERS = BODY + "/*//span[text()='Add Members']/ancestor::div[contains(@class,'Button')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    FIELD_GROUP_NAME = BODY + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(AdminAccountsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(AdminAccountsPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(AdminAccountsPopup.BODY)
        self._wait_for_element_not_present(AdminAccountsPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(AdminAccountsPopup.BODY)
        self._wait_for_element_not_present(AdminAccountsPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(AdminAccountsPopup.BODY)

    def click_button_add_members(self):
        self._click_element(AdminAccountsPopup.BUTTON_ADD_MEMBERS)
        self._wait_for_element_present(SelectTargetsPopup.BODY)

    def enter_text_into_group_name_text_field(self, text = None):
        self._find_element(AdminAccountsPopup.FIELD_GROUP_NAME).send_keys(text)

    def click_button_add(self):
        self._click_button_add(AdminAccountsPopup.BODY)
        self._wait_for_element_present(UserConfigurationPopup.BODY)


class AreYouSurePopup(BaseActions):

    # PAGE_BODY = "//span[text()='Are you sure?'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    ARE_YOU_SURE = "Are you sure?"

    def _set_popup(self, locator):
        body = "//span[text()='" + locator + "'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
        return body

    def _get_popup(self):
        body = self._set_popup(self.ARE_YOU_SURE)
        # print "PopupBase: ", body
        return body

    def click_button_ok(self):
        self._click_button_ok(self._get_popup())
        # self._click_button_ok(self.PAGE_BODY)

    def click_system_button_close(self):
       self._click_system_button_close(self._get_popup())
       # self._click_system_button_close(self.PAGE_BODY)

    def click_button_cancel(self):
        self._click_button_cancel(self._get_popup())
        # self._click_button_cancel(self.PAGE_BODY)

    def click_button_no(self):
        self._click_button_no(self._get_popup())
        # self._click_button_no(self.PAGE_BODY)

    def click_button_yes(self):
        self._click_button_yes(self._get_popup())
        # self._click_button_yes(self.PAGE_BODY)

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(self._get_popup())
        # cond = self._wait_for_element_present(self.PAGE_BODY)
        return True if cond else False


class ColumnSetDesignerPopup(BaseActions):
    #CONSTANTS
    BODY = "//span[text()='Column Set Designer'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    BUTTON_ADD = BODY + "/*//span[text()='Add >>']/ancestor::div[contains(@class,'Button')]"
    BUTTON_REMOVE = BODY + "/*//span[text()='<< Remove']/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_UP = BODY + BaseElements.BUTTON_ARROW_UP
    BUTTON_ARROW_DOWN = BODY + BaseElements.BUTTON_ARROW_DOWN
    TEXT_FIELD_NAME = BODY  + "/*//div[2]/input"
    TEXT_FIELD_DESCRIPTION = BODY  + "/*//div[1]/input"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ColumnSetDesignerPopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ColumnSetDesignerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ColumnSetDesignerPopup.BODY)

    def click_button_add(self, columnname):
        self._click_element(ColumnSetDesignerPopup.BUTTON_ADD)
        self._wait_for_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")

    def click_icon_help(self):
        self._click_icon_help(ColumnSetDesignerPopup.BODY)

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
        self._wait_for_element_selected(elem + ColumnSetDesignerPopup.ELEMENT_LABEL)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(ColumnSetDesignerPopup.LEFT_SIDE_NODE)

        # self._wait_for_element_present(ColumnSetDesignerPopup.PAGE_BODY)
        # elements = self._find_elements(ColumnSetDesignerPopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        # elements = self._find_elements(ColumnSetDesignerPopup.LEFT_SIDE_TREE + BaseElements.ARROW_EXPAND)
        # for element in elements:
        #     self.driver.execute_script("arguments[0].click();", element)

    def collaps_all_left_side_trees(self):
        self._collaps_all_trees(ColumnSetDesignerPopup.LEFT_SIDE_NODE)


    def add_columns_to_list_view(self, columns_list):
        for columnname in list(columns_list):
            self.scroll_to_element(ColumnSetDesignerPopup.BODY + "/*//span[contains(text(),'" + columnname + "')]")
            self.click_column_in_left_side_tree(columnname)
            self.click_button_add(columnname)

    def check_is_columnname_in_list_view(self, columnname):
        cond = self._wait_for_element_present(ColumnSetDesignerPopup.TABLE_BODY + "/*//span[contains(text(),'" + columnname + "')]")
        return True if cond else False

    def create_columnset(self, columnsetname=None, columns_list=None):
        self.click_system_button_maximize()
        self.enter_text_into_text_field_name(columnsetname)
        self.expand_all_left_side_trees()
        self.add_columns_to_list_view(columns_list)
        self.click_button_ok()


class ColumnSetsPopup(BaseActions):

    BODY = "//span[contains(text(),'Column Sets')][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
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
        # self._click_element(self.PAGE_BODY + "/*" + Locators.BTN_OK)
        # self._wait_for_element_not_present(self.PAGE_BODY)

    def click_icon_help(self):
        self._click_icon_help(ColumnSetsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Column Sets")
        return True if cond else False

    def click_button_cancel(self):
        self._click_button_cancel(ColumnSetsPopup.BODY)

    def click_button_new(self):
        self._click_element(ColumnSetsPopup.BUTTON_NEW)
        self._wait_for_element_present(ColumnSetDesignerPopup.BODY)

    def click_popup_button_edit(self):
        self._click_element(ColumnSetsPopup.BUTTON_EDIT)
        self._wait_for_element_present(ColumnSetDesignerPopup.BODY)

    def click_popup_button_copy(self):
        self._click_element(ColumnSetsPopup.BUTTON_COPY)
        # self._wait_for_element_present(ColumnSetsPopup.TABLE_BODY + "/*//span[text()='Copy of " + columnsetname + "']")

    def click_button_delete(self):
        self._click_element(ColumnSetsPopup.BUTTON_DELETE)
        # self._wait_for_element_present(AreYouSurePopup.PAGE_BODY)

    def click_popup_button_set_as_default(self):
        self._click_element(ColumnSetsPopup.BUTTON_SET_AS_DEFAULT)

    def click_system_button_close(self):
        self._click_system_button_close(ColumnSetsPopup.BODY)

    def click_popup_help_icon(self):
        self._click_icon_help(ColumnSetsPopup.BODY)

    def click_popup_table_header_is_default(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_IS_DEFAULT)

    def click_popup_table_header_name(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_NAME)

    def click_popup_table_header_description(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_DESCRIPTION)

    def click_popup_table_header_columns(self):
        self._click_element(ColumnSetsPopup.TABLE_HEADER_COLUMNS)

    def click_columnset_in_table_list(self, columnsetname):
        element = ColumnSetsPopup.TABLE_BODY + "/*//span[text()='" + columnsetname + "']" + ColumnSetsPopup.TABLE_ROW
        self._click_element(element)
        self._wait_for_element_selected(element)

    def check_is_columnset_present(self, columsetname):
        cond = self._wait_for_element_present(ColumnSetsPopup.TABLE_BODY + "/*//span[text()='" + columsetname  + "']")
        return True if cond else False

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ColumnSetsPopup.BODY)
        return True if cond else False

    def delete_columnset_if_exists(self, columnsetname):
        elem = ColumnSetsPopup.TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
        cond = self._is_element_present(elem)
        if cond:
            ColumnSetsPopup.click_columnset_in_table_list(self, columnsetname)
            ColumnSetsPopup.click_button_delete(self)
            are_you_sure_popup = AreYouSurePopup(self.driver)
            are_you_sure_popup.click_button_yes()
            self._wait_for_element_not_present(elem)
        else:
            pass


class ConditionEditorPopup(BaseActions):

    BODY = "//span[text()='Condition Editor'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ConditionEditorPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ConditionEditorPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create a Query")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ConditionEditorPopup.BODY)
        self._wait_for_element_not_present(ConditionEditorPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ConditionEditorPopup.BODY)
        self._wait_for_element_not_present(ConditionEditorPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ConditionEditorPopup.BODY)


class ConnectingPopup(BaseActions):

    CONNECTING = "//span[text()='Connecting....'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    PING = "//span[text()='Ping....'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def _check_popup_is_present(self, name):
        global BODY
        NAME = "//span[text()='" + str(name) + "'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
        PARTIAL_NAME = "//span[contains(text(),'" + name + "')][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
        full_name = self._is_element_present(NAME)
        partial_name = self._is_element_present(PARTIAL_NAME)
        if full_name:
            BODY = NAME
        elif partial_name:
            BODY = PARTIAL_NAME
        cond = self._wait_for_element_present(BODY)
        return str(BODY) if cond else None

    def check_popup_is_present(self):
        cond = self._check_popup_is_present("Connecting")
        return True if cond is not None else False

    def _get_popup(self):
        name = self._check_popup_is_present("Connecting")
        return str(name) if name is not None else None

    def click_button_close(self):
        self._click_button_close(self._get_popup())
        self._wait_for_element_not_present(self._get_popup())


class CurrencyPopup(BaseActions):

    BODY = "//span[text()='Currency'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(CurrencyPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(CurrencyPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Currency")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(CurrencyPopup.BODY)
        self._wait_for_element_not_present(CurrencyPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(CurrencyPopup.BODY)
        self._wait_for_element_not_present(CurrencyPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(CurrencyPopup.BODY)


class DiscoverDevicesPopup(BasePopup):

    DISCOVER_DEVICES = "Discover Devices"

    def popup_body(self):
        locator = self._set_popup(self.DISCOVER_DEVICES)
        return str(locator)

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(self.popup_body())
        msg_true = "Popup '" + self.DISCOVER_DEVICES + "' is present"
        msg_false = "Popup '" + self.DISCOVER_DEVICES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())


class SoftwareDeploymentPopup(BasePopup):

    SOFTWARE_DEPLOYMENT = "Software Deployment"

    def popup_body(self):
        locator = self._set_popup(self.SOFTWARE_DEPLOYMENT)
        return str(locator)

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(self.popup_body())
        msg_true = "Popup '" + self.SOFTWARE_DEPLOYMENT + "' is present"
        msg_false = "Popup '" + self.SOFTWARE_DEPLOYMENT + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())


class PatchManagerScanningPopup(BasePopup):

    PATCH_MANAGER_SCANNING = "Patch Manager Scanning"

    def popup_body(self):
        locator = self._set_popup(self.PATCH_MANAGER_SCANNING)
        return str(locator)

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(self.popup_body())
        msg_true = "Popup '" + self.PATCH_MANAGER_SCANNING + "' is present"
        msg_false = "Popup '" + self.PATCH_MANAGER_SCANNING + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())


class DeploySoftwareUpdatesPopup(BasePopup):

    DEPLOY_SOFTWARE_UPDATES = "Deploy Software Updates"

    def popup_body(self):
        locator = self._set_popup(self.DEPLOY_SOFTWARE_UPDATES)
        return str(locator)

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(self.popup_body())
        msg_true = "Popup '" + self.DEPLOY_SOFTWARE_UPDATES + "' is present"
        msg_false = "Popup '" + self.DEPLOY_SOFTWARE_UPDATES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())


class EditFolderPopup(BaseActions):

    BODY = "//span[text()='Edit Folder'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_EDIT_FOLDER = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(EditFolderPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EditFolderPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(EditFolderPopup.BODY)
        self._wait_for_element_not_present(EditFolderPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(EditFolderPopup.BODY)
        self._wait_for_element_not_present(EditFolderPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(EditFolderPopup.BODY)

    def enter_text_into_edit_folder_text_field(self, name):
        self._find_element(EditFolderPopup.FIELD_EDIT_FOLDER).send_keys(name)


class EndUserAccessPopup(BaseActions):

    BODY = "//span[text()=End User Access'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(EndUserAccessPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EndUserAccessPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("End User Access")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(EndUserAccessPopup.BODY)
        self._wait_for_element_not_present(EndUserAccessPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(EndUserAccessPopup.BODY)


class ErrorPopup(BaseActions):

    ERROR = "Error"
    BODY = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ErrorPopup.BODY)
        msg_true = "Popup '" + self.ERROR + "' is present"
        msg_false = "Popup '" + self.ERROR + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_popup_is_not_present(self):
        cond = self._is_element_not_present(ErrorPopup.BODY)
        msg_false = "Popup '" + self.ERROR + "' is present"
        msg_true = "Popup '" + self.ERROR + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ErrorPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(ErrorPopup.BODY)


class EventViewerPopup(BaseActions):

    BODY = "//span[text()='Event Viewer'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    TABLE_HEADER_TYPE = TABLE_HEADER + "/*//span[contains(text(),'Type')]"
    TABLE_HEADER_SIZE = TABLE_HEADER + "/*//span[contains(text(),'Size')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(EventViewerPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EventViewerPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(EventViewerPopup.BODY)
        self._wait_for_element_not_present(EventViewerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(EventViewerPopup.BODY)
        self._wait_for_element_not_present(EventViewerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(EventViewerPopup.BODY)

    def click_label_in_left_side_tree(self, label):
        elem = EventViewerPopup.LEFT_SIDE_SUBNODE + \
               "/*//span[text()='" + label + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_label(elem)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(EventViewerPopup.LEFT_SIDE_TREE)

    def check_text_is_in_list_view(self, text):
        cond = self._wait_for_element_present(EventViewerPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False

    def select_device_in_table(self, name):
        self._wait_for_element_present(EventViewerPopup.TABLE_ROW)
        row = EventViewerPopup.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class ExcludeDevicePopup(BaseActions):

    EXCLUDE_DEVICE = "Exclude Device"
    BODY = "//span[text()='Exclude Device'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ExcludeDevicePopup.BODY)
        msg_true = "Popup '" + self.EXCLUDE_DEVICE + "' is present"
        msg_false = "Popup '" + self.EXCLUDE_DEVICE + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(ExcludeDevicePopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(ExcludeDevicePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ExcludeDevicePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ExcludeDevicePopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ExcludeDevicePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclude Device")
        return True if cond else False


class ExcludeIPAddressPopup(BaseActions):

    BODY = "//span[text()='Exclude IP Address'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ExcludeIPAddressPopup.BODY)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(ExcludeIPAddressPopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(ExcludeIPAddressPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ExcludeIPAddressPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ExcludeIPAddressPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ExcludeIPAddressPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclude IP Address")
        return True if cond else False


class ExcludeSitePopup(BaseActions):

    BODY = "//span[text()='Exclude Site'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ExcludeSitePopup.BODY)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(ExcludeSitePopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(ExcludeSitePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ExcludeSitePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ExcludeSitePopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ExcludeSitePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclude Site")
        return True if cond else False


class FileExplorerPopup(BaseActions):

    BODY = "//span[text()='File Explorer'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(FileExplorerPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(FileExplorerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("File Explorer")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(FileExplorerPopup.BODY)


class InitialSetupPopup(BaseActions):

    BODY = "//span[text()='Welcome To Cloud Management Suite'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(InitialSetupPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(InitialSetupPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Initial Setup")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(InitialSetupPopup.BODY)


class InventoryViewPopup(BaseActions):

    #CONSTANTS
    BODY = "//div[contains(@id,'WRP')][last()]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self, name):
        element = "//span[text()='" + name + "'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
        cond = self._wait_for_element_present(element)
        # cond = self._wait_for_element_present(InventoryViewPopup.PAGE_BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(InventoryViewPopup.BODY)

    def click_button_close(self):
        self._click_button_close(InventoryViewPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(InventoryViewPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(InventoryViewPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Inventory")
        return True if cond else False

    def click_label_in_left_side_tree(self, label):
        elem = InventoryViewPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + label + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_label(elem)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(InventoryViewPopup.LEFT_SIDE_TREE)

    def check_text_is_in_list_view(self, text):
        cond = self._wait_for_element_present(InventoryViewPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False


class IPAddressPopup(BaseActions):

    BODY = "//span[text()='IP Address'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_START = BODY + "/*//div[4]/input"
    FIELD_END = BODY + "/*//div[1]/input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(IPAddressPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(IPAddressPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(IPAddressPopup.BODY)
        self._wait_for_element_not_present(IPAddressPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(IPAddressPopup.BODY)
        self._wait_for_element_not_present(IPAddressPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(IPAddressPopup.BODY)

    def enter_start_ip_address(self, ipaddress = "0.0.0.0"):
        self._find_element(IPAddressPopup.FIELD_START).send_keys(ipaddress)

    def enter_end_ip_address(self, ipaddress = "1.1.1.1"):
        self._find_element(IPAddressPopup.FIELD_END).send_keys(ipaddress)


class MaintenanceWindowPopup(BaseActions):

    BODY = "//span[text()='Maintenance Window'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def popup_body(self):
        pass

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(MaintenanceWindowPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(MaintenanceWindowPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Move a site or device")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(MaintenanceWindowPopup.BODY)
        self._wait_for_element_not_present(MaintenanceWindowPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(MaintenanceWindowPopup.BODY)
        self._wait_for_element_not_present(MaintenanceWindowPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(MaintenanceWindowPopup.BODY)


class ManufacturerAliasPopup(BaseActions):

    BODY = "//span[text()='Manufacturer Alias'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ManufacturerAliasPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ManufacturerAliasPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Manufacturers")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ManufacturerAliasPopup.BODY)
        self._wait_for_element_not_present(ManufacturerAliasPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ManufacturerAliasPopup.BODY)


class ModelAliasPopup(BaseActions):

    BODY = "//span[text()='Model Alias'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ModelAliasPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ModelAliasPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Models")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ModelAliasPopup.BODY)
        self._wait_for_element_not_present(ModelAliasPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ModelAliasPopup.BODY)


class MoveDevicePopup(BaseActions):

    BODY = "//span[text()='Move Device'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"


    def check_popup_is_present(self):
        cond = self._wait_for_element_present(MoveDevicePopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(MoveDevicePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Move a site or device")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(MoveDevicePopup.BODY)
        self._wait_for_element_not_present(MoveDevicePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(MoveDevicePopup.BODY)
        self._wait_for_element_not_present(MoveDevicePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(MoveDevicePopup.BODY)

    def click_label_in_left_side_tree(self, label):
        elem = MoveDevicePopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + label + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_label(elem)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(MoveDevicePopup.LEFT_SIDE_TREE)
        # self._wait_for_element_present(MoveDevicePopup.PAGE_BODY)
        # elements = self._find_elements(MoveDevicePopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        # for element in elements:
        #     self.driver.execute_script("arguments[0].click();", element)

    def check_text_is_in_list_view(self, text):
        cond = self._wait_for_element_present(MoveDevicePopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False

    def select_device_in_table(self, name):
        self._wait_for_element_present(MoveDevicePopup.TABLE_ROW)
        row = MoveDevicePopup.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class MoveSitePopup(BaseActions):

    BODY = "//span[text()='Move Site'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(MoveSitePopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(MoveSitePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Move a site or device")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(MoveSitePopup.BODY)
        self._wait_for_element_not_present(MoveSitePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(MoveSitePopup.BODY)
        self._wait_for_element_not_present(MoveSitePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(MoveSitePopup.BODY)


class NewFolderPopup(BaseActions):

    NEW_FOLDER = "New Folder"
    BODY = "//span[text()='New Folder'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    FIELD_NEW_FOLDER = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(NewFolderPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(NewFolderPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("New Folder")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(NewFolderPopup.BODY)
        self._wait_for_element_not_present(NewFolderPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(NewFolderPopup.BODY)
        self._wait_for_element_not_present(NewFolderPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(NewFolderPopup.BODY)


    def click_button_add_members(self):
        self._click_button_cancel(NewFolderPopup.BODY)
        self._wait_for_element_not_present(NewFolderPopup.BODY)

    def enter_text_into_new_folder_text_field(self, name):
        self._find_element(NewFolderPopup.FIELD_NEW_FOLDER).send_keys(name)


class NewGroupPopup(BaseActions):

    BODY = "//span[text()='New Group'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    BUTTON_ADD_MEMBERS = BODY + "/*//span[text()='Add Members']/ancestor::div[contains(@class,'Button')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    FIELD_GROUP_NAME = BODY + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(NewGroupPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(NewGroupPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create a new Group")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(NewGroupPopup.BODY)
        self._wait_for_element_not_present(NewGroupPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(NewGroupPopup.BODY)
        self._wait_for_element_not_present(NewGroupPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(NewGroupPopup.BODY)

    def click_button_add_members(self):
        self._click_element(NewGroupPopup.BUTTON_ADD_MEMBERS)
        self._wait_for_element_present(SelectTargetsPopup.BODY)

    def enter_text_into_group_name_text_field(self, text = None):
        self._find_element(NewGroupPopup.FIELD_GROUP_NAME).send_keys(text)


class OnDemandInventoryScanPopup(BaseActions):

    BODY = "//span[text()='On demand inventory scan'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    BUTTON_START_NOW = BODY + "/*//span[text()='Start Now']/ancestor::div[contains(@class,'RibbonBarButton')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(OnDemandInventoryScanPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(OnDemandInventoryScanPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("On Demand Inventory Scan")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(OnDemandInventoryScanPopup.BODY)
        self._wait_for_element_not_present(OnDemandInventoryScanPopup.BODY)

    def click_button_start_now(self):
        self._click_element(OnDemandInventoryScanPopup.BUTTON_START_NOW)

    def click_system_button_close(self):
        self._click_system_button_close(OnDemandInventoryScanPopup.BODY)


class PatchManagerPopup(BaseActions):
    #CONSTANTS
    BODY = "//span[text()='Patch Manager'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    SEARCH_FIELD = BODY + "/*//input"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    TABLE_ROW = "/ancestor::tr[contains(@class,'ListView-DataFullRow')]"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(PatchManagerPopup.BODY)
        return True if cond else False

    def check_device_name_is_present(self, device_name):
        cond = self._wait_for_element_present(PatchManagerPopup.BODY + "/*//span[text()='" + device_name + "']")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(PatchManagerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(PatchManagerPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(PatchManagerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(PatchManagerPopup.BODY)

    def enter_text_into_search_text_field(self, text):
        self._find_element(PatchManagerPopup.SEARCH_FIELD).send_keys(text)

    def click_label_in_left_side_tree(self, label):
        elem = PatchManagerPopup.LEFT_SIDE_SUBNODE +\
               "/*//span[text()='" + label + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_label(elem)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(PatchManagerPopup.LEFT_SIDE_TREE)


class PingResultPopup(BaseActions):

    PING_RESULT = "Ping Result"
    BODY = "//span[text()='Ping Result'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(PingResultPopup.BODY)
        msg_true = "Popup '" + self.PING_RESULT + "' is opened"
        msg_false = "Popup '" + self.PING_RESULT+ "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(PingResultPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Ping Result")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(PingResultPopup.BODY)


class ProcessExplorerPopup(BaseActions):

    BODY = "//span[text()='Process Explorer'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABS_PANEL = BODY + "/*//div[contains(@id,'VWGScrollable')]/div"
    TAB_PROCESSES = BODY + "/*//span[text()='Processes'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_SERVICES = BODY + "/*//span[text()='Services'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    BUTTON_OPEN = BODY + "/*//span[text()='...']/ancestor::div[contains(@class,'Button')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ProcessExplorerPopup.BODY)
        return True if cond else False

    def check_tabs_panel_is_present(self):
        cond = self._wait_for_element_present(ProcessExplorerPopup.TABS_PANEL)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(ProcessExplorerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(ProcessExplorerPopup.BODY)

    def click_button_open(self):
        self._click_element(ProcessExplorerPopup.BUTTON_OPEN)

    def click_system_button_close(self):
        self._click_system_button_close(ProcessExplorerPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ProcessExplorerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Process Explorer")
        return True if cond else False

    def click_services_tab(self):
        self._click_element(ProcessExplorerPopup.TAB_SERVICES)
        self._wait_for_element_selected(ProcessExplorerPopup.TAB_SERVICES)

    def click_processes_tab(self):
        self._click_element(ProcessExplorerPopup.TAB_PROCESSES)
        self._wait_for_element_selected(ProcessExplorerPopup.TAB_PROCESSES)


class QueryDesignerPopup(BaseActions):

    BODY = "//span[text()='Query Designer'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(QueryDesignerPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(QueryDesignerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Queries")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(QueryDesignerPopup.BODY)
        self._wait_for_element_not_present(QueryDesignerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(QueryDesignerPopup.BODY)


    def click_button_add(self):
        self._click_button_add(QueryDesignerPopup.BODY)
        self._wait_for_element_present(ConditionEditorPopup.BODY)


class RemoveDevicesPopup(BaseActions):

    BODY = "//span[text()='Remove Devices'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    CHECKBOX_KEEP_HIST_INFORM = BODY + "//span[contains(text(),'Keep')][@class='CheckBox-Label']/" \
                                       "ancestor::tr/td[contains(@id,'TRG')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(RemoveDevicesPopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(RemoveDevicesPopup.BODY)

    def click_system_button_close(self):
       self._click_system_button_close(RemoveDevicesPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(RemoveDevicesPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(RemoveDevicesPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Delete/Archive")
        return True if cond else False

    def check_keep_historical_information_check_box(self):
        self._wait_for_element_checked(RemoveDevicesPopup.BODY)
        self._click_element(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
        self._wait_for_element_checked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)

    def uncheck_keep_historical_information_check_box(self):
        self._wait_for_element_present(RemoveDevicesPopup.BODY)
        self._click_element(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
        self._wait_for_element_unchecked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)


class ReportsPopup(BaseActions):

    BODY = "//span[text()='Reports'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ReportsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ReportsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Reports")
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ReportsPopup.BODY)


class ResetPasswordPopup(BaseActions):

    BODY = "//span[text()='Reset Password'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ResetPasswordPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ResetPasswordPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Reset Password")
        return True if cond else False


class SelectDashboardPopup(BaseActions):

    BODY = "//span[text()='Select Dashboard'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(SelectDashboardPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SelectDashboardPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Select Dashboard")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(SelectDashboardPopup.BODY)
        self._wait_for_element_not_present(SelectDashboardPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(SelectDashboardPopup.BODY)
        self._wait_for_element_not_present(SelectDashboardPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SelectDashboardPopup.BODY)


class SelectTargetsPopup(BaseActions):

    BODY = "//span[text()='Select Targets'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(SelectTargetsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SelectTargetsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Select Targets")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(SelectTargetsPopup.BODY)
        self._wait_for_element_not_present(SelectTargetsPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(SelectTargetsPopup.BODY)
        self._wait_for_element_not_present(SelectTargetsPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SelectTargetsPopup.BODY)

    def click_button_add_members(self):
        self._click_button_cancel(SelectTargetsPopup.BODY)
        self._wait_for_element_not_present(SelectTargetsPopup.BODY)


class SiteConfigPopup(BaseActions):

    BODY = "//span[text()='Site Config'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_TREE_VIEW = BODY + "/*//div[@class='TreeView-PaddingContainer']/div"
    LIST_GLOBAL_SITE_VIEW = LEFT_TREE_VIEW + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_GLOBAL_SITE_VIEW = LEFT_TREE_VIEW + "/div[contains(@class,'RowContainer')]"
    LABEL_DEFAULT_SITE = LIST_GLOBAL_SITE_VIEW \
                         + "/div/div/*//span[text()='Default Site']/ancestor::div[contains(@class,'RowContainer')]"
    BUTTON_ADD_IP_RANGE = BODY + "/*//img[@alt='Add IP Range']/ancestor::div[contains(@class,'Button')]"
    BUTTON_ADD_SITE = BODY + "/*//img[@alt='Add Site']/ancestor::div[contains(@class,'Button')]"
    BUTTON_EDIT = BODY + "/*//img[@alt='Edit']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE = BODY + "/*//img[@alt='Delete']/ancestor::div[contains(@class,'Button')]"
    BUTTON_MOVE_SITE = BODY + "/*//img[@alt='Move Site']/ancestor::div[contains(@class,'Button')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(SiteConfigPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SiteConfigPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(SiteConfigPopup.BODY)
        self._wait_for_element_not_present(SiteConfigPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SiteConfigPopup.BODY)

    def click_button_add_ip_range(self):
        self._click_element(SiteConfigPopup.BUTTON_ADD_IP_RANGE)
        self._wait_for_element_present(IPAddressPopup.BODY)

    def click_button_add_site(self):
        self._click_element(SiteConfigPopup.BUTTON_ADD_SITE)
        self._wait_for_element_present(SiteNamePopup.BODY)

    def click_button_move_site(self):
        self._click_element(SiteConfigPopup.BUTTON_MOVE_SITE)
        self._wait_for_element_present(MoveSitePopup.BODY)

    def create_site_if_not_exists(self, sitename):
        self.scroll_to_element(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW)
        self.click_global_site_view_label()
        self.expand_global_site_view_tree()
        cond = self.check_site_is_in_global_site_view_tree(sitename)
        if cond is not True:
            site_name_popup = SiteNamePopup(self.driver)
            self.click_global_site_view_label()
            self.click_button_add_site()
            site_name_popup.enter_text_into_name_text_field(sitename)
            site_name_popup.click_button_ok()
        self.scroll_to_element(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW \
                  + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]")
        self.click_site_in_global_site_view_tree(sitename)

    def click_global_site_view_label(self):
        self.scroll_to_element(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW)
        self._click_label(SiteConfigPopup.LABEL_GLOBAL_SITE_VIEW)

    # def click_subsite_in_site_tree(self, sitename, subsitename):
    #     site_name = SiteConfigPopup.BODY \
    #                 + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
    #     subsite_name = SiteConfigPopup.BODY + \
    #                    "/*//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
    #     element = SiteConfigPopup.LIST_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
    #     self._click_element(element)
    #     self._wait_for_element_selected(element)

    def expand_global_site_view_tree(self):
        arrow = self._is_element_present(SiteConfigPopup.LABEL_GLOBAL_SITE_VIEW + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(SiteConfigPopup.LABEL_GLOBAL_SITE_VIEW)

    def click_site_in_global_site_view_tree(self, sitename):
        element = SiteConfigPopup.LIST_GLOBAL_SITE_VIEW \
                  + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_ADD_IP_RANGE)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_EDIT)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_DELETE)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_MOVE_SITE)

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self._wait_for_element_present(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False


class SiteNamePopup(BaseActions):

    SITE_NAME = "Site Name"
    BODY = "//span[text()='Site Name'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(SiteNamePopup.BODY)
        msg_true = "Popup '" + self.SITE_NAME + "' is present"
        msg_false = "Popup '" + self.SITE_NAME + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_popup_is_not_present(self):
        cond = self._is_element_not_present(SiteNamePopup.BODY)
        msg_false = "Popup '" + self.SITE_NAME + "' is present"
        msg_true = "Popup '" + self.SITE_NAME + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(SiteNamePopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(SiteNamePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SiteNamePopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(SiteNamePopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(SiteNamePopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create a site")
        return True if cond else False


class SubscriptionHasExpiredPopup(BaseActions):

    BODY = "//span[text()='Manage Subscriptions'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def click_system_button_close(self):
        self._click_system_button_close(SubscriptionHasExpiredPopup.BODY)

    # def close_popup(self):
    #     cond = self._is_element_present(SubscriptionHasExpitredPopup.PAGE_BODY)
    #     if cond:
    #         self._click_system_button_close()
    #     else:
    #         pass


class SubscriptionsPopup(BaseActions):

    BODY = "//span[text()='Subscriptions'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(SubscriptionsPopup.BODY)
        return self._find_element(SubscriptionsPopup.BODY) if cond else None

    def click_icon_help(self):
        self._click_icon_help(SubscriptionsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Subscriptions")
        return True if cond else False


class TermsAndConditionsPopup(BaseActions):
    BODY = "//span[text()='Terms and Conditions'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    BTN_I_AGREE = "//span[text()='I Agree']"
    BTN_I_DO_NOT_AGREE = "//span[text()='I Do Not Agree']"

    def click_button_i_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_AGREE)
        self._wait_for_element_not_present(TermsAndConditionsPopup.BODY)

    def click_button_i_do_not_agree(self):
        self._click_element(TermsAndConditionsPopup.BTN_I_DO_NOT_AGREE)

    def click_system_button_close(self):
        self._click_system_button_close(TermsAndConditionsPopup.BODY)

    def close_popup_if_exists(self):
        cond = self._is_element_present(TermsAndConditionsPopup.BODY)
        if cond:
            self.click_button_i_agree()


class UnableToRemovePopup(BaseActions):

    BODY = "//span[text()='Unable to remove']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(UnableToRemovePopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(UnableToRemovePopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(UnableToRemovePopup.BODY)


class UserConfigurationPopup(BaseActions):

    BODY = "//span[text()='User Configuration'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    FIELD_NAME = BODY + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(UserConfigurationPopup.BODY)
        return True if cond else False

    def enter_text_into_name_text_field(self, sitename):
        self._find_element(UserConfigurationPopup.FIELD_NAME).send_keys(sitename)

    def click_button_ok(self):
        self._click_button_ok(UserConfigurationPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(UserConfigurationPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(UserConfigurationPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(UserConfigurationPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create")
        return True if cond else False


class UserSettingsPopup(BaseActions):

    BODY = "//span[text()='User Settings'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(UserSettingsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(UserSettingsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("User Settings")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(UserSettingsPopup.BODY)
        self._wait_for_element_not_present(UserSettingsPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(UserSettingsPopup.BODY)
        self._wait_for_element_not_present(UserSettingsPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(UserSettingsPopup.BODY)


class ViewLogsPopup(BaseActions):

    BODY = "//span[contians(text(),'View Logs')][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ViewLogsPopup.BODY)
        return True if cond else False

    def click_system_button_close(self):
        self._click_system_button_close(ViewLogsPopup.BODY)


class WakeOnLANPopup(BaseActions):

    BODY = "//span[text()='Wake on LAN'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(WakeOnLANPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(WakeOnLANPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Wake Up")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(WakeOnLANPopup.BODY)
        self._wait_for_element_not_present(WakeOnLANPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(WakeOnLANPopup.BODY)


class WeightDisplayPopup(BaseActions):

    BODY = "//span[text()='Weight Display'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(WeightDisplayPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(WeightDisplayPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Imperial Metric")
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(WeightDisplayPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(WeightDisplayPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(WeightDisplayPopup.BODY)


class WMIExplorerPopup(BaseActions):

    BODY = "//span[text()='WMI Explorer'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(WMIExplorerPopup.BODY)
        return True if cond else False

    def click_button_ok(self):
        self._click_button_ok(WMIExplorerPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(WMIExplorerPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(WMIExplorerPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(WMIExplorerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Process Explorer")
        return True if cond else False


class SettingsPopup(BaseActions):

    BODY = "//span[text()='Settings'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TREE_VIEW = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    LABEL_CONTENT_SERVICES = TREE_VIEW + "/*//span[text()='Content Services']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_EMAIL_SETTINGS = TREE_VIEW + "/*//span[text()='Email Settings']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_INITIAL_SETUP = TREE_VIEW + "/*//span[text()='Initial Setup']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_INVENTORY = TREE_VIEW + "/*//span[text()='Inventory']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_LOCALE_OPTIONS = TREE_VIEW + "/*//span[text()='Locale Options']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_USER_OPTIONS = TREE_VIEW + "/*//span[text()='User Options']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_AUDIT_LOG_SETTINGS = TREE_VIEW + "/*//span[text()='Audit Log Settings']/ancestor::div[contains(@id,'VWGNODE')]"
    TAB_LABEL_AUDIT_LOG_SETTINGS = TAB + "/*//span[text()='Audit Log Settings']"
    LABEL_AUDIT_EMAIL_SETTINGS = TAB + "/*//span[text()='Audit Email Settings']"
    BUTTON_PURGE_ENTRIES = TAB  + "/*//span[text()='Purge older entries now']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE_LOGS = TAB  + "/*//span[text()='Delete all audit logs']/ancestor::div[contains(@class,'Button')]"
    TAB_OPTIONS = TAB + "/*//span[text()='Options']/ancestor::div[contains(@id,'TAB')]"
    TAB_LOG = TAB + "/*//span[text()='Log']/ancestor::div[contains(@id,'TAB')]"
    TAB_SMTP = TAB + "/*//span[text()='SMTP']/ancestor::div[contains(@id,'TAB')]"
    TAB_IMAP = TAB + "/*//span[text()='IMAP']/ancestor::div[contains(@id,'TAB')]"
    LABEL_DATE_AND_TIME_SETTINGS = TAB + "/*//span[text()='Date And Time Settings']"
    LABEL_DATE_FORMAT = TAB + "/*//span[text()='Date Format']"
    LABEL_TIME_ZONE = TAB + "/*//span[text()='Time Zone']"
    LABEL_USER_AUTHENTICATION = TAB + "/*//span[text()='User Authentication']"
    CHECKBOX_CHECK_NEW_DATA = TAB + \
                        "/*//span[contains(text(),'check for new data')]/ancestor::div[contains(@class,'CheckBox')]"
    BUTTON_RUN_INITIAL_SETUP = TAB + \
                        "/*//span[text()='Run Initial Setup']/ancestor::div[contains(@class,'Button')]"
    CHECKBOX_TERMS_AND_CONDITIONS = TAB + \
                        "/*//span[contains(text(),'Show Terms')]/ancestor::div[contains(@class,'CheckBox')]"
    LABEL_INVENTORY_ARCHIVE_SETTINGS = TAB + "/*//span[text()='Inventory Archive Settings']"
    BUTTON_PURGE_RECORDS = TAB + "/*//span[text()='Purge Older Records']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE_DATA = TAB + "/*//span[text()='Delete ALL Archive Data']/ancestor::div[contains(@class,'Button')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(SettingsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SettingsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Settings")
        return True if cond else False

    def click_content_services_label(self):
        self._click_label(SettingsPopup.LABEL_CONTENT_SERVICES)

    def click_email_settings_label(self):
        self._click_label(SettingsPopup.LABEL_EMAIL_SETTINGS)

    def click_initial_setup_label(self):
        self._click_label(SettingsPopup.LABEL_INITIAL_SETUP)

    def click_locale_options_label(self):
        self._click_label(SettingsPopup.LABEL_LOCALE_OPTIONS)

    def click_inventory_label(self):
        self._click_label(SettingsPopup.LABEL_INVENTORY)

    def click_user_options_label(self):
        self._click_label(SettingsPopup.LABEL_USER_OPTIONS)

    def click_audit_log_settings_label(self):
        self._click_label(SettingsPopup.LABEL_AUDIT_LOG_SETTINGS)

    def click_button_run_initial_setup(self):
        self._click_element(SettingsPopup.BUTTON_RUN_INITIAL_SETUP)
        self._wait_for_element_present(InitialSetupPopup.BODY)

    def check_content_services_tab_is_present(self):
        cond = self._wait_for_element_present(SettingsPopup.TAB_OPTIONS)
        msg_true = "Tab 'Content Services' is opened"
        msg_false = "Tab 'Content Services' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_email_settings_tab_is_present(self):
        cond = self._wait_for_element_present(SettingsPopup.TAB_SMTP)
        msg_true = "Tab 'Email Settings' is opened"
        msg_false = "Tab 'Email Settings' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_initial_setup_tab_is_present(self):
        cond = self._wait_for_element_present(SettingsPopup.BUTTON_RUN_INITIAL_SETUP)
        msg_true = "Tab 'Initial Setup' is opened"
        msg_false = "Tab 'Initial Setup' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_locale_options_tab_is_present(self):
        cond = self._wait_for_element_present(SettingsPopup.LABEL_DATE_AND_TIME_SETTINGS)
        msg_true = "Tab 'Locale Options' is opened"
        msg_false = "Tab 'Locale Options' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_inventory_tab_is_present(self):
        self.wait_for_screen_is_unlocked()
        # WebDriverWait(SettingsPopup.driver, 600). \
        #     until(EC.presence_of_element_located((By.XPATH, self.LABEL_INVENTORY_ARCHIVE_SETTINGS)))
        cond = self._wait_for_element_present(SettingsPopup.LABEL_INVENTORY_ARCHIVE_SETTINGS)
        msg_true = "Tab 'Inventory' is opened"
        msg_false = "Tab 'Inventory' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_user_options_tab_is_present(self):
        cond = self._wait_for_element_present(SettingsPopup.LABEL_USER_AUTHENTICATION)
        return True if cond else False

    def check_audit_log_settings_tab_is_present(self):
        cond= self._is_element_present(SettingsPopup.TAB_LABEL_AUDIT_LOG_SETTINGS)
        msg_true = "Tab 'Audit Log Settings' is opened"
        msg_false = "Tab 'Audit Log Settings' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False


class ConfigurationPopup(BaseActions):

    IP_ADDRESS_RANGES = "IP Address Ranges"
    BODY = "//span[text()='Configuration'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TAB = BODY + "/*//div[1][@class='TabPage-Control_bj']"
    BUTTONS_PANEL = TAB + "/*//div[contains(@class,'FlatToolBar')]"
    TABLE_HEADER = TAB + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = TAB + "/*//div[contains(@id,'VWGLVBODY')]"
    BUTTON_ADD = TAB + "/*//span[text()='Add']/ancestor::div[contains(@class,'Button')]"
    BUTTON_APPLY_CHANGES = TAB + "/*//span[text()='Apply Changes']"
    BUTTON_EDIT = TAB + "/*//span[text()='Add']/ancestor::div[contains(@class,'Button')]"
    TABS_PANEL = BODY + "/*//div[contains(@id,'VWGScrollable')]/div"
    TAB_IP_ADDRESS = BODY + "/*//span[text()='IP Address Ranges'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_SITE = BODY + "/*//span[text()='Site'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_VREPS = BODY + "/*//span[text()='vReps'][contains(@class,'Tab')]/ancestor::div[contains(@id,'TAB')]"
    TAB_CONFIGURATION = BODY + "/*//div[1][@class='TabPage-Control_bj']"
    COLUMN_SET_DROP_DOWN_LIST = TAB + "/following::div[@class='ComboBox-PopupWindow']"
    DROP_DOWN_APPLIED_VALUE = TAB + "/*//div[contains(@class,'ComboBox-Container')]/*//span[@data-vwg_appliedvalue]"
    FIELD_NAME = TAB + "/*//input"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ConfigurationPopup.BODY)
        return True if cond else False

    def check_tabs_panel_is_present(self):
        cond = self._wait_for_element_present(ConfigurationPopup.TABS_PANEL)
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ConfigurationPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ConfigurationPopup.BODY)

    def click_icon_help(self):
        self._click_icon_help(ConfigurationPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Configure a site")
        return True if cond else False

    def click_site_tab(self):
        self._click_element(ConfigurationPopup.TAB_SITE)
        # self._wait_for_element_selected(ConfigurationPopup.TAB_SITE)

    def click_ip_address_ranges_tab(self):
        self._click_element(ConfigurationPopup.TAB_IP_ADDRESS)
        # self._wait_for_element_selected(ConfigurationPopup.TAB_IP_ADDRESS)

    def click_vreps_tab(self):
        self._click_element(ConfigurationPopup.TAB_VREPS)
        # self._wait_for_element_selected(ConfigurationPopup.TAB_VREPS)

    def click_button_new(self):
        self._click_button_new(ConfigurationPopup.TAB)
        # self._wait_for_element_present(ColumnSetDesignerPopup.BODY)

    def click_column_set_dropdown_button(self):
        self._click_system_button_drop_down(ConfigurationPopup.BODY)
        # self._wait_for_element_present(ConfigurationPopup.COLUMN_SET_DROP_DOWN_LIST)

    def click_icon_restore(self):
        self._click_icon_restore(ConfigurationPopup.TAB)
        # self._wait_for_element_not_present(ConfigurationPopup.DROP_DOWN_APPLIED_VALUE)

    def enter_text_into_name_text_field(self, sitename):
        self._click_element(ConfigurationPopup.FIELD_NAME)
        self._find_element(ConfigurationPopup.FIELD_NAME).send_keys(sitename)

    def get_name_text_field_value(self):
        actual_attribute_value = self._get_attribute_value(ConfigurationPopup.FIELD_NAME, "value")
        print ("The actual value in the Name textfield is: " + actual_attribute_value)
        return actual_attribute_value

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
        self._wait_for_element_not_present(ConfigurationPopup.COLUMN_SET_DROP_DOWN_LIST)

    def check_columnset_is_selected_from_drop_down_list(self, columnsetname):
        cond = self._wait_for_element_present(
            ConfigurationPopup.DROP_DOWN_APPLIED_VALUE + "[text()='" + columnsetname + "']")
        return True if cond else False

    def check_name_text_field_disabled(self):
        cond = self._is_element_disabled(ConfigurationPopup.FIELD_NAME)
        return True if cond else False

    def check_tab_is_present(self):
        cond = self._wait_for_element_present(ConfigurationPopup.BUTTON_APPLY_CHANGES)
        msg_true = "Tab 'IP Address Ranges' is opened"
        msg_false = "Tab 'IP Address Ranges' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_button_add(self):
        self._click_button_add(ConfigurationPopup.BUTTON_ADD)
        # self._wait_for_element_present(IPAddressPopup.BODY)


class ConfigureExclusionsPopup(BaseActions):

    BODY = "//span[text()='Configure Exclusions'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_MENU = BODY + "/*//div[@class='Common-Unselectable TreeView-Container']"
    # LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    # LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    # LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ConfigureExclusionsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ConfigureExclusionsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Exclusions")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(ConfigureExclusionsPopup.BODY)
        self._wait_for_element_not_present(ConfigureExclusionsPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(ConfigureExclusionsPopup.BODY)

    def click_label_in_left_side_tree(self, label):
        elem = ConfigureExclusionsPopup.LEFT_MENU + \
               "/*//span[text()='" + str(label) + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_label(elem)

    def check_text_is_in_list_view(self, text):
        cond = self._wait_for_element_present(ConfigureExclusionsPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False

    def select_item_in_table(self, item):
        self._wait_for_element_present(ConfigureExclusionsPopup.TABLE_ROW)
        row = ConfigureExclusionsPopup.TABLE_ROW + "/*//span[text()='" + item + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)

    def click_tree_label_sites(self):
        self.click_label_in_left_side_tree("Sites")

    def click_tree_label_ip_address(self):
        self.click_label_in_left_side_tree("IP Address")

    def click_tree_label_device_name(self):
        self.click_label_in_left_side_tree("Device Name")

    def click_sites_tab_button_add(self):
        self._click_button_add(ConfigureExclusionsPopup.TAB)
        # self._wait_for_element_present(ExcludeSitePopup.BODY)

    def click_ip_address_tab_button_add(self):
        self._click_button_add(ConfigureExclusionsPopup.TAB)
        # self._wait_for_element_present(ExcludeIPAddressPopup.BODY)

    def click_device_name_tab_button_add(self):
        self._click_button_add(ConfigureExclusionsPopup.TAB)
        # self._wait_for_element_present(ExcludeDevicePopup.BODY)

    def check_sites_tab_is_opened(self):
        pass


class ClientSettingsPopup(BaseActions):

    TIMERS = "Timers"
    FEATURES = "Features"
    CLIENT_URLS = "Client URLs"
    REBOOT_UI_CONFIG = "Reboot UI Config"
    CLIENT_PROXY_SETTINGS = "Client Proxy Settings"
    BODY = "//span[text()='Client Settings'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"
    LABEL_TIMERS = LEFT_MENU + "/*//span[text()='Timers']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_FEATURES = LEFT_MENU  + "/*//span[text()='Features']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_REBOOT_UI_CONFIG = LEFT_MENU  + "/*//span[text()='Reboot UI Config']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_CLIENT_URLS = LEFT_MENU + "/*//span[text()='Client URLs']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_CLIENT_PROXY_SETTINGS = LEFT_MENU + \
                                  "/*//span[text()='Client Proxy Settings']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_PROXY_SERVER_URL = TAB + "/*//span[text()='Proxy Server URL:']"
    LABEL_PORT_NUMBER = TAB + "/*//span[text()='Port Number:']"
    LABEL_LOGIN_CREDENTIALS = TAB + "/*//span[text()='Login Credentials']"
    LABEL_PASSWORD = TAB + "/*//span[text()='Password']"
    LABEL_VREP_INSTALLER = TAB + "/*//span[text()='vRep Installer']"
    LABEL_MICRO_RESPONDER_INSTALLER = TAB + "/*//span[text()='Micro Responder Installer']"
    LABEL_REBOOT_MASSAGE = TAB + "/*//span[text()='Custom Reboot Message']"
    LABEL_REBOOT_TIMERS = TAB + "/*//span[text()='Reboot Timers']"
    LABEL_SNOOZE = TAB + "/*//span[text()='Snooze']"
    CHECKBOX_ARCHIVE = TAB + "/*//span[text()='Auto Archive:']/ancestor::div[contains(@class,'CheckBox')]"
    CHECKBOX_DISSOLVE = TAB + "/*//span[contains(text(),'Dissolve')]/ancestor::div[contains(@class,'CheckBox')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(ClientSettingsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ClientSettingsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Client")
        return True if cond else False

    def click_timers_tab(self):
        self._click_element(self.LABEL_TIMERS)
        self._wait_for_element_selected(self.LABEL_TIMERS)

    def click_features_label(self):
        self._click_label(self.LABEL_FEATURES)

    def click_client_urls_label(self):
        self._click_label(self.LABEL_CLIENT_URLS)

    def click_reboot_ui_config_tab(self):
        self._click_label(self.LABEL_REBOOT_UI_CONFIG)

    def click_client_proxy_settings_tab(self):
        self._click_label(self.LABEL_CLIENT_PROXY_SETTINGS)

    def check_timers_tab_is_present(self):
        cond = self._wait_for_element_present(self.CHECKBOX_DISSOLVE)
        msg_true = "Tab " + self.TIMERS + "' is present"
        msg_false = "Tab" + self.TIMERS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_features_tab_is_present(self):
        cond = self._wait_for_element_present(self.CHECKBOX_ARCHIVE)
        msg_true = "Tab " + self.FEATURES + "' is present"
        msg_false = "Tab" + self.FEATURES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_client_urls_tab_is_present(self):
        cond = self._wait_for_element_present(self.LABEL_VREP_INSTALLER)
        msg_true = "Tab " + self.CLIENT_URLS + "' is present"
        msg_false = "Tab" + self.CLIENT_URLS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_reboot_ui_config_tab_is_present(self):
        cond = self._wait_for_element_present(self.LABEL_REBOOT_MASSAGE)
        msg_true = "Tab " + self.REBOOT_UI_CONFIG + "' is present"
        msg_false = "Tab" + self.REBOOT_UI_CONFIG + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_client_proxy_settings_tab_is_present(self):
        cond = self._wait_for_element_present(self.LABEL_PROXY_SERVER_URL)
        msg_true = "Tab " + self.CLIENT_PROXY_SETTINGS + "' is present"
        msg_false = "Tab" + self.LABEL_CLIENT_PROXY_SETTINGS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False


class EditUserPopup(BaseActions):

    EDIT_USER = "Edit User"
    BODY = "//span[text()='Edit User'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(EditUserPopup.BODY)
        msg_true = "Popup '" + self.EDIT_USER + "' is present"
        msg_false = "Popup '" + self.EDIT_USER + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EditUserPopup.BODY)


class InventoryConfigurationPopup(BaseActions):

    INVENTORY_CONFIGURATION = "Inventory Configuration"
    BODY = "//span[text()='Inventory Configuration'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY  + "/*//div[contains(@id,'VWGLVBODY')]"
    LEFT_SIDE_TREE = BODY + "/*//div[contains(@class,'PaddingContainer')]"
    LEFT_SIDE_SUBNODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'SubNodesContainer')]"
    LEFT_SIDE_NODE = LEFT_SIDE_TREE + "/*//div[contains(@class,'RowContainer')]"
    TABLE_HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_HEADER_DEFAULT_WIDTH = TABLE_HEADER + "/*//span[contains(text(),'Default Width')]"
    TABLE_HEADER_AGGREGATE = TABLE_HEADER + "/*//span[contains(text(),'Aggregate')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    ELEMENT_LABEL = "/ancestor::div[contains(@class,'RowContainer')]"


    def check_popup_is_present(self):
        cond = self._wait_for_element_present(InventoryConfigurationPopup.BODY)
        msg_true = "Popup '" + self.INVENTORY_CONFIGURATION + "' is present"
        msg_false = "Popup '" + self.INVENTORY_CONFIGURATION + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(InventoryConfigurationPopup.BODY)

    def click_button_ok(self):
        self._click_button_ok(InventoryConfigurationPopup.BODY)
        self._wait_for_element_not_present(InventoryConfigurationPopup.BODY)

    def click_button_cancel(self):
        self._click_button_cancel(InventoryConfigurationPopup.BODY)
        self._wait_for_element_not_present(InventoryConfigurationPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(InventoryConfigurationPopup.BODY)

    def click_label_in_left_side_tree(self, label):
        elem = InventoryConfigurationPopup.LEFT_SIDE_SUBNODE + "/*//span[text()='" + label + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_label(elem)

    def expand_all_left_side_trees(self):
        self._expand_all_trees(InventoryConfigurationPopup.LEFT_SIDE_TREE)
        # self._wait_for_element_present(MoveDevicePopup.PAGE_BODY)
        # elements = self._find_elements(MoveDevicePopup.LEFT_SIDE_TREE + "/div/div/div[contains(@id,'VWGJOINT')]")
        # for element in elements:
        #     self.driver.execute_script("arguments[0].click();", element)

    def check_text_is_in_list_view(self, text):
        cond = self._wait_for_element_present(InventoryConfigurationPopup.TABLE_BODY + "/*//span[contains(text(),'" + text + "')]")
        return True if cond else False

    def select_item_in_table(self, name):
        self._wait_for_element_present(InventoryConfigurationPopup.TABLE_ROW)
        row = InventoryConfigurationPopup.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class InventoryForceUpdatePopup(BasePopup):

    INVENTORY_FORCE_UPDATE = "Inventory Force Update"

    def popup_body(self):
        locator = self._set_popup(self.INVENTORY_FORCE_UPDATE)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.INVENTORY_FORCE_UPDATE + "' is present"
        msg_false = "Popup '" + self.INVENTORY_FORCE_UPDATE + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond is not None else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class CreatePatchGroupPopup(BasePopup):

    CREATE_PATCH_GROUP = "Create Patch Group"
    BUTTON_EDIT_MEMBERS = "/*//span[text()='Edit Members']/ancestor::div[contains(@class,'Button')]"

    def popup_body(self):
        locator = self._set_popup(self.CREATE_PATCH_GROUP)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.CREATE_PATCH_GROUP + "' is present"
        msg_false = "Popup '" + self.CREATE_PATCH_GROUP + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond is not None else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_button_edit_members(self):
        self._click_element(self.popup_body() + self.BUTTON_EDIT_MEMBERS)

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class SelectPatchesPopup(BasePopup):

    SELECT_PATCHES = "Select Patches"

    def popup_body(self):
        locator = self._set_popup(self.SELECT_PATCHES)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.SELECT_PATCHES + "' is present"
        msg_false = "Popup '" + self.SELECT_PATCHES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond is not None else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class CreateApplicationPopup(BasePopup):

    CREATE_APPLICATION = "Create Application"
    SELECT_FILE = "SELECT FILE"
    IMPORT_INFORMATION = "IMPORT INFORMATION"
    ADVANCED = "ADVANCED"
    BUTTON_CHOOSE_FROM_SERVER = "/*//span[contains(text(),'Verismic server')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_CHOOSE_FROM_DEVICE = "/*//span[contains(text(),'your device')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_CONFIGURE_ADVANCED_OPTIONS = "/*//span[contains(text(),'Options')]/ancestor::div[contains(@class,'Button')]"
    LABEL_SELECT_FILE = "/*//span[text()='SELECT FILE']"
    LABEL_IMPORT_INFORMATION = "/*//span[text()='IMPORT INFORMATION']"
    LABEL_ADVANCED = "/*//span[text()='ADVANCED']"

    def popup_body(self):
        locator = BaseElements.POPUP
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else None

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_button_next(self):
        self._click_button_next(self.popup_body())

    def click_button_previous(self):
        self._click_button_previous(self.popup_body())

    def click_button_finish(self):
        self._click_button_finish(self.popup_body())

    def click_button_choose_installer_on_sever(self):
        self._click_element(self.BUTTON_CHOOSE_FROM_SERVER)

    def click_button_configure_advanced_options(self):
        self._click_element(self.BUTTON_CONFIGURE_ADVANCED_OPTIONS)

    def check_popup_is_present(self):
        cond = self._wait_for_element_present(self.popup_body())
        self.logger.critical(
            "Popup HAS NO title name. Add titile '" + self.CREATE_APPLICATION + "'!!!")
        msg_true = "Popup '" + self.CREATE_APPLICATION + "' is present"
        msg_false = "Popup '" + self.CREATE_APPLICATION + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_select_file_tab_is_present(self):
        cond = self._wait_for_element_present(self.popup_body() + self.LABEL_SELECT_FILE + BaseElements.BLACK_COLOR)
        msg_true = "Tab '" + self.SELECT_FILE + "' is present"
        msg_false = "Tab '" + self.SELECT_FILE + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_import_information_tab_is_present(self):
        cond = self._wait_for_element_present(self.popup_body() + self.LABEL_IMPORT_INFORMATION + BaseElements.BLACK_COLOR)
        msg_true = "Tab '" + self.IMPORT_INFORMATION + "' is present"
        msg_false = "Tab '" + self.IMPORT_INFORMATION + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_advanced_tab_is_present(self):
        cond = self._wait_for_element_present(self.popup_body() + self.LABEL_ADVANCED + BaseElements.BLACK_COLOR)
        msg_true = "Tab '" + self.ADVANCED + "' is present"
        msg_false = "Tab '" + self.ADVANCED + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False


class InstallersPopup(BasePopup):

    INSTALLERS = "Installers"

    def popup_body(self):
        locator = self._set_popup(self.INSTALLERS)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.INSTALLERS + "' is present"
        msg_false = "Popup '" + self.INSTALLERS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class AdvancedEditorPopup(BasePopup):

    ADVANCED_EDITOR = "Advanced Editor"
    PRE_REQUISITES = "Pre-Requisites"
    LABEL_PRE_REQUISITES = "/*//span[contains(text(),'Pre-Requisites')][contains(@class,'ListItemLabel')]" + BaseElements.LABEL
    LABEL_INFORMATION = "/*//span[contains(text(),'Information')][contains(@class,'ListItemLabel')]" + BaseElements.LABEL
    LABEL_COMPONENTS = "/*//span[contains(text(),'Components')][contains(@class,'ListItemLabel')]" + BaseElements.LABEL
    TAB_PRE_REQUISITES = "/*//span[contains(text(),'Pre-Requisites')][@dir='LTR']" + BaseElements.TAB
    TAB_INFORMATION = "/*//span[contains(text(),'Information')][@dir='LTR']" + BaseElements.TAB
    TAB_COMPONENTS = "/*//span[contains(text(),'Components')][@dir='LTR']" + BaseElements.TAB

    def popup_body(self):
        locator = self._set_popup(self.ADVANCED_EDITOR)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_add(self):
        self._click_button_add(self.popup_body())

    def click_button_edit(self):
        self._click_button_edit(self.popup_body())

    def click_button_delete(self):
        self._click_button_delete(self.popup_body())

    def click_infromation_label(self):
        self._click_element(self.LABEL_INFORMATION)

    def click_pre_requisites_label(self):
        self._click_element(self.LABEL_PRE_REQUISITES)

    def click_components_label(self):
        self._click_element(self.LABEL_COMPONENTS)

    def click_first_row_in_table(self):
        table_row = self._set_popup_table_body(self.popup_body()) + "/*//tr[1]"
        self._click_element(table_row)

    def select_first_row_in_table(self):
        table_row = self._set_popup_table_body(self.popup_body()) + "/*//tr[1]"
        cond = self._wait_for_element_present(table_row)
        if cond:
            self.click_first_row_in_table()
            return True
        else:
            self.logger.info("NO rows in the tab table")
            return False

    def select_patch_in_table(self, name):
        table_row = self._set_popup_table_body(self.popup_body()) + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(table_row)
        self._wait_for_element_selected(table_row)

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.ADVANCED_EDITOR + "' is present"
        msg_false = "Popup '" + self.ADVANCED_EDITOR + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_tab_pre_requisites_is_present(self):
        cond = self._wait_for_element_selected(self.LABEL_PRE_REQUISITES)
        msg_true = "Tab '" + self.PRE_REQUISITES + "' is present"
        msg_false = "Tab '" + self.PRE_REQUISITES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_tab_information_is_present(self):
        cond = self._wait_for_element_selected(self.LABEL_INFORMATION)
        msg_true = "Tab '" + self.PRE_REQUISITES + "' is present"
        msg_false = "Tab '" + self.PRE_REQUISITES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_tab_components_is_present(self):
        cond = self._wait_for_element_selected(self.LABEL_COMPONENTS)
        msg_true = "Tab '" + self.PRE_REQUISITES + "' is present"
        msg_false = "Tab '" + self.PRE_REQUISITES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_first_row_is_selected(self):
        table_row = self._set_popup_table_body(self.popup_body()) + "/*//tr[1]"
        cond = self._wait_for_element_selected(table_row)
        return True if cond else False

    def check_patch_is_present(self, name):
        table_row = self._set_popup_table_body(self.popup_body()) + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(table_row)
        return True if cond else False

    def check_patch_is_selected(self, name):
        table_row = self._set_popup_table_body(self.popup_body()) + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_selected(table_row)
        return True if cond else False


class SelectInstallMediaPopup(BasePopup):

    SELECT_INSTALL_MEDIA = "Select Install Media"

    def popup_body(self):
        locator = self._set_popup(self.SELECT_INSTALL_MEDIA)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.SELECT_INSTALL_MEDIA + "' is present"
        msg_false = "Popup '" + self.SELECT_INSTALL_MEDIA + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class SelectPreRequisitesPopup(BasePopup):

    SELECT_PRE_REQUISITES = "Select Pre-Requisites"

    def popup_body(self):
        locator = self._set_popup(self.SELECT_PRE_REQUISITES)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.SELECT_PRE_REQUISITES + "' is present"
        msg_false = "Popup '" + self.SELECT_PRE_REQUISITES+ "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class ComponentPopup(BasePopup):

    COMPONENT = "Component"
    BUTTON_EDIT_FILTERS = "/*//span[text()='Edit Filters']/ancestor::div[contains(@class,'Button')]"
    BUTTON_EDIT_DETECTORS = "/*//span[text()='Edit Detectors']/ancestor::div[contains(@class,'Button')]"
    BUTTON_EDIT_DEPLOYMENTS = "/*//span[text()='Edit Deployments']/ancestor::div[contains(@class,'Button')]"
    BUTTON_VIEW_DETAILS = "/*//span[text()='View Details']/ancestor::div[contains(@class,'Button')]"

    def popup_body(self):
        locator = self._set_popup(self.COMPONENT)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.COMPONENT + "' is present"
        msg_false = "Popup '" + self.COMPONENT + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_system_button_edit_filters(self):
        self._click_element(self.popup_body() + self.BUTTON_EDIT_FILTERS)

    def click_system_button_edit_detectors(self):
        self._click_element(self.popup_body() + self.BUTTON_EDIT_DETECTORS)

    def click_system_button_edit_deployments(self):
        self._click_element(self.popup_body() + self.BUTTON_EDIT_DEPLOYMENTS)

    def click_system_button_view_details(self):
        self._click_element(self.popup_body() + self.BUTTON_VIEW_DETAILS)


class FiltersPopup(BasePopup):

    FILTERS = "Filters"

    def popup_body(self):
        locator = self._set_popup(self.FILTERS)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.FILTERS + "' is present"
        msg_false = "Popup '" + self.FILTERS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class ExistingSoftwareUpdateDetectionPopup(BasePopup):

    EXISTING_SOFTWARE_UPDATE_DETECTION = "Existing Software Update Detection"

    def popup_body(self):
        locator = self._set_popup(self.EXISTING_SOFTWARE_UPDATE_DETECTION)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.EXISTING_SOFTWARE_UPDATE_DETECTION + "' is present"
        msg_false = "Popup '" + self.EXISTING_SOFTWARE_UPDATE_DETECTION + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class DeploymentsPopup(BasePopup):

    DEPLOYMENTS = "Deployments"
    INSTALLER_FILES = "Installer Files"
    INSTALL_COMMANDS = "Install Commands"
    UNINSTALL_COMMANDS = "Uninstall Commands"
    BUTTON_EDIT_COMMANDS = "/*//span[text()='Edit Commands']/ancestor::div[contains(@class,'Button')]"
    LABEL_INSTALLER_FILES = "/*//span[contains(text(),'Installer Files')][contains(@class,'ListItemLabel')]" \
                            + BaseElements.LABEL
    LABEL_INSTALL_COMMANDS = "/*//span[contains(text(),'Install Commands')][contains(@class,'ListItemLabel')]" \
                             + BaseElements.LABEL
    LABEL_UNINSTALL_COMMANDS = "/*//span[contains(text(),'Uninstall Commands')][contains(@class,'ListItemLabel')]" \
                               + BaseElements.LABEL
    TAB_INSTALLER_FILES = "/*//span[contains(text(),'Installer Files')][@dir='LTR']" + BaseElements.TAB
    TAB_INSTALL_COMMANDS = "/*//span[contains(text(),'Install Commands')][@dir='LTR']" + BaseElements.TAB
    TAB_UNINSTALL_COMMANDS = "/*//span[contains(text(),'Uninstall Commands')][@dir='LTR']" + BaseElements.TAB

    def popup_body(self):
        locator = self._set_popup(self.DEPLOYMENTS)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.DEPLOYMENTS + "' is present"
        msg_false = "Popup '" + self.DEPLOYMENTS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_edit_commands(self):
        self._click_element(self.popup_body() + self.BUTTON_EDIT_COMMANDS)

    def click_installer_files_label(self):
        self._click_element(self.LABEL_INSTALLER_FILES)

    def click_install_commands_label(self):
        self._click_element(self.LABEL_INSTALL_COMMANDS)

    def click_uninstall_commands_label(self):
        self._click_element(self.LABEL_UNINSTALL_COMMANDS)

    def check_tab_installer_files_is_present(self):
        cond = self._wait_for_element_selected(self.LABEL_INSTALLER_FILES)
        msg_true = "Tab '" + self.INSTALLER_FILES + "' is present"
        msg_false = "Tab '" + self.INSTALLER_FILES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_tab_install_commands_is_present(self):
        cond = self._wait_for_element_selected(self.LABEL_INSTALL_COMMANDS)
        msg_true = "Tab '" + self.INSTALL_COMMANDS + "' is present"
        msg_false = "Tab '" + self.INSTALL_COMMANDS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_tab_uninstall_commands_is_present(self):
        cond = self._wait_for_element_selected(self.LABEL_UNINSTALL_COMMANDS)
        msg_true = "Tab '" + self.UNINSTALL_COMMANDS + "' is present"
        msg_false = "Tab '" + self.UNINSTALL_COMMANDS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False


class InstallCommandsPopup(BasePopup):

    INSTALL_COMMANDS = "Install Commands"

    def popup_body(self):
        locator = self._set_popup(self.INSTALL_COMMANDS)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.INSTALL_COMMANDS + "' is present"
        msg_false = "Popup '" + self.INSTALL_COMMANDS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class UninstallCommandsPopup(BasePopup):

    UNINSTALL_COMMANDS = "Uninstall Commands"

    def popup_body(self):
        locator = self._set_popup(self.UNINSTALL_COMMANDS)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.UNINSTALL_COMMANDS + "' is present"
        msg_false = "Popup '" + self.UNINSTALL_COMMANDS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())


class SupersedingPatchesPopup(BasePopup):

    SUPERSEDING_PATCHES = "Superseding Patches"

    def popup_body(self):
        locator = self._set_popup(self.SUPERSEDING_PATCHES)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.SUPERSEDING_PATCHES + "' is present"
        msg_false = "Popup '" + self.SUPERSEDING_PATCHES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())

    def click_button_edit(self):
        self._click_button_edit(self.popup_body())


class SelectSupersedingPatchesPopup(BasePopup):

    SELECT_SUPERSEDING_PATCHES = "Select Superseding Patches"

    def popup_body(self):
        locator = self._set_popup(self.SELECT_SUPERSEDING_PATCHES)
        cond = self._wait_for_element_present(locator)
        return str(locator) if cond else False

    def check_popup_is_present(self):
        cond = self.popup_body()
        msg_true = "Popup '" + self.SELECT_SUPERSEDING_PATCHES + "' is present"
        msg_false = "Popup '" + self.SELECT_SUPERSEDING_PATCHES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.popup_body())

    def click_button_ok(self):
        self._click_button_ok(self.popup_body())

    def click_button_cancel(self):
        self._click_button_cancel(self.popup_body())

    def click_system_button_close(self):
        self._click_system_button_close(self.popup_body())