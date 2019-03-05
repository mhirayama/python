# -*- coding:utf-8 -*-
import requests
import codecs
from bs4 import BeautifulSoup
import re

f = codecs.open('oricon.csv', 'w', 'utf-8')
f.write("code, rank, title, artist, sales, label " "\n")

target_url = 'https://www.oricon.co.jp/rank/js/y/2018/p/{0}/'

for i in range(1, 11):
    r = requests.get(target_url.format(i))         #requestsを使って、webから取得
    req = requests.Request(r)
    soup = BeautifulSoup(r.text, 'html5lib') #要素を抽出
    ranks = soup.find_all('p',{'class':'num'})
    titles = soup.find_all('h2',{'class':'title'})
    artists = soup.find_all('p',{'class':'name'})
    sales = soup.find_all('ul',{'class':'list'})

    for rank, title, artist, sale in zip(ranks, titles, artists, sales):
        print(rank.text, title.text, artist.text,sale.text.replace('\t','').replace('\n','')[4:15],sale.text.replace('\t','').replace('\n','')[15:])
        f.write(rank.text + ',' + title.text + ',' + artist.text + ',' + sale.text.replace('\t','').replace('\n','')[4:15] +',' + sale.text.replace('\t','').replace('\n','')[15:] + "\n")

f.close()
