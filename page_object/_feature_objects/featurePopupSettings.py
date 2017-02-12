
from _base_page.base_actions import BaseActions
from _feature_objects.featurePopupInitialSetup import InitialSetupPopup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SettingsPopup(BaseActions):

    BODY = "//span[text()='Settings']/ancestor::div[contains(@id,'WRP')]"
    _LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    _TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(SettingsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SettingsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Client")
        return True if cond else False

    def click_content_services_label(self):
        self._click_element(ContentServicesTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(ContentServicesTab.LEFT_MENU_LABEL)

    def click_email_settings_label(self):
        self._click_element(EmailSettingsTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(EmailSettingsTab.LEFT_MENU_LABEL)

    def click_initial_setup_label(self):
        self._click_element(InitialSetupTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(InitialSetupTab.LEFT_MENU_LABEL)

    def click_locale_options_label(self):
        self._click_element(LocaleOptionsTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(LocaleOptionsTab.LEFT_MENU_LABEL)

    def click_inventory_label(self):
        self._click_element(InventoryTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(InventoryTab.LEFT_MENU_LABEL)

    def click_user_options_label(self):
        self._click_element(UserOptionsTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(UserOptionsTab.LEFT_MENU_LABEL)

    def click_audit_log_settings_label(self):
        self._click_element(AuditLogSettingsTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(AuditLogSettingsTab.LEFT_MENU_LABEL)


class ContentServicesTab(SettingsPopup):

    LEFT_MENU_LABEL = SettingsPopup._LEFT_MENU + "/*//span[text()='Content Services']/ancestor::div[contains(@id,'VWGNODE')]"
    TAB_OPTIONS = SettingsPopup._TAB + "/*//span[text()='Options']/ancestor::div[contains(@id,'TAB')]"
    TAB_LOG = SettingsPopup._TAB + "/*//span[text()='Log']/ancestor::div[contains(@id,'TAB')]"
    CHECKBOX_CHECK_NEW_DATA = SettingsPopup._TAB \
                              + "/*//span[contains(text(),'check for new data')]/ancestor::div[contains(@class,'CheckBox')]"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.TAB_OPTIONS)
        cond2 = self._is_element_present(self.TAB_LOG)
        return True if cond1 and cond2 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Content Services")
        return True if cond else False


class EmailSettingsTab(SettingsPopup):

    LEFT_MENU_LABEL = SettingsPopup._LEFT_MENU \
                      + "/*//span[text()='Email Settings']/ancestor::div[contains(@id,'VWGNODE')]"
    TAB_SMTP = SettingsPopup._TAB + "/*//span[text()='SMTP']/ancestor::div[contains(@id,'TAB')]"
    TAB_IMAP = SettingsPopup._TAB + "/*//span[text()='IMAP']/ancestor::div[contains(@id,'TAB')]"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.TAB_SMTP)
        cond2 = self._is_element_present(self.TAB_IMAP)
        return True if cond1 and cond2 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Email Settings")
        return True if cond else False


class InitialSetupTab(SettingsPopup):

    LEFT_MENU_LABEL = SettingsPopup._LEFT_MENU \
                      + "/*//span[text()='Initial Setup']/ancestor::div[contains(@id,'VWGNODE')]"
    BUTTON_RUN_INITIAL_SETUP = SettingsPopup._TAB \
                               + "/*//span[text()='Run Initial Setup']/ancestor::div[contains(@class,'Button')]"
    CHECKBOX_TERMS_AND_CONDITIONS = SettingsPopup._TAB \
                              + "/*//span[contains(text(),'Show Terms')]/ancestor::div[contains(@class,'CheckBox')]"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.BUTTON_RUN_INITIAL_SETUP)
        cond2 = self._is_element_present(self.CHECKBOX_TERMS_AND_CONDITIONS)
        return True if cond1 and cond2 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Initial Setup")
        return True if cond else False

    def click_button_run_initial_setup(self):
        self._click_element(InitialSetupTab.BUTTON_RUN_INITIAL_SETUP)
        self.wait_for_element_present(InitialSetupPopup.BODY)


class LocaleOptionsTab(SettingsPopup):

    LEFT_MENU_LABEL = SettingsPopup._LEFT_MENU + \
                      "/*//span[text()='Locale Options']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_DATE_AND_TIME_SETTINGS = SettingsPopup._TAB + "/*//span[text()='Date And Time Settings']"
    LABEL_DATE_FORMAT = SettingsPopup._TAB + "/*//span[text()='Date Format']"
    LABEL_TIME_ZONE = SettingsPopup._TAB + "/*//span[text()='Time Zone']"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.LABEL_DATE_AND_TIME_SETTINGS)
        cond2 = self._is_element_present(self.LABEL_DATE_FORMAT)
        cond3 = self._is_element_present(self.LABEL_TIME_ZONE)
        return True if cond1 and cond2 and cond3 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Locale Options")
        return True if cond else False


class InventoryTab(SettingsPopup):

    LEFT_MENU_LABEL = SettingsPopup._LEFT_MENU + \
                      "/*//span[text()='Inventory']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_INVENTORY_ARCHIVE_SETTINGS = SettingsPopup._TAB + "/*//span[text()='Inventory Archive Settings']"
    LABEL_DATE_FORMAT = SettingsPopup._TAB + "/*//span[text()='Date Format']"
    BUTTON_PURGE_RECORDS = SettingsPopup._TAB \
                           + "/*//span[text()='Purge Older Records']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE_DATA = SettingsPopup._TAB \
                           + "/*//span[text()='Delete ALL Archive Data']/ancestor::div[contains(@class,'Button')]"

    def check_tab_is_present(self):
        WebDriverWait(self.driver, 600).\
            until(EC.presence_of_element_located((By.XPATH, self.LABEL_INVENTORY_ARCHIVE_SETTINGS)))
        cond1 = self._is_element_present(self.LABEL_INVENTORY_ARCHIVE_SETTINGS)
        cond2 = self._is_element_present(self.LABEL_DATE_FORMAT)
        cond3 = self._is_element_present(self.BUTTON_PURGE_RECORDS)
        cond4 = self._is_element_present(self.BUTTON_DELETE_DATA)
        return True if cond1 and cond2 and cond3 and cond4 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Inventory")
        return True if cond else False


class UserOptionsTab(SettingsPopup):

    LEFT_MENU_LABEL = SettingsPopup._LEFT_MENU + \
                      "/*//span[text()='User Options']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_USER_AUTHENTICATION = SettingsPopup._TAB + "/*//span[text()='User Authentication']"

    def check_tab_is_present(self):
        cond = self._is_element_present(self.LABEL_USER_AUTHENTICATION)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("User Options")
        return True if cond else False


class AuditLogSettingsTab(SettingsPopup):

    LEFT_MENU_LABEL = SettingsPopup._LEFT_MENU + \
                      "/*//span[text()='Audit Log Settings']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_AUDIT_LOG_SETTINGS = SettingsPopup._TAB + "/*//span[text()='Audit Log Settings']"
    LABEL_AUDIT_EMAIL_SETTINGS = SettingsPopup._TAB + "/*//span[text()='Audit Email Settings']"
    BUTTON_PURGE_ENTRIES = SettingsPopup._TAB \
                           + "/*//span[text()='Purge older entries now']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE_LOGS = SettingsPopup._TAB \
                           + "/*//span[text()='Delete all audit logs']/ancestor::div[contains(@class,'Button')]"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.LABEL_AUDIT_LOG_SETTINGS)
        cond2 = self._is_element_present(self.LABEL_AUDIT_EMAIL_SETTINGS)
        cond3 = self._is_element_present(self.BUTTON_PURGE_ENTRIES)
        cond4 = self._is_element_present(self.BUTTON_DELETE_LOGS)
        return True if cond1 and cond2 and cond3 and cond4 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Audit Log Settings")
        return True if cond else False
