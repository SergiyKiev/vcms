import time
from _base_page.base_actions import BaseActions
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class UsersPage(BaseActions):

    PAGE_HEADER = "//span[text()='Users']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    SEARCH_FIELD = PAGE_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_USERNAME = TABLE_HEADER + "/*//span[contains(text(),'Username')]"
    HEADER_TYPE = TABLE_HEADER + "/*//span[contains(text(),'Type')]"
    HEADER_CURRENCY =  TABLE_HEADER + "/*//span[contains(text(),'Currency')]"
    HEADER_PERMISSIONS = TABLE_HEADER + "/*//span[contains(text(),'Permissions')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    CELL_USERNAME = "/td[1]"
    CELL_TYPE = "/td[3]"
    CELL_CURRENCY = "/td[5]"
    CELL_PERMISSIONS = "/td[7]"

    def check_page_is_present(self):
        cond = self._is_element_present(UsersPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(UsersPage.PAGE_HEADER)

    def click_icon_search(self):
        self._click_icon_search(UsersPage.PAGE_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(UsersPage.SEARCH_FIELD).send_keys(text)

    def check_user_is_present(self, name):
        row = UsersPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(UsersPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("User Management")
        return True if cond else False

    def select_user_in_table(self, name):
        row = UsersPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)




