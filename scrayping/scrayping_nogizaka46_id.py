# -*- coding:utf-8 -*-
import csv
import requests
import codecs
from bs4 import BeautifulSoup

f = codecs.open('nogi46_id.csv', 'w', 'utf-8')
f.write("code,title" "\n")

target_url = 'https://www.uta-net.com/search/?Keyword=%E4%B9%83%E6%9C%A8%E5%9D%8246&x=0&y=0&Aselect=1&Bselect={0}'

for i in range(1, 4):
    r = requests.get(target_url.format(i))         #requestsを使って、webから取得
    req = requests.Request(r)
    soup = BeautifulSoup(r.text, 'html5lib') #要素を抽出
    codes = soup.find_all('td',{'class':'side td1'})
    titles = soup.find_all('td',{'class':'side td1'})


    for code, title in zip(codes, titles):
        print(code.find('a').attrs['href'][6:].replace("/", ''), title.text)
        f.write(str(code.find('a').attrs['href'][6:].replace("/", '')) + ',' + title.text + "\n")


f.close()
