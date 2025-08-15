import numpy as np

np.random.seed(10)

matriz = np.random.randint(1,50,[4,4])

soma_linha = matriz.sum(axis=1)
soma_coluna = matriz.sum(axis=0)

media_linha = soma_linha/4
media_coluna = soma_coluna/4

aparece2 = np.unique_counts(matriz)

print(matriz)

print(f"Media: {media_linha} : {media_coluna}")

print(f"Maior numero da media: {media_linha.max()} : {media_coluna.max()}")

print(f"Mostra quantidade: {np.unique(matriz, return_counts=True)}") 

print(f" Mostra apenas numeros que aparace 2 vezes: {aparece2.values[aparece2.counts == 2]}")



