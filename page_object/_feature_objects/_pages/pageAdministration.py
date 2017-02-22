from _base_page.base_actions import BaseActions
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class AdministrationPage(BaseActions):

    PAGE_HEADER = "//span[text()='Administration']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"

    def check_page_is_present(self):
        cond = self._is_element_present(AdministrationPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(AdministrationPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Administration")
        return True if cond else False

    def open_administration_page(self):
        cond = self._is_element_not_present(AdministrationPage.PAGE_HEADER)
        if cond:
            ribbon_bar = RibbonBar(self.driver)
            ribbon_bar.open_tab_home()
            ribbon_bar.click_button_home()
            ribbon_bar.click_go_to_home_screen_label()
            # self.check_page_is_present()
            # print "Administration home screen is opened ", result