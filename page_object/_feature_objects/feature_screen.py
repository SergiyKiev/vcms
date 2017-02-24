import time

from _base.base_actions import BaseActions
from _base.base_elements import BaseElements
from _feature_objects.feature_popup import AreYouSurePopup
from _feature_objects.feature_popup import RemoveDevicesPopup
from _feature_objects.feature_ribbon_bar import RibbonBar


class BaseScreen(BaseActions):

    def _set_screen(self, name):
        locator = "//span[text()='" + str(name) + "'][@dir='LTR']/ancestor::" \
                                                 "div[@class='Panel-Control'][@data-vwgdocking='T']/parent::div"
        return str(locator)

    def _set_screen_header(self, screen_xpath):
        locator = str(screen_xpath) + "/div"
        return str(locator)

    def _set_screen_table_header(self, set_screen): #INPUT SCREEN METHOD FOR CURRENT SCREEN
        locator = str(set_screen) + BaseElements.TABLE_HEADER
        return str(locator)

    def _set_screen_table_body(self, set_screen):
        locator = str(set_screen) + BaseElements.TABLE_BODY
        return str(locator)

    def _get_all_table_header_names(self, set_screen_table_header):
        header_names = {}
        index = 1
        elements = self._find_elements(set_screen_table_header + "/*//tbody/tr/td/*//span")
        for element in elements:
            name = element.text
            print index
            # name = self._get_text(set_screen_table_header + "/*//tbody/tr/td/*//span")
            header_names[str(name)] = str(index)
            index += 2
        print header_names
        return header_names

class HomeScreen(BaseScreen):

    WELCOME_TO_CLOUD_MANAGEMENT_SUITE = "Welcome To Cloud Management Suite"
    HOME = "Home"
    # BODY = "//span[@dir='LTR'][contains(text(),'Welcome To Cloud')]/ancestor::div[@class='Panel-Control'][@data-vwgdocking='T']//parent::div"
    # SCREEN_HEADER = BODY + "/div"
    # BODY = SCREEN_HEADER + "/parent::div"

    def screen_name(self):
        locator = self._set_screen(self.WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
        return str(locator)

    def check_screen_is_present(self):
        cond = self._is_element_present(self.screen_name())
        msg_true = "Left menu '" + self.HOME + "' is opened"
        msg_false = "Left menu '" + self.HOME + "' is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_name())

    # def check_help_link_is_correct(self):
    #     cond = self._check_help_frame_header("Getting Started in CMS")
    #     return True if cond else False


class DevicesScreen(BaseActions):

    DEVICES = "Devices"
    SCREEN_HEADER = "//span[text()='Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_screen_is_present(self):
        cond = self._is_element_present(DevicesScreen.SCREEN_HEADER)
        return True if cond else False

    def select_device_in_table(self, *name):
        self._wait_for_element_present(DevicesScreen.TABLE_ROW)
        row = DevicesScreen.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)
        self.scroll_to_element(row + "/td[1]")
        self._wait_for_element_present(RibbonBar.TAB_DEVICES)
        self._wait_for_element_present(RibbonBar.TAB_TOOLS)

    def click_icon_refresh(self):
        self._click_icon_refresh(DevicesScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(DevicesScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(DevicesScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_present(self, name):
        cond = self._is_element_present(DevicesScreen.TABLE_ROW + "/*//span[text()='" + str(name) + "']/ancestor::tr")
        msg_true = "Device '" + name + "' is present"
        msg_false = "Device '" + name + "' is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_columns_are_present(self, columns_list):
        columnset = []
        for i in columns_list:
            elem = DevicesScreen.TABLE_HEADER + "/*//span[contains(text(),'" + str(i) + "')]"
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
        self._click_icon_help(DevicesScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        self._get_log_for_help_link("Devices")

    def delete_devices_in_devices_page_table(self, *names):
        try:
            for name in list(*names):
                self.enter_text_into_search_text_field(name)
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
                    self.logger.info("Device was found and deleted: " + str(name))
                else:
                    self.logger.info("No device was found:" + str(name))
        except Exception as e:
            self.logger.error("Method 'delete_devices_in_devices_page_table' is failed\n" + str(e))

    def delete_single_device_in_devices_page_table(self, name):
        try:
            self.enter_text_into_search_text_field(name)
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
                self.logger.info("Device was found and deleted: " + str(name))
            else:
                self.logger.info("No device was found:" + str(name))
        except Exception as e:
            self.logger.error("Method 'delete_single_device_in_devices_page_table' is failed\n" + str(e))


class GroupsScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Groups']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_screen_is_present(self):
        cond = self._is_element_present(GroupsScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(GroupsScreen.SCREEN_HEADER)

    def click_icon_refresh(self):
        self._click_icon_refresh(GroupsScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(GroupsScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(self.SEARCH_FIELD).send_keys(text)

    def check_group_is_present(self, name):
        cond = self._is_element_present(GroupsScreen.TABLE_ROW + "/*//span[text()='" + str(name) + "']/ancestor::tr")
        return True if cond else False

    def delete_groups_in_groups_page_table(self, *names):
        for name in list(*names):
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            cond = self.check_group_is_present(name)
            if cond:
                self.select_group_in_table(name)
                ribbon_bar = RibbonBar(self.driver)
                ribbon_bar.click_button_delete_group()
                are_you_sure_popup = AreYouSurePopup(self.driver)
                are_you_sure_popup.click_button_ok()
                print "Group was found and deleted: ", name
            else:
                print "No groups was found:", name

    def delete_single_group_in_groups_page_table(self, name):
        self.enter_text_into_search_text_field(name)
        self.click_icon_search()
        cond = self.check_group_is_present(name)
        if cond:
            self.select_group_in_table(name)
            ribbon_bar = RibbonBar(self.driver)
            ribbon_bar.click_button_delete_group()
            are_you_sure_popup = AreYouSurePopup(self.driver)
            are_you_sure_popup.click_button_ok()
            print "Group was found and deleted: ", name
        else:
            print "No group was found:", name

    def select_group_in_table(self, *name):
        self._wait_for_element_present(GroupsScreen.TABLE_ROW)
        row = GroupsScreen.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class QueriesScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Queries']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_screen_is_present(self):
        cond = self._is_element_present(QueriesScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(QueriesScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Queries")
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(QueriesScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(QueriesScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(self.SEARCH_FIELD).send_keys(text)

    def check_query_is_present(self, name):
        cond = self._is_element_present(QueriesScreen.TABLE_ROW + "/*//span[text()='" + str(name) + "']/ancestor::tr")
        return True if cond else False

    def delete_queries_in_queries_page_table(self, *names):
        for name in list(*names):
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            cond = self.check_query_is_present(name)
            if cond:
                self.select_query_in_table(name)
                ribbon_bar = RibbonBar(self.driver)
                ribbon_bar.click_button_delete()
                are_you_sure_popup = AreYouSurePopup(self.driver)
                are_you_sure_popup.click_button_ok()
                print "Query was found and deleted: ", name
            else:
                print "No queries was found:", name

    def delete_single_query_in_queries_page_table(self, name):
        self.enter_text_into_search_text_field(name)
        self.click_icon_search()
        cond = self.check_query_is_present(name)
        if cond:
            self.select_query_in_table(name)
            ribbon_bar = RibbonBar(self.driver)
            ribbon_bar.click_button_delete()
            are_you_sure_popup = AreYouSurePopup(self.driver)
            are_you_sure_popup.click_button_ok()
            print "Query was found and deleted: ", name
        else:
            print "No query was found:", name

    def select_query_in_table(self, *name):
        self._wait_for_element_present(QueriesScreen.TABLE_ROW)
        row = QueriesScreen.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class AdministrationScreen(BaseActions):
    ADMINISTRATION = "Administration"
    SCREEN_HEADER = "//span[text()='Administration']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"

    def check_screen_is_present(self):
        cond = self._is_element_present(AdministrationScreen.SCREEN_HEADER)
        msg_true = "Screen " + self.ADMINISTRATION + " is opened"
        msg_false = "Screen " + self.ADMINISTRATION + " is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(AdministrationScreen.SCREEN_HEADER)

    def open_administration_screen(self):
        cond = self._is_element_not_present(AdministrationScreen.SCREEN_HEADER)
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            ribbon_bar.open_tab_home()
            ribbon_bar.click_button_home()
            ribbon_bar.click_go_to_home_screen_menu_item()
            # self.check_screen_is_present()
            # print "Administration home screen is opened ", result


class EndpointManagementScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Endpoint Management Summary']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"

    def check_screen_is_present(self):
        cond = self._is_element_present(EndpointManagementScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EndpointManagementScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False


class DynamicallyManagedScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Dynamically Managed']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    PAGE_BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = PAGE_BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = PAGE_BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_DEVICE_NAME = TABLE_HEADER + "/*//span[contains(text(),'Device Name')]"
    HEADER_DOMAIN = TABLE_HEADER + "/*//span[contains(text(),'Domain')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_IP_ADDRESS = TABLE_HEADER + "/*//span[contains(text(),'IP Address')]"
    HEADER_SITE = TABLE_HEADER + "/*//span[contains(text(),'Site')]"
    CELL_DEVICE_NAME = "/td[1]"
    CELL_DOMAIN = "/td[3]"
    CELL_IP_ADDRESS = "/td[5]"
    CELL_SITE = "/td[7]"
    CELL_SERVER = "/td[9]"
    CELL_OS_VERSION = "/td[11]"
    CELL_DATE_DISCOVERED = "/td[13]"

    def check_screen_is_present(self):
        cond = self._is_element_present(DynamicallyManagedScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(DynamicallyManagedScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(DynamicallyManagedScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(DynamicallyManagedScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_present(self, name):
        row = DynamicallyManagedScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(DynamicallyManagedScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = DynamicallyManagedScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class UnmanagedDevicesScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Unmanaged Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_DEVICE_NAME = TABLE_HEADER + "/*//span[contains(text(),'Device Name')]"
    HEADER_DOMAIN = TABLE_HEADER + "/*//span[contains(text(),'Domain')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_IP_ADDRESS = TABLE_HEADER + "/*//span[contains(text(),'IP Address')]"
    HEADER_SITE = TABLE_HEADER + "/*//span[contains(text(),'Site')]"
    CELL_DEVICE_NAME = "/td[1]"
    CELL_DOMAIN = "/td[3]"
    CELL_IP_ADDRESS = "/td[5]"
    CELL_SITE = "/td[7]"
    CELL_SERVER = "/td[9]"
    CELL_OS_VERSION = "/td[11]"
    CELL_DATE_DISCOVERED = "/td[13]"

    def check_screen_is_present(self):
        cond = self._is_element_present(UnmanagedDevicesScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(UnmanagedDevicesScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(UnmanagedDevicesScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(UnmanagedDevicesScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_present(self, name):
        row = UnmanagedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(UnmanagedDevicesScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = UnmanagedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class ExcludedDevicesScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Excluded Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_DEVICE_NAME = TABLE_HEADER + "/*//span[contains(text(),'Device Name')]"
    HEADER_DOMAIN = TABLE_HEADER + "/*//span[contains(text(),'Domain')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_IP_ADDRESS = TABLE_HEADER + "/*//span[contains(text(),'IP Address')]"
    HEADER_SITE = TABLE_HEADER + "/*//span[contains(text(),'Site')]"
    CELL_DEVICE_NAME = "/td[1]"
    CELL_DOMAIN = "/td[3]"
    CELL_IP_ADDRESS = "/td[5]"
    CELL_SITE = "/td[7]"
    CELL_SERVER = "/td[9]"
    CELL_OS_VERSION = "/td[11]"
    CELL_DATE_DISCOVERED = "/td[13]"

    def check_screen_is_present(self):
        cond = self._is_element_present(ExcludedDevicesScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(ExcludedDevicesScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(ExcludedDevicesScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(ExcludedDevicesScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_present(self, name):
        row = ExcludedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ExcludedDevicesScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = ExcludedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class InfrastructureScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Infrastructure']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_DEVICE_NAME = TABLE_HEADER + "/*//span[contains(text(),'Device Name')]"
    HEADER_DOMAIN = TABLE_HEADER + "/*//span[contains(text(),'Domain')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_IP_ADDRESS = TABLE_HEADER + "/*//span[contains(text(),'IP Address')]"
    HEADER_SITE = TABLE_HEADER + "/*//span[contains(text(),'Site')]"
    CELL_DEVICE_NAME = "/td[1]"
    CELL_DOMAIN = "/td[3]"
    CELL_IP_ADDRESS = "/td[5]"
    CELL_SITE = "/td[7]"
    CELL_SERVER = "/td[9]"
    CELL_OS_VERSION = "/td[11]"
    CELL_DATE_DISCOVERED = "/td[13]"

    def check_screen_is_present(self):
        cond = self._is_element_present(InfrastructureScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(InfrastructureScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(InfrastructureScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(InfrastructureScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_present(self, name):
        row = InfrastructureScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(InfrastructureScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = InfrastructureScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class SiteConfigurationScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Site Configuration']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    HEADER_SITE = TABLE_HEADER + "/*//span[contains(text(),'Site')]"
    HEADER_IP_START = TABLE_HEADER + "/*//span[contains(text(),'IP Start')]"
    HEADER_IP_END = TABLE_HEADER + "/*//span[contains(text(),'IP End')]"
    HEADER_IS_EXCLUDED = TABLE_HEADER + "/*//span[contains(text(),'Excluded')]"
    CELL_SITE = "/td[1]"
    CELL_IP_START = "/td[3]"
    CELL_IP_END = "/td[5]"
    CELL_IS_EXCLUDED = "/td[7]"

    def check_screen_is_present(self):
        cond = self._is_element_present(SiteConfigurationScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(SiteConfigurationScreen.SCREEN_HEADER)

    def check_site_is_present(self, name):
        row = SiteConfigurationScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SiteConfigurationScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Site Management")
        return True if cond else False

    def select_site_in_table(self, name):
        row = SiteConfigurationScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class EventLogsScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Event Logs']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    ROW1 = SCREEN_HEADER + "//*[contains(@id,'HEADER')]/*//td[1]/following::*[contains(@id,'BODY')]/table/tbody/tr/td[1]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    HEADER_LOG_DATE = TABLE_HEADER + "/*//span[contains(text(),'Log Date')]"
    HEADER_COMPONENT = TABLE_HEADER + "/*//span[contains(text(),'Component')]"
    HEADER_DEVICE_NAME = TABLE_HEADER + "/*//span[contains(text(),'Device Name')]"
    HEADER_MESSAGE = TABLE_HEADER + "/*//span[contains(text(),'Message')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_LOG_DATE = "/td[1]"
    CELL_COMPONENT = "/td[3]"
    CELL_DEVICE_NAME = "/td[5]"
    CELL_IS_MESSAGE = "/td[7]"

    def check_screen_is_present(self):
        cond = self._is_element_present(EventLogsScreen.SCREEN_HEADER)
        return True if cond else False

    def check_event_log_is_present(self, name):
        row = EventLogsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(EventLogsScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Logs")
        return True if cond else False

    def select_event_log_in_table(self, name):
        row = EventLogsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class ColumnSetsScreen(BaseActions):

    SCREEN_HEADER = "//span[contains(text(),'Column Sets')]/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    HEADER_IS_DEFAULT = TABLE_HEADER + "/*//span[contains(text(),'Is Default')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_DESCRIPTION = TABLE_HEADER + "/*//span[contains(text(),'Description')]"
    HEADER_COLUMNS = TABLE_HEADER + "/*//span[contains(text(),'Columns')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_IS_DEFAULT = "/td[1]" #NOT CORRECT
    CELL_NAME = "/td[3]"
    CELL_DESCRIPTION = "/td[5]"
    CELL_IS_COLUMNS = "/td[7]"

    def check_screen_is_present(self):
        cond = self._is_element_present(ColumnSetsScreen.SCREEN_HEADER)
        return True if cond else False

    def check_column_set_is_present(self, name):
        row = ColumnSetsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(ColumnSetsScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Column Sets")
        return True if cond else False

    def select_column_set_in_table(self, name):
        row = ColumnSetsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class UsersScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Users']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_USERNAME = TABLE_HEADER + "/*//span[contains(text(),'Username')]"
    HEADER_TYPE = TABLE_HEADER + "/*//span[contains(text(),'Type')]"
    HEADER_CURRENCY =  TABLE_HEADER + "/*//span[contains(text(),'Currency')]"
    HEADER_PERMISSIONS = TABLE_HEADER + "/*//span[contains(text(),'Permissions')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_USERNAME = "/td[1]"
    CELL_TYPE = "/td[3]"
    CELL_CURRENCY = "/td[5]"
    CELL_PERMISSIONS = "/td[7]"

    def check_screen_is_present(self):
        cond = self._is_element_present(UsersScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(UsersScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(UsersScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(UsersScreen.SEARCH_FIELD).send_keys(text)

    def check_user_is_present(self, name):
        row = UsersScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(UsersScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("User Management")
        return True if cond else False

    def select_user_in_table(self, name):
        row = UsersScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class InventoryConfigurationScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='Inventory Configuration']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_INVENTORY_TEMPLATE = TABLE_HEADER + "/*//span[contains(text(),'Inventory')]"
    HEADER_FREQUENCY = TABLE_HEADER + "/*//span[contains(text(),'Frequency')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_INVENTORY_TEMPLATE = "/td[1]"
    CELL_FREQUENCY = "/td[3]"

    def check_screen_is_present(self):
        cond = self._is_element_present(InventoryConfigurationScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_search(self):
        self._click_icon_search(InventoryConfigurationScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(InventoryConfigurationScreen.SEARCH_FIELD).send_keys(text)

    def check_inventory_is_present(self, name):
        row = InventoryConfigurationScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(InventoryConfigurationScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Inventory Scan Configuration")
        return True if cond else False

    def select_inventory_in_table(self, name):
        row = InventoryConfigurationScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class VRepsScreen(BaseActions):

    SCREEN_HEADER = "//span[text()='vReps']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_IS_APPROVED = TABLE_HEADER + "/*//span[contains(text(),'Is approved')]"
    HEADER_IS_CONNECTED = TABLE_HEADER + "/*//span[contains(text(),'Is connected')]"
    HEADER_IS_ONLINE = TABLE_HEADER + "/*//span[contains(text(),'Is online')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_IP_ADDRESS = TABLE_HEADER + "/*//span[contains(text(),'IP Address')]"
    HEADER_LOCATION = TABLE_HEADER + "/*//span[contains(text(),'Location')]"
    CELL_CHECKBOX = "/td[1]"
    CELL_IS_APPROVED = "/td[3]"
    CELL_IS_CONNECTED = "/td[5]"
    CELL_IS_ONLINE = "/td[7]"
    CELL_NAME = "/td[9]"
    CELL_IP_ADDRESS = "/td[11]"
    CELL_LOCATION = "/td[13]"
    ROW_CHECK_BOX = "/td[1]/img[@class='ListView-CheckBoxImage']"
    TRUE = "/*//span[text()='true']"
    FALSE = "/*//span[text()='false']"

    def check_screen_is_present(self):
        cond = self._is_element_present(VRepsScreen.SCREEN_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(VRepsScreen.SCREEN_HEADER)
        time.sleep(3)

    def click_icon_search(self):
        self._click_icon_search(VRepsScreen.SCREEN_HEADER)
        time.sleep(3)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(VRepsScreen.SEARCH_FIELD).send_keys(text)

    def check_vrep_is_present(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(VRepsScreen.SCREEN_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("vReps")
        return True if cond else False

    def upprove_vreps_in_vreps_page_table(self, *names):
        for name in list(*names):
            row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            cond = self.check_vrep_is_present(name)
            if cond:
                self.select_vrep_in_table(name)
                checked = self._is_element_checked(row + self.ROW_CHECK_BOX)
                if checked:
                    pass
                else:
                    self._click_element(row + VRepsScreen.ROW_CHECK_BOX)
                    self._wait_for_element_checked(row + VRepsScreen.ROW_CHECK_BOX)
                    print "vRep is checked: ", name
                    cond1 = self.check_vrep_is_approved(name)
                    cond2 = self.check_vrep_is_connected(name)
                    cond3 = self.check_vrep_is_online_and_ready(name)
                    if cond1 and cond2 and cond3:
                        print "vRep " + name + " is online, connected and approved"
                    elif cond1 is not True:
                        print "vRep" + name + " is NOT approved"
                    elif cond2 is not True:
                        print "vRep" + name + " is NOT connected"
                    elif cond3 is not True:
                        print "vRep" + name + " is NOT online and ready"

    def upprove_single_vrep_in_vreps_page_table(self, name):
        try:
            row = self.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
            checkbox = row + self.ROW_CHECK_BOX
            self.click_icon_refresh()
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            self._wait_for_element_present(row)
            cond = self.check_vrep_is_present(name)
            if cond:
                self.select_vrep_in_table(name)
                self.click_icon_refresh()
                self.scroll_to_element(checkbox)
                self._wait_for_element_present(checkbox)
                unchecked = self._is_element_not_present(checkbox + "[contains(@src,'CheckBox1')]")
                # print checkbox + BaseActions.CHECKED + " is " + str(unchecked)
                if unchecked:
                    self.logger.info("vRep " + str(name) + " needs to be upproved" )
                    self._click_element(checkbox)
                    self.click_icon_refresh()
                    self._wait_for_element_present(checkbox + "[contains(@src,'CheckBox1')]")
                else:
                    pass
            cond1 = self.check_vrep_is_approved(name)
            cond2 = self.check_vrep_is_connected(name)
            cond3 = self.check_vrep_is_online_and_ready(name)
            cond4 = self._is_element_present(checkbox + "[contains(@src,'CheckBox1')]")
            if cond1 and cond2 and cond3 and cond4:
                self.logger.info("vRep " + str(name) + " is checked, online, connected and approved\n")
            elif cond1 is not True:
                self.logger.error("vRep " + str(name) + " is NOT approved\n")
            elif cond2 is not True:
                self.logger.error("vRep " + str(name) + " is NOT connected\n")
            elif cond3 is not True:
                self.logger.error("vRep " + str(name) + " is NOT online and ready\n")
            elif cond4 is not True:
                self.logger.error("vRep " + str(name) + " is NOT checked\n")
        except Exception as e:
            self.logger.error("Method 'Upprove a single vrep' is failed\n", str(e))

    def select_vrep_in_table(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)

    def check_vrep_is_approved(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row + VRepsScreen.CELL_IS_APPROVED + VRepsScreen.TRUE)
        return True if cond else False

    def check_vrep_is_connected(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row + VRepsScreen.CELL_IS_CONNECTED + VRepsScreen.TRUE)
        return True if cond else False

    def check_vrep_is_online_and_ready(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row + VRepsScreen.CELL_IS_ONLINE + VRepsScreen.TRUE)
        return True if cond else False

    def check_vrep_ready_for_work(self, name):
        cond1 = self.check_vrep_is_approved(name)
        cond2 = self.check_vrep_is_connected(name)
        cond3 = self.check_vrep_is_online_and_ready(name)
        return True if cond1 and cond2 and cond3 else False


class MaintenanceWindowsScreen(BaseScreen):

    MAINTENANCE_WINDOWS = "Maintenance Windows"

    def screen_name(self):
        screen = self._set_screen(self.MAINTENANCE_WINDOWS)
        return str(screen)

    def screen_table_header(self):
        table_header = self._set_screen_table_header(self.screen_name())
        return str(table_header)

    def screen_table_body(self):
        table_body = self._set_screen_table_body(self.screen_name())
        return str(table_body)
        
    def get_all_table_header_names(self):
        current_headers = self._get_all_table_header_names(self.screen_table_header())
        return current_headers

    def click_icon_help(self):
        self._click_icon_help(self.screen_name())

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Maintenance Windows")
        return True if cond else False

    def select_maintenance_window_in_table(self, name):
        row = self.screen_table_body() + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)

    def check_screen_is_present(self):
        cond = self._is_element_present(self.screen_name())
        msg_true = "Screen " + self.MAINTENANCE_WINDOWS + " is opened"
        msg_false = "Screen " + self.MAINTENANCE_WINDOWS + " is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_maintenance_window_is_present(self, name):
        row = self.screen_table_body() + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        msg_true = "Maintenance window " + str(name) + " is present"
        msg_false = "Maintenance window " + str(name) + " is NOT present"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False


class NotificationsScreen(BaseScreen):

    NOTIFICATIONS = "Notifications"

    def screen_name(self):
        screen = self._set_screen(self.NOTIFICATIONS)
        return str(screen)

    def check_screen_is_present(self):
        cond = self._is_element_present(self.screen_name())
        msg_true = "Screen " + self.NOTIFICATIONS + " is opened"
        msg_false = "Screen " + self.NOTIFICATIONS + " is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_name())


class SoftwareAndPatchManagerScreen(BaseScreen):

    SOFTWARE_AND_PATCH_MANAGER = "Software / Patch Manager"

    def screen_name(self):
        screen = self._set_screen(self.SOFTWARE_AND_PATCH_MANAGER)
        return str(screen)

    def check_screen_is_present(self):
        cond = self._is_element_present(self.screen_name())
        msg_true = "Screen " + self.SOFTWARE_AND_PATCH_MANAGER + " is opened"
        msg_false = "Screen " + self.SOFTWARE_AND_PATCH_MANAGER + " is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_name())


class TasksScreen(BaseScreen):

    TASKS = "Tasks"

    def screen_name(self):
        screen = self._set_screen(self.TASKS)
        return str(screen)

    def check_screen_is_present(self):
        cond = self._is_element_present(self.screen_name())
        msg_true = "Screen " + self.TASKS + " is opened"
        msg_false = "Screen " + self.TASKS + " is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_name())


class ReportingScreen(BaseScreen):

    REPORTING = "Reporting"

    def screen_software_and_patch_manager(self):
        screen = self._set_screen(self.REPORTING)
        return str(screen)

    def check_screen_is_present(self):
        cond = self._is_element_present(self.screen_software_and_patch_manager())
        msg_true = "Screen " + self.REPORTING + " is opened"
        msg_false = "Screen " + self.REPORTING + " is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_software_and_patch_manager())


class AuditLogScreen(BaseScreen):

    AUDIT_LOG = "Audit Log"

    TABLE_ROW = "/*//tr"
    SEARCH_FIELD = "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def screen_body(self):
        screen = self._set_screen(self.AUDIT_LOG)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_present(self):
        cond = self._is_element_present(self.screen_body())
        msg_true = "Screen " + self.AUDIT_LOG + " is opened"
        msg_false = "Screen " + self.AUDIT_LOG + " is NOT opened"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_body())

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(AuditLogScreen.SEARCH_FIELD).send_keys(text)

    def check_audit_log_is_present(self, name):
        row = AuditLogScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def select_audit_log_in_table(self, name):
        row = AuditLogScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)