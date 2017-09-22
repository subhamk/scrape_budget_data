# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:58:22 2017

@author: nk905178
"""

import requests
from bs4 import BeautifulSoup
import os
import csv
# delay request with sleep
from time import sleep
from time import time
from time import ctime
# mimic human behaviour by random delays
from random import randint
from IPython.core.display import clear_output
from warnings import warn

# work dir
print(os.getcwd())
os.chdir('C:/Projects/scrape_budget_data')
# os.chdir('C:/Users/subham-lenovo/Documents/scrape_budget_data')
ctime()

# Create url list to parse
base_url = 'https://rbi.org.in/Scripts/PublicationsView.aspx?id='


page_url_2001 = []
# 2001-02: revenue budget
for i in range(3973, 4002):
    page_url_2001.append(base_url+str(i))
# 2001-02: capital budget    
for i in range(4008, 4037):
    page_url_2001.append(base_url+str(i))
print(len(page_url_2001))

page_url_2002 = []
# 2002-03: revenue budget
for i in range(4915, 4944):
    page_url_2002.append(base_url+str(i))
# 2002-03: capital budget
for i in range(4949, 4978):
    page_url_2002.append(base_url+str(i))
print(len(page_url_2002))

page_url_2003 = []
# 2003-04: revenue budget
for i in range(6201, 6230):
    page_url_2003.append(base_url+str(i))
# 2003-04: capital budget
for i in range(6235, 6264):
    page_url_2003.append(base_url+str(i))
print(len(page_url_2003))

page_url_2004 = []
# 2004-05: revenue budget
for i in range(7138, 7167):
    page_url_2004.append(base_url+str(i))
# 2004-05: capital budget
for i in range(7172, 7201):
    page_url_2004.append(base_url+str(i))
print(len(page_url_2004))

page_url_2005 = []
# 2005-06: revenue budget
for i in range(8135, 8164):
    page_url_2005.append(base_url+str(i))
# 2005-06: capital budget
for i in range(8169, 8198):
    page_url_2005.append(base_url+str(i))
print(len(page_url_2005))

page_url_2006 = []
# 2006-07: revenue budget
for i in range(9108, 9137):
    page_url_2006.append(base_url+str(i))
# 2006-07: capital budget
for i in range(9142, 9171):
    page_url_2006.append(base_url+str(i))
print(len(page_url_2006))

page_url_2007 = []
# 2007-08: revenue budget
for i in range(10095, 10123):
    page_url_2007.append(base_url+str(i))
# 2007-08: capital budget
for i in range(10130, 10160):
    page_url_2007.append(base_url+str(i))
print(len(page_url_2007))

page_url_2008 = []
# 2008-09: revenue budget
for i in range(11201, 11232):
    page_url_2008.append(base_url+str(i))
# 2008-09: capital budget
for i in range(11236, 11267):
    page_url_2008.append(base_url+str(i))
print(len(page_url_2008))

page_url_2009 = []
# 2009-10: revenue budget
for i in range(12184, 12215):
    page_url_2009.append(base_url+str(i))
# 2009-10: capital budget
for i in range(12219, 12250):
    page_url_2009.append(base_url+str(i))
print(len(page_url_2009))

page_url_2010 = []
# 2010-11: revenue budget
for i in range(13255, 13286):
    page_url_2010.append(base_url+str(i))
# 2010-11: capital budget
for i in range(13290, 13321):
    page_url_2010.append(base_url+str(i))
print(len(page_url_2010))

page_url_2011 = []
# 2011-12: revenue budget
for i in range(14128, 14159):
    page_url_2011.append(base_url+str(i))
# 2011-12: capital budget
for i in range(14163, 14194):
    page_url_2011.append(base_url+str(i))
print(len(page_url_2011))

page_url_2012 = []
# 2012-13: revenue budget
for i in range(14849, 14880):
    page_url_2012.append(base_url+str(i))
# 2012-13: capital budget
for i in range(14884, 14915):
    page_url_2012.append(base_url+str(i))
print(len(page_url_2012))

# define function to scrap html tables 
# input: year, url_list for that year
def scrapetab(y, page_url):
    #remove csv file if it already exists
    try:
        os.remove("./output/raw_state_budget_" + str(y) + ".csv")
    except OSError:
        pass #following lines will be executed regardless of exceptions
    # preparing loop monitor
    start_time = time()
    req = 0
    # iterate over urls
    with open("./output/raw_state_budget_" + str(y) + ".csv", mode ='w') as f:
        wr = csv.writer(f)
        for j in page_url:
            try:
                page = requests.get(j)
            except:
                continue # following lines won't get executed if exceptions arise
            # pause the loop
            sleep(randint(2,6))
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
                    cols = [x.text.strip().encode('utf-8') for x in cols]
                    wr.writerow(cols)
                    
            except:
                pass

# scrap tables one year at a time to avoid one large csv dataset
scrapetab(2001, page_url_2001)

scrapetab(2002, page_url_2002)

scrapetab(2003, page_url_2003)

scrapetab(2004, page_url_2004)

scrapetab(2005, page_url_2005)

scrapetab(2006, page_url_2006)

scrapetab(2007, page_url_2007)

scrapetab(2008, page_url_2008)

scrapetab(2009, page_url_2009)

scrapetab(2010, page_url_2010)

scrapetab(2011, page_url_2011)

scrapetab(2012, page_url_2012)
