import numpy as np
import pandas as pd

df = pd.read_csv('taxi/train.csv', nrows = 500) #csvファイルの読み込み
print(df.head())

print(df.shape)

print(df.describe()) #基本統計の確認

print(df.info()) #データの基本情報

print(df.nunique()) #コラムに対するインデックスの種類数

print(df.isnull().sum()) #欠損値の集計

print(df.index) #インデックスの数

print(df.columns) #すべてのコラムを表示
