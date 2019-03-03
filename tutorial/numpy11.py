import numpy as np

array = np.random.randint(0, 100, 20)
print(array)

X = np.sum(array) #配列の総和
print(X)

X = np.mean(array) #配列の平均
print(X)

X = np.var(array) #配列の分散
print(X)

X = np.std(array) #配列の標準偏差
print(X)

X = np.max(array) #最大値
print(X)

X = np.argmax(array) #最大値のインデックス
print(X)

X = np.min(array) #最小値
print(X)

X = np.argmin(array) #最小値のインデックス
print(X)

X = array.dtype #配列のデータ型
print(X)

array = np.random.randn(10)
print(array)
y = np.round(array, 2) #小数点を丸める
print(y)
