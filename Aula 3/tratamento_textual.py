import numpy as np

array = np.array(['Goku', 'Vegeta', 'Gohan', 'Trunks', 'Bulma'])

print(np.char.find(array, 'Go')) # ele retorna a posicao do começo da string colocada

print(array[np.char.find(array, 'Go') >=0])


