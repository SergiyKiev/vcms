
from _base_page.base_actions import BaseActions
from _feature_objects._popups.popupRemoveDevices import RemoveDevicesPopup
from _feature_objects.ribbonBar import RibbonBar


class DevicesPage(BaseActions):

    PAGE_HEADER = "//span[text()='Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = PAGE_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_page_is_present(self):
        cond = self._is_element_present(DevicesPage.PAGE_HEADER)
        return True if cond else False

    def select_device_in_table(self, *name):
        self.wait_for_element_present(DevicesPage.TABLE_ROW)
        row = DevicesPage.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)

    def click_icon_refresh(self):
        self._click_icon_refresh(self.PAGE_HEADER)

    def click_icon_search(self):
        self._click_icon_search(self.PAGE_HEADER)

    def enter_text_into_search_field(self, text = None):
        self._find_element(self.SEARCH_FIELD).send_keys(text)

    def check_device_is_present(self, name):
        cond = self._is_element_present(DevicesPage.TABLE_ROW + "/*//span[text()='" + str(name) + "']/ancestor::tr")
        return True if cond else False

    def check_columns_are_present(self, columns_list):
        columnset = []
        for i in columns_list:
            elem = DevicesPage.TABLE_HEADER + "/*//span[contains(text(),'" + str(i) + "')]"
            cond = self._is_element_present(elem)
            if cond:
                columnset.append(i)
            else:
                pass
        print "Created column set is: ", columns_list
        print "Expected column set is : ", columnset
        if columnset == columns_list:
            pass
        else:
            print "Columnsets are not similar ", columns_list, columnset
        return True if columnset == columns_list else False

    def click_icon_help(self):
        self._click_icon_help(DevicesPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Devices")
        return True if cond else False

    def delete_devices_in_devices_page_table(self, *names):
        for name in list(*names):
            self.enter_text_into_search_field(name)
            self.click_icon_search()
            cond = self.check_device_is_present(name)
            if cond:
                self.select_device_in_table(name)
                ribbon_bar = RibbonBar(self.driver)
                remove_devices_popup = RemoveDevicesPopup(self.driver)
                ribbon_bar.click_button_delete_or_archive()
                cond = self._is_element_checked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
                if cond:
                    remove_devices_popup.uncheck_keep_historical_information_check_box()
                else:
                    pass
                remove_devices_popup.click_button_ok()
                self.click_icon_refresh()
                print "Device was found and deleted: ", name
            else:
                print "No device was found:", name

    def delete_single_device_in_devices_page_table(self, name):
        self.enter_text_into_search_field(name)
        self.click_icon_search()
        cond = self.check_device_is_present(name)
        if cond:
            self.select_device_in_table(name)
            ribbon_bar = RibbonBar(self.driver)
            remove_devices_popup = RemoveDevicesPopup(self.driver)
            ribbon_bar.click_button_delete_or_archive()
            cond = self._is_element_checked(RemoveDevicesPopup.CHECKBOX_KEEP_HIST_INFORM)
            if cond:
                remove_devices_popup.uncheck_keep_historical_information_check_box()
            else:
                pass
            remove_devices_popup.click_button_ok()
            self.click_icon_refresh()
            print "Device was found and deleted: ", name
        else:
            print "No device was found:", name



