from _base.base_actions import BaseActions
from _base.base_elements import BaseElements
from _feature_objects.feature_popup import AreYouSurePopup, NewFolderPopup, NewGroupPopup, \
    SiteNamePopup
from _feature_objects.feature_ribbon_bar import RibbonBar
from _feature_objects.feature_screen import AuditLogScreen


class BaseLeftMenu(BaseActions):

    #ENUMERATION
    DEVICES                      = "Devices"
    ADMINISTRATION               = "Administration"
    TASKS                        = "Tasks"
    REPORTING                    = "Reporting"
    SOFTWARE_AND_PATCH_MANAGER   = "Software / Patch Manager"
    PASSWORD_RESET               = "Password Reset"
    HOME                         = "Home"

    '''NEW'''

    def _set_left_menu(self, menu_name):
        locator = "//span[text()='" + str(menu_name) + "']/ancestor::div[contains(@style,'translate3d(0px')]"
        return locator

    def _set_left_menu_icon(self, title_name):
        icon = "//div[@title='" + title_name + "']"
        icon_home = "//td[contains(@style,'" + title_name + "')]/ancestor::div[@class='PictureBox-Control']"
        cond = self._is_element_present(icon)
        if cond:
            self._click_element(icon)
            self._wait_for_element_not_present(str(icon) + BaseElements.GREY_COLOR)
        else:
            self._click_element(icon_home)
            self._wait_for_element_not_present(str(icon_home) + BaseElements.GREY_COLOR)

    def _open_left_menu(self, menu_name):
        element = self._set_left_menu(menu_name)
        i = 0
        while i < 2:
            i += 1
            cond = self._is_element_present(element)
            if cond:
                self.logger.debug("Left menu '" + str(menu_name) + "' is opened")
                break
            elif cond is None:
                self.logger.error("Failure. Left menu '" + str(menu_name) + "' is not found")
                break
            elif i == 2:
                self.logger.error("Failure. Left menu '" + str(menu_name) + "' is not opened after " + str(i) + " attempts")
                return False
            else:
                self._set_left_menu_icon(menu_name)
                self._wait_for_element_present(element)

    def menu_home(self):
        locator = "//td[contains(@style,'" + self.HOME + "')]/ancestor::div[@class='PictureBox-Control']"
        return locator

    def menu_devices(self):
        locator = self._set_left_menu(self.DEVICES)
        return locator

    def menu_administration(self):
        locator = self._set_left_menu(self.ADMINISTRATION)
        return locator

    def menu_tasks(self):
        locator = self._set_left_menu(self.TASKS)
        return locator

    def menu_reporting(self):
        locator = self._set_left_menu(self.REPORTING)
        return locator

    def menu_software_and_patch_manager(self):
        locator = self._set_left_menu(self.SOFTWARE_AND_PATCH_MANAGER)
        return locator

    def menu_password_reset(self):
        locator = self._set_left_menu(self.PASSWORD_RESET)
        # print "Menu: ", left_menu
        return locator

    def click_icon_home(self):
        self._set_left_menu_icon(self.HOME)

    def click_icon_devices(self):
        self._set_left_menu_icon(self.DEVICES)

    def click_icon_administration(self):
        self._set_left_menu_icon(self.ADMINISTRATION)

    def click_icon_tasks(self):
        self._set_left_menu_icon(self.TASKS)

    def click_icon_reporting(self):
        self._set_left_menu_icon(self.REPORTING)

    def click_icon_software_and_patch_manager(self):
        self._set_left_menu_icon(self.SOFTWARE_AND_PATCH_MANAGER)

    def click_icon_password_reset(self):
        self._set_left_menu_icon(self.PASSWORD_RESET)

    def open_menu_home(self):
        element = "//span[text()='Home']/ancestor::div[@class='Label-Control']" + BaseElements.WHITE_COLOR
        i = 0
        while i < 2:
            i += 1
            cond = self._is_element_present(element)
            if cond:
                self.logger.debug("Left menu '" + self.HOME + "' is opened")
                break
            elif cond is None:
                self.logger.error("Failure. Left menu '" + self.HOME + "' is not found")
            elif i == 2:
                self.logger.error("Failure. Left menu '" + self.HOME + "' is not opened after " + str(i) + " attempts")
            else:
                self.click_icon_home()
                self._wait_for_element_present(
                    "//span[text()='Home']/ancestor::div[@class='Label-Control']" + BaseElements.WHITE_COLOR)

    def open_menu_devices(self):
        self._open_left_menu(self.DEVICES)

    def open_menu_administration(self):
        self._open_left_menu(self.ADMINISTRATION)

    def open_menu_tasks(self):
        self._open_left_menu(self.TASKS)

    def open_menu_reporting(self):
        self._open_left_menu(self.REPORTING)

    def open_menu_software_and_patch_manager(self):
        self._open_left_menu(self.SOFTWARE_AND_PATCH_MANAGER)

    def open_menu_password_reset(self):
        self._open_left_menu(self.PASSWORD_RESET)

    def check_menu_home_is_opened(self):
        cond = self._is_element_present(
            "//span[text()='Home']/ancestor::div[@class='Label-Control']" + BaseElements.WHITE_COLOR)
        msg_true = "Left menu '" + self.HOME + "' is opened"
        msg_false = "Left menu '" + self.HOME + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_devices_is_opened(self):
        cond = self._is_element_present(self.menu_devices())
        msg_true = "Left menu '" + self.DEVICES + "' is opened"
        msg_false = "Left menu '" + self.DEVICES + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_administration_is_opened(self):
        cond = self._is_element_present(self.menu_administration())
        msg_true = "Left menu '" + self.ADMINISTRATION + "' is opened"
        msg_false = "Left menu '" + self.ADMINISTRATION + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_tasks_is_opened(self):
        cond = self._is_element_present(self.menu_tasks())
        msg_true = "Left menu '" + self.TASKS + "' is opened"
        msg_false = "Left menu '" + self.TASKS + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_reporting_is_opened(self):
        cond = self._is_element_present(self.menu_reporting())
        msg_true = "Left menu '" + self.REPORTING + "' is opened"
        msg_false = "Left menu '" + self.REPORTING + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_software_and_patch_manager_is_opened(self):
        cond = self._is_element_present(self.menu_software_and_patch_manager())
        msg_true = "Left menu '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is opened"
        msg_false = "Left menu '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_password_reset_is_opened(self):
        cond = self._is_element_present(self.menu_password_reset())
        msg_true = "Left menu '" + self.PASSWORD_RESET + "' is opened"
        msg_false = "Left menu '" + self.PASSWORD_RESET + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    '''OLD'''
    # def _check_left_menu_visible(self, locator):
    #     LEFT_MENU = "//span[text()='" + locator + "']/ancestor::div[contains(@style,'transform')]"
    #     cond = self._is_left_menu_visible(LEFT_MENU)
    #     return True if cond else False
    #
    # def _set_left_menu_icon(self, locator):
    #     icon = "//div[@title='" + locator + "']"
    #     self._click_element(icon)
    #     self._wait_for_element_not_present(icon + self.GREY_COLOR)
    #
    # def _open_left_menu(self, locator):
    #     cond = self._check_left_menu_visible(locator)
    #     if cond is not True:
    #         i = 0
    #         while i < 5:
    #             i += 1
    #             cond = self._check_left_menu_visible(locator)
    #             if cond is not True:
    #                 self._set_left_menu_icon(locator)
    #             else:
    #                 break
    #     cond = self._check_left_menu_visible(locator)
    #     return True if cond else False

    # def _set_left_menu_icon(self, locator):
    #     ICON = "//div[@title='" + locator + "']"
    #     self._click_element(ICON)
    #     self._wait_for_element_not_present(ICON + self.GREY_COLOR)
    #
    # def _check_left_menu_visible(self, locator):
    #     LEFT_MENU = "//span[text()='" + locator + "']/ancestor::div[contains(@style,'transform')]"
    #     cond = self._is_left_menu_visible(LEFT_MENU)
    #     return True if cond else False
    #
    # def _open_left_menu(self, locator):
    #     cond = self._check_left_menu_visible(locator)
    #     if cond is not True:
    #         i = 0
    #         while i < 5:
    #             i += 1
    #             cond = self._check_left_menu_visible(locator)
    #             if cond is not True:
    #                 self._set_left_menu_icon(locator)
    #             else:
    #                 break
    #     cond = self._check_left_menu_visible(locator)
    #     return True if cond else False
    #
    # def click_icon_home(self):
    #     self._click_element(self.ICON_HOME)
    #     self._wait_for_element_not_present(self.ICON_HOME + self.GREY_COLOR)
    #
    # def click_icon_devices(self):
    #     self._set_left_menu_icon(self.DEVICES)
    #
    # def click_icon_administration(self):
    #     self._set_left_menu_icon(self.ADMINISTRATION)
    #
    # def click_icon_tasks(self):
    #     self._set_left_menu_icon(self.TASKS)
    #
    # def click_icon_reporting(self):
    #     self._set_left_menu_icon(self.REPORTING)
    #
    # def click_icon_software_and_patch_manager(self):
    #     self._set_left_menu_icon(self.SOFTWARE_AND_PATCH_MANAGER)
    #
    # def click_icon_password_reset(self):
    #     self._set_left_menu_icon(self.PASSWORD_RESET)
    #
    # def open_menu_home(self):
    #     precond = self._is_element_present(self.ICON_HOME + self.GREY_COLOR)
    #     if precond:
    #         self.click_icon_home()
    #     cond = self._is_element_not_present(self.ICON_HOME + self.GREY_COLOR)
    #     return True if cond else False
    #
    # def open_menu_devices(self):
    #     self._open_left_menu("Devices")
    #
    # def open_menu_administration(self):
    #     self._open_left_menu("Administration")
    #
    # def open_menu_tasks(self):
    #     self._open_left_menu("Tasks")
    #
    # def open_menu_reporting(self):
    #     self._open_left_menu("Reporting")
    #
    # def open_menu_software_and_patch_manager(self):
    #     self._open_left_menu("Software / Patch Manager")
    #
    # def open_menu_password_reset(self):
    #     self._open_left_menu("Password Reset")
    #
    # def check_menu_devices_is_opened(self):
    #     cond = self._check_left_menu_visible(self.DEVICES)
    #     return True if cond else False
    #
    # def check_menu_administration_is_opened(self):
    #     cond = self._check_left_menu_visible(self.ADMINISTRATION)
    #     return True if cond else False
    #
    # def check_menu_tasks_is_opened(self):
    #     cond = self._check_left_menu_visible(self.TASKS)
    #     return True if cond else False
    #
    # def check_menu_reporting_is_opened(self):
    #     cond = self._check_left_menu_visible(self.REPORTING)
    #     return True if cond else False
    #
    # def check_menu_software_and_patch_manager_is_visible(self):
    #     cond = self._check_left_menu_visible(self.SOFTWARE_AND_PATCH_MANAGER)
    #     return True if cond else False
    #
    # def check_menu_password_reset_is_visible(self):
    #     cond = self._check_left_menu_visible(self.PASSWORD_RESET)
    #     return True if cond else False


class LeftMenuDevices(BaseLeftMenu):

    BODY = "//span[text()='Devices']/ancestor::div[contains(@style,'transform')]"
    TREE_GLOBAL_SITE_VIEW = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    TREE_ACTIVE_DIRECTORIES = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    TREE_QUERIES = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    TREE_GROUPS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[4]"
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
        self._click_label(self.LABEL_GLOBAL_SITE_VIEW)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_SITE_CONFIG)
        # self._wait_for_elements_present(RibbonBar.BUTTONS_BOX_SITE_CONFIG + "/*//div[contains(@class,'RibbonBarButton-Text')]")

    def click_subsite_in_site_tree(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        element = LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        self._click_element(element)
        self._wait_for_element_selected(element)

    def expand_global_site_view_tree(self):
        arrow = self._is_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)

    def expand_queries_tree(self):
        arrow = self._is_element_present(LeftMenuDevices.LABEL_QUERIES + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(LeftMenuDevices.LABEL_QUERIES)

    def expand_groups_tree(self):
        arrow = self._is_element_present(LeftMenuDevices.LABEL_GROUPS + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(LeftMenuDevices.LABEL_GROUPS)

    def collaps_global_site_view_tree(self):
        # self._wait_for_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        arrow = self._is_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW + BaseElements.ARROW_COLLAPSE)
        if arrow:
            self._collaps_tree(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)

    def click_default_site_in_global_site_view(self):
        self._click_element(LeftMenuDevices.LABEL_DEFAULT_SITE)
        self._wait_for_element_selected(LeftMenuDevices.LABEL_DEFAULT_SITE)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_SITE_CONFIG)

    def click_site_in_global_site_view_tree(self, sitename):
        element = LeftMenuDevices.LIST_GLOBAL_SITE_VIEW \
                  + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self._wait_for_element_selected(element)
        self._wait_for_element_present(RibbonBar.BUTTON_DELETE)
        self._wait_for_element_present(RibbonBar.BUTTON_MOVE)
        self._wait_for_element_present(RibbonBar.BUTTON_CONFIG)
        self._wait_for_element_present(RibbonBar.BUTTON_NEW_SITE)

    def click_active_directories_label(self):
        self._click_element(self.LABEL_ACTIVE_DIRECTORIES)

    def click_queries_label(self):
        self._click_label(LeftMenuDevices.LABEL_QUERIES)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_QUERIES)

    def click_groups_label(self):
        self._click_label(LeftMenuDevices.LABEL_GROUPS)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_GROUPS)

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
        cond = self._is_element_not_present(
            LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
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
        site_name = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
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
            ribbon_bar.click_new_group_menu_item()
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
            ribbon_bar.click_new_folder_menu_item()
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
            ribbon_bar.click_new_folder_menu_item()
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
        self._wait_for_element_selected(element)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_GROUPS)

    def open_global_site_view_tree(self):
        self.click_global_site_view_label()
        self.expand_global_site_view_tree()


class LeftMenuAdministration(BaseLeftMenu):

    BODY = "//span[text()='Administration']/ancestor::div[contains(@style,'transform')]"
    TREE_ENDPOINT_MANAGEMENT = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    TREE_SITE_MANAGEMENT = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    TREE_LOGS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    TREE_COLUMN_SETS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[4]"
    TREE_USER_MANAGEMENT = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[5]"
    TREE_INVENTORY = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[6]"
    TREE_VREPS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[7]"
    TREE_MAINTENANCE_WINDOWS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[8]"
    TREE_NOTIFICATIONS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[9]"
    TREE_AUDIT_LOG = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[10]"
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
    LABEL_AUDIT_LOG = TREE_AUDIT_LOG + "/div[contains(@class,'RowContainer')]"

    def click_endpoint_management_label(self):
        self._click_label(LeftMenuAdministration.LABEL_ENDPOINT_MANAGEMENT)

    def expand_endpoint_management_tree(self):
        arrow = self._is_element_present(self.LABEL_ENDPOINT_MANAGEMENT + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(self.LABEL_ENDPOINT_MANAGEMENT)

    def collaps_endpoint_management_tree(self):
        self._wait_for_element_present(LeftMenuAdministration.LABEL_ENDPOINT_MANAGEMENT)
        arrow = self._is_element_not_present(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT + "/div[2][contains(@style,'display: none')]")
        if arrow:
            self._collaps_tree(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT)

    def click_site_management_label(self):
        self._click_label(LeftMenuAdministration.LABEL_SITE_MANAGEMENT)

    def click_logs_label(self):
        self._click_label(LeftMenuAdministration.LABEL_LOGS)

    def click_column_sets_label(self):
        self._click_label(LeftMenuAdministration.LABEL_COLUMN_SETS)

    def click_user_management_label(self):
        self._click_label(LeftMenuAdministration.LABEL_USER_MANAGEMENT)

    def click_inventory_scan_configuration_label(self):
        self._click_label(LeftMenuAdministration.LABEL_INVENTORY_SCAN)

    def click_vreps_label(self):
        self._click_label(LeftMenuAdministration.LABEL_VREPS)

    def click_maintenance_windows_label(self):
        self._click_label(LeftMenuAdministration.LABEL_MAINTENANCE_WINDOWS)

    def click_notifications_label(self):
        self._click_label(LeftMenuAdministration.LABEL_NOTIFICATIONS)

    def click_audit_log_label(self):
        self._click_label(LeftMenuAdministration.LABEL_AUDIT_LOG)
        audit_log_screen = AuditLogScreen(self.driver)
        self._wait_for_element_present(audit_log_screen.screen_header())

    def click_dynamically_managed_label(self):
        self._click_label(LeftMenuAdministration.LABEL_DYNAMICALLY_MANAGED)

    def click_excluded_devices_label(self):
        self._click_label(LeftMenuAdministration.LABEL_EXCLUDED_DEVICES)

    def click_unmanaged_devices_label(self):
        self._click_label(LeftMenuAdministration.LABEL_UNMANAGED_DEVICES)

    def click_infrastructure_label(self):
        self._click_label(LeftMenuAdministration.LABEL_INFRASTRUCTURE)

    def check_dynamically_managed_label_is_present(self):
        cond = self._is_element_present(LeftMenuAdministration.LABEL_DYNAMICALLY_MANAGED)
        return True if cond else False

    def check_excluded_devices_label_is_present(self):
        cond = self._is_element_present(LeftMenuAdministration.LABEL_EXCLUDED_DEVICES)
        return True if cond else False

    def check_unmanaged_devices_label_is_present(self):
        cond = self._is_element_present(LeftMenuAdministration.LABEL_UNMANAGED_DEVICES)
        return True if cond else False

    def check_infrastructure_label_is_present(self):
        cond = self._is_element_present(LeftMenuAdministration.LABEL_INFRASTRUCTURE)
        return True if cond else False
