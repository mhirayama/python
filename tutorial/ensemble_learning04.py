import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X_iris = iris.data
y_iris = iris.target

from sklearn.ensemble import RandomForestClassifier

random_forest_iris = RandomForestClassifier(n_estimators =100, random_state = 0).fit(X_iris, y_iris)

print(random_forest_iris.feature_importances_)

plt.figure(figsize = (12, 8))
plt.barh(range(iris.data.shape[1]), random_forest_iris.feature_importances_, height = 0.5)
plt.yticks(range(iris.data.shape[1]), iris.feature_names, fontsize = 20)
plt.xlabel("Feature importances", fontsize = 30)
plt.show()
