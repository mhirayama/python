import numpy as np
import pandas as pd

#pandasのseriesを生成、seriesにはdataとindexの2つの引数がある
series = pd.Series(data = [1,2,3,4,5], index = ['A','B','C','D','E'])
print(series)

array = np.arange(1,11) #変数arrayに1から10までの整数を生成
index = 'a b c d e f g h i j'.split( ) #aからjまでをスペース区切りで書いて、splitで分割

series = pd.Series(data = array, index = index) #変数に格納されたデータをそれぞれの引数に入力
print(series)
