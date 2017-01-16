from base import Base
from leftSideMenu import LeftSideMenu
from ribbonBar import RibbonBar
from popups import *
from locators import Locators
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from variables import Variables
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage(TermsAndConditionsPopup, SubscriptionHasExpitredPopup):

    def check_login_page_loaded(self):
        cond1 = self.is_element_present(Locators.BTN_SIGN_IN)
        cond2 = self.is_element_present(Locators.FIELD_USERNAME)
        cond3 = self.is_element_present(Locators.FIELD_PASSWORD)
        return True if (cond1 and cond2 and cond3) else False

    def login(self):
        self.check_login_page_loaded()
        TermsAndConditionsPopup.close_popup(self)
        self.enter_username()
        self.enter_password()
        self.do_login()

    def enter_username(self, username = Settings.username):
        self.find_element_self(Locators.FIELD_USERNAME).send_keys(username)

    def enter_password(self, password = Settings.password):
        self.find_element_self(Locators.FIELD_PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        self.click_element(Locators.BTN_SIGN_IN)

    def do_login(self):
        self.click_sign_in_button()
        cond1 = self.is_element_present(Locators.POPUP_ERROR)
        cond2 = self.is_element_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        if cond1:
            print Settings.username + " or " +  Settings.password + " are incorrect"
        elif cond2:
            SubscriptionHasExpitredPopup.close_popup(self)
            self.wait_for_element_present(Locators.BTN_EXIT)
        else:
            self.wait_for_element_present(Locators.BTN_EXIT)


class HomePage(LeftSideMenu, RibbonBar):

    def check_home_page_loaded(self):
        cond = self.wait_for_elements_present(self.TITLE_WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
        return True if cond else False

    # def click_devices_menu_button(self):
    #     self.click_element(Locators.BTN_ICON_DEVICES)
    #     self.wait_for_element_present(Locators.LEFT_SIDE_MENU_DEVICES)


class DevicesPage(LeftSideMenu, RibbonBar, ConfigurationPopup, ColumnSetsPopup, ColumnSetDesignerPopup, AreYouSurePopup,
                  NewSitePopup, ErrorPopup):

    def check_devices_page_loaded(self):
        cond = self.is_element_present(self.TITLE_DEVICES)
        return True if cond else False

    def click_global_site_view_label(self):
        self.click_element(Locators.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_present(Locators.BTN_NEW_SITE)
        self.wait_for_element_selected(Locators.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_CONTAINS_GLOBAL_SITE_VIEW)
        self.wait_for_element_not_present(Locators.BTN_DELETE)

    def click_site_in_global_site_view_tree(self, sitename):
        elem1 = "//span[text()='" + sitename + "']"
        elem2 = "//span[contains(text(),'" + sitename + "')]"
        self.click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + elem1)
        self.wait_for_element_selected(elem1 + Locators.anc + Locators.EL_NODE_CONTAINER)
        self.wait_for_element_present(Locators.BTN_CONFIG)
        self.wait_for_element_present(Locators.BTN_NEW_SITE)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + elem2)

    def click_default_site_in_global_site_view_tree(self):
        self.click_element(Locators.LABEL_DEFAULT_SITE)
        self.wait_for_element_selected(Locators.LABEL_DEFAULT_SITE)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_CONTAINS_DEFAULT_SITE)

    # def click_ok(self):
    #     self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_OK)
    #     self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)

    def click_unable_to_remove_popup_ok_button(self):
        self.click_element(Locators.POPUP_UNABLE_TO_REMOVE + "/*" + Locators.BTN_Ok)
        self.wait_for_element_not_present(Locators.POPUP_UNABLE_TO_REMOVE)

    def delete_site_if_exists(self, sitename):
        elem = Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']"
        cond = self.is_element_present(elem)
        if cond:
            self.click_site_in_global_site_view_tree(sitename)
            self.click_delete_button()
            AreYouSurePopup.click_button_ok(self)
            self.wait_for_element_not_present(elem)
        else:
            pass

    def delete_site_from_global_site_view_tree(self, sitename):
        self.click_site_in_global_site_view_tree(sitename)
        self.click_delete_button()
        AreYouSurePopup.click_button_ok(self)
        self.wait_for_element_not_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        # return True if cond else False

    # def click_site_expand_button(self, sitename):
    #     expand = "//span[text()='" + sitename + "']/ancestor::" + Locators.EL_EXPAND_ARROW
    #     self.click_element(expand)
    #     self.wait_for_element_not_present(expand)
    #
    # def expand_site_tree(self, sitename):
    #     elem = "//span[text()='" + sitename + "']/ancestor::"
    #     self.expand_tree(elem)
    #
    # def expand_default_site_tree(self):
    #     self.expand_tree(Locators.LABEL_DEFAULT_SITE + "/")
    #
    # def expand_global_site_view_tree(self):
    #     self.expand_tree(Locators.LABEL_GLOBAL_SITE_VIEW + "/")

    def create_new_site(self, sitename):
        self.click_global_site_view_label()
        RibbonBar.click_button_new_site(self)
        NewSitePopup.enter_text_into_name_text_field(self, sitename)
        NewSitePopup.click_button_ok(self)
        self.check_site_is_in_global_site_view_tree(sitename)

    def create_site_if_not_exists(self, sitename):
        cond = self.is_element_not_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        if cond:
            self.click_global_site_view_label()
            RibbonBar.click_button_new_site(self)
            NewSitePopup.enter_text_into_name_text_field(self, sitename)
            NewSitePopup.click_button_ok(self)
            self.check_site_is_in_global_site_view_tree(sitename)
        else:
            pass

    def create_new_subsite(self, sitename, subsitename):
        self.click_site_in_global_site_view_tree(sitename)
        RibbonBar.click_button_new_site(self)
        NewSitePopup.enter_text_into_name_text_field(self, subsitename)
        NewSitePopup.click_button_ok(self)
        # self.expand_site_tree(sitename)
        self.check_subsite_is_in_parent_site(sitename, subsitename)

    def create_subsite_if_not_exists(self, sitename, subsitename):
        elem = "//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']"
        self.click_site_in_global_site_view_tree(sitename)
        # self.expand_site_tree(sitename)
        cond = self.is_element_not_present(elem)
        if cond:
            self.create_new_subsite(sitename, subsitename)
            self.check_subsite_is_in_parent_site(sitename, subsitename)
        else:
            pass

    def click_subsite_in_site_tree(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']"
        subsite_name = "//span[text()='" + subsitename + "']"
        contains_subsite_name = "//span[contains(text(),'" + subsitename + "')]"
        elem = site_name + Locators.fol + Locators.EL_CHILD_SITE + "/*" + subsite_name
        self.click_element(elem)
        self.wait_for_element_selected(elem + Locators.anc + Locators.EL_NODE_CONTAINER)
        RibbonBar.wait_for_element_present(self, Locators.BTN_CONFIG)
        RibbonBar.wait_for_element_present(self, Locators.BTN_NEW_SITE)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + contains_subsite_name)

    def click_configuration_popup_system_button_close(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_CONFIGURATION)

    def click_configuration_popup_site_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)

    def click_configuration_popup_ip_address_ranges_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)

    def click_configuration_popup_vreps_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)

    def click_column_set_popup_system_button_close(self):
        self.click_element(Locators.POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        cond = self.is_element_present("//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']")
        return True if cond else False

    def open_column_sets_popup_from_ribbon_bar(self, *columnsetname):
        self.click_global_site_view_label()
        self.click_ribbon_bar_tab_view()
        self.click_button_edit_or_create()

    def create_columnset_in_column_sets_popup(self, columnsetname, columns_list):
        self.click_column_sets_popup_button_new()
        self.enter_text_into_column_set_designer_popup_text_field_name(columnsetname)
        self.add_columns_to_column_set_designer_list_view(columns_list)
        self.click_column_set_designer_popup_button_add(columns_list)

    def select_columnset_from_configuration_popup_column_set_dropdown_list(self, columnsetname):
        self.click_columnset_in_configuration_popup_drop_down_list(columnsetname)

    def check_columns_are_presented_in_devices_list_header(self, columns_list):
        names = []
        for columnname in list(columns_list):
            elem = Locators.DEVICES_LIST_HEADER + "/*//span[text()='" + columnname + "']"
            cond = self.is_element_present(elem)
            if cond:
                names.append(columnname)
                print names
            else:
                pass
        return True if names == columns_list else False

class AdministrationPage(Base):
    pass


class TasksPage(Base):
    pass


class ReportingPage(Base):
    pass


class SoftwarePatchManagerPage(Base):
    pass


class PasswordResetPage(Base):
    pass
