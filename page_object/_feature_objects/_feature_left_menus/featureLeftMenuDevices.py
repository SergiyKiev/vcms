from _base_page.base_actions import BaseActions
from _feature_objects._feature_left_menus.featureLeftMenu import LeftMenu


class LeftMenuDevices(BaseActions):

    BOX_GLOBAL_SITE_VIEW = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[1]"
    BOX_ACTIVE_DIRECTORIES = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[2]"
    BOX_QUERIES = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[3]"
    BOX_GROUPS = LeftMenu.MENU_DEVICES + "/*//div[contains(@class,'PaddingContainer')]/div[4]"
    TREE_GLOBAL_SITE_VIEW = BOX_GLOBAL_SITE_VIEW + "/div[contains(@class,'SubNodesContainer')]"
    TREE_ACTIVE_DIRECTORIES = BOX_ACTIVE_DIRECTORIES + "/div[contains(@class,'SubNodesContainer')]"
    TREE_QUERIES = BOX_QUERIES + "/div[contains(@class,'SubNodesContainer')]"
    TREE_GROUPS = BOX_GROUPS + "/div[contains(@class,'SubNodesContainer')]"
    LABEL_GLOBAL_SITE_VIEW = BOX_GLOBAL_SITE_VIEW + "/div[contains(@class,'RowContainer')]"
    LABEL_ACTIVE_DIRECTORIES = BOX_ACTIVE_DIRECTORIES + "/div[contains(@class,'RowContainer')]"
    LABEL_QUERIES = BOX_QUERIES + "/div[contains(@class,'RowContainer')]"
    LABEL_GROUPS = BOX_GROUPS + "/div[contains(@class,'RowContainer')]"
    LABEL_DEFAULT_SITE = TREE_GLOBAL_SITE_VIEW \
                         + "/div/div/*//span[text()='Default Site']/ancestor::div[contains(@class,'RowContainer')]"

    def click_global_site_view_label(self):
        self._click_element(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)

    def click_subsite_in_site_tree(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        element = LeftMenuDevices.TREE_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        self._click_element(element)
        self.wait_for_element_selected(element)

    def check_subsite_is_in_parent_site(self, sitename, subsitename):
        site_name = "//span[text()='" + sitename + "']/ancestor::" + LeftMenu.LABEL
        subsite_name = "//span[text()='" + subsitename + "']/ancestor::" + LeftMenu.LABEL
        element = LeftMenuDevices.TREE_GLOBAL_SITE_VIEW + site_name + "/parent::div/div[2]/*" + subsite_name
        cond = self._is_element_present(element)
        return True if cond else False

    def check_site_is_in_global_site_view_tree(self, sitename):
        cond = self._is_element_present(LeftMenuDevices.TREE_GLOBAL_SITE_VIEW + "/*//span[text()='" + sitename + "']")
        return True if cond else False

    def check_default_site_is_in_global_site_view_tree(self):
        cond = self._is_element_present(LeftMenuDevices.LABEL_DEFAULT_SITE)
        return True if cond else False

    def expand_global_site_view_tree(self):
        self.wait_for_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        arrow_expand = self._is_element_present(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW + "/div[contains(@style,'LTR1.gif')]")
        if arrow_expand:
            self._expand_tree(LeftMenuDevices.LABEL_GLOBAL_SITE_VIEW)
        else:
            pass

    def click_default_site_in_global_site_view(self):
        self._click_element(LeftMenuDevices.LABEL_DEFAULT_SITE)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_DEFAULT_SITE)

    def click_site_in_global_site_view_tree(self, sitename):
        element = LeftMenuDevices.TREE_GLOBAL_SITE_VIEW \
                  + "/*//span[text()='" + sitename + "']/ancestor::div[contains(@class,'RowContainer')]"
        self._click_element(element)
        self.wait_for_element_selected(element)

    def click_active_directories_label(self):
        self._click_element(LeftMenuDevices.LABEL_ACTIVE_DIRECTORIES)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_ACTIVE_DIRECTORIES)

    def click_queries_label(self):
        self._click_element(LeftMenuDevices.LABEL_QUERIES)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_QUERIES)

    def click_groups_label(self):
        self._click_element(LeftMenuDevices.LABEL_GROUPS)
        self.wait_for_element_selected(LeftMenuDevices.LABEL_GROUPS)