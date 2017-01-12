from selenium.webdriver.common.by import By
from variables import Variables


class Locators:

  def __init__(self):
    pass


  '''HTML SEARCH PATH'''
  ancestor                   = "/ancestor::"
  descendant                 = "/descendant::"
  following                  = "/following::"
  following_sibling          = "/following-sibling::"
  preceding_sibling          = "/preceding-sibling::"
  parent                     = "/parent::"
  child                      = "/child::"


  '''STATUS'''
  SELECTED                   = "[contains(@class,'Selected')]"
  DISABLED                   = "[contains(@class,'Disabled')]"
  VISIBLE                    = "[@data-vwgvisible='1']"
  INVISIBLE                  = "[@data-vwgvisible='0']"
  COLLAPSE                   = "[contains(@style,'LTR0')]"
  EXPAND                     = "[contains(@style,'LTR1')]"
  EMPTY                      = "[contains(@style,'TreeViewEmpty')]"
  PARENT_SITE                = "[contains(@style,'11LTR')]"
  CHILD_SITE                 = "[contains(@style,'10LTR')]"
  COLOR_WHITE                = "[contains(@style,'color:White')]"
  VISIBLE_LEFT_MENU          = "[contains(@style,'translate3d(0px, 0px, 0px)')]"

  '''ELEMENTS(EL)'''
  EL_LIST_VIEW_CONTROL              = "div[@class='Common-Unselectable ListView-Control']"
  EL_BAR                            = "div[contains(@id,'VWGTCTC')]"
  EL_FLAT_TOOL_BAR_BODY             = "div[@class='FlatToolBar-Center Common-FrameCenter']"
  EL_LOADING                        = "div[@id='VWG_LoadingAnimationBox']"
  EL_RIBBON_BAR_TAB                 = "div[@class='RibbonBarTabControl-Control']"
  EL_RIBBON_BAR_BODY                = "div[@class='RibbonBarTabControl-CenterFrame']"
  EL_POPUP                          = "div[contains(@id,'WRP')]"
  EL_BUTTON                         = "div[contains(@class,'Button')][contains(@id,'VWG_')]"
  EL_TABEL_HEADER                   = "div[contains(@id,'HEADER')]"
  EL_TABLE_BODY                     = "div[contains(@id,'VWGLVBODY')]"
  EL_TAB                            = "div[contains(@id,'TAB')]"
  EL_CHECKBOX                       = "div[contains(@class,'CheckBox')]"
  EL_TREE_CONTAINER                 = "div[@class='TreeView-Container']"
  EL_TREE_PADDING                   = "div[@class='TreeView-PaddingContainer']"
  EL_TREE_NODE                      = "div[contains(@class,'TreeView-RowContainer')]"
  EL_TREE_SUBNODE                   = "div[@class='TreeView-SubNodesContainer']"
  EL_PAGE_HEADER_PANEL              = "div[@class='Panel-Control'][contains(@style,'85px')]"
  EL_LEFT_MENU_CONTAINER            = "div[contains(@id,'VWG_')][contains(@style,'translate3d')]"
  EL_RIBBON_BAR_GROUP_BOX           = "div[@class='RibbonBarGroupBox-Control']"
  EL_TABLE_ROW                      = "tr[contains(@class,'ListView-DataFullRow')]"
  EL_DROP_DOWN_ARROW                = "img[contains(@src,'DropDown')]"

  '''LOADING ANIMATION XPATH'''
  LOADING_SCREEN_INVISIBLE           = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: none']"
  LOADING_SCREEN_VISIBLE             = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block']"

  '''TEXT(TXT) XPATH'''
  TEXT_GLOBAL_SITE_VIEW                 = "//span[text()='Global Site View']"
  TEXT_ERROR                            = "//span[text()='Error']"
  TEXT_DEFAULT_SITE                     = "//span[text()='Default Site']"
  TEXT_SIGN_IN                          = "//span[text()='Sign In']"
  TEXT_NEW_SITE                         = "//span[text()='New Site']"
  TEXT_OK                               = "//span[text()='OK']"
  TEXT_Ok                               = "//span[text()='Ok']"
  TEXT_CANCEL                           = "//span[text()='Cancel']"
  TEXT_I_AGREE                          = "//span[text()='I Agree']"
  TEXT_LOG_OUT                          = "//span[text()='Log Out']"
  TEXT_SETTINGS                         = "//span[text()='Settings']"
  TEXT_CONFIG                           = "//span[text()='Config']"
  TEXT_DELETE                           = "//span[text()='Delete']"
  TEXT_MOVE                             = "//span[text()='Move']"
  TEXT_MOVE_SITE                        = "//span[text()='Move Site']"
  TEXT_NEW                              = "//span[text()='New']"
  TEXT_EDIT                             = "//span[text()='Edit']"
  TEXT_ADD_MEMBERS                      = "//span[text()='Add Members']"
  TEXT_DELETE_MEMBERS                   = "//span[text()='Delete Members']"
  TEXT_REFRESH                          = "//span[text()='Refresh']"
  TEXT_INVENTORY_SCAN                   = "//span[text()='Inventory Scan']"
  TEXT_USER_INTERFACE_OPTIONS           = "//span[text()='User Interface Options']"
  TEXT_FINISH                           = "//span[text()='FINISH']"
  TEXT_CLOSE                            = "//span[text()='Close']"
  TEXT_COLUMN_SET_DESIGNER              = "//span[text()='Column Set Designer']"
  TEXT_NO                               = "//span[text()='No']"
  TEXT_YES                              = "//span[text()='Yes']"
  TEXT_SELECT_ALL                       = "//span[text()='Select All']"
  TEXT_SELECT_NONE                      = "//span[text()='Select None']"
  TEXT_SCAN_SELECTED                    = "//span[text()='Scan Selected']"
  TEXT_INSTALL_SELECTED                 = "//span[text()='Install Selected']"
  TEXT_RESET_TO_DEFAULT                 = "//span[text()='Reset to default']"
  TEXT_CONFIRM                          = "//span[text()='Confirm']"
  TEXT_CONFIGURATION                    = "//span[text()='Configuration']"
  TEXT_TOP                              = "//span[text()='Top']"
  TEXT_UP                               = "//span[text()='Up']"
  TEXT_DOWN                             = "//span[text()='Down']"
  TEXT_BOTTOM                           = "//span[text()='Bottom']"
  TEXT_GROUP                            = "//span[text()='Group']"
  TEXT_UNGROUP                          = "//span[text()='Ungroup']"
  TEXT_SELECT_COLUMNS                   = "//span[text()='Select Columns']"
  TEXT_CREATE                           = "//span[text()='Create']"
  TEXT_STOP                             = "//span[text()='Stop']"
  TEXT_RESTART                          = "//span[text()='Restart']"
  TEXT_PREVIOUS                         = "//span[text()='PREVIOUS']"
  TEXT_CREATE_NEW                       = "//span[text()='Create New']"
  TEXT_ADD_SITE                         = "//span[text()='Add Site']"
  TEXT_ADD_IP_RANGE                     = "//span[text()='Add IP Range']"
  TEXT_ADD                              = "//span[text()='Add']"
  TEXT_APPLY_CHANGES                    = "//span[text()='Apply Changes']"
  TEXT_VIEW_LOGS                        = "//span[text()='View Logs']"
  TEXT_FILE_BROWSER                     = "//span[text()='File Browser']"
  TEXT_PING                             = "//span[text()='Ping']"
  TEXT_PROCESS_VIEWER                   = "//span[text()='Process Viewer']"
  TEXT_WMI_EXPLORER                     = "//span[text()='WMI Explorer']"
  TEXT_REGISTRY_VIEWER                  = "//span[text()='Registry Viewer']"
  TEXT_EVENT_VEIWER                     = "//span[text()='Event Viewer']"
  TEXT_REMOTE_CONTROL                   = "//span[text()='Remote Control']"
  TEXT_PATCH_MANAGER                    = "//span[text()='Patch Manager']"
  TEXT_MOVE_DEVICE                      = "//span[text()='Move Device']"
  TEXT_REPORTS                          = "//span[text()='Reports']"
  TEXT_WAKE_UP                          = "//span[text()='Wake Up']"
  TEXT_END_USER_ACCESS                  = "//span[text()='End User Access']"
  TEXT_NEW_QUERY                        = "//span[text()='New Query']"
  TEXT_NEW_GROUP                        = "//span[text()='New Group']"
  TEXT_NEW_FOLDER                       = "//span[text()='New Folder']"
  TEXT_RUN_REPORT                       = "//span[text()='Run Report']"
  TEXT_SEARCH                           = "//span[text()='Search']"
  TEXT_APPLY                            = "//span[text()='Apply']"
  TEXT_UPDATE                           = "//span[text()='Update']"
  TEXT_TEST_SETTINGS                    = "//span[text()='Test Settings']"
  TEXT_RUN_ININTIAL_SETUP               = "//span[text()='Run Initial Setup']"
  TEXT_PURGE_OLDER_RECORDS              = "//span[text()='Purge Older Records']"
  TEXT_DELETE_ALL_ARCHIVE_DATA          = "//span[text()='Delete ALL Archive Data']"
  TEXT_PURGE_OLDER_ENTRIES_NOW          = "//span[text()='Purge older entries now']"
  TEXT_DELETE_ALL_AUDIT_LOGS            = "//span[text()='Delete all audit logs']"
  TEXT_REMOVE                           = "//span[text()='Remove']"
  TEXT_ARE_YOU_SURE                     = "//span[text()='Are you sure?']"
  TEXT_MANAGE_SUBSCRIPTIONS             = "//span[text()='Manage Subscriptions']"
  TEXT_TERMS_AND_CONDITIONS             = "//span[text()='Terms and Conditions']"
  TEXT_CLIENT_SETTINGS                  = "//span[text()='Client Settings']"
  TEXT_SUBSCRIPTIONS                    = "//span[text()='Subscriptions']"
  TEXT_ABOUT_CMS                        = "//span[text()='About Cloud Management Suite']"
  TEXT_RESET_PASSWORD                   = "//span[text()='Reset Password']"
  TEXT_LICENSES                         = "//span[text()='Licenses'][@dir='LTR']"
  TEXT_CMS                              = "//span[text()='Cloud Management Suite']"
  TEXT_SITE_CONFIGURATION               = "//span[text()='Site Configuration']"
  TEXT_IP_ADDRESS                       = "//span[text()='IP Address']"
  TEXT_DISCOVER_DEVICES                 = "//span[text()='Discover Devices']"
  TEXT_USER_CONFIGURATION               = "//span[text()='User Configuration']"
  TEXT_MAINTENANCE_WINDOW               = "//span[text()='Maintenance Window']"
  TEXT_REBOOT_UI_OPTIONS                = "//span[text()='Reboot UI Options']"
  TEXT_DISCOVERY_DETAILS                = "//span[text()='Discovery Details']"
  TEXT_SCANNED_ADDRESSES                = "//span[text()='Scanned Addresses']"
  TEXT_DISCOVERED_DEVICES               = "//span[text()='Discovered Devices']"
  TEXT_PATCH_MANAGER_SCANNING           = "//span[text()='Patch Manager Scanning']"
  TEXT_UNKNOWN_DEVICES                  = "//span[text()='Unknown Devices']"
  TEXT_REMOVE_DEVICES                   = "//span[text()='Remove Devices']"
  TEXT_REPORT_SCHEDULER                 = "//span[text()='Report Scheduler']"
  TEXT_MANAGEMENT_TREE                  = "//span[text()='Management Tree']"
  TEXT_DEPLOYMENTS                      = "//span[text()='Deployments']"
  TEXT_EDIT_GROUP                       = "//span[text()='Edit Group']"
  TEXT_EDIT_FOLDER                      = "//span[text()='Edit Folder']"
  TEXT_SELECT_TARGETS                   = "//span[text()='Select Targets']"
  TEXT_UNABLE_TO_REMOVE                 = "//span[text()='Unable to remove']"
  TEXT_MICROSOFT_UPDATE                 = "//span[text()='Microsoft Update']"
  TEXT_MICROSOFT_HOTFIX                 = "//span[text()='Microsoft Hotfix']"
  TEXT_SERVICE_PACK                     = "//span[text()='Service Pack']"
  TEXT_3RD_PARTY_UPDATE                 = "//span[text()='3rd Party Update']"
  TEXT_RESCHEDULE_EVERY                 = "//span[text()='Re-schedule Every']"
  TEXT_MONDAY                           = "//span[text()='Monday']"
  TEXT_TUESDAY                          = "//span[text()='Tuesday']"
  TEXT_WEDNESDAY                        = "//span[text()='Wednesday']"
  TEXT_THURSDAY                         = "//span[text()='Thursday']"
  TEXT_FRIDAY                           = "//span[text()='Friday']"
  TEXT_SATURDAY                         = "//span[text()='Saturday']"
  TEXT_SUNDAY                           = "//span[text()='Sunday']"
  TEXT_ENABLE_SNOOZE_REBOOT_DIALOG      = "//span[text()='Enable Snooze Reboot dialog']"
  TEXT_ALLOW_CANCEL_REBOOT              = "//span[text()='Allow the user to cancel the reboot']"
  TEXT_ALLOW_DEFER_REBOOT               = "//span[text()='Allow the user to defer (snooze) the reboot']"
  TEXT_SHOW_DATES                       = "//span[text()='Show Dates']"
  TEXT_FILTER_BY_LOCATION               = "//span[text()='Filter By Location']"
  TEXT_DO_NOT_DISPLAY_SCANNED_VALUES    = "//span[text()='Do not display scanned values']"
  TEXT_SYS_NOTIFICATIONS                = "//span[text()='System Notifications']"
  TEXT_VERISMIC_COMMUNICATIONS          = "//span[text()='Verismic Communications']"
  TEXT_MONITORING_ALERTS                = "//span[text()='Monitoring Alerts']"
  TEXT_AUTOMATICALLY_CHECK_FOR_NEW_DATA = "//span[text()='Automatically check for new data every day']"
  TEXT_SSL                              = "//span[text()='SSL']"
  TEXT_SHOW_TERMS_AND_CONDITIONS        = "//span[text()='Show Terms and Conditions at next login']"
  TEXT_ENFORCE_TWO_FACTOR_FOR_ALL_USERS = "//span[text()='Enforce two factor authentication for ALL users']"
  TEXT_ALLOW_STORE_TWO_FACTOR_IN_COOKIE = "//span[text()='Allow users to store their two-factor login in a cookie']"
  TEXT_PROMT_REMOTE_USER_CONTROL        = "//span[text()='Prompt remote user to accept or deny control']"
  TEXT_ACTIVE_DIRECTORIES               = "//span[text()='Active Directories']"
  TEXT_QUERIES                          = "//span[text()='Queries']"
  TEXT_GROUPS                           = "//span[text()='Groups']"
  TEXT_DEVICES                          = "//span[text()='Devices']"
  TEXT_QUERY_DESIGNER                   = "//span[text()='Query Designer']"

  '''TEXT CONTAINS XPATH'''
  TEXT_CONTAINS_DEFAULT_SITE            = "//span[contains(text(),'Default Site')]"
  TEXT_CONTAINS_GLOBAL_SITE_VIEW        = "//span[contains(text(),'Global Site View')]"
  TEXT_CONTAINS_COLUMN_SETS             = "//span[contains(text(),'Column Sets')]"
  TEXT_CONTAINS_SITE_NAME               = "//span[contains(text(),'Site') and contains(text(),'Name')]"
  TEXT_CONTAINS_IS_DEFAULT              = "//span[contains(text(),'Is Default')]"
  TEXT_CONTAINS_NAME                    = "//span[contains(text(),'Name')]"
  TEXT_CONTAINS_DESCRIPTION             = "//span[contains(text(),'Description:')]"
  TEXT_CONTAINS_COLUMNS                 = "//span[contains(text(),'Columns')]"

  '''CONTAINERS XPATH'''
  CONTAINER_GLOBAL_SITE_VIEW       = TEXT_GLOBAL_SITE_VIEW + ancestor + EL_TREE_PADDING + child + "div[1]"
  CONTAINER_ACTIVE_DIRECTORIES     = TEXT_ACTIVE_DIRECTORIES + ancestor + EL_TREE_PADDING + child + "div[2]"
  CONTAINER_QUERIES                = TEXT_QUERIES + ancestor + EL_TREE_PADDING + child + "div[3]"
  CONTAINER_GROUPS                 = TEXT_GROUPS + ancestor + EL_TREE_PADDING + child + "div[4]"
  CONTAINER_PANEL_TITLE_DEVICES    = TEXT_DEVICES + ancestor + EL_PAGE_HEADER_PANEL
  CONTAINER_HEADER_DEVICES_LIST    = CONTAINER_PANEL_TITLE_DEVICES + following + EL_TABEL_HEADER
  CONTAINER_BODY_DEVICES_LIST      = CONTAINER_PANEL_TITLE_DEVICES + following + EL_TABLE_BODY
  CONTAINER_MENU_DEVICES           = TEXT_DEVICES + ancestor + EL_LEFT_MENU_CONTAINER + VISIBLE_LEFT_MENU
  # CONTAINER_PATCHES_LIST_VIEW    = "//div[contains(@id,'VWG')][contains(@class,'ListView')]"

  '''GROUP BOX XPATH'''
  TITLE_GROUP_BOX_DISPLAY          = "//div[text()='Display']"
  TITLE_GROUP_BOX_ALIASES          = "//div[text()='Aliases']"
  TITLE_GROUP_BOX_COLUMN_SETS      = "//div[contains(text(),'Column Sets')]"
  GROUP_BOX_RIBBON_BAR_DISPLAY     = TITLE_GROUP_BOX_DISPLAY + ancestor + EL_RIBBON_BAR_GROUP_BOX
  GROUP_BOX_RIBBON_BAR_ALIASES     = TITLE_GROUP_BOX_ALIASES + ancestor + EL_RIBBON_BAR_GROUP_BOX
  GROUP_BOX_RIBBON_BAR_COLUMN_SETS = TITLE_GROUP_BOX_COLUMN_SETS + ancestor + EL_RIBBON_BAR_GROUP_BOX

  '''TREES XPATH'''
  TREE_GLOBAL_SITE_VIEW        = CONTAINER_GLOBAL_SITE_VIEW + child + EL_TREE_SUBNODE
  TREE_ACTIVE_DERICTORIES      = CONTAINER_ACTIVE_DIRECTORIES + child + EL_TREE_SUBNODE
  TREE_QUERIES                 = CONTAINER_QUERIES + child + EL_TREE_SUBNODE
  TREE_GROUPS                  = CONTAINER_GROUPS + child + EL_TREE_SUBNODE

  '''LABELS XPATH'''
  LABEL_GLOBAL_SITE_VIEW       = CONTAINER_GLOBAL_SITE_VIEW + child + EL_TREE_NODE
  LABEL_ACTIVE_DIRECTORIES     = CONTAINER_ACTIVE_DIRECTORIES + child + EL_TREE_NODE
  LABEL_QUERIES                = CONTAINER_QUERIES + child + EL_TREE_NODE
  LABEL_GROUPS                 = CONTAINER_GROUPS + child + EL_TREE_NODE
  LABEL_DEFAULT_SITE           = TREE_GLOBAL_SITE_VIEW + "/div/div/*" + TEXT_DEFAULT_SITE + ancestor + EL_TREE_NODE

  '''SITES XPATH'''
  SITE_GLOBAL_SITE_VIEW           = "//span[text()='Global Site View']"

  '''FIELD (FD) XPATH'''
  FD_                             = "//input"
  FD_USERNAME                     = "//input[@type='text']"
  FD_PASSWORD                     = "//input[@type='password']"

  '''BUTTONS (BTN) XPATH'''
  BTN_                         = "//div[contains(@class,'Button')][contains(@id,'VWG_')]"
  BTN_SIGN_IN                  = TEXT_SIGN_IN + ancestor + EL_BUTTON
  BTN_EXIT                     = "//img[@alt='Exit']"
  BTN_DEVICES                  = "//div[@title='Devices']"
  BTN_NEW_SITE                 = "//img[@alt='New Site']"
  BTN_NEW_SITE_by_text         = TEXT_NEW_SITE + ancestor + EL_BUTTON
  BTN_OK                       = TEXT_OK + ancestor + EL_BUTTON
  BTN_Ok                       = TEXT_Ok + ancestor + EL_BUTTON
  BTN_CANCEL                   = "//span[text()='Cancel']"
  BTN_I_AGREE                  = "//span[text()='I Agree']"
  BTN_ICON_ADMIN_USER          = "//td[contains(@style,'icons-gray.111-user')]"
  BTN_LOG_OUT                  = "//span[text()='Log Out']"
  BTN_SETTINGS_UPPER_CORNER    = "//span[text()='Settings']"
  BTN_CONFIG                   = "//img[@alt='Config']"
  BTN_CONFIG_by_text           = "//span[text()='Config']"
  BTN_DELETE                   = "//img[@alt='Delete']"
  BTN_DELETE_by_text           = "//span[text()='Delete']"
  BTN_DELETE_GROUP             = "//img[@alt='Delete Group']"
  BTN_DELETE_FOLDER            = "//img[@alt='Delete Folder']"
  BTN_MOVE                     = "//img[@alt='Move']"
  BTN_MOVE_by_text             = "//span[text()='Move']"
  BTN_MOVE_SITE                = "//span[text()='Move Site']"
  BTN_SETTINGS                 = "//img[@alt='Settings']"
  BTN_CLIENT                   = "//img[@alt='Client']"
  BTN_SUBSCRIPTIONS            = "//img[@alt='Subscriptions']"
  BTN_ABOUT                    = "//img[@alt='About']"
  BTN_NEW                      = "//img[@alt='New']"
  BTN_NEW_by_text              = "//span[text()='New']"
  BTN_NEW_DROP_DOWN            = BTN_NEW + following + EL_DROP_DOWN_ARROW
  BTN_EDIT_1                   = "//img[@alt='Edit']"
  BTN_EDIT_2                   = "//span[text()='Edit']"
  BTN_EDIT_GROUP               = "//img[@alt='Edit Group']"
  BTN_EDIT_FOLDER              = "//img[@alt='Edit Folder']"
  BTN_ADD_MEMBERS              = "//span[text()='Add Members']"
  BTN_DELETE_MEMBERS           = TEXT_DELETE_MEMBERS + ancestor + EL_BUTTON
  BTN_HOME                     = "//img[@alt='Home']"
  BTN_HOME_DROP_DOWN_ARROW     = BTN_HOME + following + EL_DROP_DOWN_ARROW
  BTN_INVENTORY                = "//img[@alt='Inventory']"
  BTN_INVENTORY_DROP_DOWN      = BTN_INVENTORY + following + EL_DROP_DOWN_ARROW
  BTN_REFRESH                  = "//span[text()='Refresh']"
  BTN_INVENTORY_SCAN           = "//span[text()='Inventory Scan']"
  BTN_USER_INTERFACE_OPTIONS   = "//span[text()='User Interface Options']"
  BTN_FINISH                   = "//span[text()='FINISH']"
  BTN_CLOSE                    = "//span[text()='Close']"
  BTN_NO                       = "//span[text()='No']"
  BTN_YES                      = "//span[text()='Yes']"
  BTN_SELECT_ALL               = "//span[text()='Select All']"
  BTN_SELECT_NONE              = "//span[text()='Select None']"
  BTN_SCAN_SELECTED            = "//span[text()='Scan Selected']"
  BTN_INSTALL_SELECTED         = "//span[text()='Install Selected']"
  BTN_ICON_SEARCH              = "//img[contains(@src,'06-magnify.2xw')]"
  BTN_ICON_HELP                = "//img[contains(@src,'About')]"
  BTN_ICON_EXPORT              = "//img[contains(@src,'212-action2')]"
  BTN_ICON_REFRESH             = "//img[contains(@src,'02-redo.2x')]"
  BTN_RESET_TO_DEFAULT         = "//span[text()='Reset to default']"
  BTN_CONFIRM                  = "//span[text()='Confirm']"
  BTN_EDIT                     = "//img[@alt='Edit']"
  BTN_TOP                      = "//span[text()='Top']"
  BTN_UP                       = "//span[text()='Up']"
  BTN_DOWN                     = "//span[text()='Down']"
  BTN_BOTTOM                   = "//span[text()='Bottom']"
  BTN_GROUP                    = "//span[text()='Group']"
  BTN_UNGROUP                  = "//span[text()='Ungroup']"
  BTN_SELECT_COLUMNS           = "//span[text()='Select Columns']"
  BTN_CREATE_                  = "//img[@alt='Create']"
  BTN_CREATE_by_text           = "//span[text()='Create']"
  BTN_STOP                     = "//img[@alt='Stop']"
  BTN_STOP_by_text             = "//span[text()='Stop']"
  BTN_RESTART                  = "//img[@alt='Restart']"
  BTN_RESTART_by_text          = "//span[text()='Restart']"
  BTN_CMS_UNIVERSITY           = "//img[@alt='CMS University']"
  BTN_NEXT                     = "//img[@alt='NEXT']"
  BTN_PREVIOUS                 = "//span[text()='PREVIOUS']"
  BTN_CREATE_NEW               = "//span[text()='Create New']"
  BTN_ADD_SITE                 = "//span[text()='Add Site']"
  BTN_IP_RANGE                 = "//span[text()='Add IP Range']"
  BTN_ADD                      = "//span[text()='Add']"
  BTN_APPLY_CHANGES            = "//span[text()='Apply Changes']"
  BTN_SAVE_CURRENT             = "//img[@alt='Save Current Columns']"
  BTN_DEFAULT_FOR_SITE         = "//img[@alt='Default For Site']"
  BTN_VIEW_LOGS_1              = "//img[@alt='View Logs']"
  BTN_VIEW_LOGS_2              = "//span[text()='View Logs']"
  BTN_FILE_BROWSER_1           = "//img[@alt='File Browser']"
  BTN_FILE_BROWSER_2           = "//span[text()='File Browser']"
  BTN_PING_1                   = "//img[@alt='Ping']"
  BTN_PING_2                   = "//span[text()='Ping']"
  BTN_PROCESS_VIEWER_1         = "//img[@alt='Process Viewer']"
  BTN_PROCESS_VIEWER_2         = "//span[text()='Process Viewer']"
  BTN_WMI_EXPLORER_1           = "//img[@alt='WMI Explorer']"
  BTN_WMI_EXPLORER_2           = "//span[text()='WMI Explorer']"
  BTN_REGISTRY_VIEWER_1        = "//img[@alt='Registry Viewer']"
  BTN_REGISTRY_VIEWER_2        = "//span[text()='Registry Viewer']"
  BTN_EVENT_VEIWER_1           = "//img[@alt='Event Viewer']"
  BTN_EVENT_VEIWER_2           = "//span[text()='Event Viewer']"
  BTN_REMOTE_CONTROL_1         = "//img[@alt='Remote Control']"
  BTN_REMOTE_CONTROL_2         = "//span[text()='Remote Control']"
  BTN_PATCH_MANAGER_1          = "//img[@alt='Patch Manager']"
  BTN_PATCH_MANAGER_2          = "//span[text()='Patch Manager']"
  BTN_MOVE_DEVICE_1            = "//img[@alt='Move Device']"
  BTN_MOVE_DEVICE_2            = "//span[text()='Move Device']"
  BTN_REPORTS_1                = "//img[@alt='Reports']"
  BTN_REPORTS_2                = "//span[text()='Reports']"
  BTN_WAKE_UP_1                = "//img[@alt='Wake Up']"
  BTN_WAKE_UP_2                = "//span[text()='Wake Up']"
  BTN_END_USER_ACCESS_1        = "//img[@alt='End User Access']"
  BTN_END_USER_ACCESS_2        = "//span[text()='End User Access']"
  BTN_NEW_QUERY                = "//span[text()='New Query']"
  BTN_NEW_GROUP                = "//span[text()='New Group']"
  BTN_NEW_FOLDER               = "//span[text()='New Folder']"
  BTN_RUN_REPORT               = "//span[text()='Run Report']"
  BTN_SEARCH                   = "//span[text()='Search']"
  BTN_SET_AS_DEFAULT           = "//img[@alt='Set As Default']"
  BTN_COPY                     = "//img[@alt='Copy']"
  BTN_APPLY                    = "//span[text()='Apply']"
  BTN_UPDATE                   = "//span[text()='Update']"
  BTN_TEST_SETTINGS            = "//span[text()='Test Settings']"
  BTN_RUN_ININTIAL_SETUP       = "//span[text()='Run Initial Setup']"
  BTN_PURGE_OLDER_RECORDS      = "//span[text()='Purge Older Records']"
  BTN_DELETE_ALL_ARCHIVE_DATA  = "//span[text()='Delete ALL Archive Data']"
  BTN_PURGE_OLDER_ENTRIES_NOW  = "//span[text()='Purge older entries now']"
  BTN_DELETE_ALL_AUDIT_LOGS    = "//span[text()='Delete all audit logs']"
  BTN_REMOVE                   = "//span[text()='Remove']"
  BTN_ICON_NEXT                = "//img[contains(@src,'right-double')]"
  BTN_ICON_PREVIOUS            = "//img[contains(@src,'left-double')]"
  BTN_EDIT_OR_CREATE           = "//img[@alt='Edit/ Create']"

  '''SYSTEM (SYS) ELEMENTS XPATH'''
  SYS_BTN                      = "//div[contains(@class,'Button')][contains(@id,'VWGE_')]"
  SYS_TREE_ARROW               = "//div[@data-vwgtype='joint']"
  SYS_BTN_CLOSE                = "//div[@title='Close']"
  SYS_BTN_NEXT                 = "//div[contains(@class,'NextButton')]"
  SYS_BTN_LAST                 = "//div[contains(@class,'LastButton')]"
  SYS_BTN_PREVIOUS             = "//div[contains(@class,'PrevButton')]"
  SYS_BTN_FIRST                = "//div[contains(@class,'FirstButton')]"
  SYS_BTN_NUMERIC_UP           = "//div[@class=' NumericUpDown-UpCell']"
  SYS_BTN_NUMERIC_DOWN         = "//div[@class='NumericUpDown-DownCell']"
  SYS_BTN_DROP_DOWN            = "//div[contains(@class,'ButtonContainer')]"
  SYS_TREE_ARROW_COLLAPSE      = SYS_TREE_ARROW  + COLLAPSE
  SYS_TREE_ARROW_EXPAND        = SYS_TREE_ARROW  + EXPAND

  '''POPUP XPATH'''
  POPUP_                          = "//" + EL_POPUP
  POPUP_SITE_NAME                 = TEXT_CONTAINS_SITE_NAME + ancestor + EL_POPUP
  POPUP_ARE_YOU_SURE              = TEXT_ARE_YOU_SURE + ancestor + EL_POPUP
  POPUP_SUBSCRIPTION_HAS_EXPIRED  = TEXT_MANAGE_SUBSCRIPTIONS + ancestor + EL_POPUP
  POPUP_TERMS_AND_CONDITIONS      = TEXT_TERMS_AND_CONDITIONS + ancestor + EL_POPUP
  POPUP_ERROR                     = TEXT_ERROR + ancestor + EL_POPUP
  POPUP_CONFIGURATION             = TEXT_CONFIGURATION + ancestor + EL_POPUP
  POPUP_COLUMN_SET_DESIGNER       = TEXT_COLUMN_SET_DESIGNER + ancestor + EL_POPUP
  POPUP_COLUMN_SETS               = TEXT_CONTAINS_COLUMN_SETS + ancestor + EL_POPUP
  POPUP_MOVE_SITE                 = TEXT_MOVE_SITE + ancestor + EL_POPUP
  POPUP_SETTINGS                  = TEXT_SETTINGS + ancestor + EL_POPUP
  POPUP_CLIENT_SETTINGS           = TEXT_CLIENT_SETTINGS + ancestor + EL_POPUP
  POPUP_SUBSCRIPTIONS             = TEXT_SUBSCRIPTIONS + ancestor + EL_POPUP
  POPUP_ABOUT_CMS                 = TEXT_ABOUT_CMS + ancestor + EL_POPUP
  POPUP_RESET_PASSWORD            = TEXT_RESET_PASSWORD + ancestor + EL_POPUP
  POPUP_LICENSES                  = TEXT_LICENSES + ancestor + EL_POPUP
  POPUP_CMS                       = TEXT_CMS + COLOR_WHITE + ancestor + EL_POPUP
  POPUP_SITE_CONFIGURATION        = TEXT_SITE_CONFIGURATION + ancestor + EL_POPUP
  POPUP_IP_ADDRESS                = TEXT_IP_ADDRESS + ancestor + EL_POPUP
  POPUP_DISCOVER_DEVICES          = TEXT_DISCOVER_DEVICES + ancestor + EL_POPUP
  POPUP_USER_CONFIGURATION        = TEXT_USER_CONFIGURATION + ancestor + EL_POPUP
  POPUP_MAINTENANCE_WINDOW        = TEXT_MAINTENANCE_WINDOW + ancestor + EL_POPUP
  POPUP_REBOOT_UI_OPTIONS         = TEXT_REBOOT_UI_OPTIONS + ancestor + EL_POPUP
  POPUP_DISCOVERY_DETAILS         = TEXT_DISCOVERY_DETAILS + ancestor + EL_POPUP
  POPUP_SCANNED_ADDRESSES         = TEXT_SCANNED_ADDRESSES + ancestor + EL_POPUP
  POPUP_DISCOVERED_DEVICES        = TEXT_DISCOVERED_DEVICES + ancestor + EL_POPUP
  POPUP_PATCH_MANAGER_SCANNING    = TEXT_PATCH_MANAGER_SCANNING + ancestor + EL_POPUP
  POPUP_UNKNOWN_DEVICES           = TEXT_UNKNOWN_DEVICES + ancestor + EL_POPUP
  POPUP_REMOVE_DEVICES            = TEXT_REMOVE_DEVICES + ancestor + EL_POPUP
  POPUP_MOVE_DEVICE               = TEXT_MOVE_DEVICE + ancestor + EL_POPUP
  POPUP_REPORTS                   = TEXT_REPORTS + ancestor + EL_POPUP
  POPUP_REPORT_SCHEDULER          = TEXT_REPORT_SCHEDULER + ancestor + EL_POPUP
  POPUP_MANAGEMENT_TREE           = TEXT_MANAGEMENT_TREE + ancestor + EL_POPUP
  POPUP_END_USER_ACCESS           = TEXT_END_USER_ACCESS + ancestor + EL_POPUP
  POPUP_DEPLOYMENTS               = TEXT_DEPLOYMENTS + ancestor + EL_POPUP
  POPUP_NEW_GROUP                 = TEXT_NEW_GROUP + ancestor + EL_POPUP
  POPUP_EDIT_GROUP                = TEXT_EDIT_GROUP + ancestor + EL_POPUP
  POPUP_EDIT_FOLDER               = TEXT_EDIT_FOLDER + ancestor + EL_POPUP
  POPUP_NEW_FOLDER                = TEXT_NEW_FOLDER + ancestor + EL_POPUP
  POPUP_SELECT_TARGETS            = TEXT_SELECT_TARGETS + ancestor + EL_POPUP
  POPUP_UNABLE_TO_REMOVE          = TEXT_UNABLE_TO_REMOVE + ancestor + EL_POPUP
  POPUP_QUERY_DESIGNER            = TEXT_QUERY_DESIGNER + ancestor + EL_POPUP
  POPUP_DROP_DOWN                 = "//div[@class='Form-PopupWindow']"

  '''CONTEXT MENU XPATH'''
  CONTEXT_MENU                    = "//div[@class='Menu-PopupWindow']"

  '''TABS XPATH'''
  TAB_                            = "//span[contains(@class,'TabControl')]"
  TAB_PANEL                       = "//div[contains(@id,'VWGTCHD_')]"
  TAB_HOME                        = "//span[contains(@class,'TabControl')][text()='Home']" + ancestor + EL_TAB
  TAB_VIEW                        = "//span[contains(@class,'TabControl')][text()='View']" + ancestor + EL_TAB
  TAB_DEVICES                     = "//span[contains(@class,'TabControl')][text()='Devices']" + ancestor + EL_TAB
  TAB_TOOLS                       = "//span[contains(@class,'TabControl')][text()='Tools']" + ancestor + EL_TAB
  TAB_OPTIONS                     = "//span[contains(@class,'TabControl')][text()='Options']" + ancestor + EL_TAB
  TAB_LOG                         = "//span[contains(@class,'TabControl')][text()='Log']" + ancestor + EL_TAB
  TAB_SMTP                        = "//span[contains(@class,'TabControl')][text()='SMTP']" + ancestor + EL_TAB
  TAB_IMAP                        = "//span[contains(@class,'TabControl')][text()='IMAP']" + ancestor + EL_TAB
  TAB_SITE                        = "//span[contains(@class,'TabControl')][text()='Site']" + ancestor + EL_TAB
  TAB_IP_ADDRESS_RANGES           = "//span[contains(@class,'TabControl')][text()='IP Address Ranges']" + ancestor + EL_TAB
  TAB_VREPS                       = "//span[contains(@class,'TabControl')][text()='vReps']" + ancestor + EL_TAB
  TAB_IP_ADDRESS_RANGES_LIST_VIEW_CONTROL = TAB_IP_ADDRESS_RANGES + SELECTED + following + \
                                            EL_BAR + "/div[1]/*//" + EL_LIST_VIEW_CONTROL
  TAB_IP_ADDRESS_RANGES_TOOL_BAR = TAB_IP_ADDRESS_RANGES + SELECTED + \
                                   following + "div[contains(@id,'VWGTCTC')]/div[1]/*//" + EL_FLAT_TOOL_BAR_BODY

  '''TAB BAR XPATH'''
  # TAB_BAR_CONFIGURATION_POPUP   = POPUP_CONFIGURATION + "/*//div[contains(@id,'VWGTCTC')]"
  # TAB_RIBBON_BAR


  '''RADIO BUTTON XPATH'''
  RB_CHECKED                      = "//td[contains(@style,'Radio1')]"
  RB_UNCHECKED                    = "//td[contains(@style,'Radio0')]"
  RB_ALL_DEVICES                  = "//span[text()='All Devices']/ancestor::div[contains(@class,'RadioButton')]"
  RB_SPECIFIC_DEVICES             = "//span[text()='Specific devices (select below)']/" \
                                                    "ancestor::div[contains(@class,'RadioButton')]"
  RB_ALL                          = "//span[text()='All']/ancestor::div[contains(@class,'RadioButton')]"
  RB_SPECIFIC                     = "//span[text()='Specific']/ancestor::div[contains(@class,'RadioButton')]"
  RB_PATCH_GROUPS                 = "//span[text()='Patch Groups']/ancestor::div[contains(@class,'RadioButton')]"
  RB_PATCH_QUERY_RULES            = "//span[text()='Patch Query Rules']/ancestor::div[contains(@class,'RadioButton')]"
  RB_UNSCHEDULED                  = "//span[text()='Unscheduled']/ancestor::div[contains(@class,'RadioButton')]"
  RB_START_NOW                    = "//span[text()='Start Now']/ancestor::div[contains(@class,'RadioButton')]"
  RB_START_LATER                  = "//span[text()='Start Later']/ancestor::div[contains(@class,'RadioButton')]"
  RB_USE_MAINTENANCE_WINDOW       = "//span[text()='Use Maintenance Window']/" \
                                                    "ancestor::div[contains(@class,'RadioButton')]"
  RB_DEVICES_THAT_MISSED          = "//span[text()='Devices that missed this task previously']/" \
                                                    "ancestor::div[contains(@class,'RadioButton')]"
  RB_INSTALL                      = "//span[text()='Install']/ancestor::div[contains(@class,'RadioButton')]"
  RB_UNINSTALL                    = "//span[text()='Uninstall']/ancestor::div[contains(@class,'RadioButton')]"
  RB_AND                          = "//span[text()='And']/ancestor::div[contains(@class,'RadioButton')]"
  RB_OR                           = "//span[text()='Or']/ancestor::div[contains(@class,'RadioButton')]"

  '''CHECK BOXES XPATH'''
  CB_CHECKED                        = "//td[contains(@style,'CheckBox1')]"
  CB_UNCHECKED                      = "//td[contains(@style,'CheckBox0')]"
  CB_MICROSOFT_UPDATE               = "//span[text()='Microsoft Update']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_MICROSOFT_HOTFIX               = "//span[text()='Microsoft Hotfix']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_SERVICE_PACK                   = "//span[text()='Service Pack']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_3RD_PARTY_UPDATE               = "//span[text()='3rd Party Update']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_RESCHEDULE_EVERY               = "//span[text()='Re-schedule Every']" + ancestor + EL_CHECKBOX
  CB_MONDAY                         = "//span[text()='Monday']" + ancestor + EL_CHECKBOX
  CB_TUESDAY                        = "//span[text()='Tuesday']" + ancestor + EL_CHECKBOX
  CB_WEDNESDAY                      = "//span[text()='Wednesday']" + ancestor + EL_CHECKBOX
  CB_THURSDAY                       = "//span[text()='Thursday']" + ancestor + EL_CHECKBOX
  CB_FRIDAY                         = "//span[text()='Friday']" + ancestor + EL_CHECKBOX
  CB_SATURDAY                       = "//span[text()='Saturday']" + ancestor + EL_CHECKBOX
  CB_SUNDAY                         = "//span[text()='Sunday']" + ancestor + EL_CHECKBOX
  CB_ENABLE_SNOOZE_REBOOT_DIALOG    = "//span[text()='Enable Snooze Reboot dialog']" + ancestor + EL_CHECKBOX
  CB_ALLOW_CANCEL_REBOOT            = "//span[text()='Allow the user to cancel the reboot']" + ancestor + EL_CHECKBOX
  CB_ALLOW_DEFER_REBOOT             = "//span[text()='Allow the user to defer (snooze) the reboot']" + ancestor + EL_CHECKBOX
  CB_SHOW_DATES                     = "//span[text()='Show Dates']" + ancestor + EL_CHECKBOX
  CB_FILTER_BY_LOCATION             = "//span[text()='Filter By Location']" + ancestor + EL_CHECKBOX
  CB_DO_NOT_DISPLAY_SCANNED_VALUES  = "//span[text()='Do not display scanned values']" + ancestor + EL_CHECKBOX
  CB_SYS_NOTIFICATIONS           = "//span[text()='System Notifications']" + ancestor + EL_CHECKBOX
  CB_VERISMIC_COMMUNICATIONS        = "//span[text()='Verismic Communications']" + ancestor + EL_CHECKBOX
  CB_MONITORING_ALERTS              = "//span[text()='Monitoring Alerts']" + ancestor + EL_CHECKBOX
  CB_AUTOMATICALLY_CHECK_FOR_NEW_DATA = "//span[text()='Automatically check for new data every day']" + ancestor + EL_CHECKBOX
  CB_SSL                            = "//span[text()='SSL']" + ancestor + EL_CHECKBOX
  CB_SHOW_TERMS_AND_CONDITIONS      = "//span[text()='Show Terms and Conditions at next login']" + ancestor + EL_CHECKBOX
  CB_ENFORCE_TWO_FACTOR_FOR_ALL_USERS = "//span[text()='Enforce two factor authentication for ALL users']" + ancestor + EL_CHECKBOX
  CB_ALLOW_STORE_TWO_FACTOR_IN_COOKIE = "//span[text()='Allow users to store their two-factor login in a cookie']" + ancestor + EL_CHECKBOX
  CB_PROMT_REMOTE_USER_CONTROL      = "//span[text()='Prompt remote user to accept or deny control']" + ancestor + EL_CHECKBOX



