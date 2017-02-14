
from _base_page.base_actions import BaseActions


class ClientSettingsPopup(BaseActions):

    BODY = "//span[text()='Client Settings']/ancestor::div[contains(@id,'WRP')]"
    LEFT_MENU = BODY + "/*//div[@class='TreeView-Control']"
    TAB = BODY + "/*//div[@class='TabControl-Control']"

    def check_popup_is_present(self):
        cond = self._is_element_present(ClientSettingsPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ClientSettingsPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Client")
        return True if cond else False

    def click_timers_tab(self):
        self._click_element(TimersTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(TimersTab.LEFT_MENU_LABEL)

    def click_features_label(self):
        self._click_element(FeaturesTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(FeaturesTab.LEFT_MENU_LABEL)

    def click_client_urls_label(self):
        self._click_element(ClientUrlsTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(ClientUrlsTab.LEFT_MENU_LABEL)

    def click_reboot_ui_config_tab(self):
        self._click_element(RebootUIConfigTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(RebootUIConfigTab.LEFT_MENU_LABEL)

    def click_client_proxy_settings_tab(self):
        self._click_element(ClientProxySettingsTab.LEFT_MENU_LABEL)
        self.wait_for_element_selected(ClientProxySettingsTab.LEFT_MENU_LABEL)


class TimersTab(ClientSettingsPopup):

    LEFT_MENU_LABEL = ClientSettingsPopup.LEFT_MENU + "/*//span[text()='Timers']/ancestor::div[contains(@id,'VWGNODE')]"
    CHECKBOX_DISSOLVE = ClientSettingsPopup.TAB \
                        + "/*//span[contains(text(),'Dissolve')]/ancestor::div[contains(@class,'CheckBox')]"

    def check_tab_is_present(self):
        cond = self._is_element_present(self.CHECKBOX_DISSOLVE)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Timers")
        return True if cond else False


class FeaturesTab(ClientSettingsPopup):

    LEFT_MENU_LABEL = ClientSettingsPopup.LEFT_MENU \
                      + "/*//span[text()='Features']/ancestor::div[contains(@id,'VWGNODE')]"
    CHECKBOX_ARCHIVE = ClientSettingsPopup.TAB\
                       + "/*//span[text()='Auto Archive:']/ancestor::div[contains(@class,'CheckBox')]"

    def check_tab_is_present(self):
        cond = self._is_element_present(self.CHECKBOX_ARCHIVE)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Features")
        return True if cond else False


class ClientUrlsTab(ClientSettingsPopup):

    LEFT_MENU_LABEL = ClientSettingsPopup.LEFT_MENU \
                      + "/*//span[text()='Client URLs']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_VREP_INSTALLER = ClientSettingsPopup.TAB + "/*//span[text()='vRep Installer']"
    LABEL_MICRO_RESPONDER_INSTALLER = ClientSettingsPopup.TAB + "/*//span[text()='Micro Responder Installer']"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.LABEL_VREP_INSTALLER)
        cond2 = self._is_element_present(self.LABEL_MICRO_RESPONDER_INSTALLER)
        return True if cond1 and cond2 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Client URLs")
        return True if cond else False


class RebootUIConfigTab(ClientSettingsPopup):

    LEFT_MENU_LABEL = ClientSettingsPopup.LEFT_MENU \
                      + "/*//span[text()='Reboot UI Config']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_REBOOT_MASSAGE = ClientSettingsPopup.TAB + "/*//span[text()='Custom Reboot Message']"
    LABEL_REBOOT_TIMERS = ClientSettingsPopup.TAB + "/*//span[text()='Reboot Timers']"
    LABEL_SNOOZE = ClientSettingsPopup.TAB + "/*//span[text()='Snooze']"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.LABEL_REBOOT_MASSAGE)
        cond2 = self._is_element_present(self.LABEL_REBOOT_TIMERS)
        cond3 = self._is_element_present(self.LABEL_SNOOZE)
        return True if cond1 and cond2 and cond3 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Reboot UI Config")
        return True if cond else False


class ClientProxySettingsTab(ClientSettingsPopup):

    LEFT_MENU_LABEL = ClientSettingsPopup.LEFT_MENU \
                      + "/*//span[text()='Client Proxy Settings']/ancestor::div[contains(@id,'VWGNODE')]"
    LABEL_PROXY_SERVER_URL = ClientSettingsPopup.TAB + "/*//span[text()='Proxy Server URL:']"
    LABEL_PORT_NUMBER = ClientSettingsPopup.TAB + "/*//span[text()='Port Number:']"
    LABEL_LOGIN_CREDENTIALS = ClientSettingsPopup.TAB + "/*//span[text()='Login Credentials']"
    LABEL_PASSWORD = ClientSettingsPopup.TAB + "/*//span[text()='Password']"

    def check_tab_is_present(self):
        cond1 = self._is_element_present(self.LABEL_PROXY_SERVER_URL)
        cond2 = self._is_element_present(self.LABEL_PORT_NUMBER)
        cond3 = self._is_element_present(self.LABEL_LOGIN_CREDENTIALS)
        cond4 = self._is_element_present(self.LABEL_PASSWORD)
        return True if cond1 and cond2 and cond3 and cond4 else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Client Proxy Settings")
        return True if cond else False

