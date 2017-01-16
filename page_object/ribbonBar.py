from base import Base
from locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from popups import *

class RibbonBar(Base):

    #CONSTANTS
    BUTTONS_BOX_DISPLAY = Locators.BUTTONS_BOX_DISPLAY
    TAB_VIEW = Locators.TAB_VIEW
    BUTTON_EDIT_OR_CREATE = Locators.BTN_EDIT_OR_CREATE

    # def click_tab_view(self):
    #     self.click_element(self.TAB_VIEW)
    #     self.wait_for_element_selected(self.TAB_VIEW)
    #     self.wait_for_element_present(self.BUTTONS_BOX_DISPLAY)

    def click_ribbon_bar_tab_view(self):
        self.click_element(self.TAB_VIEW)
        self.is_element_selected(self.TAB_VIEW)
        self.is_element_present(self.BUTTONS_BOX_DISPLAY)

    def click_button_edit_or_create(self):
        self.click_element(self.BUTTON_EDIT_OR_CREATE)
        self.wait_for_element_present(Locators.POPUP_COLUMN_SETS)

    def click_button_new_site(self):
        self.click_element(Locators.BTN_NEW_SITE)
        self.wait_for_element_present(Locators.POPUP_SITE_NAME)

    def click_delete_button(self):
        self.click_element(Locators.BTN_DELETE)
        cond = self.wait_for_element_present(Locators.POPUP)
        if cond:
            self.is_element_present(AreYouSurePopup.POPUP_ARE_YOU_SURE)
        else:
            self.is_element_present(UnableToRemovePopup.POPUP_UNABLE_TO_REMOVE)

    def click_button_config(self):
        self.click_element(Locators.BTN_CONFIG)
        self.wait_for_element_present(Locators.POPUP_CONFIGURATION)

