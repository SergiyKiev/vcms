# -*- coding: utf8 -*-
# we should add test cases here because we can miss some cases while writing automation code or
# some manuel testers (test analystes) can handle this more efficiently
# we can obtain test cases from test management tools, I used this for my previous project: http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx
# We can also record the result of test cases to test management tool

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array

def test_titles(number):
    return testTitles[number]


testTitles = [
    # [severity, description]
    ['Devices page', 'Open the instance'],
    ['Devices page', 'Login to the console'],
    ['Devices page', 'Open Global Site View'],
    ['Devices page', 'Open Site Name popup'],
    ['Devices page', 'Create New Site'],
    ['Devices page', 'Cancel creating Site'],
    ['Devices page', 'Create Site with duplicated name'],
    ['Devices page', 'Cancel Site Creating'],
    ['Devices page', 'Cancel Site Creating'],
]