import numpy as np

array1 = np.ones(8)
array2 = np.random.randint(0, 10, 8)

array_resultado = array1 + array2

soma_total = array_resultado.sum()

print(soma_total)


if soma_total >= 40:
    print(array_resultado.reshape(4,2))

else:
    print(array_resultado.reshape(2,4))

