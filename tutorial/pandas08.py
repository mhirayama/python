import numpy as np
import pandas as pd

#標準正規分布に従った乱数のデータフレームを２個生成
df_1 = pd.DataFrame(data = np.random.randn(5, 5), index = ['A','B','C','D','E'],
                   columns = ['C1','C2','C3','C4','C5'])

df_2 = pd.DataFrame(data = np.random.randn(5, 5), index = ['F','G','H','I','J'],
                   columns = ['C1','C2','C3','C4','C5'])

#それぞれのデータフレームを表示
print(df_1)

print(df_2)

print(pd.concat([df_1, df_2])) #2つのデータフレームを縦（行）で結合

print(pd.concat([df_1, df_2], axis = 1)) #2つのデータフレームを縦と横で結合
