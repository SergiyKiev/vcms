from base import Base
from locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class RibbonBar(Base):

    #CONSTANTS
    BUTTONS_BOX_DISPLAY = Locators.BUTTONS_BOX_DISPLAY
    TAB_VIEW = Locators.TAB_VIEW
    BUTTON_EDIT_OR_CREATE = Locators.BTN_EDIT_OR_CREATE

    def click_tab_view(self):
        self.click_element(self.TAB_VIEW)
        self.wait_for_element_selected(self.TAB_VIEW)
        self.wait_for_element_present(self.BUTTONS_BOX_DISPLAY)

    def click_button_edit_or_create(self):
        self.click_element(self.BUTTON_EDIT_OR_CREATE)
        self.wait_for_element_present(Locators.POPUP_COLUMN_SETS)


