from _base.downloadAndInstall import DownloadAndInstall
from _feature_objects.feature_popup import *
from _feature_objects.feature_screen import *
from _feature_objects.feature_left_menu import *
from _test_suites._variables.variables import Variables


class MainPage(BaseActions):

    def check_main_page_loaded(self):
        cond = self._is_element_present(BaseElements.RIBBON_BAR)
        # cond2 = self._is_element_present(BaseElements.LEFT_MENU_HOME)
        msg_true = "Main page is loaded\n"
        msg_false = "Main page is NOT loaded\n"
        self._set_log_for_true_or_false(cond, msg_true, msg_false)
        return True if cond else False

    def delete_device_from_the_console(self, device_name):
        devices_page = DevicesScreen(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        devices_page.delete_single_device_in_devices_page_table(device_name)
        cond = devices_page.check_device_is_presented(device_name)
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
        # devices_screen = DevicesScreen(self.driver)
        # delete_vrep = self.delete_device_from_the_console(device_name)
        # self.logger.info("Device is not presented in the console: " + str(device_name) + " - " + str(delete_vrep))
        # desktop = DownloadAndInstall(self.driver)
        # desktop.clean_up_device()
        # desktop.download_agent()
        # desktop.install_agent()
        # devices_page.click_icon_refresh()
        # install_vrep = devices_screen.check_device_is_presented(device_name)
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

    def run_discovery_task_if_not_exists(self, name):
        ribbon_bar = RibbonBar(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu_tasks = LeftMenuTasks(self.driver)
        discover_devices_popup = DiscoverDevicesPopup(self.driver)
        left_menu_tasks.open_menu_tasks()
        left_menu_tasks.expand_scheduled_tasks_list()
        left_menu_tasks.click_discover_label()
        cond = tasks_screen.search_task(name)
        if cond is not True:
            ribbon_bar.click_button_create()
            discover_devices_popup.click_button_select_none()
            discover_devices_popup.select_site_in_list()
            discover_devices_popup.click_button_next()
            discover_devices_popup.click_button_next()
            cond = discover_devices_popup.check_none_patches_selected()
            if cond is not True:
                print "None patches is NOT selected"
            discover_devices_popup.click_button_next()
            cond = discover_devices_popup.check_start_now_selected()
            if cond is not True:
                print "Start Now is NOT selected"
            discover_devices_popup.click_button_next()
            discover_devices_popup.click_button_next()
            discover_devices_popup.clear_text_name_text_field()
            discover_devices_popup.enter_text_into_task_name_field(name)
            discover_devices_popup.click_button_finish()
            return True
        else:
            print "Task is presented"
        postcond = tasks_screen.search_task(name)
        return True if postcond else False

    def run_patch_scan_task_on_single_device_if_not_exists(self, task_name, device_name, site_name):
        ribbon_bar = RibbonBar(self.driver)
        tasks_screen = TasksScreen(self.driver)
        left_menu_tasks = LeftMenuTasks(self.driver)
        select_targets_popup = SelectTargetsPopup(self.driver)
        patch_manager_scanning_popup = PatchManagerScanningPopup(self.driver)
        left_menu_tasks.open_menu_tasks()
        left_menu_tasks.expand_scheduled_tasks_list()
        left_menu_tasks.click_patch_manager_label()
        cond = tasks_screen.search_task(task_name)
        if cond is not True:
            ribbon_bar.click_button_scan()
            patch_manager_scanning_popup.open_select_targets_popup()
            select_targets_popup.select_site_in_list(site_name)
            select_targets_popup.select_device_in_list(device_name)
            select_targets_popup.click_button_ok()
            patch_manager_scanning_popup.click_button_next()
            patch_manager_scanning_popup.select_radio_button_all()
            patch_manager_scanning_popup.click_button_next()
            patch_manager_scanning_popup.select_radio_button_start_now()
            patch_manager_scanning_popup.click_button_next()
            patch_manager_scanning_popup.clear_text_name_text_field()
            patch_manager_scanning_popup.enter_text_into_task_name_field(task_name)
            patch_manager_scanning_popup.click_button_finish()
        postcond = tasks_screen.search_task(task_name)
        return True if postcond else False

    def run_software_deployment_task(self):
        pass

    def run_scan_updates_task(self):
        pass

    def create_and_config_site(self):
        ribbon_bar = RibbonBar(self.driver)
        left_menu_devices = LeftMenuDevices(self.driver)
        devices_screen = DevicesScreen(self.driver)
        configuration_popup = ConfigurationPopup(self.driver)
        left_menu_devices.open_menu_devices()
        left_menu_devices.click_global_site_view_label()
        left_menu_devices.expand_global_site_view_list()
        left_menu_devices.create_site_if_not_exists()
        left_menu_devices.click_site_in_global_site_view_list()
        ribbon_bar.click_button_config()
        configuration_popup.click_ip_address_ranges_tab()
        configuration_popup.delete_all_ip_address_ranges()
        configuration_popup.add_single_ip_address_range()
        configuration_popup.click_button_apply_changes()
        configuration_popup.click_button_ok_on_success_popup()
        configuration_popup.click_vreps_tab()
        configuration_popup.apply_vrep_to_the_site()
        configuration_popup.click_button_close()
        cond = devices_screen.check_device_is_presented()
        return True if cond else False

    # def create_new_dashboard_if_not_exists(self, name=Variables.help_test):
    #     ribbon_bar = RibbonBar(self.driver)
    #     left_menu = LeftMenuReporting(self.driver)
    #     create_new_dashboard_popup = CreateNewDashboardPopup(self.driver)
    #     left_menu.click_label_my_dashboards()
    #     ribbon_bar.click_button_new()
    #     create_new_dashboard_popup.enter_text_into_name_text_field(name)
    #     create_new_dashboard_popup.click_button_next()
    #     create_new_dashboard_popup.click_button_finish()
    #     left_menu.expand_list_my_dashboards()
    #     cond = self._is_element_present()











