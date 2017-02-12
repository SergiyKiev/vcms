from _base_page.base_elements import *
from _feature_objects._featureTabs.featureTabDevices import *
from _feature_objects._feature_left_menus.featureLeftMenu import LeftMenu
from _feature_objects._feature_left_menus.featureLeftMenuDevices import LeftMenuDevices
from _feature_objects._feature_popups.featurePopupAreYouSure import AreYouSurePopup
from _feature_objects._feature_popups.featurePopupColumnSetDesigner import ColumnSetDesignerPopup
from _feature_objects._feature_popups.featurePopupColumnSets import ColumnSetsPopup
from _feature_objects._feature_popups.featurePopupConfiguration import ConfigurationPopup
from _feature_objects._feature_popups.featurePopupError import ErrorPopup
from _feature_objects._feature_popups.featurePopupRemoveDevices import RemoveDevicesPopup
from _feature_objects._feature_popups.featurePopupSiteName import SiteNamePopup
from _feature_objects.featureRibbonBar import RibbonBar


class MainPage(LeftMenu, LeftMenuDevices, RibbonBar, ConfigurationPopup, ColumnSetsPopup, ColumnSetDesignerPopup,
               AreYouSurePopup, SiteNamePopup, ErrorPopup, RemoveDevicesPopup, DevicesTab):

    def check_main_page_loaded(self):
        self.wait_for_element_present(BaseElements._RIBBON_BAR)
        self.wait_for_elements_present(BaseElements._PANEL)
        cond1 = self._is_element_present(RibbonBar.BUTTON_EXIT)
        cond2 = self._is_element_present(LeftMenu.ICON_HOME)
        cond3 = self._is_element_present(LeftMenu.ICON_DEVICES)
        return True if (cond1 and cond2 and cond3) else False

    def delete_site_if_exists(self, sitename):
        element = LeftMenuDevices.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']"
        cond = self._is_element_present(element)
        if cond:
            LeftMenuDevices.click_site_in_global_site_view_tree(self, sitename)
            RibbonBar.click_button_delete(self)
            AreYouSurePopup.click_button_ok(self)
        else:
            pass

    def delete_site_from_global_site_view_tree(self, sitename):
        LeftMenuDevices.click_site_in_global_site_view_tree(self, sitename)
        RibbonBar.click_button_delete(self)
        AreYouSurePopup.click_button_ok(self)

    def create_new_site(self, sitename):
        LeftMenuDevices.click_global_site_view_label(self)
        RibbonBar.click_button_new_site(self)
        SiteNamePopup.enter_text_into_name_text_field(self, sitename)
        SiteNamePopup.click_button_ok(self)
        LeftMenuDevices.check_site_is_in_global_site_view_tree(self, sitename)

    def create_site_if_not_exists(self, sitename):
        cond = self._is_element_not_present(LeftMenuDevices.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        if cond:
            LeftMenuDevices.click_global_site_view_label(self)
            RibbonBar.click_button_new_site(self)
            SiteNamePopup.enter_text_into_name_text_field(self, sitename)
            SiteNamePopup.click_button_ok(self)
            LeftMenuDevices.check_site_is_in_global_site_view_tree(self, sitename)
        else:
            pass

    def create_new_subsite(self, sitename, subsitename):
        LeftMenuDevices.click_site_in_global_site_view_tree(self, sitename)
        RibbonBar.click_button_new_site(self)
        SiteNamePopup.enter_text_into_name_text_field(self, subsitename)
        SiteNamePopup.click_button_ok(self)
        LeftMenuDevices.check_subsite_is_in_parent_site(self, sitename, subsitename)

    def create_subsite_if_not_exists(self, sitename, subsitename):
        element = "//span[text()='" + sitename + "']/following::span[text() = '" + subsitename + "']"
        LeftMenuDevices.click_site_in_global_site_view_tree(self, sitename)
        # self.expand_site_tree(sitename)
        cond = self._is_element_not_present(element)
        if cond:
            self.create_new_subsite(sitename, subsitename)
        else:
            pass

    def open_column_sets_popup_from_ribbon_bar(self):
        LeftMenuDevices.click_global_site_view_label(self)
        RibbonBar.click_tab_view(self)
        RibbonBar.click_button_edit_or_create(self)

    def delete_devices_in_devices_tab_table(self, *names):
        for name in list(*names):
            cond = DevicesTab.check_device_is_present(self, name)
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



