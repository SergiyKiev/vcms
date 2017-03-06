from _base.downloadAndInstall import DownloadAndInstall
from _feature_objects.feature_screen import *
from _feature_objects.feature_left_menu import *
from _test_suites._variables.variables import Variables


class MainPage(BaseActions):

    def check_main_page_loaded(self):
        cond = self._is_element_present(BaseElements.RIBBON_BAR)
        # cond2 = self._is_element_present(BaseElements.LEFT_MENU_HOME)
        msg_true = "Main page is loaded\n"
        msg_false = "Main page is NOT loaded\n"
        self._set_log_msg_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def delete_device_from_the_console(self, device_name):
        devices_page = DevicesScreen(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        devices_page.delete_single_device_in_devices_page_table(device_name)
        cond = devices_page.check_device_is_present(device_name)
        return True if cond is not True else False

    def upprove_vrep(self, device_name):
        vreps_screen = VRepsScreen(self.driver)
        left_menu_administration = LeftMenuAdministration(self.driver)
        left_menu_administration.open_menu_administration()
        left_menu_administration.click_vreps_label()
        vreps_screen.upprove_single_vrep_in_vreps_page_table(device_name)
        cond = vreps_screen.check_vrep_ready_for_work(device_name)
        return True if cond else False

    def setup_for_help_tests(self):
        device_name = Variables.vrep
        devices_screen = DevicesScreen(self.driver)
        # delete_vrep = self.delete_device_from_the_console(device_name)
        # self.logger.info("Device is not presented in the console: " + str(device_name) + " - " + str(delete_vrep))
        # desktop = DownloadAndInstall(self.driver)
        # desktop.clean_up_device()
        # desktop.download_agent()
        # desktop.install_agent()
        # devices_page.click_icon_refresh()
        # install_vrep = devices_screen.check_device_is_present(device_name)
        # self.logger.info("vRep " + str(device_name) + " is installed - " + str(install_vrep))
        upprove_vrep = self.upprove_vrep(device_name)
        if upprove_vrep:
            self.logger.info("Setup is finished successfully: " + str(upprove_vrep) + "\n")
            return True
        else:
            self.logger.info("Setup is finished successfully: " + str(upprove_vrep) + "\n")
            return False

    def run_discovery_task(self):
        pass

    def run_software_deployment_task(self):
        pass

    def run_scan_updates_task(self):
        pass

    def create_and_config_site(self):
        pass








