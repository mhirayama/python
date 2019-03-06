import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from mglearn.datasets import make_wave

X, y = make_wave(n_samples = 100)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

lin_reg = LinearRegression().fit(X_train, y_train)

print(lin_reg.score(X_test, y_test))

from sklearn.metrics import mean_squared_error

y_pred = lin_reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(mse)

rmse = np.sqrt(mse)
print(rmse)
