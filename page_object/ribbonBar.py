from base import Base
from locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class RibbonBar(Base):


    def click_view_tab(self):
        self.click_element(Locators.TAB_VIEW)
        cond1 = self.is_element_selected(Locators.TAB_VIEW)
        cond2 = self.is_element_present(Locators.BUTTONS_BOX_DISPLAY)
        return True if cond1 and cond2 else False

    def click_ribbon_bar_view_tab_edit_or_create_button(self):
        self.click_element(Locators.BTN_EDIT_OR_CREATE)
        cond = self.is_element_present(Locators.POPUP_COLUMN_SETS)
        return True if cond else False

