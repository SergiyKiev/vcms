from selenium.webdriver.common.by import By
from variables import Variables


class Locators:

  def __init__(self):
    pass

  '''LOADING ANIMATION'''
  LOADING_SCREEN_INVISIBLE         = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: none']"
  LOADING_SCREEN_VISIBLE           = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block']"
  LOADING_ANIMATION_BOX            = "VWG_LoadingAnimationBox"

  '''STATUS'''
  SELECTED                   = "[contains(@class,'Selected')]"
  DISABLED                   = "[contains(@class,'Disabled')]"
  VISIBLE                    = "[@data-vwgvisible='1']"
  INVISIBLE                  = "[@data-vwgvisible='0']"

  '''ELEMENTS with the attribute data-vwgdocking : T - top, F - front, L - left, B - bottom, R - right'''
  ELEMENT_TOP                = "div[@data-vwgdocking='T']"
  ELEMENT_FRONT              = "div[@data-vwgdocking='F']"
  ELEMENT_LEFT               = "div[@data-vwgdocking='L']"
  ELEMENT_BOTTOM             = "div[@data-vwgdocking='B']"
  ELEMENT_RIGHT              = "div[@data-vwgdocking='R']"
  # DISABLED                   = "[@disabled]"
  TabPage - Control_bj

  '''TEXT'''
  TEXT_GLOBAL_SITE_VIEW           = "//span[text()='Global Site View')]"
  TEXT_ERROR                      = "//span[text()='Error']"
  TEXT_DEFAULT_SITE               = "//span[text()='Default Site']"
  TEXT_CONTAINS_DEFAULT_SITE      = "//span[contains(text(),'Default Site')]"
  TEXT_CONTAINS_GLOBAL_SITE_VIEW  = "//span[contains(text(),'Global Site View')]"
  # TEXT_SITE_NAME                = "//span[text()='" + Variables.siteName + "']"

  '''CONTAINERS'''
  CONTAINER_GLOBAL_SITE_VIEW         = "//span[text()='Global Site View']/" \
                                                "ancestor::div[@class='TreeView-PaddingContainer']/div[1]"
  CONTAINER_HEADER_DEVICES_VIEW      = "//span[text()='Devices']/ancestor::div[contains(@style,'85px')]"
  CONTAINER_DEVICES_VIEW             = "//span[text()='Devices']/ancestor::div[contains(@style,'85px')]/..//div"
  CONTAINER_HEADER_LIST_DEVICES_VIEW = CONTAINER_DEVICES_VIEW + "/ancestor::div[contains(@id,'HEADER')]"
  CONTAINER_BODY_DEVICES_VIEW        = CONTAINER_DEVICES_VIEW + "/ancestor::div[contains(@id,'VWGLVBODY')]"
  CONTAINER_MENU_DEVICES             = "//div[@title='Devices']/ancestor::div[contains(@id,'VWG_')]/*" \
                                                      "//div[contains(@style,'translate3d(0px, 0px, 0px)')]"
  CONTAINER_ACTIVE_DIRECTORIES       = "//span[text()='Active Directories']/" \
                                                      "ancestor::div[@class='TreeView-PaddingContainer']/div[2]"
  CONTAINER_QUERIES                  = "//span[text()='Queries']/ancestor::div[@class='TreeView-PaddingContainer']/div[3]"
  CONTAINER_GROUPS                   = "//span[text()='Groups']/ancestor::div[@class='TreeView-PaddingContainer']/div[4]"
  CONTAINER_PATCHES_LIST_VIEW        = "//div[contains(@id,'VWG')][contains(@class,'ListView')]"

  '''TREES'''
  TREE_GLOBAL_SITE_VIEW           = CONTAINER_GLOBAL_SITE_VIEW + "/div[contains(@id,'VWGSUBS')]"
  TREE_ACTIVE_DERICTORIES         = CONTAINER_ACTIVE_DIRECTORIES + "/div[contains(@id,'VWGSUBS')]"
  TREE_QUERIES                    = CONTAINER_QUERIES + "/div[contains(@id,'VWGSUBS')]"
  TREE_GROUPS                     = CONTAINER_GROUPS + "/div[contains(@id,'VWGSUBS')]"

  '''LABELS'''
  LABEL_GLOBAL_SITE_VIEW          = CONTAINER_GLOBAL_SITE_VIEW + "/div[contains(@id,'VWGNODE')]"
  LABEL_ACTIVE_DIRECTORIES        = CONTAINER_ACTIVE_DIRECTORIES + "/div[contains(@id,'VWGNODE')]"
  LABEL_QUERIES                   = CONTAINER_QUERIES + "/div[contains(@id,'VWGNODE')]"
  LABEL_GROUPS                    = CONTAINER_GROUPS + "/div[contains(@id,'VWGNODE')]"
  LABEL_DEFAULT_SITE              = TREE_GLOBAL_SITE_VIEW + "/div/div[contains(@id,'VWGNODE')]/*" \
                                                          + TEXT_DEFAULT_SITE + "/ancestor::div[contains(@id,'VWGNODE')]"

  '''SITES'''
  SITE_GLOBAL_SITE_VIEW           = "//span[text()='Global Site View']"

  '''FIELDS'''
  FIELD                           = "//input"
  FIELD_USERNAME                  = "//input[@type='text']"
  FIELD_PASSWORD                  = "//input[@type='password']"
  FIELD_IP_ADDRESS_RANGES_TAB     = ""

  '''BUTTONS'''
  BUTTON_SIGN_IN                  = "//span[text()='Sign In']"
  BUTTON_EXIT                     = "//img[@alt='Exit']"
  BUTTON_DEVICES                  = "//div[@title='Devices']"
  BUTTON_NEW_SITE                 = "//img[@alt='New Site']"
  # BUTTON_NEW_SITE_2             = "//span[text()='New Site']"
  BUTTON_DELETE                   = "//img[@alt='Delete']"
  BUTTON_OK_1                     = "//span[text()='OK']"
  BUTTON_OK_2                     = "//span[text()='Ok']"
  BUTTON_CANCEL                   = "//span[text()='Cancel']"
  BUTTON_I_AGREE                  = "//span[text()='I Agree']"
  BUTTON_ICON_ADMIN_USER          = "//td[contains(@style,'icons-gray.111-user')]"
  BUTTON_LOG_OUT                  = "//span[text()='Log Out']"
  BUTTON_SETTINGS_UPPER_CORNER    = "//span[text()='Settings']"
  BUTTON_CONFIG                   = "//img[@alt='Config']"
  # BUTTON_CONFIG_2               = "//span[text()='Config']"
  BUTTON_DELETE_1                 = "//img[@alt='Delete']"
  BUTTON_DELETE_2                 = "//span[text()='Delete']"
  BUTTON_DELETE_GROUP             = "//img[@alt='Delete Group']"
  BUTTON_DELETE_FOLDER            = "//img[@alt='Delete Folder']"
  BUTTON_MOVE_1                   = "//img[@alt='Move']"
  BUTTON_MOVE_2                   = "//span[text()='Move']"
  BUTTON_MOVE_SITE                = "//span[text()='Move Site']"
  BUTTON_SETTINGS                 = "//img[@alt='Settings']"
  BUTTON_CLIENT                   = "//img[@alt='Client']"
  BUTTON_SUBSCRIPTIONS            = "//img[@alt='Subscriptions']"
  BUTTON_ABOUT                    = "//img[@alt='About']"
  BUTTON_NEW                      = "//img[@alt='New']"
  BUTTON_NEW_DROP_DOWN            = BUTTON_NEW + "/following::img[contains(@src,'DropDown')]"
  BUTTON_EDIT_1                   = "//img[@alt='Edit']"
  BUTTON_EDIT_2                   = "//span[text()='Edit']"
  BUTTON_EDIT_GROUP               = "//img[@alt='Edit Group']"
  BUTTON_EDIT_FOLDER              = "//img[@alt='Edit Folder']"
  BUTTON_ADD_MEMBERS              = "//span[text()='Add Members']"
  BUTTON_DELETE_MEMBERS           = "//span[text()='Delete Members']"
  BUTTON_HOME                     = "//img[@alt='Home']"
  BUTTON_HOME_DROP_DOWN           = BUTTON_HOME + "/following::img[contains(@src,'DropDown')]"
  BUTTON_INVENTORY                = "//img[@alt='Inventory']"
  BUTTON_INVENTORY_DROP_DOWN      = BUTTON_INVENTORY + "/following::img[contains(@src,'DropDown')]"
  BUTTON_REFRESH                  = "//span[text()='Refresh']"
  BUTTON_INVENTORY_SCAN           = "//span[text()='Inventory Scan']"
  BUTTON_USER_INTERFACE_OPTIONS   = "//span[text()='User Interface Options']"
  BUTTON_FINISH                   = "//span[text()='FINISH']"
  BUTTON_CLOSE                    = "//span[text()='Close']"
  BUTTON_NO                       = "//span[text()='No']"
  BUTTON_YES                      = "//span[text()='Yes']"
  BUTTON_SELECT_ALL               = "//span[text()='Select All']"
  BUTTON_SELECT_NONE              = "//span[text()='Select None']"
  BUTTON_SCAN_SELECTED            = "//span[text()='Scan Selected']"
  BUTTON_INSTALL_SELECTED         = "//span[text()='Install Selected']"
  BUTTON_ICON_SEARCH              = "//img[contains(@src,'06-magnify.2xw')]"
  BUTTON_ICON_HELP                = "//img[contains(@src,'About')]"
  BUTTON_ICON_EXPORT              = "//img[contains(@src,'212-action2')]"
  BUTTON_ICON_REFRESH             = "//img[contains(@src,'02-redo.2x')]"
  BUTTON_RESET_TO_DEFAULT         = "//span[text()='Reset to default']"
  BUTTON_CONFIRM                  = "//span[text()='Confirm']"
  BUTTON_EDIT                     = "//img[@alt='Edit']"
  BUTTON_TOP                      = "//span[text()='Top']"
  BUTTON_UP                       = "//span[text()='Up']"
  BUTTON_DOWN                     = "//span[text()='Down']"
  BUTTON_BOTTOM                   = "//span[text()='Bottom']"
  BUTTON_GROUP                    = "//span[text()='Group']"
  BUTTON_UNGROUP                  = "//span[text()='Ungroup']"
  BUTTON_SELECT_COLUMNS           = "//span[text()='Select Columns']"
  BUTTON_CREATE_1                 = "//img[@alt='Create']"
  BUTTON_CREATE_2                 = "//span[text()='Create']"
  BUTTON_STOP_1                   = "//img[@alt='Stop']"
  BUTTON_STOP_2                   = "//span[text()='Stop']"
  BUTTON_RESTART_1                = "//img[@alt='Restart']"
  BUTTON_RESTART_2                = "//span[text()='Restart']"
  BUTTON_CMS_UNIVERSITY           = "//img[@alt='CMS University']"
  BUTTON_NEXT                     = "//img[@alt='NEXT']"
  BUTTON_PREVIOUS                 = "//span[text()='PREVIOUS']"
  BUTTON_CREATE_NEW               = "//span[text()='Create New']"
  BUTTON_ADD_SITE                 = "//span[text()='Add Site']"
  BUTTON_IP_RANGE                 = "//span[text()='Add IP Range']"
  BUTTON_ADD                      = "//span[text()='Add']"
  BUTTON_APPLY_CHANGES            = "//span[text()='Apply Changes']"
  BUTTON_SAVE_CURRENT             = "//img[@alt='Save Current Columns']"
  BUTTON_DEFAULT_FOR_SITE         = "//img[@alt='Default For Site']"
  BUTTON_VIEW_LOGS_1              = "//img[@alt='View Logs']"
  BUTTON_VIEW_LOGS_2              = "//span[text()='View Logs']"
  BUTTON_FILE_BROWSER_1           = "//img[@alt='File Browser']"
  BUTTON_FILE_BROWSER_2           = "//span[text()='File Browser']"
  BUTTON_PING_1                   = "//img[@alt='Ping']"
  BUTTON_PING_2                   = "//span[text()='Ping']"
  BUTTON_PROCESS_VIEWER_1         = "//img[@alt='Process Viewer']"
  BUTTON_PROCESS_VIEWER_2         = "//span[text()='Process Viewer']"
  BUTTON_WMI_EXPLORER_1           = "//img[@alt='WMI Explorer']"
  BUTTON_WMI_EXPLORER_2           = "//span[text()='WMI Explorer']"
  BUTTON_REGISTRY_VIEWER_1        = "//img[@alt='Registry Viewer']"
  BUTTON_REGISTRY_VIEWER_2        = "//span[text()='Registry Viewer']"
  BUTTON_EVENT_VEIWER_1           = "//img[@alt='Event Viewer']"
  BUTTON_EVENT_VEIWER_2           = "//span[text()='Event Viewer']"
  BUTTON_REMOTE_CONTROL_1         = "//img[@alt='Remote Control']"
  BUTTON_REMOTE_CONTROL_2         = "//span[text()='Remote Control']"
  BUTTON_PATCH_MANAGER_1          = "//img[@alt='Patch Manager']"
  BUTTON_PATCH_MANAGER_2          = "//span[text()='Patch Manager']"
  BUTTON_MOVE_DEVICE_1            = "//img[@alt='Move Device']"
  BUTTON_MOVE_DEVICE_2            = "//span[text()='Move Device']"
  BUTTON_REPORTS_1                = "//img[@alt='Reports']"
  BUTTON_REPORTS_2                = "//span[text()='Reports']"
  BUTTON_WAKE_UP_1                = "//img[@alt='Wake Up']"
  BUTTON_WAKE_UP_2                = "//span[text()='Wake Up']"
  BUTTON_END_USER_ACCESS_1        = "//img[@alt='End User Access']"
  BUTTON_END_USER_ACCESS_2        = "//span[text()='End User Access']"
  BUTTON_NEW_QUERY                = "//span[text()='New Query']"
  BUTTON_NEW_GROUP                = "//span[text()='New Group']"
  BUTTON_NEW_FOLDER               = "//span[text()='New Folder']"
  BUTTON_RUN_REPORT               = "//span[text()='Run Report']"
  BUTTON_SEARCH                   = "//span[text()='Search']"
  BUTTON_SET_AS_DEFAULT           = "//img[@alt='Set As Default']"
  BUTTON_COPY                     = "//img[@alt='Copy']"
  BUTTON_APPLY                    = "//span[text()='Apply']"
  BUTTON_UPDATE                   = "//span[text()='Update']"
  BUTTON_TEST_SETTINGS            = "//span[text()='Test Settings']"
  BUTTON_RUN_ININTIAL_SETUP       = "//span[text()='Run Initial Setup']"
  BUTTON_PURGE_OLDER_RECORDS      = "//span[text()='Purge Older Records']"
  BUTTON_DELETE_ALL_ARCHIVE_DATA  = "//span[text()='Delete ALL Archive Data']"
  BUTTON_PURGE_OLDER_ENTRIES_NOW  = "//span[text()='Purge older entries now']"
  BUTTON_DELETE_ALL_AUDIT_LOGS    = "//span[text()='Delete all audit logs']"
  BUTTON_REMOVE                   = "//span[text()='Remove']"
  BUTTON_ICON_NEXT                = "//img[contains(@src,'right-double')]"
  BUTTON_ICON_PREVIOUS            = "//img[contains(@src,'left-double')]"

  '''SYSTEM BUTTONS'''
  BUTTON_SYSTEM_CLOSE             = "//div[@title='Close']"
  BUTTON_SYSTEM_JOINT             = "//div[contains(@id,'JOINT')][contains(@style,'LTR')]"
  BUTTON_SYSTEM_COLLAPSE          = "//div[contains(@id,'JOINT')][contains(@style,'LTR0')]"
  BUTTON_SYSTEM_EXPAND            = "//div[contains(@id,'JOINT')][contains(@style,'LTR1')]"
  BUTTON_SYSTEM_NEXT              = "//div[contains(@class,'NextButton')]"
  BUTTON_SYSTEM_LAST              = "//div[contains(@class,'LastButton')]"
  BUTTON_SYSTEM_PREVIOUS          = "//div[contains(@class,'PrevButton')]"
  BUTTON_SYSTEM_FIRST             = "//div[contains(@class,'FirstButton')]"
  BUTTON_SYSTEM_NUMERIC_UP        = "//div[@class=' NumericUpDown-UpCell']"
  BUTTON_SYSTEM_NUMERIC_DOWN      = "//div[@class='NumericUpDown-DownCell']"
  BUTTON_SYSTEM_DROP_DOWN         = "//div[contains(@class,'ButtonContainer')]"

  '''POPUPS'''
  POPUP                           = "//div[contains(@id,'WRP')]"
  POPUP_SITE_NAME                 = "//span[contains(text(),'Site') and contains(text(),'Name')]/" \
                                                      "ancestor::div[contains(@id,'WRP')]"
  POPUP_ARE_YOU_SURE              = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"
  POPUP_SUBSCRIPTION_HAS_EXPIRED  = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"
  POPUP_TERMS_AND_CONDITIONS      = "//span[text()='Terms and Conditions']/ancestor::div[contains(@id,'WRP')]"
  POPUP_ERROR                     = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')]"
  POPUP_DROP_DOWN                 = "//div[@class='Form-PopupWindow']"
  POPUP_CONFIGURATION             = "//span[text()='Configuration']/ancestor::div[contains(@id,'WRP')]"
  POPUP_MOVE_SITE                 = "//span[text()='Move Site']/ancestor::div[contains(@id,'WRP')]"
  POPUP_SETTINGS                  = "//span[text()='Settings']/ancestor::div[contains(@id,'WRP')]"
  POPUP_CLIENT_SETTINGS           = "//span[text()='Client Settings']/ancestor::div[contains(@id,'WRP')]"
  POPUP_SUBSCRIPTIONS             = "//span[text()='Subscriptions']/ancestor::div[contains(@id,'WRP')]"
  POPUP_ABOUT_CMS                 = "//span[text()='About Cloud Management Suite']/ancestor::div[contains(@id,'WRP')]"
  POPUP_RESET_PASSWORD            = "//span[text()='Reset Password']/ancestor::div[contains(@id,'WRP')]"
  POPUP_LICENSES                  = "//span[text()='Licenses'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
  POPUP_CMS                       = "//span[text()='Cloud Management Suite'][contains(@style,'color:White')]/" \
                                                    "ancestor::div[contains(@id,'WRP')]"
  POPUP_SITE_CONFIGURATION        = "//span[text()='Site Configuration']/ancestor::div[contains(@id,'WRP')]"
  POPUP_IP_ADDRESS                = "//span[text()='IP Address']/ancestor::div[contains(@id,'WRP')]"
  POPUP_DISCOVER_DEVICES          = "//span[text()='Discover Devices']/ancestor::div[contains(@id,'WRP')]"
  POPUP_USER_CONFIGURATION        = "//span[text()='User Configuration']/ancestor::div[contains(@id,'WRP')]"
  POPUP_MAINTENANCE_WINDOW        = "//span[text()='Maintenance Window']/ancestor::div[contains(@id,'WRP')]"
  POPUP_REBOOT_UI_OPTIONS         = "//span[text()='Reboot UI Options']/ancestor::div[contains(@id,'WRP')]"
  POPUP_DISCOVERY_DETAILS         = "//span[text()='Discovery Details']/ancestor::div[contains(@id,'WRP')]"
  POPUP_SCANNED_ADDRESSES         = "//span[text()='Scanned Addresses']/ancestor::div[contains(@id,'WRP')]"
  POPUP_DISCOVERED_DEVICES        = "//span[text()='Discovered Devices']/ancestor::div[contains(@id,'WRP')]"
  POPUP_PATCH_MANAGER_SCANNING    = "//span[text()='Patch Manager Scanning']/ancestor::div[contains(@id,'WRP')]"
  POPUP_UNKNOWN_DEVICES           = "//span[text()='Unknown Devices']/ancestor::div[contains(@id,'WRP')]"
  POPUP_REMOVE_DEVICES            = "//span[text()='Remove Devices']/ancestor::div[contains(@id,'WRP')]"
  POPUP_MOVE_DEVICE               = "//span[text()='Move Device']/ancestor::div[contains(@id,'WRP')]"
  POPUP_REPORTS                   = "//span[text()='Reports']/ancestor::div[contains(@id,'WRP')]"
  POPUP_REPORT_SCHEDULER          = "//span[text()='Report Scheduler']/ancestor::div[contains(@id,'WRP')]"
  POPUP_MANAGEMENT_TREE           = "//span[text()='Management Tree']/ancestor::div[contains(@id,'WRP')]"
  POPUP_END_USER_ACCESS           = "//span[text()='End User Access']/ancestor::div[contains(@id,'WRP')]"
  POPUP_DEPLOYMENTS               = "//span[text()='Deployments']/ancestor::div[contains(@id,'WRP')]"
  POPUP_NEW_GROUP                 = "//span[text()='New Group']/ancestor::div[contains(@id,'WRP')]"
  POPUP_EDIT_GROUP                = "//span[text()='Edit Group']/ancestor::div[contains(@id,'WRP')]"
  POPUP_EDIT_FOLDER               = "//span[text()='Edit Folder']/ancestor::div[contains(@id,'WRP')]"
  POPUP_NEW_FOLDER                = "//span[text()='New Folder']/ancestor::div[contains(@id,'WRP')]"
  POPUP_SELECT_TARGETS            = "//span[text()='Select Targets']/ancestor::div[contains(@id,'WRP')]"
  POPUP_UNABLE_TO_REMOVE          = "//span[text()='Unable to remove']/ancestor::div[contains(@id,'WRP')]"

  '''CONTEXT MENU'''
  CONTEXT_MENU                    = "//div[@class='Menu-PopupWindow']"

  '''TABS'''
  TAB                             = "//span[contains(@class='TabControl-PageHeaderText']"
  TAB_PANEL                       = "//div[contains(@id,'VWGTCHD_')]"
  TAB_LABEL                       = "/ancestor::div[contains(@id,'TAB')]"
  TAB_HOME                        = TAB + "[text()='Home']" + TAB_LABEL
  TAB_VIEW                        = TAB + "[text()='View']" + TAB_LABEL
  TAB_DEVICES                     = TAB + "[text()='Devices']" + TAB_LABEL
  TAB_TOOLS                       = TAB + "[text()='Tools']" + TAB_LABEL
  TAB_OPTIONS                     = TAB + "[text()='Options']" + TAB_LABEL
  TAB_LOG                         = TAB + "[text()='Log']" + TAB_LABEL
  TAB_SMTP                        = TAB + "[text()='SMTP']" + TAB_LABEL
  TAB_IMAP                        = TAB + "[text()='IMAP']" + TAB_LABEL
  TAB_SITE                        = TAB + "[text()='Site']" + TAB_LABEL
  TAB_IP_ADDRESS_RANGES           = TAB + "[text()='IP Address Ranges']" + TAB_LABEL
  TAB_VREPS                       = TAB + "[text()='vReps']" + TAB_LABEL
  TAB_PAGE_IP_ADDRESS_RANGES      = TAB_IP_ADDRESS_RANGES + "/following::div[contains(@id,'VWGTCTC')]/div[1]/*//div[1][contains(@id,'VWG')]"


  '''RADIO BUTTONS'''
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

  '''CHECK BOXES'''
  CB_CHECKED                        = "//td[contains(@style,'CheckBox1')]"
  CB_UNCHECKED                      = "//td[contains(@style,'CheckBox0')]"
  CB_MICROSOFT_UPDATE               = "//span[text()='Microsoft Update']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_MICROSOFT_HOTFIX               = "//span[text()='Microsoft Hotfix']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_SERVICE_PACK                   = "//span[text()='Service Pack']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_3RD_PARTY_UPDATE               = "//span[text()='3rd Party Update']/ancestor::tr[contains(@class,'ListBox-Row')]"
  CB_RESCHEDULE_EVERY               = "//span[text()='Re-schedule Every']/ancestor::div[contains(@class,'CheckBox')]"
  CB_MONDAY                         = "//span[text()='Monday']/ancestor::div[contains(@class,'CheckBox')]"
  CB_TUESDAY                        = "//span[text()='Tuesday']/ancestor::div[contains(@class,'CheckBox')]"
  CB_WEDNESDAY                      = "//span[text()='Wednesday']/ancestor::div[contains(@class,'CheckBox')]"
  CB_THURSDAY                       = "//span[text()='Thursday']/ancestor::div[contains(@class,'CheckBox')]"
  CB_FRIDAY                         = "//span[text()='Friday']/ancestor::div[contains(@class,'CheckBox')]"
  CB_SATURDAY                       = "//span[text()='Saturday']/ancestor::div[contains(@class,'CheckBox')]"
  CB_SUNDAY                         = "//span[text()='Sunday']/ancestor::div[contains(@class,'CheckBox')]"
  CB_ENABLE_SNOOZE_REBOOT_DIALOG    = "//span[text()='Enable Snooze Reboot dialog']/" \
                                                      "ancestor::div[contains(@class,'CheckBox')]"
  CB_ALLOW_CANCEL_REBOOT            = "//span[text()='Allow the user to cancel the reboot']/" \
                                                      "ancestor::div[contains(@class,'CheckBox')]"
  CB_ALLOW_DEFER_REBOOT             = "//span[text()='Allow the user to defer (snooze) the reboot']/" \
                                                      "ancestor::div[contains(@class,'CheckBox')]"
  CB_SHOW_DATES                     = "//span[text()='Show Dates']/ancestor::div[contains(@class,'CheckBox')]"
  CB_FILTER_BY_LOCATION             = "//span[text()='Filter By Location']/ancestor::div[contains(@class,'CheckBox')]"
  CB_DO_NOT_DISPLAY_SCANNED_VALUES  = "//span[text()='Do not display scanned values']/" \
                                                      "ancestor::div[contains(@class,'CheckBox')]"
  CB_SYSTEM_NOTIFICATIONS           = "//span[text()='System Notifications']/ancestor::div[contains(@class,'CheckBox')]"
  CB_VERISMIC_COMMUNICATIONS        = "//span[text()='Verismic Communications']/ancestor::div[contains(@class,'CheckBox')]"
  CB_MONITORING_ALERTS              = "//span[text()='Monitoring Alerts']/ancestor::div[contains(@class,'CheckBox')]"
  CB_AUTOMATICALLY_CHECK_FOR_NEW_DATA = "//span[text()='Automatically check for new data every day']/" \
                                                        "ancestor::div[contains(@class,'CheckBox')]"
  CB_SSL                            = "//span[text()='SSL']/ancestor::div[contains(@class,'CheckBox')]"
  CB_SHOW_TERMS_AND_CONDITIONS      = "//span[text()='Show Terms and Conditions at next login']/" \
                                                      "ancestor::div[contains(@class,'CheckBox')]"
  CB_ENFORCE_TWO_FACTOR_FOR_ALL_USERS = "//span[text()='Enforce two factor authentication for ALL users']/" \
                                                        "ancestor::div[contains(@class,'CheckBox')]"
  CB_ALLOW_STORE_TWO_FACTOR_IN_COOKIE = "//span[text()='Allow users to store their two-factor login in a cookie']/" \
                                                        "ancestor::div[contains(@class,'CheckBox')]"
  CB_PROMT_REMOTE_USER_CONTROL      = "//span[text()='Prompt remote user to accept or deny control']/" \
                                                    "ancestor::div[contains(@class,'CheckBox')]"

