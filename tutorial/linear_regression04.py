import mglearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X, y = mglearn.datasets.load_extended_boston() #データセットをX,yに生成

df_X = pd.DataFrame(X) #データフレームとして読み込む
df_y = pd.DataFrame(y)

print(df_X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) #トレインデータとテストデータに分割

lin_reg = LinearRegression().fit(X_train, y_train) #モデルの作成

print(round(lin_reg.score(X_train, y_train), 3)) #トレインデータの正解率を計算
print(round(lin_reg.score(X_test, y_test), 3)) #テストデータの正解率を計算

from sklearn.linear_model import Ridge, Lasso

ridge = Ridge().fit(X_train, y_train) #モデルの生成

# 正解率の関数
def print_score(model):
    print(round(model.score(X_train, y_train), 3))
    print(round(model.score(X_test, y_test), 3))

print_score(ridge) #正解率の表示

ridge_10 = Ridge(alpha = 10).fit(X_train, y_train) #パラメーターを変更してモデルの作成
print_score(ridge_10) #正解率の表示

ridge_01 = Ridge(alpha = 0.1).fit(X_train, y_train) #パラメーターを変更してモデルの作成
print_score(ridge_01) #正解率の表示

coefficients = pd.DataFrame({'lin_reg': lin_reg.coef_, 'ridge': ridge.coef_, 'ridge_10': ridge_10.coef_, 'ridge_01': ridge_01.coef_}) #パラメーターごとのcoef_をデータフレームに格納

print(coefficients.head())

lasso = Lasso().fit(X_train, y_train) #モデルの作成

print_score(lasso)

lasso_001 = Lasso(alpha = 0.01, max_iter = 10000).fit(X_train, y_train) #パラメーターを変更してモデルの作成
print_score(lasso_001)

coefficients_lasso = pd.DataFrame({'lin_reg': lin_reg.coef_,'lasso': lasso.coef_,'lasso_001': lasso_001.coef_}) #結果をデータフレームに格納
print(coefficients_lasso.head())
