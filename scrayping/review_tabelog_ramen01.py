import pandas as pd
import MeCab
import gensim
import numpy as np
from sklearn.cluster import KMeans

reviews = pd.read_csv('tabelog_ramen_review01.csv')

mecab = MeCab.Tagger("-Ochasen")

def wakatico(x):
    kekka = mecab.parse(x)
    lines = kekka.split('\n')
    words = []
    for line in lines:
        cols = line.split("\t")
        words.append(cols[0])
    return words

reviews["wakati"] = reviews.apply(lambda row: wakatico(str(row['review'])),axis=1)

pair = r"^[ぁ-ん]{2}$"
numb = r"^[0-9]+$"
kigou = r"^[EOS,...]+$"

import re

def stopword(words):
    return [x for x in words if len(x)  > 1 and re.match( numb, x ) is None and re.match(pair,x) is None and re.match(kigou,x) is None] 

reviews["was"] = reviews.apply(lambda row: stopword(row["wakati"]),axis=1)

jisho = gensim.corpora.Dictionary(list(reviews.was))

jisho.filter_extremes(no_below=30,no_above=0.2)

terms = len(jisho)
T = [gensim.matutils.corpus2dense([jisho.doc2bow(doc)],num_terms=terms, dtype=None).T[0] for doc in list(reviews.was)]
t = np.array(T)

model = KMeans(n_clusters=8, random_state=10).fit(t)
label = model.labels_

import codecs
f = codecs.open('tabelog_ramen_learn.csv', 'w','utf-8')
f.write('type,code,date' + "\n")

for lab, code, date in zip(label, list(reviews.code), list(reviews.date)):
    f.write(str(lab) + ',' + str(code) + ',' + str(date) + "\n")
f.close
