import numpy as np
import pandas as pd

#カテゴリーのあるデータを含んだデータフレームを作成
df = pd.DataFrame({'C1':['A','A','A','B','B','C',np.nan],
                  'C2':[20,50,60,80,100,30,50],
                  'C3':[40,200,100,500,40,200,40]})

print(df)

print(df['C1'].value_counts()) #C1についてカテゴリーの数を集計

print(df[df['C1'] == 'A']) #C1についてAに関するデータのみ表示

print(df['C1'].fillna(df['C1'].mode()[0])) #C1の欠損値を最頻値で埋める

print(df) #データフレームには更新されていない

df['C1'] = df['C1'].fillna(df['C1'].mode()[0]) #データフレームに更新する

print(df) #データフレームに更新された

print(round(df['C1'].value_counts()/len(df),2)) #C1についてカテゴリーの割合を計算

print(df.groupby('C1')) #C1についてグループ化

print(df.groupby('C1').sum()) #C1についてグループ化し総和を求める

print(df.groupby('C1').mean()) #C1についてグループ化し平均を求める

print(df.groupby('C1').max()) #C1についてグループ化し最大値を表示する
