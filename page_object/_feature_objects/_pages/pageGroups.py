
from _base_page.base_actions import BaseActions
from _feature_objects._popups.popupAreYouSure import AreYouSurePopup
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class GroupsPage(BaseActions):

    PAGE_HEADER = "//span[text()='Groups']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = PAGE_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"

    def check_page_is_present(self):
        cond = self._is_element_present(GroupsPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(GroupsPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Groups")
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(GroupsPage.PAGE_HEADER)

    def click_icon_search(self):
        self._click_icon_search(GroupsPage.PAGE_HEADER)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(self.SEARCH_FIELD).send_keys(text)

    def check_group_is_present(self, name):
        cond = self._is_element_present(GroupsPage.TABLE_ROW + "/*//span[text()='" + str(name) + "']/ancestor::tr")
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
        self.wait_for_element_present(GroupsPage.TABLE_ROW)
        row = GroupsPage.TABLE_ROW + "/*//span[text()='" + str(*name) + "']/ancestor::tr"
        self._click_element(row)
        self.wait_for_element_selected(row)



