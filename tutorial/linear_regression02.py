import numpy as np
import matplotlib.pyplot as plt

data_size = 20
X = np.linspace(0,1,data_size) #0から1までを20分割する
noise = np.random.uniform(low = -1.0, high = 1.0, size = data_size) * 0.2 #sinに従った乱数を生成
y = np.sin(2.0 * np.pi * X) + noise #ノイズを入れたsinを生成

X_line = np.linspace(0,1,1000) #0から1まで1000個生成

from sklearn.linear_model import LinearRegression #線形回帰を読み込み
lin_reg = LinearRegression().fit(X.reshape(-1, 1), y) #モデルの作成
print(lin_reg.intercept_, lin_reg.coef_) #切片と傾きを表示

X_2 = X ** 2 #Xの値を２乗
X_new = np.concatenate([X.reshape(-1, 1), X_2.reshape(-1, 1)], axis = 1) #XとX_2を一つの配列にする
lin_reg_2 = LinearRegression().fit(X_new, y) #モデルの生成
print(lin_reg_2.intercept_, lin_reg_2.coef_) #切片と傾きを表示

from sklearn.preprocessing import PolynomialFeatures #多項式のライブラリを読み込み
poly = PolynomialFeatures(degree = 3) #3次の多項式を定義
poly.fit(X.reshape(-1,1)) #3次の多項式を生成
X_poly_3 = poly.transform(X.reshape(-1, 1))
print(X_poly_3)

lin_reg_3 = LinearRegression().fit(X_poly_3, y) #モデルの生成
X_line_poly_3 = poly.fit_transform(X_line.reshape(-1,1))
print(lin_reg_3.predict(X_line_poly_3)) #モデルから予測

plt.plot(X_line, lin_reg_3.predict(X_line_poly_3)) #予測データをプロット
plt.scatter(X, y)
plt.show()
