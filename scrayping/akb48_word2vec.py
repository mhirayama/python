from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence('akb48_wakati.txt')
model = word2vec.Word2Vec(sentences, size=50, min_count=5, window=5, hs=1, sg=1, seed=100, iter=50, alpha=0.1, min_alpha=0.001)
model.save("akb48.model")
