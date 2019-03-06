import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

train_df = pd.read_csv('titanic/train.csv')
test_df = pd.read_csv('titanic/test.csv')

#rain_dfとtest_dfのPclassからEmbarkedまでをつなげる
all_df = pd.concat((train_df.loc[:, 'Pclass' : 'Embarked'], test_df.loc[:, 'Pclass' : 'Embarked']))

all_df['Age'] = all_df['Age'].fillna(all_df['Age'].mean()) #欠損値のあるAgeを平均で埋める
all_df['Fare'] = all_df['Fare'].fillna(all_df['Fare'].mean()) #欠損値のあるFareを平均で埋める
all_df['Embarked'] = all_df['Embarked'].fillna(all_df['Embarked'].mode()[0]) #欠損値のあるEmbarkedを最頻値で埋める

#LabelEncoderでSexとEmbarkedを数値ラベルに置き換える
cat_features = ['Sex', 'Embarked']
for col in cat_features:
    lbl = LabelEncoder()
    all_df[col] = lbl.fit_transform(list(all_df[col].values))

#文字データのNameとTicket、欠損値の多かったCabinを削除
all_df = all_df.drop(columns = ['Name', 'Ticket', 'Cabin'])

#trainとtestに再分割
train = all_df[:train_df.shape[0]]
test = all_df[train_df.shape[0]:]

y = train_df['Survived'] #submissionと学習用に使用
ID = test_df['PassengerId'] #submission用に使用

X_train, X_test, y_train, y_test = train_test_split(train, y, random_state = 0) #トレインデータとテストデータに分割

import xgboost as xgb

#パラメータ設定はほぼデフォルト
params = {
    "objective": "binary:logistic",
    "eval_metric": "auc",
    "eta": 0.1,
    "max_depth": 6,
    "subsample": 1,
    "colsample_bytree": 1,
    "silent": 1
}

#トレインデータとテストデータをXgboost用に置き換える
dtrain = xgb.DMatrix(X_train, label = y_train)
dtest = xgb.DMatrix(X_test, label = y_test)

#モデルの作成
model = xgb.train(params = params,
                 dtrain = dtrain,
                 num_boost_round = 100,
                 early_stopping_rounds = 10,
                 evals = [(dtest, 'test')])

prediction = model.predict(xgb.DMatrix(test), ntree_limit = model.best_ntree_limit) #testデータを使って予測値を出力
prediction = np.where(prediction < 0.5, 0, 1) #予測値を0か1に置き換える

#submission用のデータフレームを作成
submission = pd.DataFrame({
    'PassengerId':  ID,
    'Survived': prediction
})

submission.to_csv('titanic/submission.csv', index = False) #submission.csvとして書き出し
