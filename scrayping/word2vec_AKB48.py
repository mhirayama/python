from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence('akb48_wakati.txt')

model = word2vec.Word2Vec(sentences, size=100, min_count=5, window=10, hs=1, sg=1, seed=100)
model.save("akb48.model")
