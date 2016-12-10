import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox()

driver = webdriver.Chrome('/Users/sol/selenium/chromedriver')
driver.get("http://www.python.org")
time.sleep(5)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(5)
#driver.close()
driver.quit()
