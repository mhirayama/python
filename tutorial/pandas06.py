import numpy as np
import pandas as pd

#欠損値のあるデータフレームを作成
df = pd.DataFrame(data=[[1,2,3,np.nan,4],
                 [5,np.nan,6,np.nan,7],
                 [8,9,10,np.nan,11],
                 [12,np.nan,np.nan,np.nan,13],
                 [14,15,16,17,18]],
                 index = ['A','B','C','D','E'],
                 columns = ['C1','C2','C3','C4','C5'])

print(df)

print(df.dropna()) #欠損値のある行をすべて削除

print(df['C2'].dropna()) #C2の列について欠損値のある行を削除しC2を表示

print(df['C2'].isnull()) #C2の列について欠損値があるかどうかをboolで返す

print(df[df['C2'].isnull() == False]) #C2の列について欠損値がない（False）行のみ表示

print(df.dropna(thresh = 3)) #欠損値が3つ以上ある行を削除

print(df.dropna(thresh = 3, axis = 1)) #欠損値が3つ以上ある列を削除

print(df['C2'].fillna(df['C2'].mean())) #C2について欠損値をC2の他の値の平均で埋める

print(df.fillna(df.mean())) #データフレーム全体に列ごとの欠損値を列ごとの平均で埋める
