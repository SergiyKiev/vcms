from _feature_objects.featureLeftSideMenu import LeftSideMenu
from _feature_objects.featureRibbonBar import RibbonBar
from _feature_objects.featurePopups import *
from _settings.settings import Settings
from _feature_objects.featureTabs import *


class MainPage(LeftSideMenu, RibbonBar, ConfigurationPopup, ColumnSetsPopup, ColumnSetDesignerPopup,
               AreYouSurePopup, SiteNamePopup, ErrorPopup, RemoveDevicesPopup, DevicesTab):

    def check_main_page_loaded(self):
        self.wait_for_element_present(BaseElements._RIBBON_BAR)
        self.wait_for_elements_present(BaseElements._PANEL)
        cond1 = self._is_element_present(RibbonBar.BUTTON_EXIT)
        cond2 = self._is_element_present(LeftSideMenu.ICON_HOME)
        cond3 = self._is_element_present(LeftSideMenu.ICON_DEVICES)
        return True if (cond1 and cond2 and cond3) else False

    def delete_site_if_exists(self, sitename):
        element = LeftSideMenu.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']"
        cond = self._is_element_present(element)
        if cond:
            LeftSideMenu.click_site_in_global_site_view_tree(self, sitename)
            RibbonBar.click_button_delete(self)
            AreYouSurePopup.click_button_ok(self)
        else:
            pass

    def delete_site_from_global_site_view_tree(self, sitename):
        LeftSideMenu.click_site_in_global_site_view_tree(self, sitename)
        RibbonBar.click_button_delete(self)
        AreYouSurePopup.click_button_ok(self)

    def create_new_site(self, sitename):
        LeftSideMenu.click_global_site_view_label(self)
        RibbonBar.click_button_new_site(self)
        SiteNamePopup.enter_text_into_name_text_field(self, sitename)
        SiteNamePopup.click_button_ok(self)
        LeftSideMenu.check_site_is_in_global_site_view_tree(self, sitename)

    def create_site_if_not_exists(self, sitename):
        cond = self._is_element_not_present(LeftSideMenu.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        if cond:
            LeftSideMenu.click_global_site_view_label(self)
            RibbonBar.click_button_new_site(self)
            SiteNamePopup.enter_text_into_name_text_field(self, sitename)
            SiteNamePopup.click_button_ok(self)
            LeftSideMenu.check_site_is_in_global_site_view_tree(self, sitename)
        else:
            pass

    def create_new_subsite(self, sitename, subsitename):
        LeftSideMenu.click_site_in_global_site_view_tree(self, sitename)
        RibbonBar.click_button_new_site(self)
        SiteNamePopup.enter_text_into_name_text_field(self, subsitename)
        SiteNamePopup.click_button_ok(self)
        LeftSideMenu.check_subsite_is_in_parent_site(self, sitename, subsitename)

    def create_subsite_if_not_exists(self, sitename, subsitename):
        element = "//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']"
        LeftSideMenu.click_site_in_global_site_view_tree(self, sitename)
        # self.expand_site_tree(sitename)
        cond = self._is_element_not_present(element)
        if cond:
            self.create_new_subsite(sitename, subsitename)
        else:
            pass

    def open_column_sets_popup_from_ribbon_bar(self):
        LeftSideMenu.click_global_site_view_label(self)
        RibbonBar.click_tab_view(self)
        RibbonBar.click_button_edit_or_create(self)

    def create_columnset_from_ribbon_bar(self, columnsetname, column_list):
        LeftSideMenu.click_global_site_view_label(self)
        RibbonBar.click_tab_view(self)
        RibbonBar.click_button_edit_or_create(self)
        cond = ColumnSetsPopup.check_is_columnset_present(self, columnsetname)
        pages = self._is_element_present(Locators.POPUP_COLUMN_SETS + "/*//" + Locators.EL_PAGES_PANEL)
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
        ColumnSetDesignerPopup.expand_all_left_side_trees(self)
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

    # def check_columns_are_present(self, columns_list):
    #     columnset = []
    #     for i in columns_list:
    #         elem = Locators.DEVICES_LIST_HEADER + "/*//span[contains(text(),'" + str(i) + "')]"
    #         cond = self._is_element_present(elem)
    #         if cond:
    #             columnset.append(i)
    #         else:
    #             pass
    #     print "Created column set is: ", columns_list
    #     print "Expected column set is : ", columnset
    #     if columnset == columns_list:
    #         pass
    #     else:
    #         print "Columnsets are not similar ", columns_list, columnset
    #     return True if columnset == columns_list else False

    # def create_columnset_from_column_sets_popup(self, columnsetname, columns_list):
    #     ColumnSetsPopup.click_button_new(self)
    #     ColumnSetDesignerPopup.click_system_button_maximize(self)
    #     ColumnSetDesignerPopup.enter_text_into_text_field_name(self,columnsetname)
    #     ColumnSetDesignerPopup.add_columns_to_list_view(self, columns_list)
    #     ColumnSetDesignerPopup.click_button_ok(self)
    #
    # def create_columnset_from_configuration_popup(self, columnsetname, columns_list):
    #     ConfigurationPopup.click_button_new(self)
    #     ColumnSetDesignerPopup.click_system_button_maximize(self)
    #     ColumnSetDesignerPopup.enter_text_into_text_field_name(self,columnsetname)
    #     ColumnSetDesignerPopup.add_columns_to_list_view(self, columns_list)
    #     ColumnSetDesignerPopup.click_button_ok(self)

    # def delete_columnset_if_exists(self, columnsetname):
    #     elem = ColumnSetsPopup.TABLE_BODY + "/*//span[text()='" + columnsetname + "']"
    #     cond = self._is_element_present(elem)
    #     if cond:
    #         ColumnSetsPopup.click_columnset_in_table_list(self, columnsetname)
    #         ColumnSetsPopup.click_button_delete(self)
    #         AreYouSurePopup.click_button_yes(self)
    #         self.wait_for_element_not_present(elem)
    #     else:
    #         pass

    def delete_devices_in_devices_tab_table(self, *names):
        for name in list(*names):
            cond = DevicesTab.check_is_device_present(self, name)
            if cond:
                DevicesTab.select_device_in_table(self, name)
                RibbonBar.click_button_delete_or_archive(self)
                cond = self._is_element_checked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
                if cond:
                    RemoveDevicesPopup.uncheck_keep_historical_information_check_box(self)
                else:
                    pass
                RemoveDevicesPopup.click_button_ok(self)
                DevicesTab.click_icon_refresh(self)
                print "Device was found and deleted: ", name
            else:
                print "No device was found:", name



