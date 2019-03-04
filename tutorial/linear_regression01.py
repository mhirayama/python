import numpy as np
X = np.random.rand(100,1) #乱数を生成
y = 5 + 3 * X + np.random.rand(100, 1) #Xに対して線形的な乱数を生成

from sklearn.linear_model import LinearRegression #線形回帰を読み込み
lin_reg = LinearRegression().fit(X, y.ravel()) #モデルの作成
print(lin_reg.intercept_,  lin_reg.coef_) #切片と傾きを表示

from sklearn.linear_model import SGDRegressor #SDG回帰を読み込み
sgd_reg = SGDRegressor(max_iter = 100).fit(X, y.ravel()) #モデルの作成
print(sgd_reg.intercept_, sgd_reg.coef_) #切片と傾きを表示

sgd_reg_00001 = SGDRegressor(eta0 = 0.0001, max_iter = 100).fit(X, y.ravel()) #eta0を0.0001にして学習不足にして学習
print(sgd_reg_00001.intercept_, sgd_reg_00001.coef_)

sgd_reg_100 = SGDRegressor(eta0 = 100, max_iter = 100).fit(X, y.ravel()) #eta0を100にして過学習にして学習
print(sgd_reg_100.intercept_, sgd_reg_100.coef_)
