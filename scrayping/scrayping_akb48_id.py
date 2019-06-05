# -*- coding:utf-8 -*-
import csv
import requests
import codecs
import time
from bs4 import BeautifulSoup

f = codecs.open('akb48_id.csv', 'w', 'utf-8')
f.write("code,title" "\n")

target_url = 'https://www.uta-net.com/search/?Aselect=1&Bselect=3&Keyword=AKB48&sort=&pnum={0}'

for i in range(1, 4):
    r = requests.get(target_url.format(i))
    req = requests.Request(r)
    soup = BeautifulSoup(r.text, 'html5lib')
    codes = soup.find_all('td',{'class':'side td1'})
    titles = soup.find_all('td',{'class':'side td1'})


    for code, title in zip(codes, titles):
        print(code.find('a').attrs['href'][6:].replace("/", ''), title.text)
        f.write(str(code.find('a').attrs['href'][6:].replace("/", '')) + ',' + title.text + "\n")
        time.sleep(1)

f.close()
