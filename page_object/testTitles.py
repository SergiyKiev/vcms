# -*- coding: utf8 -*-


def test_title(number):
    return testTitles[number]


testTitles = [
    # [severity, description]
    ['Login page'  , 'TC#0001. Open the instance'],
    ['Home page'   , 'TC#9056. Login to the console'],
    ['Devices page', 'TC#9057. Open Site Name popup'],
    ['Devices page', 'TC#9101. Create new site with acceptable name'],
    ['Devices page', 'TC#9058. Cancel creating new site with empty text field'],
    ['Devices page', 'TC#9107. Create new site with duplicated name'],
    ['Devices page', 'TC#9104. Create site with name more than 50 symbols'],
    ['Devices page', 'TC#9118. Create subsites in the Global Site View tree'],
    ['Devices page', 'TC#6746. Site Name popup. Open Help link'],
]