

class Variables(object):

    site_for_smoke_test     = "Smoke Test Site"
    # devices_for_smoke_test  = ["VKYV-DT-IK", "VKYV-VM-886IK","VKYV-VB-SRV2012IK", "VKYV-VM-VB1-W76"]
    # devices_for_smoke_test = ["VKYV-VM-816IK", "VKYV-VM-786IK"]
   # vrep                    = ["VKYV-DT-IK",]#work
    vrep                    = "LT-HP-KIPROV"
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





