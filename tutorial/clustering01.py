import numpy as np
from sklearn.datasets import make_blobs

X ,y = make_blobs(n_samples = 200, n_features = 2, centers = 3, random_state = 10)

from sklearn.cluster import KMeans

k_means = KMeans(n_clusters = 3).fit(X)

print(k_means.labels_)
