
from _feature_objects.feature_popup import *


class BaseRibbonBar(BaseActions):

    def _set_ribbon_bar_button(self, button_name):
        locator = "//img[@alt='" + button_name + "']/ancestor::div[contains(@class,'RibbonBarButton')]"
        return str(locator)

    def _set_ribbon_bar_buttons_box(self, buttons_box_name):
        locator = "//div[text()='" + buttons_box_name + "'][contains(@class,'GroupBox-Text')]" \
                                                        "/ancestor::div[@class='RibbonBarGroupBox-Control']"
        return str(locator)


class RibbonBar(BaseRibbonBar):

    COLUMN_SETS = "Column Sets"
    USERS = "Users"
    HOME = "Home"
    UPDATES = "Updates"
    FORCE_UPDATE = "Force Update"
    DISCOVERY_TASK = "Discovery Task"
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
    TAB_ADVANCED = "//span[text()='Advanced']/ancestor::div[contains(@id,'TAB')]"
    BUTTONS_BOX_APPLICATIONS = "//div[text()='Applications'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_SITE_CONFIG = "//div[text()='Site Config'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_UPDATES = "//div[text()='Updates'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_INSTALL_MEDIA = "//div[text()='Install Media'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_DISPLAY = "//div[text()='Display'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_ACTIONS = "//div[text()='Actions'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_QUERIES = "//div[text()='Queries'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_GROUPS = "//div[text()='Groups'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_PATCH_GROUPS = "//div[text()='Patch Groups'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_INVENTORY = "//div[text()='Inventory'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_SITE_MANAGEMENT = "//div[text()='Site Management'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_COMPUTER_TOOLS = "//div[text()='Computer Tools'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_CONFIGURATION = "//div[text()='Configuration'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_CONFIG = "//div[text()='Config'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_COLUMN_SETS = "//div[contains(text(),'Column Sets')][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_USERS = "//div[text()='Users'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_MAINTENANCE_WINDOWS = "//div[text()='Maintenance Windows'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_DISCOVERY_TASK = "//div[text()='Discovery Task'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_SOFTWARE_DEPLOYMENT = "//div[text()='Software Deployment'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTONS_BOX_PATCH_MANAGER = "//div[text()='Patch Manager'][contains(@class,'GroupBox-Text')]" + BUTTONS_GROUP_BOX
    BUTTON_EXIT = "//img[@alt='Exit']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_HOME = "//img[@alt='Home']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_NEW = "//img[@alt='New']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_ADD = "//img[@alt='Add']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT = "//img[@alt='Edit']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT_FOLDER = "//img[@alt='Edit Folder']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_ACCOUNTS = "//img[@alt='Accounts']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EXCLUSIONS = "//img[@alt='Exclusions']/ancestor::div[contains(@class,'RibbonBarButton')]"
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
    BUTTON_DISCOVER = "//img[@alt='Discover']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CREATE = "//img[@alt='Create']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_FORCE_UPDATE = "//img[@alt='Force Update']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SCAN = "//img[@alt='Scan']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SCAN_AND_DEPLOY = "//img[@alt='Scan and Deploy']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_QUICK_INSTALL = "//img[@alt='Quick Install']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CREATE_GROUP = "//img[@alt='Create Group']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT_GROUP = "//img[@alt='Edit Group']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CREATE_QUERY = "//img[@alt='Create Query']/ancestor::div[contains(@class,'RibbonBarButton')]"
    MENU_ITEM_SETTINGS = DROP_DOWN_LIST + "/*//span[text()='Settings']" + MENU_ITEM
    MENU_ITEM_LOG_OUT = DROP_DOWN_LIST + "/*//span[contains(text(),'Log Out')]" + MENU_ITEM
    MENU_ITEM_GO_TO_HOME_SCREEN = DROP_DOWN_LIST + "/*//span[contains(text(),'Go To')]" + MENU_ITEM
    MENU_ITEM_CHANGE_HOME_SCREEN = DROP_DOWN_LIST + "/*//span[contains(text(),'Change Home')]" + MENU_ITEM
    MENU_ITEM_NEW_GROUP = DROP_DOWN_LIST + "/*//span[contains(text(),'New Group')]" + MENU_ITEM
    MENU_ITEM_NEW_FOLDER = DROP_DOWN_LIST + "/*//span[contains(text(),'New Folder')]" + MENU_ITEM
    MENU_ITEM_VIEW = DROP_DOWN_LIST + "/*//span[contains(text(),'View')]" + MENU_ITEM
    MENU_ITEM_ON_DEMAND = DROP_DOWN_LIST + "/*//span[contains(text(),'On Demand')]" + MENU_ITEM

    def buttons_box_discovery(self):
        locator = self._set_ribbon_bar_buttons_box(self.DISCOVERY_TASK)
        return str(locator)

    def click_tab_view(self):
        self._click_element(RibbonBar.TAB_VIEW)
        self._wait_for_element_selected(RibbonBar.TAB_VIEW)

    def click_tab_home(self):
        self._click_element(RibbonBar.TAB_HOME)
        self._wait_for_element_selected(RibbonBar.TAB_HOME)

    def click_tab_devices(self):
        self._click_element(RibbonBar.TAB_DEVICES)
        self._wait_for_element_selected(RibbonBar.TAB_DEVICES)
        self._wait_for_element_present(RibbonBar.BUTTON_PATCH_MANAGER)

    def click_tab_tools(self):
        self._click_element(RibbonBar.TAB_TOOLS)
        self._wait_for_element_selected(RibbonBar.TAB_TOOLS)

    def click_tab_advanced(self):
        self._click_element(RibbonBar.TAB_ADVANCED)
        self._wait_for_element_selected(RibbonBar.TAB_ADVANCED)

    def open_tab_home(self):
        self._wait_for_element_present(RibbonBar.TAB_HOME)
        cond = self._is_element_selected(RibbonBar.TAB_HOME)
        if cond:
            pass
        else:
            self.click_tab_home()

    def open_tab_view(self):
        self._wait_for_element_present(RibbonBar.TAB_VIEW)
        cond = self._is_element_selected(RibbonBar.TAB_VIEW)
        if cond:
            pass
        else:
            self.click_tab_view()

    def open_tab_devices(self):
        self._wait_for_element_present(RibbonBar.TAB_DEVICES)
        cond = self._is_element_selected(RibbonBar.TAB_DEVICES)
        if cond is not True:
            self.click_tab_devices()

    def open_tab_tools(self):
        self._wait_for_element_present(RibbonBar.TAB_TOOLS)
        cond = self._is_element_selected(RibbonBar.TAB_TOOLS)
        if cond:
            pass
        else:
            self.click_tab_tools()

    def open_tab_advanced(self):
        self._wait_for_element_present(RibbonBar.TAB_ADVANCED)
        cond = self._is_element_selected(RibbonBar.TAB_ADVANCED)
        if cond:
            pass
        else:
            self.click_tab_advanced()

    def check_tab_home_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_ACTIONS)
        return True if cond else False

    def check_tab_view_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_DISPLAY)
        return True if cond else False

    def check_devices_tab_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_INVENTORY)
        return True if cond else False

    def click_button_edit_or_create(self):
        self._click_element(RibbonBar.BUTTON_EDIT_OR_CREATE)
        # self._wait_for_element_present(ColumnSetsPopup.BODY)

    def click_button_new_site(self):
        self._click_element(RibbonBar.BUTTON_NEW_SITE)
        # self._wait_for_element_present(SiteNamePopup.BODY)

    def click_button_delete(self):
        self._click_element(RibbonBar.BUTTON_DELETE)
        # cond1 = self._is_element_present(AreYouSurePopup.PAGE_BODY)
        # cond2 = self._is_element_present(UnableToRemovePopup.PAGE_BODY)
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
        # self._wait_for_element_present(RemoveDevicesPopup.BODY)

    def click_button_config(self):
        self._wait_for_element_present(RibbonBar.BUTTON_CONFIG)
        self._click_element(RibbonBar.BUTTON_CONFIG)
        # self._wait_for_element_present(ConfigurationPopup.BODY)

    def click_button_move(self):
        self._click_element(RibbonBar.BUTTON_MOVE)
        # self._wait_for_element_present(MoveSitePopup.BODY)

    def click_button_move_device(self):
        self._click_element(RibbonBar.BUTTON_MOVE_DEVICE)

    def click_button_admin_user(self):
        self._click_element(RibbonBar.BUTTON_ADMIN_USER)
        self._wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_settings(self):
        self._click_element(RibbonBar.BUTTON_SETTINGS)
        # self._wait_for_element_present(SettingsPopup.BODY)

    def click_button_client(self):
        self._click_element(RibbonBar.BUTTON_CLIENT)
        # self._wait_for_element_present(ClientSettingsPopup.BODY)

    def click_button_subscriptions(self):
        self._click_element(RibbonBar.BUTTON_SUBSCRIPTIONS)
        self._wait_for_element_present(SubscriptionsPopup.BODY)

    def click_button_console_guide(self):
        self._click_element(RibbonBar.BUTTON_CONSOLE_GUIDE)
        time.sleep(0.5)

    def click_button_home(self):
        self._click_element(RibbonBar.BUTTON_HOME)
        # self._wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_view_logs(self):
        self._click_element(RibbonBar.BUTTON_VIEW_LOGS)
        # self._wait_for_element_present(ViewLogsPopup.BODY)

    def click_button_file_browser(self):
        self._click_element(RibbonBar.BUTTON_FILE_BROWSER)
        self.wait_for_loading_is_finished()
        # self._wait_for_element_present(FileExplorerPopup.BODY)

    def click_button_ping(self):
        self._click_element(RibbonBar.BUTTON_PING)
        self.wait_for_loading_is_finished()
        # self._wait_for_element_present(PingResultPopup.BODY)

    def click_button_process_viewer(self):
        self._click_element(RibbonBar.BUTTON_PROCESS_VIEWER)
        self.wait_for_loading_is_finished()
        # self._wait_for_element_present(ProcessExplorerPopup.BODY)

    def click_button_event_viewer(self):
        self._click_element(RibbonBar.BUTTON_EVENT_VIEWER)
        self.wait_for_loading_is_finished()
        # self._wait_for_element_present(EventViewerPopup.BODY)

    def click_button_wmi_explorer(self):
        self._click_element(RibbonBar.BUTTON_WMI_EXPLORER)
        self.wait_for_loading_is_finished()
        # self._wait_for_element_present(WMIExplorerPopup.BODY)

    def check_drop_down_list_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.DROP_DOWN_LIST)
        msg_true = "Drop Down list '" + self.HOME + "' is present"
        msg_false = "Drop Down list '" + self.HOME + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_button_currency(self):
        self._click_element(RibbonBar.BUTTON_CURRENCY)
        # self._wait_for_element_present(CurrencyPopup.BODY)

    def click_button_imperial_and_metric(self):
        self._click_element(RibbonBar.BUTTON_IMPERIAL_METRIC)
        # self._wait_for_element_present(WeightDisplayPopup.BODY)

    def click_button_makes(self):
        self._click_element(RibbonBar.BUTTON_MAKES)
        # self._wait_for_element_present(ManufacturerAliasPopup.BODY)

    def click_button_wake_up(self):
        self._click_element(RibbonBar.BUTTON_WAKE_UP)
        # self._wait_for_element_present(WakeOnLANPopup.BODY)

    def click_button_end_user_access(self):
        self._click_element(RibbonBar.BUTTON_END_USER_ACCESS)
        # self._wait_for_element_present(EndUserAccessPopup.BODY)

    def click_button_models(self):
        self._click_element(RibbonBar.BUTTON_MODELS)
        # self._wait_for_element_present(ModelAliasPopup.BODY)

    def click_button_inventory(self):
        self._click_element(RibbonBar.BUTTON_INVENTORY)
        cond = self._is_element_present(RibbonBar.BUTTON_INVENTORY + RibbonBar.DROP_DOWN_ARROW)
        if cond:
            self._wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_reports(self):
        self._click_element(RibbonBar.BUTTON_REPORTS)
        # self._wait_for_element_present(ReportsPopup.BODY)

    def click_button_new(self):
        self._click_element(RibbonBar.BUTTON_NEW)
        cond = self._is_element_present(RibbonBar.BUTTON_NEW + RibbonBar.DROP_DOWN_ARROW)
        if cond:
            self._wait_for_element_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_edit_folder(self):
        self._click_element(RibbonBar.BUTTON_EDIT_FOLDER)
        self._wait_for_element_present(EditFolderPopup.BODY)

    def click_new_folder_menu_item(self):
        self._click_element(RibbonBar.MENU_ITEM_NEW_FOLDER)
        self._wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        # self._wait_for_element_present(NewFolderPopup.BODY)

    def click_new_group_menu_item(self):
        self._click_element(RibbonBar.MENU_ITEM_NEW_GROUP)
        self._wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        # self._wait_for_element_present(NewGroupPopup.BODY)

    def click_view_menu_item(self):
        self._click_element(RibbonBar.MENU_ITEM_VIEW)
        self._wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        # self._wait_for_element_present(InventoryViewPopup.BODY)

    def click_on_demand_menu_item(self):
        self._click_element(RibbonBar.MENU_ITEM_ON_DEMAND)
        self._wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        # self._wait_for_element_present(OnDemandInventoryScanPopup.BODY)

    def click_settings_menu_item(self):
        self._click_element(RibbonBar.MENU_ITEM_SETTINGS)
        self._wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        # self._wait_for_element_present(UserSettingsPopup.BODY)

    def click_change_home_screen_menu_item(self):
        self._click_element(RibbonBar.MENU_ITEM_CHANGE_HOME_SCREEN)
        self._wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)
        # self._wait_for_element_present(SelectDashboardPopup.BODY)

    def click_go_to_home_screen_menu_item(self):
        self._click_element(RibbonBar.MENU_ITEM_GO_TO_HOME_SCREEN)
        # self._wait_for_element_not_present(RibbonBar.DROP_DOWN_LIST)

    def click_button_patch_manager(self):
        self._click_element(RibbonBar.BUTTON_PATCH_MANAGER)
        # self._wait_for_element_present(PatchManagerPopup.BODY)

    def click_button_accounts(self):
        self._click_element(RibbonBar.BUTTON_ACCOUNTS)
        # self._wait_for_element_present(AdminAccountsPopup.BODY)

    def click_button_exclusions(self):
        self._click_element(RibbonBar.BUTTON_EXCLUSIONS)
        # self._wait_for_element_present(ConfigureExclusionsPopup.BODY)

    def click_button_discover(self):
        self._click_element(RibbonBar.BUTTON_DISCOVER)
        discover_devices_popup = DiscoverDevicesPopup(self.driver)
        # self._wait_for_element_present(discover_devices_popup.popup_body())

    def click_button_add(self):
        self._click_element(RibbonBar.BUTTON_ADD)

    def click_button_create(self):
        self._click_element(RibbonBar.BUTTON_CREATE)

    def click_button_edit(self):
        self._click_element(RibbonBar.BUTTON_EDIT)

    def click_button_force_update(self):
        self._click_element(RibbonBar.BUTTON_FORCE_UPDATE)

    def click_button_scan(self):
        self._click_element(RibbonBar.BUTTON_SCAN)

    def check_box_updates_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_UPDATES)
        msg_true = "Buttons box '" + self.UPDATES + "' is present"
        msg_false = "Buttons box '" + self.UPDATES + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_maintenance_windows_box_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_MAINTENANCE_WINDOWS)
        msg_true = "Buttons box '" + self.USERS + "' is present"
        msg_false = "Buttons box '" + self.USERS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_queries_box_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_QUERIES)
        return True if cond else False

    def check_groups_box_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_GROUPS)
        return True if cond else False

    def check_configuration_box_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_CONFIGURATION)
        return True if cond else False

    def check_box_config_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_CONFIG)
        return True if cond else False

    def check_box_inventory_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_INVENTORY)
        return True if cond else False

    def check_box_discovery_task_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_DISCOVERY_TASK)
        return True if cond else False

    def check_box_software_deployment_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_SOFTWARE_DEPLOYMENT)
        return True if cond else False

    def check_box_patch_manager_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_PATCH_MANAGER)
        return True if cond else False

    def check_box_computer_tools_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_COMPUTER_TOOLS)
        return True if cond else False

    def check_box_site_management_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_SITE_MANAGEMENT)
        return True if cond else False

    def check_box_column_sets_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_COLUMN_SETS)
        msg_true = "Buttons box '" + self.COLUMN_SETS + "' is present"
        msg_false = "Buttons box '" + self.COLUMN_SETS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_box_users_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_USERS)
        msg_true = "Buttons box '" + self.USERS + "' is present"
        msg_false = "Buttons box '" + self.USERS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_box_applications_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTONS_BOX_APPLICATIONS)
        msg_true = "Buttons box '" + self.USERS + "' is present"
        msg_false = "Buttons box '" + self.USERS + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_button_edit_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_EDIT)
        return True if cond else False

    def check_button_edit_folder_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_EDIT_FOLDER)
        return True if cond else False

    def check_button_patch_manager_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_PATCH_MANAGER)
        return True if cond else False

    def click_button_scan_and_deploy(self):
        self._click_element(RibbonBar.BUTTON_SCAN_AND_DEPLOY)

    def check_button_discover_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_DISCOVER)
        return True if cond else False

    def check_button_force_update_is_unabled(self):
        cond = self._wait_for_element_unabled(RibbonBar.BUTTON_FORCE_UPDATE)
        msg_true = "Button '" + self.FORCE_UPDATE + "' is unabled"
        msg_false = "Button '" + self.FORCE_UPDATE + "' is NOT unabled"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_button_new_site_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_NEW_SITE)
        msg_true = "Button 'New Site' is present"
        msg_false = "Button 'New Site' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_button_config_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_CONFIG)
        return True if cond else False

    def check_button_exit_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_EXIT)
        return True if cond else False

    def check_button_edit_or_create_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_EDIT_OR_CREATE)
        return True if cond else False

    def check_button_delete_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_DELETE)
        return True if cond else False

    def check_button_wake_up_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_WAKE_UP)
        return True if cond else False

    def check_button_reports_is_present(self):
        cond = self._wait_for_element_present(RibbonBar.BUTTON_REPORTS)
        return True if cond else False

