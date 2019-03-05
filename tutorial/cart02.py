import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import mglearn
from sklearn.tree import DecisionTreeRegressor

reg_X, reg_y = mglearn.datasets.make_wave(n_samples = 100)

tree_reg = DecisionTreeRegressor().fit(reg_X, reg_y)
tree_reg_3 = DecisionTreeRegressor(max_depth = 3).fit(reg_X, reg_y)

def plot_regression_predictions(tree_reg, X, y):
        x1 = np.linspace(X.min()-1, X.max()+1, 500).reshape(-1,1)
        y_pred = tree_reg.predict(x1)
        plt.xlabel('x', fontsize = 30)
        plt.ylabel('y', fontsize = 30, rotation = 0)
        plt.plot(X, y, "bo", ms =15)
        plt.plot(x1, y_pred, "r-", linewidth = 6)
    
plt.figure(figsize = (24, 8))
plt.subplot(121)
plot_regression_predictions(tree_reg, reg_X, reg_y)

plt.subplot(122)
plot_regression_predictions(tree_reg_3, reg_X, reg_y)

plt.show()
