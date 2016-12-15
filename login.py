# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


class Login:
    username = "ikiprov@verismic.com"
    password = "R2ffman"

    driver = webdriver.Chrome('F:\chromedriver')
    options = webdriver.ChromeOptions()
    driver.maximize_window()
    driver.get("https://testteamdev.cloudmanagementsuite.com/")
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    time.sleep(3)

    elem = driver.find_element_by_xpath("//input[@type='text']")
    elem.clear()
    elem.send_keys(username)

    elem = driver.find_element_by_xpath("//input[@type='password']")
    elem.clear()
    elem.send_keys(password)
    time.sleep(1)

    elem = driver.find_element_by_xpath("//span[text()='Sign In']")
    elem.click()

    element1 = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Exit']")))
    time.sleep(3)
    assert (driver.find_element_by_xpath("//img[@alt='Exit']"))

    time.sleep(5)
    quit()