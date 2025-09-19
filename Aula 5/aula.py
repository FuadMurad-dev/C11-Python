import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

# Plost com matplotlib


x = np.array([1,2,3,4,5])

y = x * 2 
y2 = x * x

# explicando eixos x e y

plt.xlabel("valores de x")
plt.ylabel("Valores de y")

plt.subplot(1,2,1) # craindo a matriz de subplots, ou seja, onde vamos tracas os graficos separados
plt.plot(x,y, "*:r", linewidth = 3, markersize = 10)

plt.subplot(1,2,2)
plt.plot(x,y2 ,'s--g', linewidth = 3, markersize = 10)

#plotando o grafico
plt.show()