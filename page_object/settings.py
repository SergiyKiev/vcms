import openpyxl
import os


class Settings(object):

    os.chdir('E:\\python\\vcms')
    settings = openpyxl.load_workbook('settings.xlsx')
    sheet = settings.get_sheet_by_name('Sheet1')
    username  = str(sheet['B2'].value)
    password  = str(sheet['B3'].value)
    baseUrl   = str(sheet['B4'].value)
