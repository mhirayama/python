import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

df = pd.read_csv('taxi/train.csv', nrows = 50000)

df_location = df.loc[:, ['fare_amount', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']]

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

df_location = outlier_iqr(df_location, columns = ['fare_amount'])

def calculation_distance(x_1, y_1, x_2, y_2):
    
    R = 6371
    
    _x1, _y1, _x2, _y2 = map(np.radians, [x_1, y_1, x_2, y_2])
    
    delta_x = _x2 - _x1
    delta_y = _y2 - _y1
    
    a = np.sin(delta_y/2.0)**2 + np.cos(_y1) * np.cos(_y2) * np.sin(delta_x/2.0)**2
    return 2 * R * np.arcsin(np.sqrt(a))

df_location['distance'] = calculation_distance(df_location['pickup_longitude'],
                                              df_location['pickup_latitude'],
                                              df_location['dropoff_longitude'],
                                              df_location['dropoff_latitude'])

def calculation_azimuth(x_1, y_1, x_2, y_2):
    
    _x1, _y1, _x2, _y2 = map(np.radians, [x_1, y_1, x_2, y_2])
    
    delta_x = _x2 - _x1
    _y = np.sin(delta_x)
    _x = np.cos(_y1) * np.tan(_y2) - np.sin(_y1) * np.cos(delta_x)
    
    psi = np.rad2deg(np.arctan2(_y, _x))
    
    return np.where(psi < 0, 360 + psi, psi)

df_location['azimuth'] = calculation_azimuth(df_location['pickup_longitude'],
                                              df_location['pickup_latitude'],
                                              df_location['dropoff_longitude'],
                                              df_location['dropoff_latitude'])

def direction(azimuth, n_ways = 8):
    bins = np.linspace(0, 360, n_ways + 1)
    
    _azimuth = azimuth + 180/n_ways
    _azimuth = np.where(_azimuth >= 360, _azimuth - 360, _azimuth)
    return np.digitize(_azimuth, bins = bins) - 1

df_location['direction'] = direction(df_location['azimuth'])

print(df_location.head(10))

def plot_with_color(x, y, data, axis = None):
    plt.scatter(x, y, s = data, c = data, cmap = plt.get_cmap('jet'), alpha = 0.3)
    plt.axis(axis)
    plt.colorbar()
    
    plt.xlabel('longitude', fontsize = 15)
    plt.ylabel('latitude', fontsize = 15)

df_location = df_location[(df_location['fare_amount'] > 0) & (df_location['fare_amount'] <= 30)]

plt.figure(figsize = (12, 10))
plot_with_color(x = df_location['pickup_longitude'], 
              y = df_location['pickup_latitude'],
              data = df_location['fare_amount'],
             axis = [-74.1, -73.7, 40.6, 40.9])

plt.show()
