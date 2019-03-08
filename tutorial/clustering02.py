import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans

X, y = make_moons(n_samples = 200, noise = 0.1, random_state = 0)

k_means = KMeans(n_clusters = 2).fit(X)

print(k_means.labels_)
