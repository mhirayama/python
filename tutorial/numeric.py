import numpy as np
import pandas as pd

df = pd.read_csv('house_sales/kc_house_data.csv')

df = df.loc[:, ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot']]

def outlier_std(df, thresh=3, columns = None):
    if columns == None:
        columns = df.columns
    
    for col in columns:
        mean = df[col].mean()
        std = df[col].std()
        
        border = (np.abs(df[col] - mean)) / std
        
        df = df[(border < 3)]
    
    return df

df = outlier_std(df, ['price'])

df['price'] = np.log1p(df['price'])

from sklearn.preprocessing import StandardScaler, MinMaxScaler

for col in df.columns:
    scaler = StandardScaler()
    df[col] = scaler.fit_transform(np.array(df[col].values).reshape(-1, 1))
    
print(df.head())
