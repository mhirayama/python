import numpy as np
X = np.random.rand(100,1)
y = 5 + 3 * X + np.random.rand(100, 1)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression().fit(X, y.ravel())
print(lin_reg.intercept_,  lin_reg.coef_)

from sklearn.linear_model import SGDRegressor
sgd_reg = SGDRegressor(max_iter = 100).fit(X, y.ravel())
print(sgd_reg.intercept_, sgd_reg.coef_)

sgd_reg_00001 = SGDRegressor(eta0 = 0.0001, max_iter = 100).fit(X, y.ravel())
print(sgd_reg_00001.intercept_, sgd_reg_00001.coef_)

sgd_reg_100 = SGDRegressor(eta0 = 100, max_iter = 100).fit(X, y.ravel())
print(sgd_reg_100.intercept_, sgd_reg_100.coef_)
