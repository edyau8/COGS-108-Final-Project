# import required tools
import csv
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

# fill in parameters
driver = webdriver.Chrome()
driver.get('https://ucannualwage.ucop.edu/wage/')

location_box = driver.find_element_by_name('location')
location_box.send_keys('San Diego')

title_box = driver.find_element_by_name('title')
title_box.send_keys('LECT')

number_button = driver.find_element_by_class_name('ui-pg-selbox')
number_button.send_keys('60')

search_button = driver.find_element_by_id('searchButton')
search_button.click()

next_button = driver.find_element_by_id('next')

# add data to list
rows = []
rowlist = list()

# add all lecturer data
i = 0
pages = 12
while i <= pages:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(3)
    table = soup.find_all('table')[4]
    rows = table.find_all('tr')
    print(rows)
    for tr in rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        rowlist.append(row)
    next_button.click()
    i = i + 1

# add all professor data
title_box.clear()
title_box.send_keys('PROF')
search_button.click()
i = 0
pages = 54
while i <= pages:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(3)
    table = soup.find_all('table')[4]
    rows = table.find_all('tr')
    print(rows)
    for tr in rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        rowlist.append(row)
    next_button.click()
    i = i + 1


# clean up data and convert to csv file
df = pd.DataFrame(rowlist, columns=['Index', 'N', 'Year', 'Location', 'First Name', 'Last Name', 'Title', 'Gross Pay', 
    'Regular Pay', 'Overtime Pay', 'Other Pay'])

df.set_index('Last Name', inplace=True)
df = df.drop(['Index', 'N', 'Gross Pay', 'Overtime Pay', 'Other Pay'], axis=1)
df = df.replace('*****', np.nan)
df = df.dropna()
df.to_csv('income.csv')