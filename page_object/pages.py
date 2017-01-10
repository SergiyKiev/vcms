from basePage import BasePage
from locators import Locators
from settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from variables import Variables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    def check_login_page_loaded(self):
        cond1 = self.is_element_present(Locators.BUTTON_SIGN_IN)
        cond2 = self.is_element_present(Locators.FIELD_USERNAME)
        cond3 = self.is_element_present(Locators.FIELD_PASSWORD)
        return True if (cond1 and cond2 and cond3) else False

    def login(self):
        self.check_login_page_loaded()
        self.close_terms_and_conditions_popup()
        self.enter_username()
        self.enter_password()
        self.do_login()
        return HomePage(self.driver)

    def click_terms_and_conditions_popup_i_agree_button(self):
        self.click_element(Locators.POPUP_TERMS_AND_CONDITIONS + "/*" + Locators.BUTTON_I_AGREE)
        cond = self.wait_for_element_not_present(Locators.POPUP_TERMS_AND_CONDITIONS)
        return True if cond else False

    def close_terms_and_conditions_popup(self):
        cond = self.is_element_present(Locators.POPUP_TERMS_AND_CONDITIONS)
        if cond:
            self.click_terms_and_conditions_popup_i_agree_button()
            return True
        else:
            pass


    def click_subscription_has_expired_popup_system_button_close(self):
        self.click_element(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED + "/*" + Locators.SYSTEM_BUTTON_CLOSE)
        cond = self.wait_for_element_not_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        return True if cond else False

    def close_subscription_has_expired_popup(self):
        cond = self.is_element_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        if cond:
            self.click_subscription_has_expired_popup_system_button_close()
        else:
            pass
        return True

    def enter_username(self, username = Settings.username):
        self.find_element_self(Locators.FIELD_USERNAME).send_keys(username)
        return True

    def enter_password(self, password = Settings.password):
        self.find_element_self(Locators.FIELD_PASSWORD).send_keys(password)
        return True

    def click_sign_in_button(self):
        self.click_element(Locators.BUTTON_SIGN_IN)
        return True

    def do_login(self):
        self.click_sign_in_button()
        cond1 = self.is_element_present(Locators.POPUP_ERROR)
        cond2 = self.is_element_present(Locators.POPUP_SUBSCRIPTION_HAS_EXPIRED)
        if cond1:
            print Settings.username + " or " +  Settings.password + " are incorrect"
            return False
        elif cond2:
            self.close_subscription_has_expired_popup()
            self.wait_for_element_present(Locators.BUTTON_EXIT)
            return HomePage(self.driver)
        else:
            self.wait_for_element_present(Locators.BUTTON_EXIT)
            return HomePage(self.driver)

    def close_error_popup(self):
        self.click_element(Locators.POPUP_ERROR + "/*" + Locators.SYSTEM_BUTTON_CLOSE)
        cond = self.wait_for_element_not_present(Locators.POPUP_ERROR)
        return True if cond else False


class HomePage(BasePage):

    def check_home_page_loaded(self):
        cond = self.wait_for_elements_present(Locators.BUTTON_DEVICES)
        return True if cond else False

    def click_devices_menu_button(self):
        self.click_element(Locators.BUTTON_DEVICES)
        cond = self.wait_for_element_present(Locators.CONTAINER_MENU_DEVICES)
        return True if cond else None

    def open_devices_menu(self):
        cond = self.is_element_present(Locators.CONTAINER_MENU_DEVICES)
        if cond:
            return DevicesPage(self.driver)
        else:
            self.click_devices_menu_button()
            return DevicesPage(self.driver)


class DevicesPage(BasePage):

    def check_devices_page_loaded(self):
        cond = self.wait_for_element_present(Locators.CONTAINER_MENU_DEVICES)
        return True if cond else False

    def click_global_site_view_main_label(self):
        self.click_element(Locators.LABEL_GLOBAL_SITE_VIEW)
        cond1 = self.wait_for_element_present(Locators.BUTTON_NEW_SITE)
        cond2 = self.wait_for_element_selected(Locators.LABEL_GLOBAL_SITE_VIEW)
        cond4 = self.wait_for_element_present(Locators.CONTAINER_HEADER_DEVICES_VIEW + "/*" + Locators.TEXT_CONTAINS_GLOBAL_SITE_VIEW)
        cond3 = self.wait_for_element_not_present(Locators.BUTTON_DELETE)
        return True if (cond1 and cond2 and cond3 and cond4) else False

    def click_new_site_button(self):
        self.click_element(Locators.BUTTON_NEW_SITE)
        cond = self.wait_for_element_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def enter_text_into_site_name_text_field(self, sitename = Variables.site_name):
        self.find_element_self(Locators.POPUP_SITE_NAME + "/*" + Locators.FIELD).send_keys(sitename)
        return True

    def click_site_name_popup_ok_button(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BUTTON_OK)
        cond = self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def click_site_name_popup_system_button_close(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.SYSTEM_BUTTON_CLOSE)
        cond = self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def click_site_in_global_site_view_tree(self, sitename = Variables.site_name):
        self.click_element(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        cond1 = self.wait_for_element_selected("//span[text()='" + sitename + "']" + "/ancestor::div")
        cond2 = self.wait_for_element_present(Locators.BUTTON_CONFIG)
        cond3 = self.wait_for_element_present(Locators.BUTTON_NEW_SITE)
        cond4 = self.wait_for_element_present(Locators.CONTAINER_HEADER_DEVICES_VIEW + "/*//span[contains(text(),'" + sitename + "')]")
        return True if (cond1 and cond2 and cond3 and cond4) else False

    def click_default_site_in_global_site_view_tree(self):
        self.click_element(Locators.LABEL_DEFAULT_SITE)
        cond1 = self.wait_for_element_selected(Locators.LABEL_DEFAULT_SITE)
        cond2 = self.wait_for_element_present(Locators.CONTAINER_HEADER_DEVICES_VIEW + "/*" + Locators.TEXT_CONTAINS_DEFAULT_SITE)
        return True if (cond1 and cond2) else False

    def click_delete_button(self):
        self.click_element(Locators.BUTTON_DELETE)
        cond = self.wait_for_element_present(Locators.POPUP)
        cond1 = self.is_element_present(Locators.POPUP_ARE_YOU_SURE)
        cond2 = self.is_element_present(Locators.POPUP_UNABLE_TO_REMOVE)
        return True if cond and (cond1 or cond2) else False

    def click_are_you_sure_popup_ok_button(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.BUTTON_OK)
        cond = self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_are_you_sure_popup_system_button_close(self):
        self.click_element(Locators.POPUP_ARE_YOU_SURE + "/*" + Locators.SYSTEM_BUTTON_CLOSE)
        cond = self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)
        return True if cond else False

    def click_unable_to_remove_popup_ok_button(self):
        self.click_element(Locators.POPUP_UNABLE_TO_REMOVE + "/*" + Locators.BUTTON_Ok)
        cond = self.wait_for_element_not_present(Locators.POPUP_UNABLE_TO_REMOVE)
        return True if cond else False

    def delete_site_if_exists(self, sitename):
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        if cond:
            self.click_site_in_global_site_view_tree(sitename)
            self.click_delete_button()
            self.click_are_you_sure_popup_ok_button()
            self.wait_for_element_not_present(Locators.POPUP_ARE_YOU_SURE)
            return True
        else:
            pass

    def delete_site_from_global_site_view_tree(self, sitename):
        self.click_site_in_global_site_view_tree(sitename)
        self.click_delete_button()
        self.click_are_you_sure_popup_ok_button()
        cond = self.wait_for_element_not_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def click_site_name_popup_cancel_button(self):
        self.click_element(Locators.POPUP_SITE_NAME + "/*" + Locators.BUTTON_CANCEL)
        cond = self.wait_for_element_not_present(Locators.POPUP_SITE_NAME)
        return True if cond else False

    def click_error_popup_ok_button(self):
        self.click_element(Locators.POPUP_ERROR + "/*" + Locators.BUTTON_Ok)
        cond = self.wait_for_element_not_present(Locators.POPUP_ERROR)
        return True if cond else False

    def click_site_expand_button(self, sitename):
        expand = "//span[text()='" + sitename + "']/ancestor::/div[contains(@id,'VWGNODE')]" + Locators.SYSTEM_TREE_ARROW_EXPAND
        self.click_element(expand)
        cond = self.wait_for_element_not_present(EC.presence_of_element_located((By.XPATH, expand)))
        return True if cond else False

    def expand_site_tree(self, sitename):
        expand = "//span[text()='" + sitename + "']/ancestor::div[contains(@id,'VWGNODE')]" + Locators.SYSTEM_TREE_ARROW_EXPAND
        cond = self.is_element_present(expand)
        if cond:
            self.click_site_expand_button(expand)
            return True
        else:
            pass

    def expand_default_site_tree(self):
        expand = Locators.LABEL_DEFAULT_SITE + Locators.SYSTEM_TREE_ARROW_EXPAND
        cond=self.is_element_present(expand)
        if cond:
            self.click_site_expand_button(expand)
            return True
        else:
            pass


    def expand_global_site_view_tree(self):
        try:
            expand = Locators.LABEL_GLOBAL_SITE_VIEW + Locators.SYSTEM_TREE_ARROW_EXPAND
            cond=self.is_element_present(expand)
            if cond:
                self.click_site_expand_button(expand)
                return True
            else:
                pass
        except(NoSuchElementException):
            return True

    def create_new_site(self, sitename):
        self.click_global_site_view_main_label()
        self.click_new_site_button()
        self.enter_text_into_site_name_text_field(sitename)
        self.click_site_name_popup_ok_button()
        self.check_site_is_in_global_site_view_tree(sitename)

    def create_site_if_not_exists(self, sitename):
        cond = self.is_element_not_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        if cond:
            self.click_global_site_view_main_label()
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
        #         self.click_global_site_view_main_label()
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
        self.click_site_in_global_site_view_tree(sitename)
        self.expand_site_tree(sitename)
        self.check_subsite_is_in_parent_site(sitename, subsitename)

    def create_subsite_if_not_exists(self, sitename, subsitename):
        self.click_site_in_global_site_view_tree(sitename)
        self.expand_site_tree(sitename)
        cond = self.is_element_not_present(
            "//span[text()='" + sitename + "']/following::div" + Locators.CHILD_SITE + "/*//span[text()='" + subsitename + "']")
        if cond:
            self.create_new_subsite(sitename, subsitename)
            cond1 = self.check_subsite_is_in_parent_site(sitename, subsitename)
            return True if cond1 else False
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
        self.text_sitename = "//span[text()='" + sitename + "']"
        self.text_subsitename = "//span[text()='" + subsitename + "']"
        self.elem = self.text_sitename + "/following::div" + Locators.CHILD_SITE + "/*" + self.text_subsitename
        self.click_element(self.elem)
        cond1 = self.wait_for_element_selected(self.elem + "/ancestor::div")
        cond2 = self.wait_for_element_present(Locators.BUTTON_CONFIG)
        cond3 = self.wait_for_element_present(Locators.BUTTON_NEW_SITE)
        cond4 = self.wait_for_element_present(Locators.CONTAINER_HEADER_DEVICES_VIEW + "/*//span[contains(text(),'" + subsitename + "')]")
        return True if (cond1 and cond2 and cond3 and cond4) else False

    def click_config_button(self):
        self.click_element(Locators.BUTTON_CONFIG)
        cond = self.wait_for_element_present(Locators.POPUP_CONFIGURATION)
        return True if cond else False

    def click_configuration_popup_close_button(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.BUTTON_CLOSE)
        cond = self.wait_for_element_not_present(Locators.POPUP_CONFIGURATION)
        return True if cond else False

    def click_configuration_popup_system_button_close(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.SYSTEM_BUTTON_CLOSE)
        cond = self.wait_for_element_not_present(Locators.POPUP_CONFIGURATION)
        return True if cond else False

    def enter_text_into_site_tab_name_text_field(self, sitename):
        self.find_element_self(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD).send_keys(sitename)
        return True

    def click_configuration_popup_site_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)
        cond = self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)
        return True if cond else False

    def click_configuration_popup_ip_address_ranges_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)
        cond = self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)
        return True if cond else False

    def click_configuration_popup_vreps_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)
        cond = self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)
        return True if cond else False

    def check_site_is_in_global_site_view_tree(self, sitename = Variables.site_name):
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        cond = self.is_element_present(
            "//span[text()='" + sitename + "']/following::span[text()='" + subsitename + "']")
        return True if cond else False

    def check_name_text_field_input_value(self):
        elem = Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD
        actual_attribute_value = self.get_attribute_value(elem, "value")
        print ("\n" + "The actual Name text field value of the attribute 'value' is: " + actual_attribute_value + "\n")
        return actual_attribute_value
        # try:
        #     a = self.find_element_self(Locators.POPUP_CONFIGURATION + "/*" + Locators.FIELD).get_attribute(value)
        #     print "The actual Name text field value of the attribute 'value' is " + a
        #     return a
        # except NoSuchElementException:
        #     return None
    #     elem = self.find_element_self(Locators.POPUP_CONFIGURATION + Locators.FIELD)
    #     cond = self.get_attribute_value(elem, "value")
    #     return True if expected_attribue_value == cond else False


class AdministrationPage(BasePage):
    pass


class TasksPage(BasePage):
    pass


class ReportingPage(BasePage):
    pass


class SoftwarePatchManagerPage(BasePage):
    pass


class PasswordReset(BasePage):
    pass
