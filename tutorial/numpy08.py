import numpy as np

array = np.arange(3,10) #0から9までの10個の整数を生成し、そのうち3以降を生成する
print(array)

array = np.zeros([3,3]) #3列3行の0を生成
print(array)

array = np.array([[1,2],[3,4],[5,6]]) #任意の3列3行の配列
print(array)
array = np.zeros_like(array) #配列の数値をすべて0に置き換える
print(array)

array = np.ones([3,3]) #3列3行の1を生成
print(array)

array = np.array([[1,2],[3,4],[5,6]]) #任意の3列3行の配列
print(array)
array = np.ones_like(array) #配列の数値をすべて1に置き換える
print(array)

array = np.eye(3) #1を対角線に生成、それ以外は0
print(array)

array = np.linspace(0, 1, 11) #0から1を11分割
print(array)
