import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns

df = pd.read_csv('taxi/train.csv', nrows = 5000)

df = df[df['fare_amount'] > 0]

df = df[df['fare_amount'] < 100]

def outlier_iqr(df, columns = None):
    if columns == None:
        columns = df.columns
        
    for col in columns:
        q1 = df[col].describe()['25%']
        q3 = df[col].describe()['75%']
        
        iqr = q3 - q1
        
        outlier_min = q1 - iqr * 1.5
        outlier_max = q3 + iqr * 1.5
        
        df = df[(df[col] >= outlier_min) & (df[col] <= outlier_max)]
    return df

df = outlier_iqr(df, columns = ['fare_amount'])

df = df[(df['pickup_longitude'] > -75) & (df['pickup_longitude'] < -73)]
df = df[(df['pickup_latitude'] > 40) & (df['pickup_latitude'] < 42)]
df = df[(df['dropoff_longitude'] > -75) & (df['dropoff_longitude'] < -73)]
df = df[(df['dropoff_latitude'] > 40) & (df['dropoff_latitude'] < 42)]

df = df[(df['passenger_count'] > 0)]

def calculation_distance(x_1, y_1, x_2, y_2):
    
    R = 6371
    
    _x1, _y1, _x2, _y2 = map(np.radians, [x_1, y_1, x_2, y_2])
    
    delta_x = _x2 - _x1
    delta_y = _y2 - _y1
    
    a = np.sin(delta_y/2.0)**2 + np.cos(_y1) * np.cos(_y2) * np.sin(delta_x/2.0)**2
    return 2 * R * np.arcsin(np.sqrt(a))

def calculation_azimuth(x_1, y_1, x_2, y_2):
    
    _x1, _y1, _x2, _y2 = map(np.radians, [x_1, y_1, x_2, y_2])
    
    delta_x = _x2 - _x1
    _y = np.sin(delta_x)
    _x = np.cos(_y1) * np.tan(_y2) - np.sin(_y1) * np.cos(delta_x)
    
    psi = np.rad2deg(np.arctan2(_y, _x))
    
    return np.where(psi < 0, 360 + psi, psi)

df['distance'] = calculation_distance(df['pickup_longitude'],
                                     df['pickup_latitude'],
                                     df['dropoff_longitude'],
                                     df['dropoff_latitude'])

df['azimuth'] = calculation_azimuth(df['pickup_longitude'],
                                     df['pickup_latitude'],
                                     df['dropoff_longitude'],
                                     df['dropoff_latitude'])

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format = "%Y-%m-%d %H:%M:%S UTC")

df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['dayofweek'] = df['pickup_datetime'].dt.dayofweek
df['year'] = df['pickup_datetime'].dt.year

from sklearn.model_selection import train_test_split
import xgboost as xgb

X = df.drop(columns = ['key', 'fare_amount', 'pickup_datetime'])
y = df['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

params = {
    'silent' : 1,
    'max_depth' : 6,
    'min_chiled_weight' : 1,
    'eta' : 0.1,
    'tree_method' : 'exact',
    'objective' : 'reg:linear',
    'eval_metric' : 'rmse',
    'predictor' : 'cpu_predictor'
}

dtrain = xgb.DMatrix(X_train, label = y_train)
dtest = xgb.DMatrix(X_test, label = y_test)

model = xgb.train(params = params,
                 dtrain = dtrain,
                 num_boost_round = 1000,
                 early_stopping_rounds = 5,
                 evals = [(dtest, 'test')])

gridsearch_params = [
    (max_depth, eta)
    for max_depth in [6, 7, 8]
    for eta in [0.1, 0.05, 0.01]
]

min_rmse = float('Inf')

best_param = []

for max_depth, eta in gridsearch_params:
    print('max_depth = {}, eta = {}'.format(max_depth, eta))
    
    params['max_depth'] = max_depth
    params['eta'] = eta
    
    cv_results = xgb.cv(
        params,
        dtrain,
        num_boost_round = 1000,
        seed = 0,
        nfold = 5,
        metrics = {'rmse'},
        early_stopping_rounds = 5
    )
    
    mean_rmse = cv_results['test-rmse-mean'].min()
    boost_rounds = cv_results['test-rmse-mean'].argmin()
    print('RMSE {} for {} rounds'.format(mean_rmse, boost_rounds))
    if mean_rmse < min_rmse:
        min_rmse = mean_rmse
        best_param = (max_depth, eta)

print('Best params {}, RMSE {}'.format(best_param, min_rmse))

params['ma_depth'] = 6
params['eta'] = 0.1

model = xgb.train(params = params,
                 dtrain = dtrain,
                 num_boost_round = 1000,
                 early_stopping_rounds = 5,
                 evals = [(dtest, 'test')])

prediction = model.predict(xgb.DMatrix(X_test),
                          ntree_limit = model.best_ntree_limit)

plt.figure(figsize = (12,12))
plt.scatter(y_test[:1000], prediction[:1000], alpha = 0.2)
plt.show()
