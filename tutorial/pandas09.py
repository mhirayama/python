import numpy as np
import pandas as pd

#標準正規分布に従った乱数のデータフレームを生成
df = pd.DataFrame(data = np.random.randn(5, 5), index = ['A','B','C','D','E'],
                   columns = ['C1','C2','C3','C4','C5'])

print(df)

#2乗の関数を作成
def square(x):
  return x**2

print(df['C1'].apply(square)) #C1の列に関数を適用

#和の関数を作成
def add(x, y):
  return x + y

print(add(df['C1'], df['C2'])) #C1の列に関数を適用

#和の関数を作成
def add2(df):
  return df['C1'] + df['C2']

print(df.apply(add2, axis = 1)) #C1の列に関数を適用

#2乗と3乗の関数を作成
def square_and_cube(x):
  return pd.Series([x**2, x**3])

#データフレームにsquareとcubeの列を追加して、関数を適用
df[['square', 'cubed']] = df['C1'].apply(square_and_cube)

print(df)
