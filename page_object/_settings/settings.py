import openpyxl
import os
import logging

class Settings:

    def __init__(self):
        pass

    # os.chdir('D:\\python\\vcms\\vcms') # KIPROV WORK
    # logging.basicConfig(filename='D:\\python\\vcms\\vcms\\page_object\\_test_suites\\test_logs.log',
    #                     level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s') # KIPROV WORK
    os.chdir('E:\\python\\vcms\\vcms')  # KIPROV HOME
    logging.basicConfig(filename='E:\\python\\vcms\\vcms\\page_object\\_test_suites\\test_logs.log',
                        level=logging.INFO, format='%(asctime)-24s %(levelname)-6s %(message)s') # KIPROV HOME

    set = openpyxl.load_workbook('settings.xlsx')
    sheet = set.get_sheet_by_name('Sheet1')
    baseUrl = "https://testteamtest.cloudmanagementsuite.com/"
    # baseUrl = "https://testteamdev.cloudmanagementsuite.com/"
    # baseUrl = str(sheet['B2'].value)
    username = str(sheet['B3'].value)
    password = str(sheet['B4'].value)


# if __name__ == '__main__':
#    pass