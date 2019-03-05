import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

moons = make_moons(n_samples = 200, noise = 0.1, random_state = 0)

X = moons[0]
y = moons[1]

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

lin_svm = LinearSVC().fit(X_train_scaled, y_train)

print(lin_svm.intercept_, lin_svm.coef_) #切片と傾きの表示
print(lin_svm.score(X_train, y_train)) #正解率の計算
print(lin_svm.score(X_test, y_test)) #正解率の計算

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree = 3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.fit_transform(X_test)

X_train_poly_scaled = scaler.fit_transform(X_train_poly)
X_test_poly_scaled = scaler.fit_transform(X_test_poly)
lin_svm = LinearSVC().fit(X_train_poly_scaled, y_train)

print(lin_svm.predict(X_test_poly_scaled) == y_test)
