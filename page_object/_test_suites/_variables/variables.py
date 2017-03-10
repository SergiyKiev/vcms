

class Variables(object):

    help_test_discovery_task = "DiscoveryHelpTest"
    help_test_scan_task      = "ScanHelpTest"
    site_for_smoke_test      = "Smoke Test Site"
    # devices_for_smoke_test  = ["VKYV-DT-IK", "VKYV-VM-886IK","VKYV-VB-SRV2012IK", "VKYV-VM-VB1-W76"]
    # devices_for_smoke_test = ["VKYV-VM-816IK", "VKYV-VM-786IK"]
    vrep                    = "VKYV-DT-IK"#work'
    ip_address              = "010.006.002.067"
    # vrep                    = "WIN100213LAB1A"
    # vrep                  = "LT-HP-KIPROV"#home
    software                = "7z920 IK"
    patch                   = "MS12-011"
    help_test               = "HelpTest"
    site_name               = "New site #9101"
    default_site_name       = "Default Site"
    fifty_symbols_name      = "51symbols51symbols51symbols51symbols51symbols!<ok>"
    fifty_one_symbols_name  = fifty_symbols_name + "1"
    parent_site_name        = "Site #9118"
    subsite_1_name          = parent_site_name + "-01"
    subsite_2_name          = parent_site_name + "-02"
    columns_list1           = ["Device Name", "OS Name", "Caption", "IP Address"]
    columns_list2           = ["Device Name", "Device ID", "Domain", "Site", "User Name"]


    if __name__ == '__main__':

        elem = columns_list1
        e = []
        for x in elem:
            e.append(x)
        print e

        a = columns_list2
        set = []
        for y in a:
            set.append(y)
        print set

        if e == set:
            print "NOT GOOD"
        else:
            print "GOOD"





