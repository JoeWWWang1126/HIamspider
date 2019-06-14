from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.imdb.com/')
# inputElement = driver.find_element_by_id('kw')
# searchButton = driver.find_element_by_id('su')
# inputElement.send_keys("Python")
# searchButton.click()
# time.sleep(15)
inputsearch=driver.find_element_by_xpath('//*[@id="navbar-query"]')
searchbutton=driver.find_element_by_xpath('//*[@id="navbar-submit-button"]/div')
inputsearch.send_keys('Frozen')
searchbutton.click()
