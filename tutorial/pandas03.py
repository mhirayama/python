import numpy as np
import pandas as pd

df = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]]) #データフレームを生成、引数はdataとindexとcolumns
print(df)

from sklearn.datasets import load_iris #アイリスデータを読み込み

iris = load_iris() #インスタンスを生成 
iris_df = pd.DataFrame(data = iris.data, columns = iris.feature_names) #アイリスデータのデータフレームを生成
print(iris_df.head()) #最初の5行を表示する
