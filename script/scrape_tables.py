# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:32:25 2017
Import data from various issues of 
 State Finance: A Study of Budgets 
@author: subham-lenovo
"""
import requests
from bs4 import BeautifulSoup
import os
import csv
# delay request with sleep
from time import sleep
from time import time
# mimic human behaviour by random delays
from random import randint
from IPython.core.display import clear_output
from warnings import warn

# work dir
print(os.getcwd())
os.chdir('C:/Users/subham-lenovo/Documents/scrape_budget_data')

# Create url list to parse
base_url = 'https://rbi.org.in/Scripts/PublicationsView.aspx?id='
page_url = []
# 2001-02: revenue budget
    # +1 for range to include upper interval
for i in range(3973, 4002):
    page_url.append(base_url+str(i))
# 2001-02: capital budget    
for i in range(4008, 4037):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2002-03: revenue budget
for i in range(4915, 4944):
    page_url.append(base_url+str(i))
# 2002-03: capital budget
for i in range(4949, 4978):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2003-04: revenue budget
for i in range(6201, 6230):
    page_url.append(base_url+str(i))
# 2003-04: capital budget
for i in range(6235, 6264):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2004-05: revenue budget
for i in range(7138, 7167):
    page_url.append(base_url+str(i))
# 2004-05: capital budget
for i in range(7172, 7201):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2005-06: revenue budget
for i in range(8135, 8164):
    page_url.append(base_url+str(i))
# 2005-06: capital budget
for i in range(8169, 8198):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2006-07: revenue budget
for i in range(9108, 9137):
    page_url.append(base_url+str(i))
# 2006-07: capital budget
for i in range(9142, 9171):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2007-08: revenue budget
for i in range(10095, 10123):
    page_url.append(base_url+str(i))
# 2007-08: capital budget
for i in range(10130, 10160):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2008-09: revenue budget
for i in range(11021, 11232):
    page_url.append(base_url+str(i))
# 2008-09: capital budget
for i in range(11236, 11267):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2009-10: revenue budget
for i in range(12184, 12215):
    page_url.append(base_url+str(i))
# 2009-10: capital budget
for i in range(12219, 12250):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2010-11: revenue budget
for i in range(13255, 13286):
    page_url.append(base_url+str(i))
# 2010-11: capital budget
for i in range(13290, 13321):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2011-12: revenue budget
for i in range(14128, 14159):
    page_url.append(base_url+str(i))
# 2011-12: capital budget
for i in range(14163, 14194):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2012-13: revenue budget
for i in range(14849, 1480):
    page_url.append(base_url+str(i))
# 2012-13: capital budget
for i in range(14884, 14915):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2013-14: revenue budget
for i in range(15615, 15646):
    page_url.append(base_url+str(i))
# 2013-14: capital budget
for i in range(15650, 15681):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2014-15: revenue budget
for i in range(16332, 16364):
    page_url.append(base_url+str(i))
# 2014-15: capital budget
for i in range(16368, 16400):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2015-16: revenue budget
for i in range(16897, 16929):
    page_url.append(base_url+str(i))
# 2015-16: capital budget
for i in range(16933, 16965):
    page_url.append(base_url+str(i))
print(len(page_url))
# 2016-17: revenue budget
for i in range(17533, 17565):
    page_url.append(base_url+str(i))
# 2016-17: capital budget
for i in range(17569, 17601):
    page_url.append(base_url+str(i))
print(len(page_url))
    
# preparing loop monitor
start_time = time()
req = 0

#remove csv file if it already exists
try:
    os.remove('./output/raw_state_budget.csv')
except OSError:
    pass #following lines will be executed regardless of exceptions
# iterate over urls
with open('./output/raw_state_budget.csv', 'a') as f:
    wr = csv.writer(f)
    for j in page_url:
        try:
            page = requests.get(j)
        except:
            continue # following lines won't get executed if exceptions arise
        # pause the loop
        sleep(randint(8,15))
        # Monitor the requests
        req += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(req, req/elapsed_time))
        clear_output(wait = True)
        # Throw a warning for non-200 status codes
        if page.status_code != 200:
            warn('Request: {}; Status code: {}'.format(req, page.status_code))
        # parse content with BeautifulSoup
        bs = BeautifulSoup(page.content, 'lxml')
        try:
            table = bs.find('table')
            rows = table.find_all('tr')[2:]
            
            for row in rows:
                cols = row.find_all(['td'])
                cols = [x.text.strip() for x in cols]
                try:
                    wr.writerow(cols)
                except UnicodeEncodeError:
                    pass
        except:
            pass

#--------------- EoF ------------------
