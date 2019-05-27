# -*- coding:utf-8 -*-
import csv
import requests
import codecs
from bs4 import BeautifulSoup
import pandas as pd

f = codecs.open('nogi46_lyrics.csv', 'w', 'utf-8')
f.write("lyrics" "\n")

target_url = 'https://www.uta-net.com/song/{0}/'

nogi46_01 = pd.read_csv('nogi46_id.csv',dtype = 'object')
nogi46_02 = nogi46_01["code"].values.tolist()

for i in nogi46_02:
    r = requests.get(target_url.format(i))         #requestsを使って、webから取得
    req = requests.Request(r)
    soup = BeautifulSoup(r.text, 'html5lib') #要素を抽出
    lyrics = soup.find_all('div',{'id':'kashi_area'})

    for lyric in lyrics:

        print(lyric.text.replace(",", ''))

        f.write(str(lyric.text.replace(",", '') + "\n"))


f.close()
