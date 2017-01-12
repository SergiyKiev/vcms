from base import Base
from leftMenu import LeftSideMenu
from ribbonBar import RibbonBar
from popups import *
from locators import Locators
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from variables import Variables
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage(Base):

    def check_login_page_loaded(self):
        cond1 = self.is_element_present(Locators.BTN_SIGN_IN)
        cond2 = self.is_element_present(Locators.FIELD_USERNAME)
        cond3 = self.is_element_present(Locators.FIELD_PASSWORD)
        return True if (cond1 and cond2 and cond3) else False

    def login(self):
        self.check_login_page_loaded()
        self.close_terms_and_conditions_popup()
        self.enter_username()
        self.enter_password()
        self.do_login()

    def click_terms_and_conditions_popup_i_agree_button(self):
        self.click_element(Locators.POPUP_TERMS_AND_CONDITIONS + "/*" + Locators.BTN_I_AGREE)
        self.wait_for_element_not_present(Locators.POPUP_TERMS_AND_CONDITIONS)

    def close_terms_and_conditions_popup(self):
        cond = self.is_element_present(Locators.POPUP_TERMS_AND_CONDITIONS)
        if cond:
            self.click_terms_and_conditions_popup_i_agree_button()
            return True
        else:
            pass

    def click_subscription_has_expired_popup_system_button_close(self):
        self.click_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)

    def close_subscription_has_expired_popup(self):
        cond = self.is_element_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        if cond:
            self.click_subscription_has_expired_popup_system_button_close()
        else:
            pass

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
            return False
        elif cond2:
            self.close_subscription_has_expired_popup()
            self.wait_for_element_present(Locators.BTN_EXIT)
            return True
        else:
            self.wait_for_element_present(Locators.BTN_EXIT)
            return True

    def close_error_popup(self):
        self.click_element(Locators.POPUP_ERROR + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_ERROR)


class HomePage(LeftSideMenu, RibbonBar):

    def check_home_page_loaded(self):
        cond = self.wait_for_elements_present(Locators.BTN_ICON_DEVICES)
        return True if cond else False

    def click_devices_menu_button(self):
        self.click_element(Locators.BTN_ICON_DEVICES)
        self.wait_for_element_present(Locators.MENU_DEVICES)

class DevicesPage(LeftSideMenu, ColumnSetsPopup, RibbonBar):

    def check_devices_page_loaded(self):
        cond = self.wait_for_element_present(Locators.MENU_DEVICES)
        return True if cond else False

    def click_global_site_view_label(self):
        self.click_element(Locators.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_present(Locators.BTN_NEW_SITE)
        self.wait_for_element_selected(Locators.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_CONTAINS_GLOBAL_SITE_VIEW)
        self.wait_for_element_not_present(Locators.BTN_DELETE)

    def click_new_site_button(self):
        self.click_element(Locators.BTN_NEW_SITE)
        self.wait_for_element_present(Locators.POPUP_SITE_NAME)

    def enter_text_into_site_name_text_field(self, sitename = Variables.site_name):
        self.find_element_self(Locators.POPUP_SITE_NAME + "/*" + Locators.FIELD_).send_keys(sitename)

    def click_site_name_popup_ok_button(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BTN_OK)
        self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)

    def click_site_name_popup_system_button_close(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)

    def click_site_in_global_site_view_tree(self, sitename = Variables.site_name):
        site_name = "//span[text()='" + sitename + "']"
        contains_site_name = "//span[contains(text(),'" + sitename + "')]"
        self.click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + site_name)
        self.wait_for_element_selected(site_name + Locators.anc + Locators.EL_TREE_NODE)
        self.wait_for_element_present(Locators.BTN_CONFIG)
        self.wait_for_element_present(Locators.BTN_NEW_SITE)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + contains_site_name)

    def click_default_site_in_global_site_view_tree(self):
        self.click_element(Locators.LABEL_DEFAULT_SITE)
        cond1 = self.wait_for_element_selected(Locators.LABEL_DEFAULT_SITE)
        cond2 = self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_CONTAINS_DEFAULT_SITE)
        return True if (cond1 and cond2) else False

    def click_ribbon_bar_delete_button(self):
        self.click_element(Locators.BTN_DELETE)
        cond = self.wait_for_element_present(Locators.POPUP)
        cond1 = self.is_element_present(Locators.POPUP_ARE_YOU_SURE)
        cond2 = self.is_element_present(Locators.POPUP_UNABLE_TO_REMOVE)
        return True if cond and (cond1 or cond2) else False

    def click_are_you_sure_popup_ok_button(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BTN_OK)
        cond = self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_are_you_sure_popup_system_button_close(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.SYS_BTN_CLOSE)
        cond = self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_unable_to_remove_popup_ok_button(self):
        self.click_element(Locators.POPUP_UNABLE_TO_REMOVE + "/*" + Locators.BTN_Ok)
        cond = self.wait_for_element_not_present(Locators.POPUP_UNABLE_TO_REMOVE)
        return True if cond else False

    def delete_site_if_exists(self, sitename):
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        if cond:
            self.click_site_in_global_site_view_tree(sitename)
            self.click_ribbon_bar_delete_button()
            self.click_are_you_sure_popup_ok_button()
            self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)
            return True
        else:
            pass

    def delete_site_from_global_site_view_tree(self, sitename):
        self.click_site_in_global_site_view_tree(sitename)
        self.click_ribbon_bar_delete_button()
        self.click_are_you_sure_popup_ok_button()
        cond = self.wait_for_element_not_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def click_site_name_popup_cancel_button(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BTN_CANCEL)
        cond = self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def click_error_popup_ok_button(self):
        self.click_element(Locators.POPUP_ERROR + "/*" + Locators.BTN_Ok)
        cond = self.wait_for_element_not_present(Locators.POPUP_ERROR)
        return True if cond else False

    def click_site_expand_button(self, sitename):
        # expand = "//span[text()='" + sitename + "']/ancestor::div[contains(@id,'VWGNODE')]/" + Locators.SYS_TREE_ARROW_EXPAND
        site_name = "//span[text()='" + sitename + "']"
        expand = site_name + Locators.fol + "div" + Locators.EXPAND
        self.click_element(expand)
        self.wait_for_element_not_present(EC.presence_of_element_located((By.XPATH, expand)))

    def expand_site_tree(self, sitename):
        site_name = "//span[text()='" + sitename + "']"
        expand = site_name + Locators.fol + "div" + Locators.EXPAND
        cond = self.is_element_present(expand)
        if cond:
            self.click_site_expand_button(expand)
        else:
            pass

    def expand_default_site_tree(self):
        expand = Locators.LABEL_DEFAULT_SITE + Locators.SYS_TREE_ARROW_EXPAND
        cond = self.is_element_present(expand)
        if cond:
            self.click_site_expand_button(expand)
        else:
            pass

    def expand_global_site_view_tree(self):
        expand = Locators.LABEL_GLOBAL_SITE_VIEW + Locators.SYS_TREE_ARROW_EXPAND
        cond = self.is_element_present(expand)
        if cond:
            self.click_site_expand_button(expand)
        else:
            pass


    def create_new_site(self, sitename):
        self.click_global_site_view_label()
        self.click_new_site_button()
        self.enter_text_into_site_name_text_field(sitename)
        self.click_site_name_popup_ok_button()
        self.check_site_is_in_global_site_view_tree(sitename)

    def create_site_if_not_exists(self, sitename):
        site_name = "//span[text()='" + sitename + "']"
        cond = self.is_element_not_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + site_name)
        if cond:
            self.click_global_site_view_label()
            self.click_new_site_button()
            self.enter_text_into_site_name_text_field(sitename)
            self.click_site_name_popup_ok_button()
            cond1 = self.check_site_is_in_global_site_view_tree(sitename)
            return True if cond1 else False
        else:
            pass
        # try:
        #     cond=self.is_element_not_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        #     if cond:
        #         self.click_global_site_view_label()
        #         self.click_new_site_button()
        #         self.enter_text_into_site_name_text_field(sitename)
        #         self.click_site_name_popup_ok_button()
        #         cond1 = self.check_site_is_in_global_site_view_tree(sitename)
        #         return True if cond1 else False
        #     else:
        #         pass
        # except NoSuchElementException:
        #     return False

    def create_new_subsite(self, sitename, subsitename):
        self.click_site_in_global_site_view_tree(sitename)
        self.click_new_site_button()
        self.enter_text_into_site_name_text_field(subsitename)
        self.click_site_name_popup_ok_button()
        # self.expand_site_tree(sitename)
        self.check_subsite_is_in_parent_site(sitename, subsitename)

    def create_subsite_if_not_exists(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']"
        subsite_name = "span[text() = '" + subsitename + "']"
        elem = site_name + Locators.fol + subsite_name
        self.click_site_in_global_site_view_tree(sitename)
        self.expand_site_tree(sitename)
        cond = self.is_element_not_present(elem)
        if cond:
            self.create_new_subsite(sitename, subsitename)
            self.check_subsite_is_in_parent_site(sitename, subsitename)
        else:
            pass
        # try:
        #     self.click_site_in_global_site_view_tree(sitename)
        #     self.expand_site_tree(sitename)
        #     cond = self.is_element_not_present(
        #         "//span[text()='" + sitename + "']/following::span[text()='" + subsitename + "']")
        #     if cond:
        #         self.create_new_site(subsitename)
        #         cond1 = self.check_subsite_is_in_parent_site(sitename, subsitename)
        #         return True if cond1 else False
        #     else:
        #         pass
        # except NoSuchElementException:
        #     return False

    def click_subsite_in_site_tree(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']"
        subsite_name = "//span[text()='" + subsitename + "']"
        contains_subsite_name = "//span[contains(text(),'" + subsitename + "')]"
        elem = site_name + Locators.fol + Locators.EL_CHILD_SITE + "/*" + subsite_name
        self.click_element(elem)
        self.wait_for_element_selected(elem + Locators.anc + Locators.EL_TREE_NODE)
        self.wait_for_element_present(Locators.BTN_CONFIG)
        self.wait_for_element_present(Locators.BTN_NEW_SITE)
        self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + contains_subsite_name)

    def click_config_button(self):
        self.click_element(Locators.BTN_CONFIG)
        self.wait_for_element_present(Locators.POPUP_CONFIGURATION)


    def click_configuration_popup_close_button(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_CONFIGURATION)

    def click_configuration_popup_system_button_close(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_CONFIGURATION)

    def enter_text_into_site_tab_name_text_field(self, sitename):
        self.find_element_self(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_).send_keys(sitename)

    def click_configuration_popup_site_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)

    def click_configuration_popup_ip_address_ranges_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)

    def click_configuration_popup_vreps_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)

    def click_configuration_popup_site_tab_column_set_new_button(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.BTN_NEW_by_text)
        self.wait_for_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def click_column_set_popup_system_button_close(self):
        self.click_element(Locators.POPUP_COLUMN_SET_DESIGNER + "/*" + Locators.SYS_BTN_CLOSE)
        self.wait_for_element_not_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def check_site_is_in_global_site_view_tree(self, sitename = Variables.site_name):
        site_name = "//span[text()='" + sitename + "']"
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + site_name)
        return True if cond else False

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']"
        subsite_name = "span[text() = '" + subsitename + "']"
        cond = self.is_element_present(site_name + Locators.fol + subsite_name)
        return True if cond else False

    def check_name_text_field_input_value(self):
        elem = Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD_
        actual_attribute_value = self.get_attribute_value(elem, "value")
        print ("\n" + "The actual Name text field value of the attribute 'value' is: " + actual_attribute_value + "\n")
        return actual_attribute_value
        # try:
        #     a = self.find_element_self(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD).get_attribute(value)
        #     print "The actual Name text field value of the attribute 'value' is " + a
        #     return a
        # except NoSuchElementException:
        #     return None
        # elem = self.find_element_self(Locators.POPUP_CONFIGURATION + Locators.FIELD)
        # cond = self.get_attribute_value(elem, "value")
        # return True if expected_attribue_value == cond else False

    # def create_column_sets_from_ribbon_bar(self, columnsetname):
    #     self.click_global_site_view_label()
    #     self.click_ribbon_bar_view_tab()
    #     self.click_ribbon_bar_view_tab_edit_or_create_button()
    #     self.delete_columnset_in_column_sets_popup_if_exist(columnsetname)
    #     self.create_columnset_in_column_sets_popup(columnsetname)
    #     self.click_column_sets_popup_ok_button()

    def click_ribbon_bar_view_tab(self):
        self.click_element(Locators.TAB_VIEW)
        self.is_element_selected(Locators.TAB_VIEW)
        self.is_element_present(Locators.BUTTONS_BOX_DISPLAY)

    def click_ribbon_bar_view_tab_edit_or_create_button(self):
        self.click_element(Locators.BTN_EDIT_OR_CREATE)
        self.is_element_present(Locators.POPUP_COLUMN_SETS)

    def click_column_sets_popup_new_button(self):
        self.click_element(Locators.POPUP_COLUMN_SETS + "/*" + Locators.BTN_NEW)
        self.is_element_present(Locators.POPUP_COLUMN_SET_DESIGNER)

    def delete_columnset_in_column_sets_popup_if_exist(self, columnsetname):
        columnset_name = "//span[text()='" + columnsetname + "']"
        elem = Locators.POPUP_COLUMN_SETS + "/*" + Locators.EL_TABLE_BODY + "/*" + columnset_name
        cond = self.is_element_present(elem)
        if cond:
            self.click_columnset_in_column_sets_popup_table_list(columnsetname)
            self.click_ribbon_bar_delete_button()
            self.click_are_you_sure_popup_ok_button()
            self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)
            return True
        else:
            pass

    def click_columnset_in_column_sets_popup_table_list(self, columsetname):
        columnset_name = "//span[text()='" + columsetname + "']"
        self.click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*" + columnset_name)
        self.wait_for_element_selected(columnset_name + Locators.anc + Locators.EL_TABLE_ROW)

    def create_columnset_in_column_sets_popup(self, columnsetname, *param):
        self.click_column_sets_popup_new_button()


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
