import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

moons = make_moons(n_samples = 200, noise = 0.2, random_state = 0)
X = moons[0]
y = moons[1]

from matplotlib.colors import ListedColormap

def plot_decision_boundary(model, X ,y, margin = 0.3):
    _x1 = np.linspace(X[:, 0].min()-margin, X[:, 0].max()+margin, 100)
    _x2 = np.linspace(X[:, 1].min()-margin, X[:, 1].max()+margin, 100)
    x1, x2 = np.meshgrid(_x1, _x2)
    X_new = np.c_[x1.ravel(), x2.ravel()]
    y_pred = model.predict(X_new).reshape(x1.shape)
    custom_cmap = ListedColormap(['mediumblue', 'orangered'])
    plt.contourf(x1, x2, y_pred, alpha = 0.3, cmap = custom_cmap)
    
def plot_dataset(X, y):
    plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], "bo", ms = 15)
    plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], "r^", ms = 15)
    plt.xlabel("$x_0$", fontsize = 30)
    plt.ylabel("$x_1$", fontsize = 30, rotation = 0)
    
plt.figure(figsize = (12, 8))
plot_dataset(X, y)
plt.show()
