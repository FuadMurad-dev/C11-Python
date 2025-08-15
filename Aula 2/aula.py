import numpy as np # o as é um apelido para chamar mais facilmente o numpy

# 
arr = np.array([10, 20 ,30])

print(arr)

print(type(arr))

matriz = np.array([[10,20,30], [40,50,60]])

print(matriz)

#----------------------------------------//----------------------------------

# FUncoes para estruturar numpy arrays

array = np.ones(10)

print(array)

matriz2 = np.zeros(10).reshape(5,2) # esse reshape esta reformatando a matriz para 5 linas e 2 colunas = 10 

matriz3 = np.zeros([5,2]) # criando uma matriz direto 

print(matriz2)
print(matriz3)

array2 = np.arange(10 ,31 ,10) # esse arange vai criar um array começando do 10 até o 30 porque o 31 e exclusivo e o outro 10 e os passos

print(array2)

array3 = np.arange(10 ,101 ,10)

print(array3)

print(array3.min())

print(array3.max())

print(array3.mean()) # media do valor

print(array3.argmax()) # indice de maior valor







