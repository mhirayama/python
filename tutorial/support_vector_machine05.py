import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

moons = make_moons(n_samples = 200, noise = 0.1, random_state = 0)

X = moons[0]
y = moons[1]

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

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

plt.figure(figsize = (20, 15))

for i, degree in enumerate([2, 3, 5, 10]):
        poly_kernel_svm = Pipeline([
                ('scaler', StandardScaler()),
                ('svm', SVC(kernel = 'poly', degree = degree, coef0 = 1))
        ])
        poly_kernel_svm.fit(X, y)
    
        plt.subplot(221 + i)
        plot_decision_function(poly_kernel_svm)
        plot_dataset(X, y)
        plt.title("d = {}".format(degree), fontsize=30)
    
plt.show()
