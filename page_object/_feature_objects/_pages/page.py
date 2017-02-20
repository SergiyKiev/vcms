from _base_page.base_actions import BaseActions


class MainPage(BaseActions):
    pass

    PAGE_HEADER = "//span[text()='Event Logs']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    TABLE_HEADER = "//*[@class='Common-Unselectable ListView-Control']/*[contains(@id,'HEADER')]"
    TABLE_BODY = "//*[@class='Common-Unselectable ListView-Control']/div/*[contains(@id,'VWGLVBODY')]"

    def _set_page(self, locator):
        pass

    def _get_all_columns_name(self):
        pass


