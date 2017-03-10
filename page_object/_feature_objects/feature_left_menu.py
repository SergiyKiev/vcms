
from _base.base_actions import BaseActions
from _base.base_elements import BaseElements
from _feature_objects.feature_popup import AreYouSurePopup, NewFolderPopup, NewGroupPopup, \
    SiteNamePopup, CreatePatchGroupPopup, CreateNewDashboardPopup
from _feature_objects.feature_ribbon_bar import RibbonBar
from _test_suites._variables.variables import Variables

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
        cond = self._wait_for_element_present(
            "//span[text()='Home']/ancestor::div[@class='Label-Control']" + BaseElements.WHITE_COLOR)
        msg_true = "Left menu '" + self.HOME + "' is opened"
        msg_false = "Left menu '" + self.HOME + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_devices_is_opened(self):
        cond = self._wait_for_element_present(self.menu_devices())
        msg_true = "Left menu '" + self.DEVICES + "' is opened"
        msg_false = "Left menu '" + self.DEVICES + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_administration_is_opened(self):
        cond = self._wait_for_element_present(self.menu_administration())
        msg_true = "Left menu '" + self.ADMINISTRATION + "' is opened"
        msg_false = "Left menu '" + self.ADMINISTRATION + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_tasks_is_opened(self):
        cond = self._wait_for_element_present(self.menu_tasks())
        msg_true = "Left menu '" + self.TASKS + "' is opened"
        msg_false = "Left menu '" + self.TASKS + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_reporting_is_opened(self):
        cond = self._wait_for_element_present(self.menu_reporting())
        msg_true = "Left menu '" + self.REPORTING + "' is opened"
        msg_false = "Left menu '" + self.REPORTING + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_software_and_patch_manager_is_opened(self):
        cond = self._wait_for_element_present(self.menu_software_and_patch_manager())
        msg_true = "Left menu '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is opened"
        msg_false = "Left menu '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_menu_password_reset_is_opened(self):
        cond = self._wait_for_element_present(self.menu_password_reset())
        msg_true = "Left menu '" + self.PASSWORD_RESET + "' is opened"
        msg_false = "Left menu '" + self.PASSWORD_RESET + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
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
    #     precond = self._wait_for_element_present(self.ICON_HOME + self.GREY_COLOR)
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

    GLOBAL_SITE_VIEW = "Global Site View"
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
        self._click_label(self.LABEL_GLOBAL_SITE_VIEW, "Label " + self.GLOBAL_SITE_VIEW)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_SITE_CONFIG)
        # self._wait_for_all_elements_present(RibbonBar.BUTTONS_BOX_SITE_CONFIG + "/*//div[contains(@class,'RibbonBarButton-Text')]")

    def click_subsite_in_site_list(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        element = LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        self._click_element(element)
        self._wait_for_element_selected(element)

    def expand_global_site_view_list(self):
        arrow = self._is_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)

    def expand_queries_list(self):
        arrow = self._is_element_present(LeftMenuDevices.LABEL_QUERIES + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(LeftMenuDevices.LABEL_QUERIES)

    def expand_groups_list(self):
        arrow = self._is_element_present(LeftMenuDevices.LABEL_GROUPS + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(LeftMenuDevices.LABEL_GROUPS)

    def collaps_global_site_view_list(self):
        # self._wait_for_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        arrow = self._is_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW + BaseElements.ARROW_COLLAPSE)
        if arrow:
            self._collaps_list(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)

    def click_default_site_in_global_site_view(self):
        self._click_element(LeftMenuDevices.LABEL_DEFAULT_SITE)
        self._wait_for_element_selected(LeftMenuDevices.LABEL_DEFAULT_SITE)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_SITE_CONFIG)

    def click_site_in_global_site_view_list(self, sitename=Variables.help_test):
        element = self.LIST_GLOBAL_SITE_VIEW + \
                  "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
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
        self.expand_global_site_view_list()
        self.scroll_to_element(self.LIST_GLOBAL_SITE_VIEW)
        element = self.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']"
        cond = self._is_element_present(element)
        if cond:
            left_menu_devices = LeftMenuDevices(self.driver)
            ribbon_bar = RibbonBar(self.driver)
            are_you_sure_popup = AreYouSurePopup(self.driver)
            left_menu_devices.click_site_in_global_site_view_list(sitename)
            ribbon_bar.click_button_delete()
            are_you_sure_popup.click_button_ok()

    def delete_site_from_global_site_view_list(self, sitename):
        ribbon_bar = RibbonBar(self.driver)
        are_you_sure_popup = AreYouSurePopup(self.driver)
        self.click_site_in_global_site_view_list(sitename)
        ribbon_bar.click_button_delete()
        are_you_sure_popup.click_button_ok()

    def create_new_site(self, sitename):
        self.click_global_site_view_label()
        ribbon_bar = RibbonBar(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar.click_button_new_site()
        site_name_popup.enter_text_into_name_text_field(sitename)
        site_name_popup.click_button_ok()
        self.check_site_is_in_global_site_view_list(sitename)

    def create_site_if_not_exists(self, sitename=Variables.help_test):
        self.expand_global_site_view_list()
        self.scroll_to_element(self.LIST_GLOBAL_SITE_VIEW)
        element = self.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']"
        cond = self._is_element_present(element)
        if cond is not True:
            ribbon_bar = RibbonBar(self.driver)
            site_name_popup = SiteNamePopup(self.driver)
            self.click_global_site_view_label()
            ribbon_bar.click_button_new_site()
            site_name_popup.enter_text_into_name_text_field(sitename)
            site_name_popup.click_button_ok()
        site = self.check_site_is_in_global_site_view_list(sitename)
        return True if site else False

    def create_new_subsite(self, sitename, subsitename):
        self.click_site_in_global_site_view_list(sitename)
        ribbon_bar = RibbonBar(self.driver)
        site_name_popup = SiteNamePopup(self.driver)
        ribbon_bar.click_button_new_site()
        site_name_popup.enter_text_into_name_text_field(subsitename)
        site_name_popup.click_button_ok()

    def create_subsite_if_not_exists(self, sitename, subsitename):
        site = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]/parent::div"
        element = "//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        self.expand_global_site_view_list()
        self.scroll_to_element(self.LIST_GLOBAL_SITE_VIEW)
        self.click_global_site_view_label()
        self._expand_list(site)
        self.scroll_to_element(site)
        cond = self._is_element_present(element)
        if cond is not True:
            self.create_new_subsite(sitename, subsitename)
            print "SUBSITE WAS CREATED"
        else:
            print "NO SUBSITES FOUND"

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        element = self.LIST_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        cond = self._wait_for_element_present(element)
        return True if cond else False

    def check_site_is_in_global_site_view_list(self, sitename):
        cond = self._wait_for_element_present(LeftMenuDevices.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_default_site_is_in_global_site_view_list(self):
        cond = self._wait_for_element_present(LeftMenuDevices.LABEL_DEFAULT_SITE)
        return True if cond else False

    def create_group_if_not_exists(self, name):
        self.expand_groups_list()
        cond = self._is_element_not_present(self.LIST_GROUPS + "/*//span[text()='" + name + "']")
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            new_group_popup = NewGroupPopup(self.driver)
            self.click_groups_label()
            ribbon_bar.click_button_new()
            ribbon_bar.click_menu_item_new_group()
            new_group_popup.enter_text_into_group_name_text_field(name)
            new_group_popup.click_button_ok()

    def create_group_folder_if_not_exists(self, name):
        self.expand_groups_list()
        self.scroll_to_element(self.LIST_GROUPS)
        self.click_groups_label()
        element = self.LIST_GROUPS + "/*//span[text()='" + name + "']"
        cond = self._is_element_present(element)
        if cond is not True:
            ribbon_bar = RibbonBar(self.driver)
            new_folder_popup = NewFolderPopup(self.driver)
            self.click_groups_label()
            ribbon_bar.click_button_new()
            ribbon_bar.click_menu_item_new_folder()
            new_folder_popup.enter_text_into_new_folder_text_field(name)
            new_folder_popup.click_button_ok()

    def create_queries_folder_if_not_exists(self, name):
        self.expand_queries_list()
        self.click_queries_label()
        cond = self._is_element_present(self.LIST_QUERIES + "/*//span[text()='" + name + "']")
        if cond is not True:
            ribbon_bar = RibbonBar(self.driver)
            new_folder_popup = NewFolderPopup(self.driver)
            self.click_queries_label()
            ribbon_bar.click_button_new()
            ribbon_bar.click_menu_item_new_folder()
            new_folder_popup.enter_text_into_new_folder_text_field(name)
            new_folder_popup.click_button_ok()
            self.check_folder_is_in_queries_list(name)
        else:
            pass

    def check_group_is_in_groups_list(self, name):
        cond = self._wait_for_element_present(LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']")
        return True if cond else False

    def check_folder_is_in_groups_list(self, name):
        cond = self._wait_for_element_present(LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']")
        return True if cond else False

    def check_folder_is_in_queries_list(self, name):
        cond = self._wait_for_element_present(LeftMenuDevices.LIST_QUERIES + "/*//span[text()='" + name + "']")
        return True if cond else False

    def click_group_in_groups_list(self, name):
        self.expand_groups_list()
        self.scroll_to_element(self.LIST_GLOBAL_SITE_VIEW)
        element = LeftMenuDevices.LIST_GROUPS + "/*//span[text()='" + name + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self._wait_for_element_selected(element)
        self._wait_for_element_present(RibbonBar.BUTTONS_BOX_GROUPS)

    def open_global_site_view_list(self):
        self.click_global_site_view_label()
        self.expand_global_site_view_list()


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

    def expand_endpoint_management_list(self):
        arrow = self._is_element_present(self.LABEL_ENDPOINT_MANAGEMENT + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_ENDPOINT_MANAGEMENT)

    def collaps_endpoint_management_list(self):
        self._wait_for_element_present(LeftMenuAdministration.LABEL_ENDPOINT_MANAGEMENT)
        arrow = self._is_element_not_present(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT +
                                             "/div[2][contains(@style,'display: none')]")
        if arrow:
            self._collaps_list(LeftMenuAdministration.TREE_ENDPOINT_MANAGEMENT)

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

    def click_dynamically_managed_label(self):
        self._click_label(LeftMenuAdministration.LABEL_DYNAMICALLY_MANAGED)

    def click_excluded_devices_label(self):
        self._click_label(LeftMenuAdministration.LABEL_EXCLUDED_DEVICES)

    def click_unmanaged_devices_label(self):
        self._click_label(LeftMenuAdministration.LABEL_UNMANAGED_DEVICES)

    def click_infrastructure_label(self):
        self._click_label(LeftMenuAdministration.LABEL_INFRASTRUCTURE)

    def check_dynamically_managed_label_is_presented(self):
        cond = self._wait_for_element_present(LeftMenuAdministration.LABEL_DYNAMICALLY_MANAGED)
        return True if cond else False

    def check_excluded_devices_label_is_presented(self):
        cond = self._wait_for_element_present(LeftMenuAdministration.LABEL_EXCLUDED_DEVICES)
        return True if cond else False

    def check_unmanaged_devices_label_is_presented(self):
        cond = self._wait_for_element_present(LeftMenuAdministration.LABEL_UNMANAGED_DEVICES)
        return True if cond else False

    def check_infrastructure_label_is_presented(self):
        cond = self._wait_for_element_present(LeftMenuAdministration.LABEL_INFRASTRUCTURE)
        return True if cond else False


class LeftMenuTasks(BaseLeftMenu):

    BODY = "//span[text()='Tasks']/ancestor::div[contains(@style,'transform')]"
    TREE_SCHEDULED_TASKS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    LIST_SCHEDULED_TASKS = TREE_SCHEDULED_TASKS + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_SCHEDULED_TASKS = TREE_SCHEDULED_TASKS + "/div[contains(@class,'RowContainer')]"
    LABEL_DISCOVER = LIST_SCHEDULED_TASKS \
                                + "/div/div/*//span[text()='Discover']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_SOFTWARE_DEPLOYMENT = LIST_SCHEDULED_TASKS \
                                + "/div/div/*//span[text()='Software Deployments']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_PATCH_MANAGER = LIST_SCHEDULED_TASKS \
                                + "/div/div/*//span[text()='Patch Manager']/ancestor::div[contains(@class,'RowContainer')]"

    def click_scheduled_tasks_label(self):
        self._click_label(self.LABEL_SCHEDULED_TASKS)

    def expand_scheduled_tasks_list(self):
        arrow = self._is_element_present(self.LABEL_SCHEDULED_TASKS + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_SCHEDULED_TASKS)

    def collaps_scheduled_tasks_list(self):
        self._wait_for_element_present(self.LABEL_SCHEDULED_TASKS)
        arrow = self._is_element_not_present(self.TREE_SCHEDULED_TASKS + "/div[2][contains(@style,'display: none')]")
        if arrow:
            self._collaps_list(self.TREE_SCHEDULED_TASKS)

    def click_discover_label(self):
        self._click_label(self.LABEL_DISCOVER)

    def click_software_deployment_label(self):
        self._click_label(self.LABEL_SOFTWARE_DEPLOYMENT)

    def click_patch_manager_label(self):
        self._click_label(self.LABEL_PATCH_MANAGER)

    def check_scheduled_tasks_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_SCHEDULED_TASKS)
        return True if cond else False

    def check_discover_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_DISCOVER)
        return True if cond else False

    def check_software_deployment_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_SOFTWARE_DEPLOYMENT)
        return True if cond else False

    def check_patch_manager_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_PATCH_MANAGER)
        return True if cond else False


class LeftMenuReporting(BaseLeftMenu):

    BODY = "//span[text()='Reporting']/ancestor::div[contains(@style,'transform')]"
    TREE_MY_DASHBOARDS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    TREE_SHARED_DASHBOARDS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    TREE_MY_REPORTS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    TREE_SHARED_REPORTS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[4]"
    LABEL_MY_DASHBOARDS = TREE_MY_DASHBOARDS \
                          + "/div/div/*//span[text()='My Dashboards']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_SHARED_DASHBOARDS = TREE_SHARED_DASHBOARDS \
                              + "/div/div/*//span[text()='Shared Dashboards']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_MY_REPORTS = TREE_MY_REPORTS \
                       + "/*//span[text()='My Reports']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_SHARED_REPORTS = TREE_SHARED_REPORTS \
                           + "/*//span[text()='Shared Reports']/ancestor::div[contains(@class,'RowContainer')]"
    LIST_MY_DASHBOARDS = TREE_MY_DASHBOARDS + "/div[contains(@class,'SubNodesContainer')]"
    LIST_SHARED_DASHBOARD = TREE_SHARED_DASHBOARDS + "/div[contains(@class,'SubNodesContainer')]"

    def click_label_my_dashboards(self):
        self._click_label(self.LABEL_MY_DASHBOARDS)

    def expand_list_my_dashboards(self):
        arrow = self._is_element_present(self.LABEL_MY_DASHBOARDS + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_MY_DASHBOARDS)

    def collaps_list_my_dashboards(self):
        self._wait_for_element_present(self.LABEL_MY_DASHBOARDS)
        arrow = self._is_element_not_present(self.TREE_MY_DASHBOARDS + "/div[2][contains(@style,'display: none')]")
        if arrow:
            self._collaps_list(self.TREE_MY_DASHBOARDS)

    def click_label_shared_dashboards(self):
        self._click_label(self.LABEL_SHARED_DASHBOARDS)

    def click_label_my_reports(self):
        self._click_label(self.LABEL_MY_REPORTS)

    def click_label_shared_reports(self):
        self._click_label(self.LABEL_SHARED_REPORTS)

    def click_dashboard_in_my_dashboards_list(self, name=Variables.help_test):
        element = self.LIST_MY_DASHBOARDS \
                  + "/*//span[text()='" + name + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self._wait_for_element_selected(element)

    def check_label_my_dashboard_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_MY_DASHBOARDS)
        return True if cond else False

    def check_label_shared_dashboards_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_SHARED_DASHBOARDS)
        return True if cond else False

    def check_label_my_reports_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_MY_REPORTS)
        return True if cond else False

    def check_label_shared_reports_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_SHARED_REPORTS)
        return True if cond else False

    def expand_my_dashboards_list(self):
        arrow = self._is_element_present(self.LABEL_MY_DASHBOARDS + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_MY_DASHBOARDS)

    def create_dashboard_if_not_exists(self, name=Variables.help_test):
        self.expand_my_dashboards_list()
        self.scroll_to_element(self.LABEL_MY_DASHBOARDS)
        self.click_label_my_dashboards()
        element = self.LIST_MY_DASHBOARDS + "/*//span[text()='" + name + "']"
        cond = self._is_element_present(element)
        if cond is not True:
            ribbon_bar = RibbonBar(self.driver)
            create_new_dashboard_popup = CreateNewDashboardPopup(self.driver)
            ribbon_bar.click_button_new()
            create_new_dashboard_popup.check_popup_is_presented()
            create_new_dashboard_popup.clear_text_name_text_field()
            create_new_dashboard_popup.enter_text_into_name_text_field(name)
            create_new_dashboard_popup.click_button_next()
            create_new_dashboard_popup.click_button_finish()
            self.expand_list_my_dashboards()
        else:
            pass
        site = self.check_dashboard_is_in_my_dashboards_list(name)
        return True if site else False

    def check_dashboard_is_in_my_dashboards_list(self, name=Variables.help_test):
        cond = self._wait_for_element_present(self.LIST_MY_DASHBOARDS + "/*//span[text()='" + name + "']")
        return True if cond else False


class LeftMenuSoftwareAndPatchManager(BaseLeftMenu):

    BODY = "//span[text()='Software / Patch Manager']/ancestor::div[contains(@style,'transform')]"
    TREE_APPLICATIONS = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    TREE_PATCH_MANGER = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    TREE_MEDIA_MANAGEMENT = BODY + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    LABEL_APPLICATIONS = TREE_APPLICATIONS + "/div[contains(@class,'RowContainer')]"
    LIST_PATCH_MANAGER = TREE_PATCH_MANGER + "/div[contains(@class,'SubNodesContainer')]"
    LIST_MEDIA_MANAGEMENT = TREE_PATCH_MANGER + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_PATCH_MANAGER = TREE_PATCH_MANGER + "/div[contains(@class,'RowContainer')]"
    LABEL_MEDIA_MANAGEMENT = TREE_MEDIA_MANAGEMENT + "/div[contains(@class,'RowContainer')]"
    LABEL_BY_VENDOR = LIST_PATCH_MANAGER + \
                          "/div/div/*//span[text()='By Vendor']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_BY_GROUP = LIST_PATCH_MANAGER + \
                          "/div/div/*//span[text()='By Group']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_BY_SYSTEM_RULE = LIST_PATCH_MANAGER + \
                          "/div/div/*//span[text()='By System Rule']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_BY_QUERY_RULE = LIST_PATCH_MANAGER + \
                          "/div/div/*//span[text()='By Query Rule']/ancestor::div[contains(@class,'RowContainer')]"
    LABEL_MY_PATCHES = TREE_MEDIA_MANAGEMENT + \
                          "/*//span[text()='My Patches']/ancestor::div[contains(@class,'RowContainer')]"
    LIST_BY_GROUP = LABEL_BY_GROUP + "/parent::div/div[2]"
    LIST_BY_QUERY_RULE = LABEL_BY_QUERY_RULE + "/parent::div/div[2]"
    LABEL_TO_BE_CHECKED = LIST_PATCH_MANAGER + \
                          "/*//span[text()='To Be Checked']/ancestor::div[contains(@class,'RowContainer')]"

    def click_applications_label(self):
        self._click_label(self.LABEL_APPLICATIONS)

    def click_discover_label(self):
        self._click_label(self.LABEL_PATCH_MANAGER)

    def click_by_vendor_label(self):
        self._click_label(self.LABEL_BY_VENDOR)

    def click_by_group_label(self):
        self._click_label(self.LABEL_BY_GROUP)

    def click_to_be_checked_label(self):
        self._click_label(self.LABEL_TO_BE_CHECKED)

    def click_by_system_rule_label(self):
        self._click_label(self.LABEL_BY_SYSTEM_RULE)

    def click_by_query_rule_label(self):
        self._click_label(self.LABEL_BY_QUERY_RULE)

    def click_my_patches_label(self):
        self._click_label(self.LABEL_MY_PATCHES)

    def click_patch_manager_label(self):
        self._click_label(self.LABEL_PATCH_MANAGER)

    def click_group_in_by_group_list(self, name):
        element = self.LIST_BY_GROUP + "/*//span[text()='" + name + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self._wait_for_element_selected(element)
        # self._wait_for_element_present(RibbonBar.BUTTONS_BOX_PATCH_GROUPS)

    def expand_patch_manager_list(self):
        arrow = self._is_element_present(self.LABEL_PATCH_MANAGER + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_PATCH_MANAGER)

    def collaps_scheduled_tasks_list(self):
        self._wait_for_element_present(self.LABEL_PATCH_MANAGER)
        arrow = self._is_element_not_present(self.TREE_PATCH_MANGER + "/div[2][contains(@style,'display: none')]")
        if arrow:
            self._collaps_list(self.TREE_PATCH_MANGER)

    def expand_by_vendor_list(self):
        arrow = self._is_element_present(self.LABEL_BY_VENDOR + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_BY_VENDOR)

    def expand_by_group_list(self):
        arrow = self._is_element_present(self.LABEL_BY_GROUP + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_BY_GROUP)

    def expand_by_system_rule_list(self):
        arrow = self._is_element_present(self.LABEL_BY_SYSTEM_RULE + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_BY_SYSTEM_RULE)

    def expand_by_query_rule_list(self):
        arrow = self._is_element_present(self.LABEL_BY_QUERY_RULE + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_BY_QUERY_RULE)

    def expand_media_management_list(self):
        arrow = self._is_element_present(self.LABEL_MEDIA_MANAGEMENT + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_list(self.LABEL_MEDIA_MANAGEMENT)

    def check_applications_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_APPLICATIONS)
        return True if cond else False

    def check_by_vendor_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_BY_VENDOR)
        return True if cond else False

    def check_by_group_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_BY_GROUP)
        return True if cond else False

    def check_by_system_rule_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_BY_SYSTEM_RULE)
        return True if cond else False

    def check_by_query_rule_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_BY_QUERY_RULE)
        return True if cond else False

    def check_media_management_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_MEDIA_MANAGEMENT)
        return True if cond else False

    def check_my_patches_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_MY_PATCHES)
        return True if cond else False

    def check_patch_manager_label_is_presented(self):
        cond = self._wait_for_element_present(self.LABEL_PATCH_MANAGER)
        return True if cond else False

    def create_patch_group_if_not_exists(self, name):
        self.expand_patch_manager_list()
        self.expand_by_group_list()
        self.scroll_to_element(self.LABEL_BY_GROUP)
        self.click_by_group_label()
        element = self.LIST_BY_GROUP + "/*//span[text()='" + name + "']"
        cond = self._is_element_present(element)
        if cond is not True:
            ribbon_bar = RibbonBar(self.driver)
            create_patch_group_popup = CreatePatchGroupPopup(self.driver)
            ribbon_bar.click_button_create_group()
            create_patch_group_popup.check_popup_is_presented()
            create_patch_group_popup.enter_text_into_group_name_text_field(name)
            create_patch_group_popup.click_button_ok()
            self.check_patch_group_is_in_by_group_list(name)
        else:
            pass
        site = self.check_patch_group_is_in_by_group_list(name)
        return True if site else False

    def check_patch_group_is_in_by_group_list(self, name):
        cond = self._wait_for_element_present(self.LIST_BY_GROUP + "/*//span[text()='" + name + "']")
        return True if cond else False



