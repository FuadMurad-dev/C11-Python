import numpy as np

array1 = np.arange(0, 51, 1)
array2 = np.arange(100,50, -1)

array_con = np.concatenate([array1, array2])

array_con.sort()

print(array_con)