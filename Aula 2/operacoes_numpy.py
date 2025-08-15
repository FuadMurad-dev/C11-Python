import numpy as np

array1 = np.arange (1,10,1)
array2 = np.arange (9,0,-1)


print(array1)
print(array2)

print(array1 + array2) # somando os arrays

print(np.concatenate([array1, array2])) # funcao para concatenar(juntar um array com outro array)

#-------------------------------------------//--------------------------------------

# Operacoes com matrizes

matriz1 = np.array([50, 10, 100, 60 ,25, 100 ,80, 75 ,100]).reshape(3,3)

print(matriz1)

print(matriz1.sum(axis=1)) # 0 = coluna , 1 = linhas. passamos o valor para somar linhas

print(matriz1.sum(axis=0)[2]) # esse [2] é pra mostrar so o valor na posicao 2

print(matriz1/10) # BROACASTING


