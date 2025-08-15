import numpy as np

matriz1 = np.zeros([2,2])

matriz1[np.random.randint (0,2) ,np.random.randint(0,2)] = 1

jogador = matriz1[int(input("Selecione a linha da matriz: ")),int(input("Selecione a coluna da matriz: "))]


print(matriz1)

if jogador != 1:
    print("Congratulations! you beat the game")
else:
    print("game over :( try again")
