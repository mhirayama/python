import numpy as np

array = np.array([[1,2],[3,4],[5,6]])

array = array.reshape(2,3) #配列のシェイプを変更する
print(array)

array = array.reshape(-1, 1) #配列のシェイプを変更する（縦に一列）
print(array)

array = np.array([[1,2],[3,4],[5,6]])
array = array.ravel() #配列のシェイプを変更する（横に一列）
print(array)
