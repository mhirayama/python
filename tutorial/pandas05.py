import numpy as np
import pandas as pd

np.random.seed(10)
#標準正規分布に従った乱数で、5列5行のデータフレームを生成し、indexはAからE、columnsはC1からC5として定義
df = pd.DataFrame(data = np.random.randn(5,5), index = ['A','B','C','D','E'], columns = ['C1','C2','C3','C4','C5'])

print(df)

print(df.loc['A']) #A行のデータをすべて表示

print(df.loc[:, 'C1']) #C1列のデータをすべて表示

print(df.loc['A',['C1','C3']]) #A行のC1列目とC3列目を表示

print(df > 0) #0より大きいかどうかをboolで返す

print(df[df > 0]) #0より大きいデータを数値で返し、そうでないものはNaNで返す

print(df['C1'] > 0) #C1列に適応した場合

print(df[df['C1'] > 0]) #C1列に適応した場合

print(df[(df['C1'] > 0) & (df['C1'] < 1)]) #条件を二つ付けた場合

df['new_columns'] = df['C1'] * df['C2'] #新しいコラムを生成し、そこにC1とC2の乗算
print(df)

print(df.drop(columns = ['C1'])) #C1列を削除

print(df) #元のデータフレームは削除されていない

df.drop(index = ['A'], inplace =True) #元のデータフレームからA行を削除

print(df) #元のデータフレームが削除された
