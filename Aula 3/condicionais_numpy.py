import numpy as np

matriz = np.arange(1,10,1).reshape(3,3)

print(matriz > 5) # mostra true e false na matriz

print(matriz [matriz > 5]) # quando eu faço isso ele mostra os valores trues da matriz

print(matriz[matriz%2 ==0]) # mostrando os numeros que sao par
