import openpyxl
import os


class Settings(object):

    os.chdir('D:\\python\\vcms\\vcms')
    # os.chdir('E:\\python\\vcms\\vcms')
    settings = openpyxl.load_workbook('settings.xlsx')
    sheet = settings.get_sheet_by_name('Sheet1')
    baseUrl = str(sheet['B2'].value)
    username  = str(sheet['B3'].value)
    password  = str(sheet['B4'].value)

