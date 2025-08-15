import numpy as np


linha_random = np.random.randint(1,10)
coluna_random = np.random.randint(1,10)

matriz_alatoria = np.zeros([linha_random,coluna_random])

print(matriz_alatoria)

mutiplicar = linha_random * coluna_random

if mutiplicar %2 == 0:
    print("Pode se tornar par")
else:
    print("Pode se tornar impar")

