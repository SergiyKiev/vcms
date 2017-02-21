import time
from _base_page.base_actions import BaseActions
from _feature_objects._ribbon_bar.ribbonBar import RibbonBar


class VRepsPage(BaseActions):

    PAGE_HEADER = "//span[text()='vReps']/ancestor::div[@class='Panel-Control'][contains(@style,'85px')]"
    BODY = PAGE_HEADER + "/parent::div"
    TABLE_HEADER = BODY + "/*//div[contains(@id,'HEADER')]"
    TABLE_BODY = BODY + "/*//div[contains(@id,'VWGLVBODY')]"
    TABLE_ROW = TABLE_BODY + "/*//tr"
    SEARCH_FIELD = PAGE_HEADER + "/*//input[contains(@class,'TextBox-Input')][@type='text']"
    HEADER_IS_APPROVED = TABLE_HEADER + "/*//span[contains(text(),'Is approved')]"
    HEADER_IS_CONNECTED = TABLE_HEADER + "/*//span[contains(text(),'Is connected')]"
    HEADER_IS_ONLINE = TABLE_HEADER + "/*//span[contains(text(),'Is online')]"
    HEADER_NAME = TABLE_HEADER + "/*//span[contains(text(),'Name')]"
    HEADER_IP_ADDRESS = TABLE_HEADER + "/*//span[contains(text(),'IP Address')]"
    HEADER_LOCATION = TABLE_HEADER + "/*//span[contains(text(),'Location')]"
    CELL_CHECKBOX = "/td[1]"
    CELL_IS_APPROVED = "/td[3]"
    CELL_IS_CONNECTED = "/td[5]"
    CELL_IS_ONLINE = "/td[7]"
    CELL_NAME = "/td[9]"
    CELL_IP_ADDRESS = "/td[11]"
    CELL_LOCATION = "/td[13]"
    ROW_CHECK_BOX = "/td[1]/img[@class='ListView-CheckBoxImage']"
    TRUE = "/*//span[text()='true']"
    FALSE = "/*//span[text()='false']"

    def check_page_is_present(self):
        cond = self._is_element_present(VRepsPage.PAGE_HEADER)
        return True if cond else False

    def click_icon_refresh(self):
        self._click_icon_refresh(VRepsPage.PAGE_HEADER)
        time.sleep(3)

    def click_icon_search(self):
        self._click_icon_search(VRepsPage.PAGE_HEADER)
        time.sleep(3)

    def enter_text_into_search_text_field(self, text = None):
        self._find_element(VRepsPage.SEARCH_FIELD).send_keys(text)

    def check_vrep_is_present(self, name):
        row = VRepsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row)
        return True if cond else False

    def click_icon_help(self):
        self._click_icon_help(VRepsPage.PAGE_HEADER)

    def check_help_link_is_correct(self):
        cond = self._check_help_frame_header("vReps")
        return True if cond else False

    def upprove_vreps_in_vreps_page_table(self, *names):
        for name in list(*names):
            row = VRepsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            cond = self.check_vrep_is_present(name)
            if cond:
                self.select_vrep_in_table(name)
                checked = self._is_element_checked(row + self.ROW_CHECK_BOX)
                if checked:
                    pass
                else:
                    self._click_element(row + VRepsPage.ROW_CHECK_BOX)
                    self._wait_for_element_checked(row + VRepsPage.ROW_CHECK_BOX)
                    print "vRep is checked: ", name
                    cond1 = self.check_vrep_is_approved(name)
                    cond2 = self.check_vrep_is_connected(name)
                    cond3 = self.check_vrep_is_online_and_ready(name)
                    if cond1 and cond2 and cond3:
                        print "vRep " + name + " is online, connected and approved"
                    elif cond1 is not True:
                        print "vRep" + name + " is NOT approved"
                    elif cond2 is not True:
                        print "vRep" + name + " is NOT connected"
                    elif cond3 is not True:
                        print "vRep" + name + " is NOT online and ready"

    def upprove_single_vrep_in_vreps_page_table(self, name):
        try:
            row = self.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
            checkbox = row + self.ROW_CHECK_BOX
            self.click_icon_refresh()
            self.enter_text_into_search_text_field(name)
            self.click_icon_search()
            self._wait_for_element_present(row)
            cond = self.check_vrep_is_present(name)
            if cond:
                self.select_vrep_in_table(name)
                self.click_icon_refresh()
                self.scroll_to_element(checkbox)
                self._wait_for_element_present(checkbox)
                unchecked = self._is_element_not_present(checkbox + "[contains(@src,'CheckBox1')]")
                # print checkbox + BaseActions.CHECKED + " is " + str(unchecked)
                if unchecked:
                    self.logger.info("vRep " + str(name) + " needs to be upproved" )
                    self._click_element(checkbox)
                    self.click_icon_refresh()
                    self._wait_for_element_present(checkbox + "[contains(@src,'CheckBox1')]")
                else:
                    pass
            cond1 = self.check_vrep_is_approved(name)
            cond2 = self.check_vrep_is_connected(name)
            cond3 = self.check_vrep_is_online_and_ready(name)
            cond4 = self._is_element_present(checkbox + "[contains(@src,'CheckBox1')]")
            if cond1 and cond2 and cond3 and cond4:
                self.logger.info("vRep " + str(name) + " is checked, online, connected and approved\n")
            elif cond1 is not True:
                self.logger.error("vRep " + str(name) + " is NOT approved\n")
            elif cond2 is not True:
                self.logger.error("vRep " + str(name) + " is NOT connected\n")
            elif cond3 is not True:
                self.logger.error("vRep " + str(name) + " is NOT online and ready\n")
            elif cond4 is not True:
                self.logger.error("vRep " + str(name) + " is NOT checked\n")
        except Exception as e:
            self.logger.error("Method 'Upprove a single vrep' is failed\n", str(e))

    def select_vrep_in_table(self, name):
        row = VRepsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        self._click_element(row)
        self._wait_for_element_selected(row)

    def check_vrep_is_approved(self, name):
        row = VRepsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row + VRepsPage.CELL_IS_APPROVED + VRepsPage.TRUE)
        return True if cond else False

    def check_vrep_is_connected(self, name):
        row = VRepsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row + VRepsPage.CELL_IS_CONNECTED + VRepsPage.TRUE)
        return True if cond else False

    def check_vrep_is_online_and_ready(self, name):
        row = VRepsPage.TABLE_ROW + "/*//span[text()='" + name + "']/ancestor::tr"
        cond = self._is_element_present(row + VRepsPage.CELL_IS_ONLINE + VRepsPage.TRUE)
        return True if cond else False

    def check_vrep_ready_for_work(self, name):
        cond1 = self.check_vrep_is_approved(name)
        cond2 = self.check_vrep_is_connected(name)
        cond3 = self.check_vrep_is_online_and_ready(name)
        return True if cond1 and cond2 and cond3 else False






