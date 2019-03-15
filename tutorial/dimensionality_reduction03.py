import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv('house-prices/train.csv')

df.isnull().sum()[df.isnull().sum() > 0] 

df = df.drop(columns = ['LotFrontage', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature'], axis = 1)

all_columns = df.columns.values
non_cat_cols = ['LotFrontage', 'LotArea', 'MasVnrArea', 'BsmtFinSF1',
               'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF',
               '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'GarageArea',
               'ScreenPorch', 'PoolArea', 'MiscVal']

cat_cols = [col for col in all_columns if col not in non_cat_cols]

nan_cols = df.isnull().sum()[df.isnull().sum() > 0].index

for col in nan_cols:
    if col in non_cat_cols:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

df = pd.get_dummies(df)

X = df.drop(columns = ['Id', 'SalePrice'])
y = df['SalePrice']

X = np.log1p(X)
y = np.log1p(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)

pca = PCA()

X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.fit_transform(X_test)

X_train_pca = X_train_pca[:, :8]
X_test_pca = X_test_pca[:, :8]

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score

cv = KFold(n_splits = 5, shuffle = True, random_state = 0)

rf_score = np.sqrt(-cross_val_score(RandomForestRegressor(n_estimators=500, max_depth=6),
                          X = X_train,
                          y = y_train,
                          cv = cv,
                          scoring='neg_mean_squared_error'))

print(rf_score.mean())

cv = KFold(n_splits = 5, shuffle = True, random_state = 0)

rf_pca_score = np.sqrt(-cross_val_score(RandomForestRegressor(n_estimators=500, max_depth=6),
                          X = X_train_pca,
                          y = y_train,
                          cv = cv,
                          scoring='neg_mean_squared_error'))

print(rf_pca_score.mean())

from sklearn.model_selection import GridSearchCV

rf_param_grid = {
    'max_depth' : range(5, 11)
}

rf_scores = np.sqrt(-cross_val_score(GridSearchCV(RandomForestRegressor(n_estimators=500),
                                                  param_grid = rf_param_grid,
                                                  cv = cv),
                          X = X_train_pca,
                          y = y_train,
                          cv = cv,
                          scoring='neg_mean_squared_error'))

print(rf_scores.mean())
