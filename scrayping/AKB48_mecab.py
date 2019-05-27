import MeCab

lyrics = open('akb48_lyrics.csv', 'r')
text = lyrics.readlines()

def extractKeyword(line):
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(line)
    keywords = []
    while node:
        if node.feature.split(",")[0] == u"名詞":
            keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"形容詞":
             keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"動詞":
             keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"副詞":
             keywords.append(node.surface)
        node = node.next
    return keywords

import codecs
import re
f = codecs.open('akb48_wakati.txt', 'w', 'utf-8')
single =  r"^[ぁ-ん]$"

for line in text:
    kekka = extractKeyword(line)
    wakati = ' '.join(kekka)
    re_wakati1 = wakati.split()
    
    for line2 in re_wakati1:
        if re.match(single,line2):
            re_wakati2 = ""
        else:
            re_wakati2 = line2
        print(re_wakati2,end=" ")
        f.write(re_wakati2)
        f.write(" ")
    print("\n")
    f.write("\n")
f.close()
