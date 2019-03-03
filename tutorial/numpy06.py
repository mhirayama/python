import numpy as np

X = np.arange(20).reshape(-1, 1) #0から19までの整数を生成
print(X)

np.random.seed(0)
y = np.random.rand(20) #２０個の正規分布に従う数値を生成
print(y)

y = np.where(y < 0.5, 0, 1).reshape(-1, 1) #0.5以下を0、そうでないものを1で返す
print(y)

z = X[:][y == 1] #yが1のインデックスと同じXを返す
print(z)
