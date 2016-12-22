# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


class CreateSite:
    # Variables
    baseUrl = "https://testteamdev.cloudmanagementsuite.com/"
    username = "ikiprov@verismic.com"
    password = "R2ffman"
    siteName = "New site IK"
    field = "//input"
    fieldUsername = "//input[@type='text']"
    fieldPassword = "//input[@type='password']"
    buttonSignIn = "//span[text()='Sign In']"
    buttonExit = "//img[@alt='Exit']"
    buttonDevices = "//div[@title='Devices']"
    textGlobalSiteView = "//span[contains(text(),'Global Site View')]"
    labelGlobalSiteView = "//span[text()='Global Site View']/ancestor::div[@class='TreeView-PaddingContainer']/div[1]/div[contains(@id,'VWGNODE')]"
    treeGlobalSiteView = "//span[text()='Global Site View']/ancestor::div[@class='TreeView-PaddingContainer']/div[1]/div[contains(@id,'VWGSUBS')]"
    buttonNewSite = "//img[@alt='New Site']"
    buttonOK = "//span[text()='OK']"
    buttonDelete = "//img[@alt='Delete']"
    popupSiteName = "//span[text()='Site Name']/ancestor::div[contains(@id,'WRP')]"
    popupAreYouSure = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"
    popup = "//div[contains(@id,'WRP')]"
    labelSiteName = "//span[text()='" + siteName + "']"

    #Start test
    driver = webdriver.Chrome('E:\python\chromedriver')
    options = webdriver.ChromeOptions()
    driver.maximize_window()
    #Open instance
    driver.get(baseUrl)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, fieldUsername)))
    time.sleep(5)
    # type username
    driver.find_element_by_xpath(fieldUsername).send_keys(username)
    # type password
    elem = driver.find_element_by_xpath(fieldPassword).send_keys(password)
    time.sleep(1)
    #click SignIn
    driver.find_element_by_xpath(buttonSignIn).click()
    #wait for page to load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, buttonExit)))
    time.sleep(3)
    #click Devices on left menu
    driver.find_element_by_xpath(buttonDevices).click()
    time.sleep(4)
    #click Global Site View main site
    driver.find_element_by_xpath(labelGlobalSiteView + '/*' + textGlobalSiteView).click()
    time.sleep(4)
    #click New Site on Ribbon bar
    driver.find_element_by_xpath(buttonNewSite).click()
    time.sleep(3)
    #type Site Name
    driver.find_element_by_xpath(popupSiteName + "/*" + field).send_keys(siteName)
    time.sleep(1)
    #Click OK
    driver.find_element_by_xpath(popupSiteName + "/*" + buttonOK).click()
    time.sleep(4)
    #Verify Site is created
    assert siteName in driver.page_source
    #Select created site
    driver.find_element_by_xpath(treeGlobalSiteView + "/*" + labelSiteName).click()
    time.sleep(3)
    #Click Delete on Ribbon bar
    driver.find_element_by_xpath(buttonDelete).click()
    time.sleep(3)
    #Click OK on popup
    driver.find_element_by_xpath(popupAreYouSure + "/*" + buttonOK).click()
    time.sleep(3)
    #Verify Site is deleted
    assert siteName not in driver.page_source
    time.sleep(3)
    #print massage
    print("Test is successfull! " + siteName + " Site is created and deleted")
    #End test
    #Close console
    quit()