import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

moons = make_moons(n_samples = 200, noise = 0.1, random_state = 0)

X = moons[0]
y = moons[1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

from sklearn.tree import DecisionTreeClassifier

tree_clf = DecisionTreeClassifier().fit(X_train, y_train)
tree_clf_3 = DecisionTreeClassifier(max_depth = 3).fit(X_train, y_train)

print(tree_clf.score(X_test, y_test))
print(tree_clf_3.score(X_test, y_test))

from matplotlib.colors import ListedColormap

def plot_decision_boundary(clf, X ,y):
    _x1 = np.linspace(X[:, 0].min()-0.5, X[:, 0].max()+0.5, 100)
    _x2 = np.linspace(X[:, 1].min()-0.5, X[:, 1].max()+0.5, 100)
    x1, x2 = np.meshgrid(_x1, _x2)
    X_new = np.c_[x1.ravel(), x2.ravel()]
    y_pred = clf.predict(X_new).reshape(x1.shape)
    y_decision = clf.predict(X_new).reshape(x1.shape)
    custom_cmap = ListedColormap(['mediumblue', 'orangered'])
    plt.contourf(x1, x2, y_pred, alpha = 0.3, cmap = custom_cmap)
    
def plot_dataset(X, y):
    plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], "bo", ms = 15)
    plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], "r^", ms = 15)
    plt.xlabel("$x_0$", fontsize = 30)
    plt.ylabel("$x_1$", fontsize = 30, rotation = 0)
    
plt.figure(figsize = (24, 8))
plt.subplot(121)
plot_decision_boundary(tree_clf, X, y)
plot_dataset(X, y)

plt.subplot(122)
plot_decision_boundary(tree_clf_3, X, y)
plot_dataset(X, y)

plt.show()
