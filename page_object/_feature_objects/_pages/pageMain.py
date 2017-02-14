from _base_page.base_elements import *
from _feature_objects._left_menus.leftMenu import LeftMenu
from _feature_objects._left_menus.leftMenuDevices import LeftMenuDevices
from _feature_objects._pages.pageDevices import *
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class MainPage(DevicesPage, RibbonBar, LeftMenuDevices):

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
        devices_page.delete_devices_in_devices_page_table(device_name)


