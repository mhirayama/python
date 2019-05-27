f = open('akb48_wakati.txt')
lines2 = f.readlines() 
f.close()

import codecs
f = codecs.open('akb48_count.txt', 'w', 'utf-8')

words =[]
for line in lines2:
    line3 = line.replace(" ", "\n")
    f.write(line3)
f.close()

f = open('akb48_count.txt')
lines2 = f.read() 
f.close()

lines3 = lines2.split()

import collections
words = collections.Counter(lines3)

print(words.most_common())
