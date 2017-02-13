from _base_page.base_actions import BaseActions


class SoftwareAndPatchManagerPage(BaseActions):

    PAGE_HEADER = "//span[text()='Software / Patch Manager']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"

    def check_page_is_present(self):
        cond = self._is_element_present(SoftwareAndPatchManagerPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(SoftwareAndPatchManagerPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("Software / Patch Manager")
        return True if cond else False