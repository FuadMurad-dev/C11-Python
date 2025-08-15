
import numpy as np

np.random.seed(10)

array = np.random.randint (1, 10, 10)  

print(array)

print(np.unique(array, return_counts=True)) # para extrair numeros unicos e deixar eles ordenados, esse return_counts e pra contar quantas vezes aquele elemento apareceu

