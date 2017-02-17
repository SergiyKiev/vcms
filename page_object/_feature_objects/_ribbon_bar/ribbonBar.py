
from _feature_objects._popups.popupColumnSets import ColumnSetsPopup
from _feature_objects._popups.popupClientSettings import ClientSettingsPopup
from _feature_objects._popups.popupConfiguration import ConfigurationPopup
from _feature_objects._popups.popupCurrency import CurrencyPopup
from _feature_objects._popups.popupEditFolder import EditFolderPopup
from _feature_objects._popups.popupEndUserAccess import EndUserAccessPopup
from _feature_objects._popups.popupEventViewer import EventViewerPopup
from _feature_objects._popups.popupFileExplorer import FileExplorerPopup
from _feature_objects._popups.popupInventoryView import InventoryViewPopup
from _feature_objects._popups.popupManufacturerAlias import ManufacturerAliasPopup
from _feature_objects._popups.popupModelAlias import ModelAliasPopup
from _feature_objects._popups.popupMoveDevice import MoveDevicePopup
from _feature_objects._popups.popupMoveSite import MoveSitePopup
from _feature_objects._popups.popupNewFolder import NewFolderPopup
from _feature_objects._popups.popupNewGroup import NewGroupPopup
from _feature_objects._popups.popupOnDemandInventoryScan import OnDemandInventoryScanPopup
from _feature_objects._popups.popupPatchManager import PatchManagerPopup
from _feature_objects._popups.popupPingResult import PingResultPopup
from _feature_objects._popups.popupProcessExplorer import ProcessExplorerPopup
from _feature_objects._popups.popupRemoveDevices import RemoveDevicesPopup
from _feature_objects._popups.popupReports import ReportsPopup
from _feature_objects._popups.popupSelectDashboard import SelectDashboardPopup
from _feature_objects._popups.popupSettings import SettingsPopup
from _feature_objects._popups.popupSiteName import SiteNamePopup
from _feature_objects._popups.popupSubscriptionHasExpired import *
from _feature_objects._popups.popupSubscriptions import SubscriptionsPopup
from _feature_objects._popups.popupUserSettings import UserSettingsPopup
from _feature_objects._popups.popupViewLogs import ViewLogsPopup
from _feature_objects._popups.popupWMIExplorer import WMIExplorerPopup
from _feature_objects._popups.popupWakeOnLAN import WakeOnLANPopup
from _feature_objects._popups.popupWeightDisplay import WeightDisplayPopup
from _feature_objects._popups.popupAreYouSure import AreYouSurePopup
from _feature_objects._popups.popupUnableToRemove import UnableToRemovePopup
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class RibbonBar(BaseActions):

    DROP_DOWN_LIST = "//div[@class='Menu-PopupWindow']"
    DROP_DOWN_ARROW = "/*//img[contains(@src,'DropDown')]"
    BUTTONS_GROUP_BOX = "/ancestor::div[@class='RibbonBarGroupBox-Control']"
    MENU_ITEM = "/ancestor::div[contains(@class,'MenuItem-Control')]"
    RIBBON_BAR_TAB_HEADER = "//div[@class='RibbonBarTabControl-HeadersRow']"
    RIBBON_BAR_TAB_PAGE = "//div[@class='RibbonBarTabControl-CenterFrame']"
    TAB_HOME = "//span[text()='Home']/ancestor::div[contains(@id,'TAB')]"
    TAB_VIEW = "//span[text()='View']/ancestor::div[contains(@id,'TAB')]"
    TAB_TOOLS = "//span[text()='Tools']/ancestor::div[contains(@id,'TAB')]"
    TAB_DEVICES = "//span[text()='Devices']/ancestor::div[contains(@id,'TAB')]"
    BUTTONS_BOX_DISPLAY = "//div[text()='Display'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_ACTIONS = "//div[text()='Actions'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_QUERIES = "//div[text()='Queries'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_GROUPS = "//div[text()='Groups'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_INVENTORY = "//div[text()='Inventory'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_SITE_MANAGEMENT = "//div[text()='Site Management'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_COMPUTER_TOOLS = "//div[text()='Computer Tools'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTON_EXIT = "//img[@alt='Exit']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_HOME = "//img[@alt='Home']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_NEW = "//img[@alt='New']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT = "//img[@alt='Edit']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT_FOLDER = "//img[@alt='Edit Folder']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_NEW_SITE = "//img[@alt='New Site']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CONFIG = "//img[@alt='Config']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE = "//img[@alt='Delete']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE_OR_ARCHIVE = "//img[@alt='Delete / Archive']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE_SELECTED = "//img[@alt='Delete Selected']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE_GROUP = "//img[@alt='Delete Group']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE_FOLDER = "//img[@alt='Delete Folder']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_MOVE = "//img[@alt='Move']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SETTINGS = "//img[@alt='Settings']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_INVENTORY = "//img[@alt='Inventory']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CLIENT = "//img[@alt='Client']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SUBSCRIPTIONS = "//img[@alt='Subscriptions']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CONSOLE_GUIDE = "//img[@alt='Console Guide']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_ABOUT = "//img[@alt='About']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SAVE_CURRENT = "//img[@alt='Save Current Columns']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT_OR_CREATE = "//img[@alt='Edit/ Create']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_MOVE_DEVICE = "//img[@alt='Move Device']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_PATCH_MANAGER = "//img[@alt='Patch Manager']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CURRENCY = "//img[@alt='Currency']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_IMPERIAL_METRIC = "//img[@alt='Imperial / Metric']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_MAKES = "//img[@alt='Makes']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_MODELS = "//img[@alt='Models']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_ADMIN_USER = "//td[contains(@style,'icons-gray.111-user')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_WAKE_UP = "//img[@alt='Wake Up']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_END_USER_ACCESS = "//img[@alt='End User Access']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_REPORTS = "//img[@alt='Reports']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_VIEW_LOGS = "//img[@alt='View Logs']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_FILE_BROWSER = "//img[@alt='File Browser']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_PING = "//img[@alt='Ping']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_PROCESS_VIEWER = "//img[@alt='Process Viewer']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EVENT_VIEWER = "//img[@alt='Event Viewer']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_WMI_EXPLORER = "//img[@alt='WMI Explorer']/ancestor::div[contains(@class,'RibbonBarButton')]"
    MENU_ITEM_SETTINGS = DROP_DOWN_LIST + "/*//span[text()='Settings']" + MENU_ITEM
    MENU_ITEM_LOG_OUT = DROP_DOWN_LIST + "/*//span[contains(text(),'Log Out')]" + MENU_ITEM
    MENU_ITEM_GO_TO_HOME_SCREEN = DROP_DOWN_LIST + "/*//span[contains(text(),'Go To')]" + MENU_ITEM
    MENU_ITEM_CHANGE_HOME_SCREEN = DROP_DOWN_LIST + "/*//span[contains(text(),'Change Home')]" + MENU_ITEM
    MENU_ITEM_NEW_GROUP = DROP_DOWN_LIST + "/*//span[contains(text(),'New Group')]" + MENU_ITEM
    MENU_ITEM_NEW_FOLDER = DROP_DOWN_LIST + "/*//span[contains(text(),'New Folder')]" + MENU_ITEM
    MENU_ITEM_VIEW = DROP_DOWN_LIST + "/*//span[contains(text(),'View')]" + MENU_ITEM
    MENU_ITEM_ON_DEMAND = DROP_DOWN_LIST + "/*//span[contains(text(),'On Demand')]" + MENU_ITEM

    def click_tab_view(self):
        self._click_element(RibbonBar.TAB_VIEW)
        self.wait_for_element_selected(RibbonBar.TAB_VIEW)

    def click_tab_home(self):
        self._click_element(RibbonBar.TAB_HOME)
        self.wait_for_element_selected(RibbonBar.TAB_HOME)

    def click_tab_devices(self):
        self._click_element(RibbonBar.TAB_DEVICES)
        self.wait_for_element_selected(RibbonBar.TAB_DEVICES)

    def click_tab_tools(self):
        self._click_element(RibbonBar.TAB_TOOLS)
        self.wait_for_element_selected(RibbonBar.TAB_TOOLS)

    def open_tab_home(self):
        self.wait_for_element_present(RibbonBar.TAB_HOME)
        cond = self._is_element_selected(RibbonBar.TAB_HOME)
        if cond:
            pass
        else:
            self.click_tab_home()

    def open_tab_view(self):
        self.wait_for_element_present(RibbonBar.TAB_VIEW)
        cond = self._is_element_selected(RibbonBar.TAB_VIEW)
        if cond:
            pass
        else:
            self.click_tab_view()

    def open_tab_devices(self):
        self.wait_for_element_present(RibbonBar.TAB_DEVICES)
        cond = self._is_element_selected(RibbonBar.TAB_DEVICES)
        if cond:
            pass
        else:
            self.click_tab_devices()

    def open_tab_tools(self):
        self.wait_for_element_present(RibbonBar.TAB_TOOLS)
        cond = self._is_element_selected(RibbonBar.TAB_TOOLS)
        if cond:
            pass
        else:
            self.click_tab_tools()

    def check_tab_home_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_ACTIONS)
        return True if cond else False

    def check_tab_view_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_DISPLAY)
        return True if cond else False

    def check_devices_tab_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_INVENTORY)
        return True if cond else False

    def click_button_edit_or_create(self):
        self._click_element(RibbonBar.BUTTON_EDIT_OR_CREATE)
        self.wait_for_element_present(ColumnSetsPopup.BODY)

    def click_button_new_site(self):
        self._click_element(RibbonBar.BUTTON_NEW_SITE)
        self.wait_for_element_present(SiteNamePopup.BODY)

    def click_button_delete(self):
        self._click_element(RibbonBar.BUTTON_DELETE)
        # cond1 = self._is_element_present(AreYouSurePopup.BODY)
        # cond2 = self._is_element_present(UnableToRemovePopup.BODY)
        # if cond1:
        #     return AreYouSurePopup(self.driver)
        # elif cond2:
        #     return UnableToRemovePopup(self.driver)

    def click_button_delete_selected(self):
        self._click_element(RibbonBar.BUTTON_DELETE_SELECTED)

    def click_button_delete_group(self):
        self._click_element(RibbonBar.BUTTON_DELETE_GROUP)

    def click_button_delete_folder(self):
        self._click_element(RibbonBar.BUTTON_DELETE_FOLDER)

    def click_button_delete_or_archive(self):
        self._click_element(RibbonBar.BUTTON_DELETE_OR_ARCHIVE)
        self.wait_for_element_present(RemoveDevicesPopup.BODY)

    def click_button_config(self):
        self._click_element(RibbonBar.BUTTON_CONFIG)
        self.wait_for_element_present(ConfigurationPopup.BODY)

    def click_button_move(self):
        self._click_element(RibbonBar.BUTTON_MOVE)
        self.wait_for_element_present(MoveSitePopup.BODY)

    def click_button_move_device(self):
        self._click_element(RibbonBar.BUTTON_MOVE_DEVICE)
        self.wait_for_element_present(MoveDevicePopup.BODY)

    def click_button_admin_user(self):
        self._click_element(RibbonBar.BUTTON_ADMIN_USER)
        self.wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def check_button_new_site_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_NEW_SITE)
        return True if cond else False

    def check_button_config_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_CONFIG)
        return True if cond else False

    def check_button_exit_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_EXIT)
        return True if cond else False

    def check_button_edit_or_create_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_EDIT_OR_CREATE)
        return True if cond else False

    def check_button_delete_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_DELETE)
        return True if cond else False

    def check_button_wake_up_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_WAKE_UP)
        return True if cond else False

    def check_button_reports_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_REPORTS)
        return True if cond else False

    def click_button_settings(self):
        self._click_element(RibbonBar.BUTTON_SETTINGS)
        self.wait_for_element_present(SettingsPopup.BODY)

    def click_button_client(self):
        self._click_element(RibbonBar.BUTTON_CLIENT)
        self.wait_for_element_present(ClientSettingsPopup.BODY)

    def click_button_subscriptions(self):
        self._click_element(RibbonBar.BUTTON_SUBSCRIPTIONS)
        self.wait_for_element_present(SubscriptionsPopup.BODY)

    def click_button_console_guide(self):
        self._click_element(RibbonBar.BUTTON_CONSOLE_GUIDE)

    def click_button_home(self):
        self._click_element(RibbonBar.BUTTON_HOME)
        self.wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_view_logs(self):
        self._click_element(RibbonBar.BUTTON_VIEW_LOGS)
        self.wait_for_element_present(ViewLogsPopup.BODY)

    def click_button_file_browser(self):
        self._click_element(RibbonBar.BUTTON_FILE_BROWSER)
        self.wait_for_element_present(FileExplorerPopup.BODY)

    def click_button_ping(self):
        self._click_element(RibbonBar.BUTTON_PING)
        self.wait_for_element_present(PingResultPopup.BODY)

    def click_button_process_viewer(self):
        self._click_element(RibbonBar.BUTTON_PROCESS_VIEWER)
        self.wait_for_element_present(ProcessExplorerPopup.BODY)

    def click_button_event_viewer(self):
        self._click_element(RibbonBar.BUTTON_EVENT_VIEWER)
        self.wait_for_element_present(EventViewerPopup.BODY)

    def click_button_wmi_explorer(self):
        self._click_element(RibbonBar.BUTTON_WMI_EXPLORER)
        self.wait_for_element_present(WMIExplorerPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("CMS Quick Help Videos")
        return True if cond else False

    def check_drop_down_list_is_present(self):
        cond = self._is_element_present(RibbonBar.DROP_DOWN_LIST)
        return True if cond else False

    def click_button_currency(self):
        self._click_element(RibbonBar.BUTTON_CURRENCY)
        self.wait_for_element_present(CurrencyPopup.BODY)

    def click_button_imperial_and_metric(self):
        self._click_element(RibbonBar.BUTTON_IMPERIAL_METRIC)
        self.wait_for_element_present(WeightDisplayPopup.BODY)

    def click_button_makes(self):
        self._click_element(RibbonBar.BUTTON_MAKES)
        self.wait_for_element_present(ManufacturerAliasPopup.BODY)

    def click_button_wake_up(self):
        self._click_element(RibbonBar.BUTTON_WAKE_UP)
        self.wait_for_element_present(WakeOnLANPopup.BODY)

    def click_button_end_user_access(self):
        self._click_element(RibbonBar.BUTTON_END_USER_ACCESS)
        self.wait_for_element_present(EndUserAccessPopup.BODY)

    def click_button_models(self):
        self._click_element(RibbonBar.BUTTON_MODELS)
        self.wait_for_element_present(ModelAliasPopup.BODY)

    def click_button_inventory(self):
        cond = self._is_element_present(RibbonBar.BUTTON_INVENTORY + RibbonBar.DROP_DOWN_ARROW)
        self._click_element(RibbonBar.BUTTON_INVENTORY)
        if cond:
            self.wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_reports(self):
        self._click_element(RibbonBar.BUTTON_REPORTS)
        self.wait_for_element_present(ReportsPopup.BODY)

    def click_button_new(self):
        cond = self._is_element_present(RibbonBar.BUTTON_NEW + RibbonBar.DROP_DOWN_ARROW)
        self._click_element(RibbonBar.BUTTON_NEW)
        if cond:
            self.wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_edit_folder(self):
        self._click_element(RibbonBar.BUTTON_EDIT_FOLDER)
        self.wait_for_element_present(EditFolderPopup.BODY)

    def check_queries_box_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_QUERIES)
        return True if cond else False

    def check_groups_box_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_GROUPS)
        return True if cond else False

    def check_inventory_box_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_INVENTORY)
        return True if cond else False

    def check_computer_tools_box_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_COMPUTER_TOOLS)
        return True if cond else False

    def check_site_management_box_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTONS_BOX_SITE_MANAGEMENT)
        return True if cond else False

    def click_new_folder_label(self):
        self._click_element(RibbonBar.MENU_ITEM_NEW_FOLDER)
        self.wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        self.wait_for_element_present(NewFolderPopup.BODY)

    def click_new_group_label(self):
        self._click_element(RibbonBar.MENU_ITEM_NEW_GROUP)
        self.wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        self.wait_for_element_present(NewGroupPopup.BODY)

    def click_view_label(self):
        self._click_element(RibbonBar.MENU_ITEM_VIEW)
        self.wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        self.wait_for_element_present(InventoryViewPopup.BODY)

    def click_on_demand_label(self):
        self._click_element(RibbonBar.MENU_ITEM_ON_DEMAND)
        self.wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        self.wait_for_element_present(OnDemandInventoryScanPopup.BODY)

    def click_settings_label(self):
        self._click_element(RibbonBar.MENU_ITEM_SETTINGS)
        self.wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        self.wait_for_element_present(UserSettingsPopup.BODY)

    def click_change_home_screen_label(self):
        self._click_element(RibbonBar.MENU_ITEM_CHANGE_HOME_SCREEN)
        self.wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        self.wait_for_element_present(SelectDashboardPopup.BODY)

    def click_go_to_home_screen_label(self):
        self._click_element(RibbonBar.MENU_ITEM_GO_TO_HOME_SCREEN)
        self.wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)

    def check_button_edit_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_EDIT)
        return True if cond else False

    def check_button_edit_folder_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_EDIT_FOLDER)
        return True if cond else False

    def click_button_patch_manager(self):
        self._click_element(RibbonBar.BUTTON_PATCH_MANAGER)
        self.wait_for_element_present(PatchManagerPopup.BODY)

    def check_button_patch_manager_is_present(self):
        cond = self._is_element_present(RibbonBar.BUTTON_PATCH_MANAGER)
        return True if cond else False
