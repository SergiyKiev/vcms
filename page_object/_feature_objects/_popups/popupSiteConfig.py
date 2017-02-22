import time
from _base_page.base_actions import BaseActions
from _base_page.base_elements import BaseElements
from _feature_objects._popups.popupIPAddress import IPAddressPopup
from _feature_objects._popups.popupMoveSite import MoveSitePopup
from _feature_objects._popups.popupSiteName import SiteNamePopup


class SiteConfigPopup(BaseActions):

    BODY = "//span[text()='Site Config'][@dir='LTR']/ancestor::div[contains(@id,'WRP')]"
    LEFT_TREE_VIEW = BODY + "/*//div[@class='TreeView-PaddingContainer']/div"
    LIST_GLOBAL_SITE_VIEW = LEFT_TREE_VIEW + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_GLOBAL_SITE_VIEW = LEFT_TREE_VIEW + "/div[contains(@class,'RowContainer')]"
    LABEL_DEFAULT_SITE = LIST_GLOBAL_SITE_VIEW \
                         + "/div/div/*//span[text()='Default Site']/ancestor::div[contains(@class,'RowContainer')]"
    BUTTON_ADD_IP_RANGE = BODY + "/*//img[@alt='Add IP Range']/ancestor::div[contains(@class,'Button')]"
    BUTTON_ADD_SITE = BODY + "/*//img[@alt='Add Site']/ancestor::div[contains(@class,'Button')]"
    BUTTON_EDIT = BODY + "/*//img[@alt='Edit']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE = BODY + "/*//img[@alt='Delete']/ancestor::div[contains(@class,'Button')]"
    BUTTON_MOVE_SITE = BODY + "/*//img[@alt='Move Site']/ancestor::div[contains(@class,'Button')]"

    def check_popup_is_present(self):
        cond = self._is_element_present(SiteConfigPopup.BODY)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SiteConfigPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Create")
        return True if cond else False

    def click_button_close(self):
        self._click_button_close(SiteConfigPopup.BODY)
        self._wait_for_element_not_present(SiteConfigPopup.BODY)

    def click_system_button_close(self):
        self._click_system_button_close(SiteConfigPopup.BODY)

    def click_button_add_ip_range(self):
        self._click_element(SiteConfigPopup.BUTTON_ADD_IP_RANGE)
        self._wait_for_element_present(IPAddressPopup.BODY)

    def click_button_add_site(self):
        self._click_element(SiteConfigPopup.BUTTON_ADD_SITE)
        self._wait_for_element_present(SiteNamePopup.BODY)

    def click_button_move_site(self):
        self._click_element(SiteConfigPopup.BUTTON_MOVE_SITE)
        self._wait_for_element_present(MoveSitePopup.BODY)

    def create_site_if_not_exists(self, sitename):
        self.scroll_to_element(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW)
        self.click_global_site_view_label()
        self.expand_global_site_view_tree()
        cond = self.check_site_is_in_global_site_view_tree(sitename)
        if cond is not True:
            site_name_popup = SiteNamePopup(self.driver)
            self.click_global_site_view_label()
            self.click_button_add_site()
            site_name_popup.enter_text_into_name_text_field(sitename)
            site_name_popup.click_button_ok()
        self.scroll_to_element(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW \
                  + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]")
        self.click_site_in_global_site_view_tree(sitename)

    def click_global_site_view_label(self):
        self.scroll_to_element(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW)
        self._click_element(SiteConfigPopup.LABEL_GLOBAL_SITE_VIEW)
        self._wait_for_element_selected(SiteConfigPopup.LABEL_GLOBAL_SITE_VIEW)

    # def click_subsite_in_site_tree(self, sitename, subsitename):
    #     site_name = SiteConfigPopup.BODY \
    #                 + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
    #     subsite_name = SiteConfigPopup.BODY + \
    #                    "/*//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
    #     element = SiteConfigPopup.LIST_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
    #     self._click_element(element)
    #     self._wait_for_element_selected(element)

    def expand_global_site_view_tree(self):
        arrow = self._is_element_present(SiteConfigPopup.LABEL_GLOBAL_SITE_VIEW + BaseElements.ARROW_EXPAND)
        if arrow:
            self._expand_tree(SiteConfigPopup.LABEL_GLOBAL_SITE_VIEW)

    def click_site_in_global_site_view_tree(self, sitename):
        element = SiteConfigPopup.LIST_GLOBAL_SITE_VIEW \
                  + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_ADD_IP_RANGE)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_EDIT)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_DELETE)
        self._wait_for_element_unabled(SiteConfigPopup.BUTTON_MOVE_SITE)

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self._is_element_present(SiteConfigPopup.LIST_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False
