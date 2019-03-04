import numpy as np
import matplotlib.pyplot as plt

data_size = 20
X = np.linspace(0,1,data_size) #0から1までを20分割する
noise = np.random.uniform(low = -1.0, high = 1.0, size = data_size) * 0.2 #sinに従った乱数を生成
y = np.sin(2.0 * np.pi * X) + noise #ノイズを入れたsinを生成

X_line = np.linspace(0,1,1000) #0から1まで1000個生成

from sklearn.linear_model import LinearRegression #線形回帰を読み込み
from sklearn.preprocessing import PolynomialFeatures #多項式のライブラリを読み込み

fig, axes = plt.subplots(1, 3, figsize = (16, 4))

#次元を5、15、25でそれぞれモデルを作成しプロット
for degree, ax in zip([5, 15, 25], axes):
    poly = PolynomialFeatures(degree = degree)
    X_poly = poly.fit_transform(X.reshape(-1, 1))
    lin_reg = LinearRegression().fit(X_poly, y)
    X_line_poly = poly.fit_transform(X_line.reshape(-1, 1))
    ax.plot(X_line, lin_reg.predict(X_line_poly))
    ax.scatter(X, y)
plt.show()
