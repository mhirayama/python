import numpy as np

array_1 = np.array([[1,2],[3,4],[5,6]])
array_2 = np.array([[7,8],[9,10],[11,12]])

array = np.vstack([array_1, array_2])
print(array)

array = np.hstack([array_1, array_2])
print(array)
