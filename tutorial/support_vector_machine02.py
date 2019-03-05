import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

moons = make_moons(n_samples = 200, noise = 0.1, random_state = 0) #データセットの生成

X = moons[0] #Xに１列目のデータを格納
y = moons[1] #yに２列目のデータを格納

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0) #データの分割

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) #スケーラーの適用
X_test_scaled = scaler.fit_transform(X_test) #スケーラーの適用

lin_svm = LinearSVC().fit(X_train_scaled, y_train) #モデルの作成

print(lin_svm.intercept_, lin_svm.coef_) #切片と傾きの表示
print(lin_svm.score(X_train, y_train)) #正解率の計算
print(lin_svm.score(X_test, y_test)) #正解率の計算

from sklearn.preprocessing import PolynomialFeatures #多項式のライブラリ

poly = PolynomialFeatures(degree = 3) #3次元のインスタンスを生成
X_train_poly = poly.fit_transform(X_train) #3次元に適用
X_test_poly = poly.fit_transform(X_test) #3次元に適用

X_train_poly_scaled = scaler.fit_transform(X_train_poly) #スケーラーの適用
X_test_poly_scaled = scaler.fit_transform(X_test_poly) #スケーラーの適用
lin_svm = LinearSVC().fit(X_train_poly_scaled, y_train) #モデルの作成

print(lin_svm.predict(X_test_poly_scaled) == y_test) #予測データとテストデータをboolで返す
