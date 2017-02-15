from _base_page.base_elements import *
from _feature_objects._left_menus.leftMenu import LeftMenu
from _feature_objects._left_menus.leftMenuAdministration import LeftMenuAdministration
from _feature_objects._left_menus.leftMenuDevices import LeftMenuDevices
from _feature_objects._pages.pageAdministration import AdministrationPage
from _feature_objects._pages.pageDevices import *
from _feature_objects._pages.pageVReps import VRepsPage
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class MainPage(RibbonBar, LeftMenuDevices, LeftMenuAdministration, DevicesPage, AdministrationPage, VRepsPage):

    def check_main_page_loaded(self):
        self.wait_for_element_present(BaseElements._RIBBON_BAR)
        self.wait_for_elements_present(BaseElements._PANEL)
        cond1 = self._is_element_present(RibbonBar.BUTTON_EXIT)
        cond2 = self._is_element_present(LeftMenu.ICON_HOME)
        cond3 = self._is_element_present(LeftMenu.ICON_DEVICES)
        return True if cond1 and cond2 and cond3 else False

    def delete_device_from_the_console(self, device_name):
        devices_page = DevicesPage(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        devices_page.delete_single_device_in_devices_page_table(device_name)
        cond = self.check_device_is_present(device_name)
        return True if cond is not True else False

    def upprove_vrep(self, device_name):
        vreps_page = VRepsPage(self.driver)
        left_menu_administration = LeftMenuAdministration(self.driver)
        left_menu_administration.open_menu_administration()
        left_menu_administration.click_vreps_label()
        vreps_page.upprove_single_vrep_in_vreps_page_table(device_name)
        cond = self.check_vrep_ready_for_work(device_name)
        return True if cond else False


