import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv" , delimiter= ";")

north_america = ds[ds["Region"].str.contains("NORTHERN AMERICA")]

deathrate = north_america["Deathrate"]

birthrate = north_america["Birthrate"]


plt.xlabel("Paises NORTHERN AMERICA ")
plt.ylabel("Taxa em %")


plt.title("Grafico de Deathrate e  Birthrate")
plt.plot(deathrate, 'r-', label = "deathrate")
plt.plot(birthrate, 'b--', label = "birthrate")

plt.legend()
plt.show()



