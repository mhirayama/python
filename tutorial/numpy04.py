import numpy as np

array = np.array([[1,2],[3,4],[5,6]])

print(array[0]) #インデックスを指定する

print(array[1:]) #インデックスが１以降のデータを表示

print(array[:2]) #インデックスが１以前のデータを表示

print(array[0,1]) #インデックスとカラムを指定する

print(array[0][1]) #インデックスとカラムを指定する

print(array[:, 1]) #指定したカラムのみ表示する
print(array[:, 0]) #指定したカラムのみ表示する
