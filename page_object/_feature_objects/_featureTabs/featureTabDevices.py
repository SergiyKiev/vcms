
from _base_page.base_actions import BaseActions


class HomeTab(BaseActions):

    TAB_HEADER = "//span[contains(text(),'Welcome To Cloud')]/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = TAB_HEADER + "/parent::div"

    def check_tab_is_present(self):
        cond = self._is_element_present(HomeTab.TAB_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(HomeTab.TAB_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Getting Started in CMS")
        return True if cond else False


class DevicesTab(BaseActions):

    TAB_HEADER = "//span[text()='Devices']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = TAB_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = TAB_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def select_device_in_table(self, *name):
        self.wait_for_element_present(DevicesTab.BODY)
        row = DevicesTab.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)

    def click_icon_refresh(self):
        self._click_icon_refresh(self.TAB_HEADER)

    def click_icon_search(self):
        self._click_icon_search(self.TAB_HEADER)

    def enter_text_into_search_field(self, text = None):
        self._find_element(self.SEARCH_FIELD).send_keys(text)

    def check_is_tab_present(self):
        try:
            cond = self._is_element_present(DevicesTab.BODY)
            return True if cond else False
        except Exception as e:
            print "Step failed: ", e

    def check_device_is_present(self, *name):
        cond = self._is_element_present(DevicesTab.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr")
        return True if cond else False

    def check_columns_are_present(self, columns_list):
        columnset = []
        for i in columns_list:
            elem = DevicesTab.TABLE_HEADER + "/*//span[contains(text(),'" + str(i) + "')]"
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
        self._click_icon_help(DevicesTab.TAB_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Devices")
        return True if cond else False


class AdministrationTab(BaseActions):

    TAB_HEADER = "//span[text()='Administration']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = TAB_HEADER + "/parent::div"

    def click_icon_help(self):
        self._click_icon_help(AdministrationTab.TAB_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Administration")
        return True if cond else False

class TasksTab(BaseActions):

    TAB_HEADER = "//span[text()='Tasks']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = TAB_HEADER + "/parent::div"

    def click_icon_help(self):
        self._click_icon_help(TasksTab.TAB_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Tasks")
        return True if cond else False


class ReportingTab(BaseActions):

    TAB_HEADER = "//span[text()='Reporting']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = TAB_HEADER + "/parent::div"

    def click_icon_help(self):
        self._click_icon_help(ReportingTab.TAB_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Reporting")
        return True if cond else False


class SoftwareAndPatchManagerTab(BaseActions):

    TAB_HEADER = "//span[text()='Software / Patch Manager']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = TAB_HEADER + "/parent::div"

    def click_icon_help(self):
        self._click_icon_help(SoftwareAndPatchManagerTab.TAB_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Software / Patch Manager")
        return True if cond else False