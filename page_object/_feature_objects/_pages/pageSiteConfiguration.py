import time
from _base_page.base_actions import BaseActions
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class SiteConfigurationPage(BaseActions):

    PAGE_HEADER = "//span[text()='Site Configuration']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
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

    def check_page_is_present(self):
        cond = self._is_element_present(SiteConfigurationPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(SiteConfigurationPage.PAGE_HEADER)

    def check_site_is_present(self, name):
        row = SiteConfigurationPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SiteConfigurationPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Site Management")
        return True if cond else False

    def select_site_in_table(self, name):
        row = SiteConfigurationPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)







