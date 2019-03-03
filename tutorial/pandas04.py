import numpy as np
import pandas as pd

df = pd.read_csv('taxi/train.csv', nrows = 500)
print(df.head())

print(df.shape)

print(df.describe())

print(df.info())

print(df.nunique())

print(df.isnull().sum())

print(df.index)

print(df.columns)
