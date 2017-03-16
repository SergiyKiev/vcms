import openpyxl
import os
import logging

class Settings:

    os.chdir('D:\\python\\vcms\\vcms') # KIPROV WORK
    # os.chdir('E:\\python\\vcms\\vcms')  # KIPROV HOME
    set = openpyxl.load_workbook('settings.xlsx')
    sheet = set.get_sheet_by_name('Sheet1')
    baseUrl = "https://testteamtest.cloudmanagementsuite.com/"
    endUserAccess = "https://testteamtest.cloudmanagementsuite.com/EndUserAccess.wgx"
    # baseUrl = "https://testteamdev.cloudmanagementsuite.com/"
    # baseUrl = str(sheet['B2'].value)
    username = str(sheet['B3'].value)
    password = str(sheet['B4'].value)


# if __name__ == '__main__':
#    pass