import numpy as np
import pandas as pd

df = pd.read_csv('taxi/train.csv', nrows = 50000)

df = df.loc[:, 'fare_amount': 'pickup_datetime']

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format = "%Y-%m-%d %H:%M:%S UTC")

df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['dayofweek'] = df['pickup_datetime'].dt.dayofweek
df['year'] = df['pickup_datetime'].dt.year

import datetime as dt

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format = "%Y-%m-%d %H:%M:%S UTC")
df['dropoff_datetime'] = df['pickup_datetime'] + dt.timedelta(minutes = 30)

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format = "%Y-%m-%d %H:%M:%S UTC")
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'], format = "%Y-%m-%d %H:%M:%S UTC")

df['ride_time_m'] = (df['dropoff_datetime'] - df['pickup_datetime']).astype('timedelta64[m]')

def judge_holiday(dayofweek):
    return np.where((dayofweek == 5) | (dayofweek == 6), 1, 0)

df['holiday'] = judge_holiday(df['dayofweek'])

def judge_next_day_is_holiday(dayofweek):
    return np.where((dayofweek == 4) | (dayofweek == 5), 1, 0)

df['next_day_is_holiday'] = judge_next_day_is_holiday(df['dayofweek'])

def judge_season(month):
    if 3 <= month <= 5:
        season = 0
    elif 6 <= month <= 8:
        season = 1
    elif 9 <= month <= 11:
        season = 2
    else:
        season = 3
    
    return season

df['season'] = df['month'].apply(judge_season)

print(df.head())
