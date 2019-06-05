from gensim.models import word2vec

model = word2vec.Word2Vec.load("nogizaka46.model")
results = model.wv.most_similar(positive=["自由"], topn=20)
for result in results:
    print(result[0], result[1])
