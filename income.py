# import required tools
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

# fill in parameters
driver = webdriver.Chrome()
driver.get('https://ucannualwage.ucop.edu/wage/')

location_box = driver.find_element_by_name('location')
location_box.send_keys('San Diego')

title_box = driver.find_element_by_name('title')
title_box.send_keys('LECT')

search_button = driver.find_element_by_id('searchButton')
search_button.click()

next_button = driver.find_element_by_id('next')

# add data to lists
pages = driver.find_element_by_id('sp_1')
for i in range(1, pages):