import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns = iris.feature_names) #irisのデータセットをデータフレームに格納
df['target'] = iris.target #iris.targetをデータフォレームに追加

X = iris.data[50:, 2].reshape(-1, 1) #50行目以降をXに配列として格納
y = iris.target[50:] - 1 #50行目以降を配列として格納

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

scaler = StandardScaler() #インスタンスの作成
X_scaled = scaler.fit_transform(X) #StandardScalerの適用

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, random_state = 0) #データの分割

log_reg = LogisticRegression().fit(X_train, y_train) #モデルの作成

print(log_reg.intercept_, log_reg.coef_) #切片と傾きの表示
print(log_reg.score(X_train, y_train)) #正解率の計算
print(log_reg.score(X_test, y_test)) #正解率の計算
