import numpy as np
import pandas as pd

#pandasのseriesを生成、seriesにはdataとindexの2つの引数がある
series = pd.Series(data = [1,2,3,4,5], index = ['A','B','C','D','E'])
print(series)

print(series['A']) #Aのインデックスのdataを表示する

print(series['A':'D']) #AからDまでのインデックスのdataを表示する

print(series.loc['A']) #正しい書き方

print(series.loc['A':'D']) #正しい書き方

print(series.loc[['B','D']]) #BとDのインデックスのdataを表示

print(series.iloc[1]) #インデックスの番号が1のdataを表示

print(series.iloc[:2]) #インデックスの番号が0から1までのdataを表示
