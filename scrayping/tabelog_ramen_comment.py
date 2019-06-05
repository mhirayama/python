# -*- coding:utf-8 -*-
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd
import itertools
import numpy as np
import re
import time

f = codecs.open('tabelog_ramen_review01.csv', 'w', 'utf-8')
f.write("code,date,review" "\n")

target_url = 'https://tabelog.com/tokyo/A1316/A131601/{0}/dtlrvwlst/COND-0/smp1/?lc=0&rvw_part=all&PG={1}'

tabelog01 = pd.read_csv('tabelog_ramen.csv',dtype = 'object')
tabelog02 = tabelog01['code'].values.tolist()
list2 = np.array([j for j in range(1,24)])
list3 = list(itertools.product(tabelog02, list2))

for i,j in list3:
    r = requests.get(target_url.format(i,j))         #requestsを使って、webから取得

    soup = BeautifulSoup(r.text, 'html5lib') #要素を抽出
    codes = soup.find_all('div',{'class': 'rvw-item js-rvw-item-clickable-area'})
    dates = soup.find_all('div',{'class':'rvw-item__date'})
    reviews = soup.find_all('div',{'class':'rvw-item__rvw-comment'})

    for code, date, review in zip(codes, dates, reviews):
        print(re.sub(r'\D','',code.attrs['data-detail-url'])[10:18], date.text.replace("\n", ' ').replace(" ",''), review.text.replace("\n", ' ').replace(" ",'').replace(",",' '))
        f.write(re.sub(r'\D','',code.attrs['data-detail-url'])[10:18] + ',' + date.text.replace("\n", ' ').replace(" ",'') + ',' + review.text.replace("\n", ' ').replace(" ",'').replace(",",' ') + "\n")
        time.sleep(1)
f.close()
