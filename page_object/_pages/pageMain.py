from _feature_objects.leftSideMenu import LeftSideMenu
from _feature_objects.ribbonBar import RibbonBar
from _feature_objects.popups import *
from _settings.settings import Settings


class MainPage(LeftSideMenu, RibbonBar, ConfigurationPopup, ColumnSetsPopup, ColumnSetDesignerPopup, AreYouSurePopup,
               NewSitePopup, ErrorPopup):

    def check_main_page_loaded(self):
        time.sleep(5)
        # cond1 = self.wait_for_element_present(Locators.TEXT_WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
        cond1 = self.is_element_present(RibbonBar.BUTTON_EXIT)
        cond2 = self.is_element_present(LeftSideMenu.ICON_HOME)
        cond3 = self.is_element_present(LeftSideMenu.ICON_DEVICES)
        return True if (cond1 and cond2 and cond3) else False

    # def click_global_site_view_label(self):
    #     self.click_element(Locators.LABEL_GLOBAL_SITE_VIEW)
    #     self.wait_for_element_present(Locators.BTN_NEW_SITE)
    #     self.wait_for_element_selected(Locators.LABEL_GLOBAL_SITE_VIEW)
    #     self.wait_for_element_present(Locators.CONTAINER_PANEL_TITLE_DEVICES + "/*" + Locators.TEXT_CONTAINS_GLOBAL_SITE_VIEW)
    #     self.wait_for_element_not_present(Locators.BTN_DELETE)

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
        RibbonBar.click_delete_button(self)
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

    def click_configuration_popup_site_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_SITE)

    def click_configuration_popup_ip_address_ranges_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_IP_ADDRESS_RANGES)

    def click_configuration_popup_vreps_tab(self):
        self.click_element(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)
        self.wait_for_element_selected(Locators.POPUP_CONFIGURATION + "/*" + Locators.TAB_VREPS)

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self.is_element_present(Locators.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        cond = self.is_element_present("//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']")
        return True if cond else False

    def open_column_sets_popup_from_ribbon_bar(self):
        self.click_global_site_view_label()
        RibbonBar.click_tab_view(self)
        RibbonBar.click_button_edit_or_create(self)

    def create_columnset_from_ribbon_bar(self, columnsetname, column_list):
        LeftSideMenu.click_global_site_view_label(self)
        RibbonBar.click_tab_view(self)
        RibbonBar.click_button_edit_or_create(self)
        cond = ColumnSetsPopup.check_is_columnset_present(self, columnsetname)
        pages = self.is_element_present(Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_PAGES_PANEL)
        # if pages:
        #     pages_number = self._find_element(Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_LIST_PAGES_NUMBER).text()
        #     # number = pages_number.text()
        #     print pages_number
        #     while pages_number >= 1:
        #         self.send_keys_and_enter(Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_FIELD_GO_TO, pages_number)
        # else:
        #     pass
        while cond:
            ColumnSetsPopup.click_columnset_in_table_list(self, columnsetname)
            ColumnSetsPopup.click_button_delete(self)
            AreYouSurePopup.click_button_ok(self)
        else:
            pass
        ColumnSetsPopup.click_button_new(self)
        ColumnSetDesignerPopup.click_system_button_maximize(self)
        ColumnSetDesignerPopup.enter_text_into_text_field_name(self, columnsetname)
        ColumnSetDesignerPopup.expand_all_left_side_lists(self)
        for columnname in list(column_list):
            ColumnSetDesignerPopup.click_column_in_left_side_tree(self, columnname)
            ColumnSetDesignerPopup.click_button_add(self, columnname)
        # ColumnSetDesignerPopup.add_columns_to_list_view(self, column_list)
        ColumnSetDesignerPopup.click_button_ok(self)
        result = ColumnSetsPopup.check_is_columnset_present(self,columnsetname)
        ColumnSetsPopup.click_button_ok(self)
        RibbonBar.click_tab_home(self)
        LeftSideMenu.click_global_site_view_label(self)
        return result

    # def create_columnset_from_column_sets_popup(self, columnsetname, columns_list):
    #     self.click_button_new()
    #     self.enter_text_into_text_field_name(columnsetname)
    #     self.add_columns_to_list_view(columns_list)
    #     ColumnSetDesignerPopup.click_button_add(self, columns_list)

    def select_columnset_from_configuration_popup_column_set_dropdown_list(self, columnsetname):
        ConfigurationPopup.select_columnset_in_configuration_popup_drop_down_list(self, columnsetname)

    def check_columns_are_presented_in_devices_list_header(self, columns_list):
        columnset = []
        for i in columns_list:
            elem = Locators.DEVICES_LIST_HEADER + "/*//span[contains(text(),'" + str(i) + "')]"
            cond = self.is_element_present(elem)
            if cond:
                columnset.append(i)
            else:
                pass
        print columnset
        if columnset == columns_list:
            pass
        else:
            print "\n" + "Expected columns for columnset is"
            print columns_list
            print "Actual columns for columnset is"
            print columnset
            print "The result is "
            print columns_list == columnset
        return True if columnset == columns_list else False

    def create_columnset_from_column_sets_popup(self, columnsetname, columns_list):
        ColumnSetsPopup.click_button_new(self)
        ColumnSetDesignerPopup.click_system_button_maximize(self)
        ColumnSetDesignerPopup.enter_text_into_text_field_name(self,columnsetname)
        ColumnSetDesignerPopup.add_columns_to_list_view(self, columns_list)
        ColumnSetDesignerPopup.click_button_ok(self)

    def create_columnset_from_configuration_popup(self, columnsetname, columns_list):
        ConfigurationPopup.click_button_new(self)
        ColumnSetDesignerPopup.click_system_button_maximize(self)
        ColumnSetDesignerPopup.enter_text_into_text_field_name(self,columnsetname)
        ColumnSetDesignerPopup.add_columns_to_list_view(self, columns_list)
        ColumnSetDesignerPopup.click_button_ok(self)

    def delete_columnset_if_exist(self, columnsetname):
        elem = self.CS_TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
        cond = self.is_element_present(elem)
        if cond:
            ColumnSetsPopup.click_columnset_in_table_list(self, columnsetname)
            ColumnSetsPopup.click_button_delete(self)
            AreYouSurePopup.click_button_yes(self)
            self.wait_for_element_not_present(elem)
            return True
        else:
            pass

    # def delete_columnset_if_exist(self, columnsetname):
    #     elem = self.CS_TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
    #     cond = self.is_element_present(elem)
    #     cond_pages = self.is_element_present(Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_PAGES_PANEL)
    #     pages_number = self.get_attribute_value(Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_PAGES_NUMBER)
    #
    #     if cond:
    #         ColumnSetsPopup.click_columnset_in_table_list(self, columnsetname)
    #         ColumnSetsPopup.click_button_delete(self)
    #         AreYouSurePopup.click_button_yes(self)
    #         self.wait_for_element_not_present(elem)
    #         return True
    #     else:
    #         pass
