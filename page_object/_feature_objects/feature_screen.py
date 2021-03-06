import time

from _base._settings.settings import Settings
from _base.base_actions import BaseActions
from _base.base_elements import BaseElements
from _feature_objects.feature_popup import AreYouSurePopup
from _feature_objects.feature_popup import RemoveDevicesPopup
from _feature_objects.feature_ribbon_bar import RibbonBar
from _test_suites._variables.variables import Variables


class BaseScreen(BaseActions):

    # def __init__(self, driver, base_url=Settings.baseUrl):
    #     super(BaseScreen, self).__init__(driver, base_url=Settings.baseUrl)
    #     self._set_screen_table_row = None

    def _set_screen_body(self, name):
        # locator = "//span[contains(text(),'" + str(name) + "')][@dir='LTR'][contains(@style,'White')]/ancestor::div[@class='Label-Control']" \
        #                 "[contains(@style,'White')]/parent::div/parent::div/parent::div/parent::div/parent::div"
        # locator = "//span[contains(text(),'" + str(name) + "')][@dir='LTR']/ancestor::div[@class='Panel-Control']" \
                                                # "/*//div[contains(@style,'opacity')]/parent::div/parent::div"
        locator = "//span[contains(text(),'" + str(name) + "')][@dir='LTR'][contains(@style,'White')]" \
                   "/ancestor::div[@class='Label-Control']/parent::div/parent::div/parent::div/parent::div/parent::div"
        return str(locator)

    def _set_screen_header(self, set_screen_method):
        locator = str(set_screen_method) + "/div[@class='Panel-Control']"
        return str(locator)

    def _set_screen_table_header(self, set_screen_method): #INPUT SCREEN METHOD FOR CURRENT SCREEN
        locator = str(set_screen_method) + BaseElements.TABLE_HEADER
        return str(locator)

    def _set_screen_table_body(self, set_screen_method):
        locator = str(set_screen_method) + BaseElements.TABLE_BODY
        return str(locator)

    def _set_screen_table_row(self, set_screen_table_body_method):
        locator = str(set_screen_table_body_method) + "/*//tr"
        return str(locator)

    def _set_screen_bottom_body(self, set_screen):
        locator = str(set_screen) + "/*//div[@data-vwgdocking='F']"
        return str(locator)

    def _set_row_sel(self, set_table_row):
        pass

    def _set_screen_search_field(self, set_screen_header):
        locator = str(set_screen_header) + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
        return str(locator)

    def _type_into_screen_header_search_field(self, set_screen_search_field, text=None):
        self._find_element(set_screen_search_field).send_keys(text)

    def _get_all_table_header_names(self, set_screen_table_header):
        header_names = {}
        index = 1
        elements = self._find_elements(str(set_screen_table_header) + "/*//tbody/tr/td/*//span")
        for element in elements:
            name = element.text
            print index
            # name = self._get_text(set_screen_table_header + "/*//tbody/tr/td/*//span")
            header_names[str(name)] = str(index)
            index += 2
        print header_names
        return header_names

    # def handler_home_screen(self, screen_name):
    #     cond = self._is_element_present(self._set_screen_body(screen_name))
    #     print "Handle Home screen ", cond
    #     if cond:
    #         left_menu = BaseLeftMenu(self.driver)
    #         left_menu.open_menu_home()


class HomeScreen(BaseScreen):

    WELCOME_TO_CLOUD_MANAGEMENT_SUITE = "Welcome To Cloud Management Suite"
    HOME = "Home"
    # BODY = "//span[@dir='LTR'][contains(text(),'Welcome To Cloud')]/ancestor::div[@class='Panel-Control'][@data-vwgdocking='T']//parent::div"
    # SCREEN_HEADER = BODY + "/div"
    # BODY = SCREEN_HEADER + "/parent::div"

    def screen_body(self):
        locator = self._set_screen_body(self.WELCOME_TO_CLOUD_MANAGEMENT_SUITE)
        return str(locator)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Left menu '" + self.HOME + "' is opened"
        msg_false = "Left menu '" + self.HOME + "' is NOT opened"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())


class DevicesScreen(BaseScreen):

    DEVICES = "Devices"

    def screen_body(self):
        screen = self._set_screen_body(self.DEVICES)
        return str(screen)

    def screen_header(self):
        screen_header = self._set_screen_header(self.screen_body())
        return str(screen_header)
    
    def screen_table_header(self):
        table_header = self._set_screen_table_header(self.screen_body())
        return str(table_header)

    def screen_table_body(self):
        table_body = self._set_screen_table_body(self.screen_body())
        return str(table_body)

    def screen_table_row(self):
        table_row = self._set_screen_table_row(self.screen_table_body())
        return str(table_row)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.DEVICES + "' is presented"
        msg_false = "Screen '" + self.DEVICES + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text=None):
        self._type_into_screen_header_search_field(self.screen_header(), text)

    def select_device_in_table(self, *name):
        self._wait_for_element_present(self.screen_table_row())
        table_row = self.screen_table_row() + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(table_row)
        self._wait_for_element_selected(table_row)
        self.scroll_to_element(table_row + "/td[1]")
        self._wait_for_element_present(RibbonBar.TAB_DEVICES)
        self._wait_for_element_present(RibbonBar.TAB_TOOLS)

    def check_device_is_presented(self, name=Variables.vrep):
        cond = self._wait_for_element_present(self.screen_table_row() + "/*//span[text()='" + str(name) + "']/ancestor::tr")
        msg_true = "Device '" + name + "' is presented"
        msg_false = "Device '" + name + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_columns_are_present(self, columns_list):
        columnset = []
        for i in columns_list:
            elem = self.screen_table_header() + "/*//span[contains(text(),'" + str(i) + "')]"
            cond = self._wait_for_element_present(elem)
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

    def check_help_link_is_correct(self):
        self._get_log_for_help_link("Devices")

    def delete_devices_in_devices_page_table(self, *names):
        try:
            for name in list(*names):
                self.enter_text_into_search_text_field(name)
                self.click_icon_search()
                cond = self.check_device_is_presented(name)
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
            cond = self.check_device_is_presented(name)
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


class GroupsScreen(BaseScreen):

    SCREEN_HEADER = "//span[text()='Groups']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = SCREEN_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = SCREEN_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"


    GROUPS = "Groups"

    def screen_body(self):
        screen = self._set_screen_body(self.GROUPS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.GROUPS + "' is presented"
        msg_false = "Screen '" + self.GROUPS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(GroupsScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(GroupsScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(self.SEARCH_FIELD).send_keys(text)

    def check_group_is_presented(self, name):
        cond = self._wait_for_element_present(GroupsScreen.TABLE_ROW + "/*//span[text()='" + str(name) + "']/ancestor::tr")
        return True if cond else False

    def delete_groups_in_groups_page_table(self, *names):
        for name in list(*names):
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            cond = self.check_group_is_presented(name)
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
        cond = self.check_group_is_presented(name)
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


class QueriesScreen(BaseScreen):

    TABLE_HEADER = "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    QUERIES = "Queries"

    def screen_body(self):
        screen = self._set_screen_body(self.QUERIES)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.QUERIES + "' is presented"
        msg_false = "Screen '" + self.QUERIES + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Queries")
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(self.SEARCH_FIELD).send_keys(text)

    def check_query_is_presented(self, name):
        cond = self._wait_for_element_present(QueriesScreen.TABLE_ROW +
                                              "/*//span[text()='" + str(name) + "']/ancestor::tr")
        return True if cond else False

    def delete_queries_in_queries_page_table(self, *names):
        for name in list(*names):
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            cond = self.check_query_is_presented(name)
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
        cond = self.check_query_is_presented(name)
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
        self._wait_for_element_present(self.screen_body() +  self.TABLE_ROW)
        row = self.screen_body() + self.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class AdministrationScreen(BaseScreen):

    ADMINISTRATION = "Administration"

    def screen_body(self):
        screen = self._set_screen_body(self.ADMINISTRATION)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.ADMINISTRATION + "' is presented"
        msg_false = "Screen '" + self.ADMINISTRATION + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def open_administration_screen(self):
        cond = self._is_element_not_present(self.screen_header())
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            ribbon_bar.open_tab_home()
            ribbon_bar.click_button_home()
            ribbon_bar.click_menu_item_go_to_home_screen()
            self._wait_for_element_present(self.screen_header())
            # self.check_screen_is_presented()
            # print "Administration home screen is present ", result


class EndpointManagementScreen(BaseScreen):

    ENDPOINT_MANAGEMENT = "Endpoint Management Summary"

    def screen_body(self):
        screen = self._set_screen_body(self.ENDPOINT_MANAGEMENT)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.ENDPOINT_MANAGEMENT + "' is presented"
        msg_false = "Screen '" + self.ENDPOINT_MANAGEMENT + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())


class DynamicallyManagedScreen(BaseScreen):

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

    DYNAMICALLY_MANAGED = "Dynamically Managed"

    def screen_body(self):
        screen = self._set_screen_body(self.DYNAMICALLY_MANAGED)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.DYNAMICALLY_MANAGED + "' is presented"
        msg_false = "Screen '" + self.DYNAMICALLY_MANAGED + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(DynamicallyManagedScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(DynamicallyManagedScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(DynamicallyManagedScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_presented(self, name):
        row = DynamicallyManagedScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = DynamicallyManagedScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class UnmanagedDevicesScreen(BaseScreen):

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

    UNMANAGED_DEVICES = "Unmanaged Devices"

    def screen_body(self):
        screen = self._set_screen_body(self.UNMANAGED_DEVICES)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.UNMANAGED_DEVICES + "' is presented"
        msg_false = "Screen '" + self.UNMANAGED_DEVICES + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text=None):
        self._find_element(UnmanagedDevicesScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_presented(self, name):
        row = UnmanagedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = UnmanagedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class ExcludedDevicesScreen(BaseScreen):

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

    EXCLUDED_DEVICES = "Excluded Devices"

    def screen_body(self):
        screen = self._set_screen_body(self.EXCLUDED_DEVICES)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.EXCLUDED_DEVICES + "' is presented"
        msg_false = "Screen '" + self.EXCLUDED_DEVICES + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(ExcludedDevicesScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(ExcludedDevicesScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(ExcludedDevicesScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_presented(self, name):
        row = ExcludedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = ExcludedDevicesScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class InfrastructureScreen(BaseScreen):

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

    INFRASTRUCTURE = "Infrastructure"

    def screen_body(self):
        screen = self._set_screen_body(self.INFRASTRUCTURE)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.INFRASTRUCTURE + "' is presented"
        msg_false = "Screen '" + self.INFRASTRUCTURE + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(InfrastructureScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(InfrastructureScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(InfrastructureScreen.SEARCH_FIELD).send_keys(text)

    def check_device_is_presented(self, name):
        row = InfrastructureScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Endpoint Management")
        return True if cond else False

    def select_device_in_table(self, name):
        row = InfrastructureScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class SiteConfigurationScreen(BaseScreen):

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

    SITE_CONFIGURATION = "Site Configuration"

    def screen_body(self):
        screen = self._set_screen_body(self.SITE_CONFIGURATION)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.SITE_CONFIGURATION + "' is presented"
        msg_false = "Screen '" + self.SITE_CONFIGURATION + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(SiteConfigurationScreen.SCREEN_HEADER)

    def check_site_is_presented(self, name):
        row = SiteConfigurationScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Site Management")
        return True if cond else False

    def select_site_in_table(self, name):
        row = SiteConfigurationScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class EventLogsScreen(BaseScreen):

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

    EVENT_LOGS = "Event Logs"

    def screen_body(self):
        screen = self._set_screen_body(self.EVENT_LOGS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.EVENT_LOGS + "' is presented"
        msg_false = "Screen '" + self.EVENT_LOGS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def check_event_log_is_presented(self, name):
        row = EventLogsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Logs")
        return True if cond else False

    def select_event_log_in_table(self, name):
        row = EventLogsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class ColumnSetsScreen(BaseScreen):

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

    COLUMN_SETS = "Column Sets"

    def screen_body(self):
        screen = self._set_screen_body(self.COLUMN_SETS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.COLUMN_SETS + "' is presented"
        msg_false = "Screen '" + self.COLUMN_SETS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def check_column_set_is_presented(self, name):
        row = ColumnSetsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Column Sets")
        return True if cond else False

    def select_column_set_in_table(self, name):
        row = ColumnSetsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class UsersScreen(BaseScreen):

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

    USERS = "Users"

    def screen_body(self):
        screen = self._set_screen_body(self.USERS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.USERS + "' is presented"
        msg_false = "Screen '" + self.USERS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(UsersScreen.SCREEN_HEADER)

    def click_icon_search(self):
        self._click_icon_search(UsersScreen.SCREEN_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(UsersScreen.SEARCH_FIELD).send_keys(text)

    def check_user_is_presented(self, name):
        row = UsersScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("User Management")
        return True if cond else False

    def select_user_in_table(self, name):
        row = UsersScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class InventoryConfigurationScreen(BaseScreen):

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

    INVENTORY_CONFIGURATION = "Inventory Configuration"

    def screen_body(self):
        screen = self._set_screen_body(self.INVENTORY_CONFIGURATION)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def screen_table_body(self):
        table_body = self._set_screen_table_body(self.screen_body())
        return str(table_body)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.INVENTORY_CONFIGURATION + "' is presented"
        msg_false = "Screen '" + self.INVENTORY_CONFIGURATION + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(InventoryConfigurationScreen.SEARCH_FIELD).send_keys(text)

    def check_inventory_is_presented(self, name):
        row = self.screen_table_body() + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def select_inventory_in_table(self, name):
        full_scan = self.screen_table_body() + "/*//span[text()='" + str(name) + "']/ancestor::td"
        self._click_element(full_scan)
        self._wait_for_element_selected(full_scan + "/parent::tr")

    def select_full_scan_inventory_in_table(self):
        self.select_inventory_in_table("Full Scan")


class VRepsScreen(BaseScreen):

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

    VREPS = "vReps"

    def screen_body(self):
        screen = self._set_screen_body(self.VREPS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def screen_table_header(self):
        table_header = self._set_screen_table_header(self.screen_body())
        return str(table_header)

    def screen_table_body(self):
        table_body = self._set_screen_table_body(self.screen_body())
        return str(table_body)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.VREPS + "' is presented"
        msg_false = "Screen '" + self.VREPS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(VRepsScreen.SCREEN_HEADER)
        time.sleep(3)

    def click_icon_search(self):
        self._click_icon_search(VRepsScreen.SCREEN_HEADER)
        time.sleep(3)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(VRepsScreen.SEARCH_FIELD).send_keys(text)

    def check_vrep_is_presented(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
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
            cond = self.check_vrep_is_presented(name)
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
            cond = self.check_vrep_is_presented(name)
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
        cond = self._wait_for_element_present(row + VRepsScreen.CELL_IS_APPROVED + VRepsScreen.TRUE)
        return True if cond else False

    def check_vrep_is_connected(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row + VRepsScreen.CELL_IS_CONNECTED + VRepsScreen.TRUE)
        return True if cond else False

    def check_vrep_is_online_and_ready(self, name):
        row = VRepsScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row + VRepsScreen.CELL_IS_ONLINE + VRepsScreen.TRUE)
        return True if cond else False

    def check_vrep_ready_for_work(self, name):
        cond1 = self.check_vrep_is_approved(name)
        cond2 = self.check_vrep_is_connected(name)
        cond3 = self.check_vrep_is_online_and_ready(name)
        return True if cond1 and cond2 and cond3 else False


class MaintenanceWindowsScreen(BaseScreen):

    MAINTENANCE_WINDOWS = "Maintenance Windows"

    def screen_body(self):
        screen = self._set_screen_body(self.MAINTENANCE_WINDOWS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def screen_table_header(self):
        table_header = self._set_screen_table_header(self.screen_body())
        return str(table_header)

    def screen_table_body(self):
        table_body = self._set_screen_table_body(self.screen_body())
        return str(table_body)
        
    def get_all_table_header_names(self):
        current_headers = self._get_all_table_header_names(self.screen_table_header())
        return current_headers

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Maintenance Windows")
        return True if cond else False

    def select_maintenance_window_in_table(self, name):
        row = self.screen_table_body() + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.MAINTENANCE_WINDOWS + "' is presented"
        msg_false = "Screen '" + self.MAINTENANCE_WINDOWS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_maintenance_window_is_presented(self, name):
        row = self.screen_table_body() + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        msg_true = "Maintenance window " + str(name) + "' is presented"
        msg_false = "Maintenance window " + str(name) + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False


class NotificationsScreen(BaseScreen):

    NOTIFICATIONS = "Notifications"

    def screen_body(self):
        screen = self._set_screen_body(self.NOTIFICATIONS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.NOTIFICATIONS + "' is presented"
        msg_false = "Screen '" + self.NOTIFICATIONS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())


class SoftwareAndPatchManagerScreen(BaseScreen):

    SOFTWARE_AND_PATCH_MANAGER = "Software / Patch Manager"

    def screen_body(self):
        screen = self._set_screen_body(self.SOFTWARE_AND_PATCH_MANAGER)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is presented"
        msg_false = "Screen '" + self.SOFTWARE_AND_PATCH_MANAGER + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())


class TasksScreen(BaseScreen):

    TASKS = "Tasks"
    TO_SCAN = "to scan"
    DISCOVERED = "discovered"
    UNKNOWN = "Unknown"
    SUCCESSFULLY = "Successfully"
    TO_BE_DONE = "To Be Done"
    FAILED_TO = "Failed To"
    PARTIALLY_PATCHED = "Partially Patched"
    DEVICES = "Devices"
    VIEW_SOFTWARE_UPDATE_DETAILS = "View Software Update Details"

    def screen_body(self):
        locator = self._set_screen_body(self.TASKS)
        return str(locator)

    def screen_header(self):
        locator = self._set_screen_header(self.screen_body())
        return str(locator)
    
    def screen_table_body(self):
        locator = self._set_screen_table_body(self.screen_body())
        return str(locator)

    def screen_bottom_body(self):
        locator = self._set_screen_bottom_body(self.screen_body())
        return str(locator)

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def enter_text_into_search_field(self, text):
        self._send_keys_and_enter(self.screen_header() + BaseElements.FIELD, text)

    def clear_text_search_text_field(self):
        self._find_element(self.screen_header() + BaseElements.FIELD).clear()

    def search_task(self, name):
        element = self.screen_table_body() + "/*//span[text()='" + name + "']"
        self.clear_text_search_text_field()
        self.enter_text_into_search_field(name)
        cond = self._is_element_present(element)
        return True if cond else False

    def clickable_label(self, name):
        locator = self.screen_bottom_body() + "/*//span[contains(text(),'" + name + "')]"
        return str(locator)

    def click_label_addresses_to_scan(self):
        self._click_element(self.clickable_label(self.TO_SCAN))

    def click_label_devices_discovered(self):
        self.scroll_to_element(self.clickable_label(self.DISCOVERED))
        self._click_element(self.clickable_label(self.DISCOVERED))

    def click_label_unknown_devices(self):
        self._click_element(self.clickable_label(self.UNKNOWN))

    def click_label_devices_successfully_scannned(self):
        self._click_element(self.clickable_label(self.SUCCESSFULLY))

    def click_label_devices_successfully_updated(self):
        self._click_element(self.clickable_label(self.SUCCESSFULLY))

    def click_label_devices_still_to_be_done(self):
        self._click_element(self.clickable_label(self.TO_BE_DONE))

    def click_label_devices_failed_to_patch(self):
        self._click_element(self.clickable_label(self.FAILED_TO))

    def click_label_devices_partially_patched(self):
        self._click_element(self.clickable_label(self.PARTIALLY_PATCHED))

    def click_task_in_table(self, name):
        element = self.screen_table_body() + "/*//span[text()='" + name + "']"
        self._click_element(element)
        self._wait_for_element_selected(element + "/ancestor::tr")

    def click_tab_devices(self):
        element = self.screen_body() + "/*//span[text()='" + self.DEVICES + "']/ancestor::div[contains(@id,'TAB')]"
        self._click_element(element)
        self._wait_for_element_selected(element)

    def click_device_in_table(self, device):
        element = self.screen_body() + "/*//div[contains(@id,'BODY')]/*//span[text()='" + device + "']"
        self._click_element(element)
        self._wait_for_element_selected(element + "/ancestor::tr")

    def click_button_view_software_update_details(self):
        element = self.screen_body() + "/*//span[contains(text(),'" \
                  + self.VIEW_SOFTWARE_UPDATE_DETAILS + "')]/ancestor::div[contains(@class,'Button')]"
        self._click_element(element)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.TASKS + "' is presented"
        msg_false = "Screen '" + self.TASKS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def check_task_is_presented(self, name):
        element = self.screen_table_body() + "/*//span[text()='" + name + "']"
        cond = self._wait_for_element_present(element)
        return True if cond else False

    def check_label_addresses_to_scan_is_presented(self):
        cond = self._wait_for_element_present(self.clickable_label(self.TO_SCAN))
        return True if cond else False

    def check_label_devices_discovered_is_presented(self):
        cond = self._wait_for_element_present(self.clickable_label(self.DISCOVERED))
        return True if cond else False

    def check_label_unknown_devices_is_presented(self):
        cond = self._wait_for_element_present(self.clickable_label(self.UNKNOWN))
        return True if cond else False

    def check_label_devices_successfully_scanned_is_presented(self):
        # self._resize_element()
        # self.scroll_to_element(self.clickable_label(self.SUCCESSFULLY))
        cond = self._wait_for_element_present(self.clickable_label(self.SUCCESSFULLY))
        return True if cond else False

    def check_label_devices_still_to_be_done_is_presented(self):
        # self._resize_element()
        # self.scroll_to_element(self.clickable_label(self.TO_BE_DONE))
        cond = self._wait_for_element_present(self.clickable_label(self.TO_BE_DONE))
        return True if cond else False

    def check_label_devices_failed_to_patch_is_presented(self):
        # self._resize_element()
        # self.scroll_to_element(self.clickable_label(self.FAILED_TO))
        cond = self._wait_for_element_present(self.clickable_label(self.FAILED_TO))
        return True if cond else False

    def check_label_devices_partially_patched_is_presented(self):
        # self._resize_element()
        # self.scroll_to_element(self.clickable_label(self.PARTIALLY_PATCHED))
        cond = self._wait_for_element_present(self.clickable_label(self.PARTIALLY_PATCHED))
        return True if cond else False

    def check_device_is_present_in_table(self, device):
        element= self.screen_body() + "/*//div[contains(@id,'BODY')]/*//span[text()='" + device + "']"
        cond = self._wait_for_element_present(element)
        return True if cond else False

    def check_button_view_software_update_is_presented(self):
        element = self.screen_body() + "/*//span[contains(text(),'" \
                  + self.VIEW_SOFTWARE_UPDATE_DETAILS + "')]/ancestor::div[contains(@class,'Button')]"
        cond = self._wait_for_element_present(element)
        return True if cond else False

    def check_tab_devices_is_presented(self):
        element = self.screen_body() + "/*//span[text()='" + self.DEVICES + "']/ancestor::div[contains(@id,'TAB')]"
        cond = self._wait_for_element_present(element)
        return True if cond else False


class ReportingScreen(BaseScreen):

    REPORTING = "Reporting"

    def screen_body(self):
        screen = self._set_screen_body(self.REPORTING)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_body())
        msg_true = "Screen '" + self.REPORTING + "' is presented"
        msg_false = "Screen '" + self.REPORTING + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())


class AuditLogScreen(BaseScreen):

    AUDIT_LOG = "Audit Log"
    TABLE_ROW = "/*//tr"
    SEARCH_FIELD = "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def screen_body(self):
        screen = self._set_screen_body(self.AUDIT_LOG)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        # print str(self.screen_header()) + " - " + str(cond)
        msg_true = "Screen '" + self.AUDIT_LOG + "' is presented"
        msg_false = "Screen '" + self.AUDIT_LOG + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(AuditLogScreen.SEARCH_FIELD).send_keys(text)

    def check_audit_log_is_presented(self, name):
        row = AuditLogScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def select_audit_log_in_table(self, name):
        row = AuditLogScreen.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)


class ApplicationsScreen(BaseScreen):

    APPLICATIONS = "Applications"
    SEARCH_FIELD = "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def screen_body(self):
        screen = self._set_screen_body(self.APPLICATIONS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.APPLICATIONS + "' is presented"
        msg_false = "Screen '" + self.APPLICATIONS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text = None):
        self._send_keys_and_enter(self.screen_body() + ApplicationsScreen.SEARCH_FIELD, text)
        # self._find_element(self.screen_body() + ApplicationsScreen.SEARCH_FIELD).send_keys(text)

    def check_application_is_presented(self, name):
        row = self.screen_body() + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(row)
        return True if cond else False

    def click_application_in_table(self, name):
        table_row = self.screen_body() + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(table_row)
        self._wait_for_element_selected(table_row)

    def select_application_in_table(self, *name):
        # self._wait_for_element_present(ApplicationsScreen.TABLE_ROW)
        table_row = self.screen_body() + "/*//tr/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self.enter_text_into_search_text_field(*name)
        # self.click_icon_search()
        cond = self._wait_for_element_present(table_row)
        if cond:
            self._click_element(table_row)
            self._wait_for_element_selected(table_row)
            self.scroll_to_element(table_row + "/td[1]")
            self._wait_for_element_enabled(RibbonBar.BUTTON_EDIT)
            self._wait_for_element_enabled(RibbonBar.BUTTON_DELETE)
            return True
        else:
            self.logger.error("Applilcation " + str(*name) + " is not found")
            return False


class PatchMangerScreen(BaseScreen):

    PATCH_MANAGER = "Patch Manager"
    SEARCH_FIELD = "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    FILTER_FIELD = "/*//input[contains(@class,'TextBox-Input')][@readonly]"

    def screen_body(self):
        screen = self._set_screen_body(self.PATCH_MANAGER)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.PATCH_MANAGER + "' is presented"
        msg_false = "Screen '" + self.PATCH_MANAGER + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_at_filter_field(self):
        self._click_element(self.screen_header() + self.FILTER_FIELD)

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(PatchMangerScreen.SEARCH_FIELD).send_keys(text)

    def click_first_row_in_table(self):
        table_row = self.screen_body() + "/*//tr[1]"
        self._click_element(table_row)

    def select_first_row_in_table(self):
        table_row = self.screen_body() + "/*//tr[1]"
        cond = self._wait_for_element_present(table_row)
        if cond:
            self.click_first_row_in_table()
            return True
        else:
            self.logger.info("NO rows in the " + self.PATCH_MANAGER + " table")
            return False

    def check_first_row_is_selected(self):
        table_row = self.screen_body() + "/*//tr[1]"
        cond = self._wait_for_element_selected(table_row)
        return True if cond else False

    def check_patch_is_presented(self, name):
        table_row = self.screen_body() + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(table_row)
        return True if cond else False

    def select_patch_in_table(self, name):
        table_row = self.screen_body() + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(table_row)
        self._wait_for_element_selected(table_row)


class ManageInstallMediaScreen(BaseScreen):

    MANAGE_INSTALL_MEDIA = "Manage Install Media"

    def screen_body(self):
        screen = self._set_screen_body(self.MANAGE_INSTALL_MEDIA)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.MANAGE_INSTALL_MEDIA + "' is presented"
        msg_false = "Screen '" + self.MANAGE_INSTALL_MEDIA + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def click_icon_refresh(self):
        self._click_icon_refresh(self.screen_header())

    def click_icon_search(self):
        self._click_icon_search(self.screen_header())

    def check_patch_or_software_is_presented(self, name):
        table_row = self.screen_body() + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._wait_for_element_present(table_row)
        return True if cond else False

    def select_patch_or_software_in_table(self, name):
        table_row = self.screen_body() + "/*//tr/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(table_row)
        self._wait_for_element_selected(table_row)


class MyDashboardsScreen(BaseScreen):

    MY_DASHBOARDS = "My Dashboards"

    def screen_body(self):
        screen = self._set_screen_body(self.MY_DASHBOARDS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.MY_DASHBOARDS + "' is presented"
        msg_false = "Screen '" + self.MY_DASHBOARDS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())


class MyReportsScreen(BaseScreen):

    MY_REPORTS = "My Reports"

    def screen_body(self):
        screen = self._set_screen_body(self.MY_REPORTS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.MY_REPORTS + "' is presented"
        msg_false = "Screen '" + self.MY_REPORTS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())


class SharedReportsScreen(BaseScreen):

    SHARED_REPORTS = "Shared Reports"

    def screen_body(self):
        screen = self._set_screen_body(self.SHARED_REPORTS)
        return str(screen)

    def screen_header(self):
        table_header = self._set_screen_header(self.screen_body())
        return str(table_header)

    def check_screen_is_presented(self):
        cond = self._wait_for_element_present(self.screen_header())
        msg_true = "Screen '" + self.SHARED_REPORTS + "' is presented"
        msg_false = "Screen '" + self.SHARED_REPORTS + "' is NOT present"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(self.screen_header())

    def select_single_report(self, name='Archive and Delete History'):
        element = self.screen_body() \
                  + "/*//div[@class='TabPage-Control_bj'][1]/*//span[contains(text(),'" + name + "')]"
        self._click_element(element)

    def check_report_is_presented(self, name='Archive and Delete History'):
        element = self.screen_body() \
                  + "/*//div[@class='TabPage-Control_bj'][1]/*//span[contains(text(),'" + name + "')]"
        cond = self._wait_for_element_present(element)
        return True if cond else False
