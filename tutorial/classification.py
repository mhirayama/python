import pandas as pd
import numpy as np

df = pd.read_csv('kickstarter/ks-projects-201801.csv')

df = df[(df['state'] == 'failed') | (df['state'] == 'successful')]
df['state'] = df['state'].map({
    'failed' : 0,
    'successful' : 1
})

df['usd_goal_real'] = np.log1p(df['usd_goal_real'])

df['deadline'] = pd.to_datetime(df['deadline'], format = "%Y-%m-%d %H:%M:%S")
df['launched'] = pd.to_datetime(df['launched'], format = "%Y-%m-%d %H:%M:%S")

df['duration'] = (df['deadline'] - df['launched']). dt.days
df['quarter'] = df['launched'].dt.quarter
df['month'] = df['launched'].dt.month
df['year'] = df['launched'].dt.year
df['dayofweek'] = df['launched'].dt.dayofweek

df = df.drop(columns = ['ID', 'deadline', 'goal', 'launched', 'pledged', 'backers', 'usd pledged', 'usd_pledged_real'])

df['name_len'] = df['name'].str.len()
df['num_words'] = df['name'].apply(lambda x: len(str(x).split(' ')))
df.drop(columns = ['name'], inplace = True)

df['name_len'] = df['name_len'].fillna(0)

df = pd.get_dummies(df, ['category', 'main_category', 'currency', 'country'])

import xgboost as xgb
from sklearn.model_selection import train_test_split

X = df.drop(columns = ['state'])
y = df['state']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

params = {
    'silent' : 1,
    'max_depth' : 6,
    'min_chiled_weight' : 1,
    'eta' : 0.1,
    'tree_method' : 'exact',
    'objective' : 'binary:logistic',
    'eval_metric' : 'logloss',
    'predictor' : 'cpu_predictor'
}

dtrain = xgb.DMatrix(X_train, label = y_train)
dtest = xgb.DMatrix(X_test, label = y_test)

model = xgb.train(params = params,
                 dtrain = dtrain,
                 num_boost_round = 1000,
                 early_stopping_rounds = 5,
                 evals = [(dtest, 'test')])

from sklearn.metrics import accuracy_score

y_pred = model.predict(xgb.DMatrix(X_test), ntree_limit = model.best_ntree_limit)
predictions = [round(pred) for pred in y_pred]

acc = accuracy_score(y_test, predictions)
print(round(acc * 100, 2))

from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier

class SklearnHelper(object):
    def __init__(self, clf, seed = 0, params = None):
        params['random_state'] = seed
        self.clf = clf(**params)
        
    def fit(self, x, y):
        return self.clf.fit(x, y)
    
    def predict(self, x):
        return self.clf.predict(x)
    
    def predict_proba(self, x):
        return self.clf.predict_proba(x)

rfc_params = {
    'n_jobs': -1,
    'n_estimators': 500,
    'warm_start': True,
    'max_depth': 6,
    'min_samples_leaf': 2,
    'max_features': 'sqrt',
    'verbose': 1
}

etc_params = {
    'n_jobs': -1,
    'n_estimators': 500,
    'max_depth': 8,
    'min_samples_leaf': 2,
    'verbose': 1
}

ada_params = {
    'n_estimators': 500,
    'learning_rate': 0.75
}

gbc_params = {
    'n_estimators': 500,
    'max_depth': 5,
    'min_samples_leaf': 2,
    'verbose': 1
}

rfc = SklearnHelper(RandomForestClassifier, seed = 0, params = rfc_params).fit(X_train, y_train)
etc = SklearnHelper(clf = ExtraTreesClassifier, seed = 0, params = etc_params).fit(X_train, y_train)
ada = SklearnHelper(clf = AdaBoostClassifier, seed = 0, params = ada_params).fit(X_train, y_train)
gbc = SklearnHelper(clf = GradientBoostingClassifier, seed = 0, params = gbc_params).fit(X_train, y_train)

rfc_pred = rfc.predict_proba(X_train)
etc_pred = etc.predict_proba(X_train)
ada_pred = ada.predict_proba(X_train)
gbc_pred = gbc.predict_proba(X_train)

preds_train = pd.DataFrame({'rfc_pred': rfc_pred[:, 1],
                            'etc_pred': etc_pred[:, 1],
                            'ada_pred': ada_pred[:, 1],
                            'gbc_pred': gbc_pred[:, 1]})

rfc_pred_test = rfc.predict_proba(X_test)
etc_pred_test = etc.predict_proba(X_test)
ada_pred_test = ada.predict_proba(X_test)
gbc_pred_test = gbc.predict_proba(X_test)

preds_test = pd.DataFrame({'rfc_pred': rfc_pred_test[:, 1],
                           'etc_pred': etc_pred_test[:, 1],
                           'ada_pred': ada_pred_test[:, 1],
                           'gbc_pred': gbc_pred_test[:, 1]})

params = {
    'silent' : 1,
    'max_depth' : 2,
    'min_chiled_weight' : 1,
    'eta' : 0.1,
    'tree_method' : 'exact',
    'objective' : 'binary:logistic',
    'eval_metric' : 'logloss',
    'predictor' : 'cpu_predictor'
}

dtrain = xgb.DMatrix(preds_train, label = y_train)
dtest = xgb.DMatrix(preds_test, label = y_test)

model = xgb.train(params = params,
                 dtrain = dtrain,
                 num_boost_round = 1000,
                 early_stopping_rounds = 5,
                 evals = [(dtest, 'test')])

y_pred = model.predict(xgb.DMatrix(preds_test), ntree_limit = model.best_ntree_limit)
predictions = [round(pred) for pred in y_pred]

acc = accuracy_score(y_test, predictions)
print(round(acc * 100, 2))
