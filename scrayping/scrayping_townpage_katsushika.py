# -*- coding:utf-8 -*-
import urllib.request
import codecs
from bs4 import BeautifulSoup

f = codecs.open('townpage_katsushika.csv', 'w', 'utf-8')
f.write('cammpany,tel,adress' + u"\n")

target_url = 'https://itp.ne.jp/tokyo/13122/genre_dir/buildingplan/pg/{0}/?nad=1&sr=1&sr=1&sr=1&sr=1&sr=1&evdc=1&sr=1&num=50'

for i in range(1,3):
    r = urllib.request.urlopen(target_url.format(i))         #requestsを使って、webから取得
    soup = BeautifulSoup(r, 'html5lib') #要素を抽出
    tr_arr = soup.findAll('article')

    for tr in tr_arr:
        lrg = tr.find('h4')
        cammpany = lrg.find('a').string
        address = tr.find('p').text.replace(' ',',').replace('　',',')
        tel = tr.find('b').text

        print(cammpany, tel, address)
        f.write(cammpany + ',' + tel + ',' + address + u"\n")

f.close()