
from _feature_objects.featurePopupClientSettings import ClientSettingsPopup
from _feature_objects.featurePopupColumnSets import ColumnSetsPopup
from _feature_objects.featurePopupConfiguration import ConfigurationPopup
from _feature_objects.featurePopupMoveSite import MoveSitePopup
from _feature_objects.featurePopupRemoveDevices import RemoveDevicesPopup
from _feature_objects.featurePopupSelectDashboard import SelectDashboardPopup
from _feature_objects.featurePopupSettings import SettingsPopup
from _feature_objects.featurePopupSiteName import SiteNamePopup
from _feature_objects.featurePopupSubscriptions import SubscriptionsPopup
from _feature_objects.featurePopups import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException


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
    BUTTON_MOVE = "//img[@alt='Move']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SETTINGS = "//img[@alt='Settings']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CLIENT = "//img[@alt='Client']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SUBSCRIPTIONS = "//img[@alt='Subscriptions']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_CONSOLE_GUIDE = "//img[@alt='Console Guide']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_ABOUT = "//img[@alt='About']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_SAVE_CURRENT = "//img[@alt='Save Current Columns']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_EDIT_OR_CREATE = "//img[@alt='Edit/ Create']/ancestor::div[contains(@class,'RibbonBarButton')]"
    BUTTON_DELETE_OR_ARCHIVE = "//img[@alt='Delete / Archive']/ancestor::div[contains(@class,'RibbonBarButton')]"
    DROP_DOWN_ARROW_HOME = "//img[@alt='Home']/following::img[contains(@src,'DropDown')]"
    HOME_DROP_DOWN_LIST = BUTTON_HOME + "/following::div[@class='Menu-PopupWindow']"
    MENU_ITEM_GO_TO_HOME_SCREEN = HOME_DROP_DOWN_LIST \
                                  + "/*//span[contains(text(),'Go To')]/ancestor::div[contains(@class,'MenuItem-Control')]"
    MENU_ITEM_CHANGE_HOME_SCREEN = HOME_DROP_DOWN_LIST \
                                  + "/*//span[contains(text(),'Change Home')]/ancestor::div[contains(@class,'MenuItem-Control')]"


    def click_tab_view(self):
        self._click_element(self.TAB_VIEW)
        self.wait_for_element_selected(self.TAB_VIEW)

    def click_tab_home(self):
        self._click_element(self.TAB_HOME)
        self.wait_for_element_selected(self.TAB_HOME)

    def open_tab_home(self):
        try:
            self.wait_for_element_present(self.TAB_HOME)
            cond = self._is_element_selected(self.TAB_HOME)
            if cond:
                pass
            else:
                self.click_tab_home()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def open_tab_view(self):
        try:
            self.wait_for_element_present(self.TAB_VIEW)
            cond = self._is_element_selected(self.TAB_VIEW)
            if cond:
                pass
            else:
                self.click_tab_view()
        except (NoSuchElementException, TimeoutException):
            print "Object not found"

    def click_button_edit_or_create(self):
        self._click_element(self.BUTTON_EDIT_OR_CREATE)
        self.wait_for_element_present(ColumnSetsPopup.BODY)

    def click_button_new_site(self):
        self._click_element(self.BUTTON_NEW_SITE)
        self.wait_for_element_present(SiteNamePopup.BODY)

    def click_button_delete(self):
        cond = self._click_element(self.BUTTON_DELETE)
        print "Delete is:", cond
        # cond1 = self._is_element_present(AreYouSurePopup.BODY)
        # cond2 = self._is_element_present(UnableToRemovePopup.BODY)
        # if cond1:
        #     return AreYouSurePopup(self.driver)
        # elif cond2:
        #     return UnableToRemovePopup(self.driver)

    def click_button_config(self):
        self._click_element(self.BUTTON_CONFIG)
        self.wait_for_element_present(ConfigurationPopup.BODY)

    def click_button_move(self):
        self._click_element(self.BUTTON_MOVE)
        self.wait_for_element_present(MoveSitePopup.BODY)

    def click_button_delete_or_archive(self):
        self._click_element(self.BUTTON_DELETE_OR_ARCHIVE)
        self.wait_for_element_present(RemoveDevicesPopup.BODY)

    def check_button_new_site_is_present(self):
        cond = self._is_element_present(self.BUTTON_NEW_SITE)
        return True if cond else False

    def check_button_config_is_present(self):
        cond = self._is_element_present(self.BUTTON_CONFIG)
        return True if cond else False

    def check_button_exit_is_present(self):
        cond = self._is_element_present(self.BUTTON_EXIT)
        return True if cond else False

    def check_button_edit_or_create_is_present(self):
        cond = self._is_element_present(self.BUTTON_EDIT_OR_CREATE)
        return True if cond else False

    def check_button_delete_is_present(self):
        cond = self._is_element_present(self.BUTTON_DELETE)
        return True if cond else False

    def click_button_settings(self):
        self._click_element(self.BUTTON_SETTINGS)
        self.wait_for_element_present(SettingsPopup.BODY)

    def click_button_client(self):
        self._click_element(self.BUTTON_CLIENT)
        self.wait_for_element_present(ClientSettingsPopup.BODY)

    def click_button_subscriptions(self):
        self._click_element(self.BUTTON_SUBSCRIPTIONS)
        self.wait_for_element_present(SubscriptionsPopup.BODY)

    def click_button_console_guide(self):
        self._click_element(self.BUTTON_CONSOLE_GUIDE)

    def click_button_home(self):
        self._click_element(self.BUTTON_HOME)
        self.wait_for_element_present(self.HOME_DROP_DOWN_LIST)

    def click_change_home_screen_label(self):
        self._click_element(self.MENU_ITEM_CHANGE_HOME_SCREEN)
        self.wait_for_element_not_present(self.HOME_DROP_DOWN_LIST)
        self.wait_for_element_present(SelectDashboardPopup.BODY)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("CMS Quick Help Videos")
        return True if cond else False

    def check_tab_home_is_present(self):
        cond = self._is_element_present(self.GROUP_BOX_ACTIONS)
        return True if cond else False

    def check_tab_view_is_present(self):
        cond = self._is_element_present(self.GROUP_BOX_DISPLAY)
        return True if cond else False

    def check_home_drop_down_list_is_present(self):
        cond = self._is_element_present(self.HOME_DROP_DOWN_LIST)
        return True if cond else False



