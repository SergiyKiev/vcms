
from _base_page.base_actions import BaseActions
from _feature_objects.popups import *


class RibbonBar(BaseActions):

    RIBBON_BAR_TAB_HEADER = "//div[@class='RibbonBarTabControl-HeadersRow']"
    RIBBON_BAR_TAB_PAGE = "//div[@class='RibbonBarTabControl-CenterFrame']"
    TAB_VIEW = "//span[text()='View']/ancestor::div[contains(@id,'TAB')]"
    TAB_HOME = "//span[text()='Home']/ancestor::div[contains(@id,'TAB')]"
    GROUP_BOX_DISPLAY = "//div[text()='Display'][contains(@class,'GroupBox-Text')]/ancestor::div[@class='RibbonBarGroupBox-Control']"
    GROUP_BOX_ACTIONS = "//div[text()='Actions'][contains(@class,'GroupBox-Text')]/ancestor::div[@class='RibbonBarGroupBox-Control']"
    BUTTON_EXIT = "//img[@alt='Exit']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_HOME = "//img[@alt='Home']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_NEW_SITE = "//img[@alt='New Site']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CONFIG = "//img[@alt='Config']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE = "//img[@alt='Delete']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SETTINGS = "//img[@alt='Settings']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CLIENT = "//img[@alt='Client']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SUBSCRIPTIONS = "//img[@alt='Subscriptions']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CONSOLE_GUIDE = "//img[@alt='Console Guide']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_ABOUT = "//img[@alt='About']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SAVE_CURRENT = "//img[@alt='Save Current Columns']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT_OR_CREATE = "//img[@alt='Edit/ Create']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE_OR_ARCHIVE = "//img[@alt='Delete / Archive']/ancestor::div[contains(@class,'RibbonBarButton')]"

    def click_tab_view(self):
        self._click_element(RibbonBar.TAB_VIEW)
        self.wait_for_element_selected(RibbonBar.TAB_VIEW)

    def click_tab_home(self):
        self._click_element(RibbonBar.TAB_HOME)
        self.wait_for_element_selected(RibbonBar.TAB_HOME)

    def click_button_edit_or_create(self):
        self._click_element(RibbonBar.BUTTON_EDIT_OR_CREATE)
        self.wait_for_element_present(ColumnSetsPopup.FRAME)

    def click_button_new_site(self):
        self._click_element(RibbonBar.BUTTON_NEW_SITE)
        self.wait_for_element_present(SiteNamePopup.FRAME)

    def click_button_delete(self):
        self._click_element(RibbonBar.BUTTON_DELETE)
        cond1 = self._is_element_present(AreYouSurePopup.FRAME)
        cond2 = self._is_element_present(UnableToRemovePopup.FRAME)
        if cond1:
            return AreYouSurePopup(self.driver)
        elif cond2:
            return UnableToRemovePopup(self.driver)
        else:
            return None

    def click_button_config(self):
        self._click_element(RibbonBar.BUTTON_CONFIG)
        self.wait_for_element_present(ConfigurationPopup.FRAME)

    def click_button_delete_or_archive(self):
        self._click_element(RibbonBar.BUTTON_DELETE_OR_ARCHIVE)
        self.wait_for_element_present(RemoveDevicesPopup.FRAME)


