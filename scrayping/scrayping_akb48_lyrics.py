# -*- coding:utf-8 -*-
import csv
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd

f = codecs.open('akb48_lyrics.csv', 'w', 'utf-8')
f.write("lyrics" "\n")

target_url = 'https://www.uta-net.com/song/{0}/'

akb48_01 = pd.read_csv('akb48_id.csv',dtype = 'object')
akb48_02 = akb48_01["code"].values.tolist()

for i in akb48_02:
    r = requests.get(target_url.format(i))
    req = requests.Request(r)
    soup = BeautifulSoup(r.text, 'html5lib')
    lyrics = soup.find_all('div',{'id':'kashi_area'})

    for lyric in lyrics:

        print(lyric.text.replace(",", ''))

        f.write(str(lyric.text.replace(",", '') + "\n"))


f.close()
