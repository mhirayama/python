import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

moons = make_moons(n_samples = 200, noise = 0.1, random_state = 0)

X = moons[0]
y = moons[1]

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import LinearSVC

from sklearn.pipeline import Pipeline

poly_svm = Pipeline([
    ('poly', PolynomialFeatures(degree = 3)),
    ('scaler', StandardScaler()),
    ('svm', LinearSVC())
])

poly_svm.fit(X, y)

def plot_decision_function(model):
    _x0 = np.linspace(-1.5, 2.5, 100)
    _x1 = np.linspace(-1.0, 1.5, 100)
    x0, x1 = np.meshgrid(_x0, _x1)
    X = np.c_[x0.ravel(), x1.ravel()]
    y_pred = model.predict(X).reshape(x0.shape)
    y_decision = model.decision_function(X).reshape(x0.shape)
    plt.contourf(x0, x1, y_pred, cmap = plt.cm.brg, alpha = 0.2)
    plt.contourf(x0, x1, y_decision, levels = [y_decision.min(), 0, y_decision.max()], alpha = 0.3)
    
def plot_dataset(X, y):
    plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], "bo", ms = 15)
    plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], "r^", ms = 15)
    plt.xlabel("$x_1$", fontsize = 20)
    plt.ylabel("$x_2$", fontsize = 20, rotation = 0)
    
plt.figure(figsize = (12, 8))
plot_decision_function(poly_svm)
plot_dataset(X, y)
plt.show()
