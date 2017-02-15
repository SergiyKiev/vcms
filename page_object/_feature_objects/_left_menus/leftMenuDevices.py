from _base_page.base_elements import BaseElements
from _feature_objects._left_menus.leftMenu import LeftMenu
from _feature_objects._popups.popupAreYouSure import AreYouSurePopup
from _feature_objects._popups.popupNewFolder import NewFolderPopup
from _feature_objects._popups.popupNewGroup import NewGroupPopup
from _feature_objects._popups.popupSiteName import SiteNamePopup
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class LeftMenuDevices(LeftMenu):

    TREE_GLOBAL_SITE_VIEW = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    TREE_ACTIVE_DIRECTORIES = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    TREE_QUERIES = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    TREE_GROUPS = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[4]"
    LIST_GLOBAL_SITE_VIEW = TREE_GLOBAL_SITE_VIEW + "/div[contains(@class,'SubNodesContainer')]"
    LIST_ACTIVE_DIRECTORIES = TREE_ACTIVE_DIRECTORIES + "/div[contains(@class,'SubNodesContainer')]"
    LIST_QUERIES = TREE_QUERIES + "/div[contains(@class,'SubNodesContainer')]"
    LIST_GROUPS = TREE_GROUPS + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_GLOBAL_SITE_VIEW = TREE_GLOBAL_SITE_VIEW + "/div[contains(@class,'RowContainer')]"
    LABEL_ACTIVE_DIRECTORIES = TREE_ACTIVE_DIRECTORIES + "/div[contains(@class,'RowContainer')]"
    LABEL_QUERIES = TREE_QUERIES + "/div[contains(@class,'RowContainer')]"
    LABEL_GROUPS = TREE_GROUPS + "/div[contains(@class,'RowContainer')]"
    LABEL_DEFAULT_SITE = LIST_GLOBAL_SITE_VIEW \
                         + "/div/div/*//span[text()='Default Site']/ancestor::div[contains(@class,'RowContainer')]"

    def click_global_site_view_label(self):
        self._click_element(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)

    def click_subsite_in_site_tree(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        element = LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        self._click_element(element)
        self.wait_for_element_selected(element)

    def expand_global_site_view_tree(self):
        self.wait_for_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        arrow = self._is_element_present(LeftMenuDevices.TREE_GLOBAL_SITE_VIEW + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(LeftMenuDevices.TREE_GLOBAL_SITE_VIEW)

    def expand_groups_tree(self):
        self.wait_for_element_present(LeftMenuDevices.LABEL_GROUPS)
        arrow = self._is_element_present(LeftMenuDevices.TREE_GROUPS + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(LeftMenuDevices.TREE_GROUPS)

    def expand_queries_tree(self):
        self.wait_for_element_present(LeftMenuDevices.LABEL_QUERIES)
        arrow = self._is_element_present(LeftMenuDevices.TREE_QUERIES + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(LeftMenuDevices.TREE_QUERIES)
        else:
            pass

    def collaps_global_site_view_tree(self):
        self.wait_for_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        arrow = self._is_element_present(LeftMenuDevices.TREE_GLOBAL_SITE_VIEW + BaseElements.ARROW_COLLAPSE)
        if arrow:
            self._collaps_tree(LeftMenuDevices.TREE_GLOBAL_SITE_VIEW)
        else:
            pass

    def click_default_site_in_global_site_view(self):
        self._click_element(LeftMenuDevices.LABEL_DEFAULT_SITE)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_DEFAULT_SITE)

    def click_site_in_global_site_view_tree(self, sitename):
        element = LeftMenuDevices.LIST_GLOBAL_SITE_VIEW \
                  + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self.wait_for_element_selected(element)

    def click_active_directories_label(self):
        self._click_element(LeftMenuDevices.LABEL_ACTIVE_DIRECTORIES)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_ACTIVE_DIRECTORIES)

    def click_queries_label(self):
        self._click_element(LeftMenuDevices.LABEL_QUERIES)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_QUERIES)

    def click_groups_label(self):
        self._click_element(LeftMenuDevices.LABEL_GROUPS)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_GROUPS)

    def delete_site_if_exists(self, sitename):
        element = LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']"
        cond = self._is_element_present(element)
        if cond:
            left_menu_devices = LeftMenuDevices(self.driver)
            ribbon_bar = RibbonBar(self.driver)
            are_you_sure_popup = AreYouSurePopup(self.driver)
            left_menu_devices.click_site_in_global_site_view_tree(sitename)
            ribbon_bar.click_button_delete()
            are_you_sure_popup.click_button_ok()

    def delete_site_from_global_site_view_tree(self, sitename):
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        self.click_site_in_global_site_view_tree(sitename)
        ribbon_bar.click_button_delete()
        are_you_sure_popup.click_button_ok()

    def create_new_site(self, sitename):
        self.click_global_site_view_label()
        ribbon_bar = RibbonBar(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar.click_button_new_site()
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.check_site_is_in_global_site_view_tree(sitename)

    def create_site_if_not_exists(self, sitename):
        self.scroll_to_element(LeftMenuDevices.LIST_GLOBAL_SITE_VIEW)
        cond = self._is_element_not_present(LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            site_name_popup = SiteNamePopup(self.driver)
            left_menu_devices = LeftMenuDevices(self.driver)
            left_menu_devices.click_global_site_view_label()
            ribbon_bar.click_button_new_site()
            site_name_popup.enter_text_into_name_text_field(sitename)
            site_name_popup.click_button_ok()

    def create_new_subsite(self, sitename, subsitename):
        self.click_site_in_global_site_view_tree(sitename)
        ribbon_bar = RibbonBar(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar.click_button_new_site()
        site_name_popup.enter_text_into_name_text_field(subsitename)
        site_name_popup.click_button_ok()

    def create_subsite_if_not_exists(self, sitename, subsitename):
        site = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]/parent::div"
        element = "//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        self.click_site_in_global_site_view_tree(sitename)
        self._expand_tree(site)
        self.scroll_to_element(site)
        cond = self._is_element_not_present(element)
        if cond:
            self.create_new_subsite(sitename, subsitename)
            print "SUBSITE WAS CREATED"
        else:
            print "NO SUBSITES FOUND"

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::" + LeftMenu.LABEL
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::" + LeftMenu.LABEL
        element = LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        cond = self._is_element_present(element)
        return True if cond else False

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self._is_element_present(LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_default_site_is_in_global_site_view_tree(self):
        cond = self._is_element_present(LeftMenuDevices.LABEL_DEFAULT_SITE)
        return True if cond else False

    def create_group_if_not_exists(self, name):
        self.expand_groups_tree()
        cond = self._is_element_not_present(
            LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']")
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            new_group_popup = NewGroupPopup(self.driver)
            left_menu_devices = LeftMenuDevices(self.driver)
            left_menu_devices.click_groups_label()
            ribbon_bar.click_button_new()
            ribbon_bar.click_new_group_label()
            new_group_popup.enter_text_into_group_name_text_field(name)
            new_group_popup.click_button_ok()

    def create_group_folder_if_not_exists(self, name):
        self.expand_groups_tree()
        self.scroll_to_element(LeftMenuDevices.LIST_GROUPS)
        element = LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']"
        cond = self._is_element_not_present(element)
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            new_folder_popup = NewFolderPopup(self.driver)
            left_menu_devices = LeftMenuDevices(self.driver)
            left_menu_devices.click_groups_label()
            ribbon_bar.click_button_new()
            ribbon_bar.click_new_folder_label()
            new_folder_popup.enter_text_into_new_folder_text_field(name)
            new_folder_popup.click_button_ok()

    def create_queries_folder_if_not_exists(self, name):
        cond = self._is_element_not_present(
            LeftMenuDevices.LIST_QUERIES + "/*//span[text()='" + name + "']")
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            new_folder_popup = NewFolderPopup(self.driver)
            left_menu_devices = LeftMenuDevices(self.driver)
            left_menu_devices.click_queries_label()
            ribbon_bar.click_button_new()
            ribbon_bar.click_new_folder_label()
            new_folder_popup.enter_text_into_new_folder_text_field(name)
            new_folder_popup.click_button_ok()
            self.check_folder_is_in_queries_tree(name)
        else:
            pass

    def check_group_is_in_groups_tree(self, name):
        cond = self._is_element_present(LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']")
        return True if cond else False

    def check_folder_is_in_groups_tree(self, name):
        cond = self._is_element_present(LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']")
        return True if cond else False

    def check_folder_is_in_queries_tree(self, name):
        cond = self._is_element_present(LeftMenuDevices.LIST_QUERIES + "/*//span[text()='" + name + "']")
        return True if cond else False

    def click_group_in_groups_tree(self, name):
        element = LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self.wait_for_element_selected(element)