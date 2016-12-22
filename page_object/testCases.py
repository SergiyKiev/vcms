# -*- coding: utf8 -*-
# we should add test cases here because we can miss some cases while writing automation code or
# some manuel testers (test analystes) can handle this more efficiently
# we can obtain test cases from test management tools, I used this for my previous project: http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx
# We can also record the result of test cases to test management tool

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array

def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['TC#0001', 'Open the instance'],
    ['TC#0002', 'Login to the console'],
    ['TC#0003', 'Open Global Site View'],
    ['TC#0004', 'Open Site Name popup'],
    ['TC#0005', 'Create New Site'],
    ['Blocker', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
]