import numpy as np

np.random.seed(0)

array = np.random.randn(10) #標準正規分布（平均０、分散１）に従って乱数を生成
print(array)

array = np.random.rand(10) #0から1までの範囲で乱数を生成
print(array)

array = np.random.randint(0, 100, 10) #指定した範囲の整数をランダムに抽出
print(array)
