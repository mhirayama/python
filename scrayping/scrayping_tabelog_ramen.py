# -*- coding:utf-8 -*-
import csv
import requests
import codecs
from bs4 import BeautifulSoup

f = codecs.open('tabelog_ramen.csv', 'w', 'utf-8')
f.write("code,name,area,point,count" "\n")

target_url = 'https://tabelog.com/tokyo/A1316/rstLst/ramen/{0}/'

for i in range(1, 6):
    r = requests.get(target_url.format(i))         #requestsを使って、webから取得
    req = requests.Request(r)
    soup = BeautifulSoup(r.text, 'html5lib') #要素を抽出
    codes = soup.find_all('a',{'class':'list-rst__favorite-rvwr js-follow-reviewer-fav'})
    names = soup.find_all('a',{'class':'list-rst__rst-name-target cpy-rst-name'})
    areas = soup.find_all('span',{'class':'list-rst__area-genre cpy-area-genre'})
    points = soup.find_all('span',{'class':'c-rating__val c-rating__val--strong list-rst__rating-val'})
    counts = soup.find_all('em',{'class':'list-rst__rvw-count-num cpy-review-count'})

    for code, name, area, point, count in zip(codes, names, areas, points, counts):
        print(code.attrs['data-rst-id'], name.text, area.text, point.text, count.text)
        f.write(str(code.attrs['data-rst-id']) + ',' + name.text + ',' + area.text + ',' + point.text  + ',' + count.text  + "\n")


f.close()