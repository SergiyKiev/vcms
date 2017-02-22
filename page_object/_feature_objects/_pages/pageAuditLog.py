
from _base_page.base_actions import BaseActions


class AuditLogPage(BaseActions):

    PAGE_HEADER = "//span[text()='Audit Log']/ancestor::div[@class='Panel-Control'][contains(@style,'78px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = PAGE_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_page_is_present(self):
        cond = self._is_element_present(AuditLogPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(AuditLogPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Audit Log")
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(AuditLogPage.PAGE_HEADER)

    def click_icon_search(self):
        self._click_icon_search(AuditLogPage.PAGE_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(AuditLogPage.SEARCH_FIELD).send_keys(text)

    def check_audit_log_is_present(self, name):
        row = AuditLogPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def select_audit_log_in_table(self, name):
        row = AuditLogPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)






