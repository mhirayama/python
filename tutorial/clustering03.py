import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage

iris = load_iris()
X = iris.data

z = linkage(X, method = 'average', metric = 'euclidean')
plt.figure(figsize = (18, 12))
dendrogram(z)
plt.show()
