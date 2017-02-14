from _base_page.base_elements import BaseElements
from _feature_objects._left_menus.leftMenu import LeftMenu


class LeftMenuAdministration(LeftMenu):

    TREE_ENDPOINT_MANAGEMENT = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    TREE_SITE_MANAGEMENT = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    TREE_LOGS = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    TREE_COLUMN_SETS = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[4]"
    TREE_USER_MANAGEMENT = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[5]"
    TREE_INVENTORY = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[6]"
    TREE_VREPS = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[7]"
    TREE_MAINTENANCE_WINDOWS = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[8]"
    TREE_NOTIFICATIONS = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[9]"
    TREE_AUDIT_LOGS = LeftMenu.MENU_ADMINISTRATION + "/*//div[contains(@class,'PaddingContainer')]/div[10]"
    LIST_ENDPOINT_MANAGEMENT = TREE_ENDPOINT_MANAGEMENT + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_DYNAMICALLY_MANAGED = LIST_ENDPOINT_MANAGEMENT \
                                + "/div/div/*//span[text()='Dynamically Managed']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_EXCLUDED_DEVICES = LIST_ENDPOINT_MANAGEMENT \
                                + "/div/div/*//span[text()='Excluded Devices']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_UNMANAGED_DEVICES = LIST_ENDPOINT_MANAGEMENT \
                                + "/div/div/*//span[text()='Unmanaged Devices']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_INFRASTRUCTURE = LIST_ENDPOINT_MANAGEMENT \
                                + "/div/div/*//span[text()='Infrastructure']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_ENDPOINT_MANAGEMENT = TREE_ENDPOINT_MANAGEMENT + "/div[contains(@class,'RowContainer')]"
    LABEL_SITE_MANAGEMENT = TREE_SITE_MANAGEMENT + "/div[contains(@class,'RowContainer')]"
    LABEL_LOGS = TREE_LOGS + "/div[contains(@class,'RowContainer')]"
    LABEL_COLUMN_SETS = TREE_COLUMN_SETS + "/div[contains(@class,'RowContainer')]"
    LABEL_USER_MANAGEMENT = TREE_USER_MANAGEMENT + "/div[contains(@class,'RowContainer')]"
    LABEL_INVENTORY_SCAN = TREE_INVENTORY + "/div[contains(@class,'RowContainer')]"
    LABEL_VREPS = TREE_VREPS + "/div[contains(@class,'RowContainer')]"
    LABEL_MAINTENANCE_WINDOWS = TREE_MAINTENANCE_WINDOWS + "/div[contains(@class,'RowContainer')]"
    LABEL_NOTIFICATIONS = TREE_NOTIFICATIONS + "/div[contains(@class,'RowContainer')]"
    LABEL_AUDIT_LOG = TREE_AUDIT_LOGS + "/div[contains(@class,'RowContainer')]"


    def click_endpoint_management_label(self):
        self._click_element(LeftMenuAdministration.LABEL_ENDPOINT_MANAGEMENT)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_ENDPOINT_MANAGEMENT)

    def expand_endpoint_management_tree(self):
        self.wait_for_element_present(LeftMenuAdministration.LABEL_ENDPOINT_MANAGEMENT)
        arrow = self._is_element_present(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT)
        else:
            pass

    def collaps_endpoint_management_tree(self):
        self.wait_for_element_present(LeftMenuAdministration.LABEL_ENDPOINT_MANAGEMENT)
        arrow = self._is_element_present(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT + BaseElements.ARROW_EXPAND)
        if arrow:
            self._collaps_tree(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT)
        else:
            pass

    def click_site_management_label(self):
        self._click_element(LeftMenuAdministration.LABEL_SITE_MANAGEMENT)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_SITE_MANAGEMENT)

    def click_logs_label(self):
        self._click_element(LeftMenuAdministration.LABEL_LOGS)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_LOGS)

    def click_column_sets_label(self):
        self._click_element(LeftMenuAdministration.LABEL_COLUMN_SETS)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_COLUMN_SETS)

    def click_user_management_label(self):
        self._click_element(LeftMenuAdministration.LABEL_USER_MANAGEMENT)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_USER_MANAGEMENT)

    def click_inventory_scan_configuration_label(self):
        self._click_element(LeftMenuAdministration.LABEL_INVENTORY_SCAN)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_INVENTORY_SCAN)

    def click_vreps_label(self):
        self._click_element(LeftMenuAdministration.LABEL_VREPS)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_VREPS)

    def click_maintenance_windows_label(self):
        self._click_element(LeftMenuAdministration.LABEL_MAINTENANCE_WINDOWS)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_MAINTENANCE_WINDOWS)

    def click_notifications_label(self):
        self._click_element(LeftMenuAdministration.LABEL_NOTIFICATIONS)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_NOTIFICATIONS)

    def click_audit_log_label(self):
        self._click_element(LeftMenuAdministration.LABEL_AUDIT_LOG)
        self.wait_for_element_selected(LeftMenuAdministration.LABEL_AUDIT_LOG)