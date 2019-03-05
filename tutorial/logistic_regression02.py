import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits() #データセットの読み込み
X = digits.data #Xにdataを読み込み
y = digits.target #yにtargetを読み込み

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) #データの分割

scaler = StandardScaler() #インスタンスの作成
X_train_scaled = scaler.fit_transform(X_train) #StandardScalerの適用
X_test_scaled = scaler.fit_transform(X_test) #SrandartdScalerの適用

log_reg = LogisticRegression().fit(X_train_scaled, y_train) #モデルの作成

prediction = log_reg.predict(X_test_scaled) #テストデータでモデルに適用

print(prediction == y_test) #予測データとテストデータでboolで返す

from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(prediction, y_test) #配列の集計を適用
print(confusion)

print(log_reg.score(X_test_scaled, y_test)) #正解率の計算
