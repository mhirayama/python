import numpy as np

array_1 = np.array([[1,2],[3,4],[5,6]])
array_2 = np.array([[7,8],[9,10],[11,12]])

array = array_1 + array_2 #配列同士の和
print(array)

array = array_1 - array_2 #配列同士の差
print(array)

array = array_1 * array_2 #配列同士の積
print(array)

array = array_1 / array_2 #配列同士の商
print(array)

array = array_1**2 #配列の乗算
print(array)

array = np.sqrt(array_1) #配列の平方根
print(array)

array = np.exp(array_1) #配列の自然対数
print(array)

array = np.log1p(array_1) #配列の対数
print(array)
